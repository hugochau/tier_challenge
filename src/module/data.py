"""
data.py

Defines Data
"""

__version__ = '1.0'
__author__ = 'Hugo Chauvary'
__email__ = 'chauvary.hugo@gmail.com'

from pyspark.sql.dataframe import DataFrame
from pyspark.sql import SparkSession

from config.constant import DATA_FOLDER
from util.util import get_df_types, get_new_names


class Data:
    def __init__(self, spark: SparkSession, filename: str) -> None:
        """
        Class constructor

        attributes:
            - spark: spark session
            - filename: file to load
            - schema: custom schema
        """
        self.spark = spark
        self.filename = f'{filename}.json'
        self.schema = get_df_types(self.filename)


    def load(self) -> DataFrame:
        """
        Read JSON file into dataframe

        returns:
            - df: loaded data into DataFrame object
        """
        # read file
        filepath = f'{DATA_FOLDER}/{self.filename}'
        # df = self.spark.read.json(filepath, multiLine=True)
        df = self.spark.read.schema(self.schema).json(filepath)

        df = df.toDF(*get_new_names(self.filename))

        return df
