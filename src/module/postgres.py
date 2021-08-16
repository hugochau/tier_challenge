"""
postgres.py

Defines Postgres
"""

from pyspark.sql.dataframe import DataFrame
from pyspark.sql import SparkSession

from util.util import get_pg_types
from config.constant import PGHOST

class Postgres:
    def __init__(self, spark: SparkSession) -> None:
        """
        Class constructor

        args:
            - spark: spark session
        """
        self.spark = spark


    def write(self, df: DataFrame, table: str) -> None:
        """
        Writes spark DataFrame to table

        args:
            - df: data to be inserted
            - table: target table in RDBMS
        """
        url = f"jdbc:postgresql://{PGHOST}/tier"
        properties = {
            "user": "tier"
        }

        df.write \
            .option("driver", "org.postgresql.Driver") \
            .option("createTableColumnTypes", get_pg_types(table)) \
            .jdbc(url=url,
                  table=table,
                  mode='overwrite',
                  properties=properties)


    # def read(table):
    #     """
    #     """
    #     df = self.spark.read \
    #         .format("jdbc") 
    #         .option("url", "jdbc:postgresql:dbserver")
    #         .option("dbtable", "schema.tablename")
    #         .option("user", "username")
    #         .option("password", "password")
    #         .load()
