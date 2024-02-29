#
# This script makes use of homebrew and the brew packages postgresql@13 and mysql
# The script can be run with bash run_full_benchmark
#
echo Ensuring databases services are running
brew services start postgresql@13
brew services start mysql

echo Creating databases
psql -h localhost -d postgres -U root -f create_postgres.sql
mysql -u root < create_mysql.sql

echo Creating tables
pipenv run python3 create_postgres_tables.py
pipenv run python3 create_mysql_tables.py

### Test 1
echo Loading data for benchmark test 1 - 1,000 records per table
# Load 10,000 records per table
pipenv run python3 load_data.py 1000

echo
echo -------------------------------
echo Benchmarking Postgres test 1
brew services stop mysql
pipenv run python3 benchmark_postgres.py
echo -------------------------------

echo
echo -------------------------------
echo Benchmarking MySQL test 1
brew services start mysql
brew services stop postgresql@13
pipenv run python3 benchmark_mysql.py
echo -------------------------------

### Test 2
echo
echo Loading data for benchmark test 2 - 4,000 records per table
brew services start postgresql@13
# Load an additional 90,0000 records to get to 100,000 records per table
pipenv run python3 load_data.py 3000

echo -------------------------------
echo Benchmarking Postgres test 2
brew services stop mysql
pipenv run python3 benchmark_postgres.py
echo -------------------------------

echo
echo -------------------------------
echo Benchmarking MySQL test 2
brew services start mysql
brew services stop postgresql@13
pipenv run python3 benchmark_mysql.py
echo -------------------------------

### Test 3
echo
echo Loading data for benchmark test 3 - 7,000 records per table
brew services start postgresql@13
# Load an additional 100,000 records to get to 200,000 records per table
pipenv run python3 load_data.py 3000

echo
echo -------------------------------
echo Benchmarking Postgres test 3
brew services stop mysql
pipenv run python3 benchmark_postgres.py
echo -------------------------------

echo
echo -------------------------------
echo Benchmarking MySQL test 3
brew services start mysql
brew services stop postgresql@13
pipenv run python3 benchmark_mysql.py
echo -------------------------------

### Test 4
echo
echo Loading data for benchmark test 4 - 10,000 records per table
brew services start postgresql@13
# Load an additional 100,000 records to get to 300,000 records per table
pipenv run python3 load_data.py 3000

echo
echo -------------------------------
echo Benchmarking Postgres test 4
brew services stop mysql
pipenv run python3 benchmark_postgres.py
echo -------------------------------

echo
echo -------------------------------
echo Benchmarking MySQL test 4
brew services start mysql
brew services stop postgresql@13
pipenv run python3 benchmark_mysql.py
echo -------------------------------
echo Benchmark Complete
