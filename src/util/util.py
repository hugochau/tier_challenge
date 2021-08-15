"""
util.py

Defines util functions
"""

import sys
import os
import functools
from inspect import getframeinfo, stack
from typing import Callable

from pyspark.sql.types import StructType

from config.schema import (
    TRACK_EVENTS_MAPPING,
    WEATHER_DF_DTYPES,
    WEATHER_PG_DTYPES,
    WEATHER_MAPPING,
    TRACK_EVENTS_DF_DTYPES,
    TRACK_EVENTS_PG_DTYPES,
    TRACK_EVENTS_MAPPING,
    TEST_PG_DTYPES
)
from module.logger.logger import Logger


def log_item(func: Callable) -> Callable:
    """
    Logging decorator

    args:
        - decorated function

    returns
        - wrapper around function
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = Logger().logger # get a logger

        # creating a list of positional args
        # repr() is similar but more precise than str()
        args_str = [repr(a) for a in args]
        # creating a list of keyword args
        # f-string formats each arg as key=value
        # where the !r specifier means that repr()
        # is used to represent the value
        kwargs_str = [f"{k}={v!r}" for k, v in kwargs.items()]
        basic_args = ", ".join(args_str + kwargs_str)

        # generate file/function name for calling functions
        # __func.name__ will give the name of the caller function
        # ie. wrapper and caller file name ie log_item.py
        # using extra param to get the actual function name
        # by leveraging inspect.getframeinfo
        pyfile = getframeinfo(stack()[1][0])
        extra_args = {
            'func_name_override': f'{func.__globals__["__name__"]}.{func.__name__}',
            'file_name_override': os.path.basename(pyfile.filename)
        }

        # executing function and logging args
        if basic_args:
            logger.info(f"begin function, args: {basic_args}", extra=extra_args)
        else:
            logger.info(f"begin function, no arg", extra=extra_args)
        try:
            value = func(*args, **kwargs)
            if value:
                logger.info(f"end function, returned {value!r}", extra=extra_args)
            else:
                logger.info(f"end function, no return", extra=extra_args)

            return value
        except:
            # log error if fails but don't raise
            logger.error(f"exception: {str(sys.exc_info()[1])}", extra=extra_args)
            pass

    return wrapper


def get_df_types(filename: str) -> StructType:
    """
    Get DataFrame dtypes

    args:
        - filename: file to load

    returns:
        - pyspark StructType
    """
    if filename == 'weather.json':
        return WEATHER_DF_DTYPES

    elif filename == 'track_events.json':
        return TRACK_EVENTS_DF_DTYPES


def get_pg_types(table: str) -> str:
    """
    Get postgreSQL dtypes

    args:
        - filename: file to load

    returns:
        - postgres data types, similar as in a create script
    """
    if table == 'weather':
        return WEATHER_PG_DTYPES

    elif table == 'track_events':
        return TRACK_EVENTS_PG_DTYPES

    elif table == 'test':
        return TEST_PG_DTYPES


def get_new_names(filename: str) -> list:
    """
    Get postgreSQL dtypes

    args:
        - filename: file to load

    returns:
        - mapping list
    """
    if filename == 'weather.json':
        return WEATHER_MAPPING

    elif filename == 'track_events.json':
        return TRACK_EVENTS_MAPPING
