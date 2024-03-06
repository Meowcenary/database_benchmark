# Postgres Mysql Benchmark Scripts
This repository contains Python scripts for programmatically creating tables for
Postgres and MySQL, scripts to create fake data to load into the created tables,
and scripts to benchmark queries of different complexities run on the two
databases.

### Setup
This project uses Python 3.8 and Pipenv to manage dependencies. From the project
directory run the following to install pipenv and the Python dependencies:
```
pip install pipenv
pipenv install
```

You will also need to install MySQL and PostgreSQL. The benchmarking scripts
provided were written for usage with the packages `mysql` and `postgresql@13`
provided by the package manager [Homebrew](https://brew.sh/) and make use of
homebrew CLI commands. The scripts can be easily modified to work on any
operating system that provides a command line interface for starting and
stopping the database softwares used.

Once you have installed the necessary software, you can run the following
commands to create the testing databases and database users:

Postgres: `psql -h localhost -d postgres -U postgres -f create_postgres.sql`

Mysql: `mysql -u root < create_mysql.sql`

The above commands are included in the provided benchmarking scripts, but are
useful to be aware of for debugging when making modifications.

### Running the Scripts

#### Data Generation:
The script `load_data.py` is used to create reecords with the library [Faker](https://pypi.org/project/Faker/24.0.0/):

`pipenv run python3 load_data.py <number of records to create>`

For example, to create10,000 reecords for each database:

`pipenv run python3 load_data.py 10000`

For the script to work properly without modification

#### Benchmarking:
There are three bash scripts provided for benchmarking:
- `run_full_benchmark.sh` will benchmark both Postgres and MySQL
- `run_mysql_benchmarks.sh` will benchmark only MySQL
- `run_postgres_benchmarks.sh` will benchmark only Postgres

It's recommended to redirect output from these scripts to a text file. For
example:

`bash run_full_benchmark.sh > full_benchmark_output.txt`

The scripts can be easily modified as necessary for specific benchmarking tasks:
- To use other package managers modifiy commands that use `brew` to use the
specific package manager
- To modify the amount of data to use for each test of the benchmark change the
argument passed to `load_data.py` wherever it appears in these scripts to the
amount of records necessary for each test
- To increase or decrease the number of benchmark tests either copy and paste a
benchmarking block or remove it entirely from the bash script in use modifiyng
the echo statementes to reflect the change
- To change the number of iterations per a query for the benchmarks modify the
variable `iterations` within `benchmark_mysql.py` and `benchmark_postgres.py`
- To change the number of trials kept or discarded modify the assignment of the
variable runtimes within `benchmark_mysql.py` and `benchmark_postgres.py`
