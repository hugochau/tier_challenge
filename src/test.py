"""
test.py

Defines tests functions
"""

__version__ = '1.0'
__author__ = 'Hugo Chauvary'
__email__ = 'chauvary.hugo@gmail.com'

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType
)

from module import *
from module.logger import *


# logger
def test_logger():
    logger = Logger().logger
    logger.info("test")


# parser
def test_parser_parse():
    args = Parser().parse()

    print(args.filename)


# spark
def test_spark_constructor():
    return Spark.session()


# data
def test_data_load():
    spark = Spark.session()
    data = Data(spark, 'weather')
    df = data.load()

    df.printSchema()

# postgres
def test_postgres_write():
    spark = Spark.session()
    df = [
        ('James', 'Smith', '1991-04-01','M',3000),
        ('Michael','Rose','2000-05-19','M',4000),
        ('Robert', 'Williams','1978-09-05','M',4000),
        ('Maria','Jones','1967-12-01','F',4000),
        ('Jen','Brown','1980-02-17','F',-1)
    ]
    schema = StructType([
        StructField('firstname', StringType(), True),
        StructField('lastname', StringType(), True),
        StructField('dob', StringType(), True),
        StructField('gender', StringType(), True),
        StructField('salary', IntegerType(), True)
    ])

    df = spark.createDataFrame(data=df,
                               schema=schema)

    pg = Postgres(spark)
    pg.write(df, 'test')


if __name__ == '__main__':
    # test_parser_parse
    # test_logger()

    # # test_parser_parse
    # test_parser_parse()

    # # test_spark_constructor
    test_spark_constructor()

    # # test_data_load
    # test_data_load()

    # # test_postgres_write
    # test_postgres_write()
