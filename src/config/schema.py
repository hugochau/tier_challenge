"""
schema.py

Defines schemas
"""

__version__ = '1.0'
__author__ = 'Hugo Chauvary'
__email__ = 'chauvary.hugo@gmail.com'


from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType,
    TimestampType
)

# spark df dtypes
WEATHER_DF_DTYPES = StructType([
    StructField("weather_data.city", StringType(), True),
    StructField("weather_data.currently_apparenttemperature", DoubleType(), True),
    StructField("weather_data.currently_humidity", DoubleType(), True),
    StructField("weather_data.currently_precipintensity", DoubleType(), True),
    StructField("weather_data.currently_precipprobability", DoubleType(), True),
    StructField("weather_data.currently_preciptype", StringType(), True),
    StructField("weather_data.currently_temperature", DoubleType(), True),
    StructField("weather_data.currently_visibility", DoubleType(), True),
    StructField("weather_data.currently_windspeed", DoubleType(), True),
    StructField("weather_data.date_time", TimestampType(), True)
])

TRACK_EVENTS_DF_DTYPES = StructType([
    StructField("segment_tracks.anonymous_id", StringType(), True),
    StructField("segment_tracks.context_app_build", StringType(), True),
    StructField("segment_tracks.context_app_name", StringType(), True),
    StructField("segment_tracks.context_app_version", StringType(), True),
    StructField("segment_tracks.context_device_id", StringType(), True),
    StructField("segment_tracks.context_device_manufacturer", StringType(), True),
    StructField("segment_tracks.context_device_model", StringType(), True),
    StructField("segment_tracks.context_device_type", StringType(), True),
    StructField("segment_tracks.context_os_name", StringType(), True),
    StructField("segment_tracks.context_os_version", StringType(), True),
    StructField("segment_tracks.context_timezone", StringType(), True),
    StructField("segment_tracks.event_name", StringType(), True),
    StructField("segment_tracks.properties_rating", StringType(), True),
    StructField("segment_tracks.received_time", TimestampType(), True),
    StructField("segment_tracks.sent_time", TimestampType(), True)
])

# columns mapping
WEATHER_MAPPING = [
    'city',
    'apparenttemperature',
    'humidity',
    'precipintensity',
    'precipprobability',
    'preciptype',
    'temperature',
    'visibility',
    'windspeed',
    'date_time'
]

TRACK_EVENTS_MAPPING = [
    'anonymous_id',
    'app_build',
    'app_name',
    'app_version',
    'device_id',
    'device_manufacturer',
    'device_model',
    'device_type',
    'os_name',
    'os_version',
    'timezone',
    'event_name',
    'properties_rating',
    'received_time',
    'sent_time'
]

# pg dtypes
WEATHER_PG_DTYPES = """
city varchar(255),
apparenttemperature DECIMAL(6, 2),
humidity DECIMAL(6, 2),
precipintensity DECIMAL(6, 2),
precipprobability DECIMAL(6, 2),
preciptype varchar(255),
temperature DECIMAL(6, 2),
visibility DECIMAL(6, 2),
windspeed DECIMAL(6, 2),
date_time timestamp
"""

TRACK_EVENTS_PG_DTYPES = """
anonymous_id varchar(255),
app_build varchar(255),
app_name varchar(255),
app_version varchar(255),
device_id varchar(255),
device_manufacturer varchar(255),
device_model varchar(255),
device_type varchar(255),
os_name varchar(255),
os_version varchar(255),
timezone varchar(255),
event_name varchar(255),
properties_rating varchar(255),
received_time timestamp,
sent_time timestamp
"""

TEST_PG_DTYPES = """
firstname varchar(255),
lastname varchar(255),
dob varchar(255),
gender varchar(255),
salary integer
"""
