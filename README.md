# Tier coding challenge

Tier Coding Challenge aims at giving the Senior Data Engineers candidates an idea about what kind of challenges would await while working at Tier.

## Prerequisite

To be able to run this app, you must have [Docker](https://docs.docker.com/get-docker/) installed on your machine.

Set up the following environement variable:
- `$PGHOST`: postgresql host - the docker VM IP

Input data files are not included in the repository. Copy them into `data`.

NB: How to determine VM IP:
```bash
# solution 1
docker rum --rm --net host alpine ip address

# solution 2
docker-machine ip default
```


## Installation

Run the following commands under package root.

```bash
cd docker
docker-compose build
```

## Structure

```bash
tree .

.
├── LICENSE
├── README.md
├── data
│   ├── __MACOSX
│   ├── blank
│   ├── log
│   │   ├── blank
│   ├── track_events.json
│   ├── weather.json
├── doc
│   └── challenge_requirements.pdf
├── docker
│   ├── docker-compose.yml
│   ├── postgres
│   │   ├── Dockerfile
│   │   └── init_db.sh
│   └── python
│       ├── Dockerfile
│       ├── requirements.txt
│       └── start.sh
└── src
    ├── config
    │   ├── constant.py
    │   └── schema.py
    ├── main.py
    ├── main.sh
    ├── module
    │   ├── __init__.py
    │   ├── data.py
    │   ├── logger
    │   │   ├── __init__.py
    │   │   ├── _formatter.py
    │   │   ├── adapter.py
    │   │   └── logger.py
    │   ├── parser.py
    │   ├── postgres.py
    │   └── spark.py
    ├── test.py
    └── util
        └── util.py
```

## Usage

Run the following commands:

```bash
cd docker
# will create two microservices
# tier_python and tier_postgres 
docker-compose up
```

For accessing tier_python in bash mode - useful for validating results:

```bash
docker-compose run --service-ports python bash

psql \
  -h $PGHOST \
  -d tier \
  -U tier \
  -p 5432

# sample queries
# count rows
select count(*) from weather

# list tables
\dt+
```

## Implementation

For the sake of simplicity and scalability, the code follows an object-oriented approach:
- classes are stored in the `src/module` folder
- utility functions in `src/util`
- constants and config files in `src/config`

`src/main.py` provides the main function.

From a high level perspective, the main function is implemented as follows:
  - parse CLI arguments
  - define spark session
  - load data into spark DataFrame
  - insert result to RDBMS table
  - stop spark session

Logs are saved under `data/log`. A logging decorator is defined in `util.log_item` and can be used throughout the code.


## Improvements

Further improvements to the code, listed below:

- Unit tests could be implemented in place of `test.py`.

- The logging module is not yet used at its full capacity. Suggested improvements:
  - Capture `pyspark` stdout output
  - Enrich log record with additional attributes
  - Add `logging.info` messages throughout the code, if need be.
  - Decorate other methods

## Case Study

The idea is to capture those events from mutliple event streams, write them into the datalake and ultimately ingest a subset into a datawarehouse.

One can build such architecture in an AWS ecosystem, by leveraging the following services:
- Kinesis - collecting the streaming data
- Firehose - loading data into the data lake
- S3 - hosting the data lake
- Glue - building and scheduling the ELT jobs
- RDS - hosting the RDBMS

Key takeaways from the proposed architecture:
- These are managed services. This is not the most cost efficient approach. However, it makes it easy to scale up and drastically decreases the maintenance effort.
- Numbers of Kinesis shards must be properly defined. Underestimation would result in data loss whereas overestimating would result in money loss.
- Kinesis processes events in order. There should be no data loss, assuming the system is well designed. Main delivery KPIs can be monitored on AWS Cloudwatch.
- For a better integration to any project in the Hadoop ecosystem, Firehouse should deliver the data to the data lake in a parquet format.
- Amazon S3 is a decent approach for building a data lake because of its virtually unlimited scalability.
- Glue is well designed for data flows within the AWS ecosystem.
- Selected RDBMS could be postgreSQL based - native or Redshift.

Alternative:
- Apache Kafka for capturing events
- S3 for storing the data
- Spark for aggregating data into the DWH
- Airflow for orchestrating data flows

As opposed to managed services, open source alternatives should certainly decrease the overall infrastructure cost. However it should result in an extra maintenance effort.

## License
This product is licensed under the [MIT](https://choosealicense.com/licenses/mit/) license.

## Contact

Please reach out to chauvary.hugo@gmail.com

# Thank you!
