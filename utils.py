from pyspark.sql import SparkSession
from dotenv import load_dotenv
from pydantic import BaseModel
import os

load_dotenv()


def spark_session() -> SparkSession:
    return (
        SparkSession.builder.config("spark.driver.host", "127.0.0.1")  # type: ignore
        .config("spark.jars", "./postgresql-42.7.5.jar")
        .config("spark.sql.session.timeZone", "UTC")
        .appName("app")
        .getOrCreate()
    )


def build_url(host: str, port: str, name: str) -> str:
    return f"jdbc:postgresql://{host}:{port}/{name}"


class Settings(BaseModel):
    DB1_HOST: str
    DB1_PORT: str
    DB1_USER: str
    DB1_PASSWORD: str
    DB1_NAME: str
    DB2_HOST: str
    DB2_PORT: str
    DB2_USER: str
    DB2_PASSWORD: str
    DB2_NAME: str


def get_settings() -> Settings:
    return Settings(**os.environ)
