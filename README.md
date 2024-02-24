# Postgres Mysql Benchmark Scripts
This repository contains Python scripts for programmatically creating tables for
Postgres and MySQL, scripts to create fake data to load into the created tables,
and scripts to benchmark queries of different complexities run on the two
databases.

### Setup
This project uses Python 3.8 and Pipenv to manage dependencies. You will also
need to install MySQL and PostgreSQL. Once you have installed the software you can run
these command to create the testing database and database user:

Postgres: `psql -h localhost -d postgres -U postgres -f create_postgres.sql`

Mysql: `mysql -u root < create_mysql.sql`

### Running the scripts
**Data Generation:**

Postgres: `pipenv run create_and_load_postgres_data.py`

Mysql: `pipenv run create_and_load_mysql_data`

**Benchmarking:**

Postgres: `pipenv run ...`

MySQL: `pipenv run ...`
