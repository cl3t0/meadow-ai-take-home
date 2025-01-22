from typing import Tuple
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as f
from dotenv import load_dotenv
import os
import random
import time
import uuid
import datetime

load_dotenv()

spark = (
    SparkSession.builder.config("spark.driver.host", "127.0.0.1")
    .config("spark.jars", "./postgresql-42.7.5.jar")
    .appName("app")
    .getOrCreate()
)

SOURCE_URL = f"jdbc:postgresql://{os.getenv('DB1_HOST')}:{os.getenv('DB1_PORT')}/{os.getenv('DB1_NAME')}"


def get_table(name: str) -> DataFrame:
    return (
        spark.read.format("jdbc")
        .option("url", SOURCE_URL)
        .option("dbtable", name)
        .option("user", os.getenv("DB1_USER"))
        .option("password", os.getenv("DB1_PASSWORD"))
        .option("driver", "org.postgresql.Driver")
        .load()
    )


open_close_times = get_table("open_close_times")

open_times = (
    open_close_times.filter(open_close_times.type == "open")
    .withColumnRenamed("time", "open")
    .drop("type")
)

close_times = (
    open_close_times.filter(open_close_times.type == "close")
    .withColumnRenamed("time", "close")
    .drop("type")
)

open_close_times_joined = open_times.join(close_times, on="location_id").collect()

transactions_per_day = 200
days = 7

descriptions = [
    "burgers",
    "fries and milkshake",
    "cheese pizza",
    "grilled chicken sandwich",
    "iced coffee",
    "steak",
    "salad",
    "pasta",
    "soda",
    "water",
    "hot dog",
    "chicken wings",
    "dessert",
    "coffee",
]

start_time = datetime.datetime(2025, 1, 1)
transactions = []

for restaurant_id, open_time, close_time in open_close_times_joined:
    for day in range(days):
        for _ in range(
            int(random.uniform(transactions_per_day - 20, transactions_per_day + 20))
        ):
            # Generate random transaction details
            amount = round(
                random.uniform(5, 100), 2
            )  # Random transaction amount between $5 and $100
            transaction_time: datetime.datetime = random.uniform(open_time, close_time)  # type: ignore
            timestamp = int(
                time.mktime(
                    (
                        start_time
                        + datetime.timedelta(
                            days=day,
                            hours=transaction_time.hour,
                            minutes=transaction_time.minute,
                        )
                    ).timetuple()
                )
            )
            description = random.choice(descriptions)
            transaction_id = str(uuid.uuid4())[:12]  # Generate unique transaction ID

            transactions.append(
                (transaction_id, amount, timestamp, description, restaurant_id)
            )

# Generate the SQL insert statements
with open("mocks/insert_transactions.sql", "w") as f:
    f.write(
        "INSERT INTO transactions (transaction_id, amount, unix_timestamp, description, location_id) VALUES\n"
    )
    for i, t in enumerate(transactions):
        f.write(f"('{t[0]}', {t[1]}, {t[2]}, '{t[3]}', {t[4]})")
        if i < len(transactions) - 1:
            f.write(",\n")
        else:
            f.write(";\n")
