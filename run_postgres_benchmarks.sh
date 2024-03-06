#
# This script makes use of homebrew and the brew packages postgresql@13 and mysql
# The script can be run with bash run_postgres_benchmarks.sh
#
echo Ensuring correct databases services are running
brew services stop mysql
brew services start postgresql@13

echo Creating database
psql -h localhost -d postgres -U root -f create_postgres.sql

echo Creating tables
pipenv run python3 create_postgres_tables.py

echo Loading data for benchmark test 1 - 1,000 records per table
# Load 10,000 records per table
pipenv run python3 load_data.py 1000

echo
echo -------------------------------
echo Benchmarking Postgres test 1
pipenv run python3 benchmark_postgres.py
echo -------------------------------

echo
echo Loading data for benchmark test 2 - 4,000 records per table
pipenv run python3 load_data.py 3000

echo
echo -------------------------------
echo Benchmarking Postgres test 2
pipenv run python3 benchmark_postgres.py
echo -------------------------------

echo
echo Loading data for benchmark test 3 - 7,000 records per table
pipenv run python3 load_data.py 3000

echo
echo -------------------------------
echo Benchmarking Postgres test 3
pipenv run python3 benchmark_postgres.py
echo -------------------------------

echo
echo Loading data for benchmark test 4 - 10,000 records per table
pipenv run python3 load_data.py 3000

echo
echo -------------------------------
echo Benchmarking Postgres test 4
pipenv run python3 benchmark_postgres.py
echo -------------------------------
echo
echo Benchmark Complete
