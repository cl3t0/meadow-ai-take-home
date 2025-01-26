from pyspark.sql import DataFrame
from syrupy.assertion import SnapshotAssertion

from job import main


def test_main(
    restaurants: DataFrame,
    open_close_times: DataFrame,
    groups: DataFrame,
    transactions: DataFrame,
    snapshot: SnapshotAssertion,
) -> None:

    locations, hourly_sales = main(restaurants, open_close_times, groups, transactions)

    assert locations.orderBy("id").collect() == snapshot
    assert hourly_sales.orderBy("location_id", "local_time").collect() == snapshot
