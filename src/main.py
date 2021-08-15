"""
main.py

Defines main function
"""

__version__ = '1.0'
__author__ = 'Hugo Chauvary'
__email__ = 'chauvary.hugo@gmail.com'

from module import *


def main() -> None:
    # parse args
    args = Parser.parse()

    # spark session
    spark = Spark.session()

    # load data
    df = Data(spark, args.filename).load()

    # write df to postgres
    Postgres(spark).write(df, args.filename)

    # stop session
    spark.stop()


if __name__ == '__main__':
    main()
