from typing import Tuple
from pyspark.sql import DataFrame
from pyspark.sql import functions as f

from utils import spark_session, build_url, get_settings


def main(
    restaurants: DataFrame,
    open_close_times: DataFrame,
    groups: DataFrame,
    transactions: DataFrame,
) -> Tuple[DataFrame, DataFrame]:

    clean_restaurants = (
        restaurants.withColumn("name", f.initcap(f.trim(restaurants.name)))
        .withColumn("city", f.initcap(f.trim(restaurants.city)))
        .withColumn("state", f.initcap(f.trim(restaurants.state)))
        .withColumn("address1", f.initcap(f.trim(restaurants.address1)))
    )
    open_times = (
        open_close_times.filter(open_close_times.type == "open")
        .withColumn("time", f.lower(f.date_format(open_close_times.time, "ha")))
        .withColumnRenamed("time", "open")
        .drop("type")
    )

    close_times = (
        open_close_times.filter(open_close_times.type == "close")
        .withColumn("time", f.lower(f.date_format(open_close_times.time, "ha")))
        .withColumnRenamed("time", "close")
        .drop("type")
    )

    locations = (
        clean_restaurants.drop("timezone")
        .join(groups, groups.location_id == clean_restaurants.id)
        .drop("location_id")
        .withColumnRenamed("group_name", "group")
        .join(open_times, open_times.location_id == clean_restaurants.id)
        .drop("location_id")
        .join(close_times, close_times.location_id == clean_restaurants.id)
        .drop("location_id")
    )

    hourly_sales = (
        transactions.join(
            restaurants.select(
                restaurants.id.alias("location_id"), restaurants.timezone
            ),
            "location_id",
        )
        .withColumn(
            "timezone",
            f.when(f.col("timezone") == "Central Time", "America/Chicago")
            .when(f.col("timezone") == "Eastern Time", "America/New_York")
            .when(f.col("timezone") == "Mountain Time", "America/Denver")
            .when(f.col("timezone") == "Hawaii-Aleutian Time", "Pacific/Honolulu")
            .when(f.col("timezone") == "Pacific Time", "America/Los_Angeles"),
        )
        .withColumn(
            "local_time",
            f.date_trunc(
                "hour",
                f.from_unixtime(transactions.unix_timestamp),
            ),
        )
        .withColumn(
            "offset",
            (
                f.unix_timestamp(f.col("local_time"))
                - f.unix_timestamp(
                    f.convert_timezone(
                        f.col("timezone"), f.lit("UTC"), f.col("local_time")
                    )
                )
            )
            / 3600,
        )
        .withColumn(
            "local_time",
            f.concat(
                f.col("local_time"),
                f.lit(f.when(f.col("offset") >= 0, "+").otherwise("-")),
                f.lpad(f.abs(f.col("offset")).cast("int"), 2, "0"),
                f.lit(":00"),
            ),
        )
        .drop("offset", "timezone", "unix_timestamp", "description")
        .groupBy("local_time", "location_id")
        .agg(
            f.count(f.col("transaction_id")).alias("total_orders"),
            f.sum(f.col("amount")).alias("total_sales"),
        )
    )
    return locations, hourly_sales


if __name__ == "__main__":
    spark = spark_session()
    settings = get_settings()

    source_url = build_url(settings.DB1_HOST, settings.DB1_HOST, settings.DB1_NAME)
    target_url = build_url(settings.DB2_HOST, settings.DB2_HOST, settings.DB2_NAME)

    def get_table(name: str) -> DataFrame:
        return (
            spark.read.format("jdbc")
            .option("url", source_url)
            .option("dbtable", name)
            .option("user", settings.DB1_USER)
            .option("password", settings.DB1_PASSWORD)
            .option("driver", "org.postgresql.Driver")
            .load()
        )

    def write_table(df: DataFrame, name: str) -> None:
        (
            df.write.format("jdbc")
            .option("url", target_url)
            .option("dbtable", name)
            .option("user", settings.DB2_USER)
            .option("password", settings.DB2_PASSWORD)
            .option("driver", "org.postgresql.Driver")
            .save()
        )

    ## --------- MAIN LOGIC ---------

    restaurants = get_table("restaurants")
    open_close_times = get_table("open_close_times")
    groups = get_table("groups")
    transactions = get_table("transactions")

    locations, hourly_sales = main(restaurants, open_close_times, groups, transactions)

    write_table(locations, "locations")
    write_table(hourly_sales, "hourly_sales")
