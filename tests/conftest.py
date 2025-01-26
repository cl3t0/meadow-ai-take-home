from pyspark.sql import SparkSession, DataFrame
import pytest

from utils import spark_session


@pytest.fixture
def spark() -> SparkSession:
    return spark_session()


@pytest.fixture
def restaurants(spark: SparkSession) -> DataFrame:
    return spark.createDataFrame(
        [
            (1, " McDees", "Houston  ", "TX", "123 Cowboy Dr", "Central Time"),
            (
                2,
                " Pizzas To Go  ",
                " new York",
                "NY",
                "456 Times Square",
                "Eastern Time",
            ),
        ],
        schema=["id", "name", "city", "state", "address1", "timezone"],
    )


@pytest.fixture
def open_close_times(spark: SparkSession) -> DataFrame:
    return spark.createDataFrame(
        [
            (1, "open", "09:00:00"),
            (1, "close", "20:00:00"),
            (2, "open", "10:00:00"),
            (2, "close", "22:00:00"),
        ],
        schema=["location_id", "type", "time"],
    )


@pytest.fixture
def groups(spark: SparkSession) -> DataFrame:
    return spark.createDataFrame(
        [(1, "blue"), (2, "green")], schema=["location_id", "group_name"]
    )


@pytest.fixture
def transactions(spark: SparkSession) -> DataFrame:
    return spark.createDataFrame(
        [
            ("b9f2197b-2a1", 23.59, 1735765500, "fries and milkshake", 1),
            ("ec19d9e7-880", 97.34, 1735742280, "grilled chicken sandwich", 1),
            ("f54c9626-be2", 25.87, 1735772100, "soda", 1),
            ("c9d11c3b-7dc", 75.17, 1735767480, "water", 1),
            ("80776e23-7b1", 34.25, 1735771020, "coffee", 1),
            ("e632b7fd-4e7", 57.11, 1735743360, "steak", 1),
            ("6272f5e1-379", 12.2, 1735741920, "coffee", 1),
            ("a6203b15-205", 63.47, 1735740540, "cheese pizza", 1),
            ("73f6bcff-183", 44.01, 1735768740, "burgers", 1),
            ("0d48c8be-db9", 71.32, 1735752780, "iced coffee", 1),
            ("c8594773-f10", 58.99, 1735772340, "coffee", 1),
            ("36f205a4-068", 43.05, 1735777440, "steak", 2),
            ("f2a40bf8-ad3", 82.47, 1735773240, "dessert", 2),
            ("ddc2b44e-5d3", 11.58, 1735757400, "water", 2),
            ("5360db5f-17c", 58.24, 1735770900, "soda", 2),
            ("48509e4b-92c", 89.21, 1735760280, "steak", 2),
            ("570967de-b26", 22.54, 1735778520, "soda", 2),
            ("1c4ccbf8-911", 32.53, 1735761300, "dessert", 2),
            ("2e697bae-a1d", 94.05, 1735777860, "grilled chicken sandwich", 2),
            ("83cd658d-11a", 70.79, 1735755600, "hot dog", 2),
            ("8c7805b2-c36", 8.59, 1735764840, "coffee", 2),
        ],
        schema=[
            "transaction_id",
            "amount",
            "unix_timestamp",
            "description",
            "location_id",
        ],
    )
