#
# This script makes use of homebrew and the brew packages postgresql@13 and mysql
# The script can be run with bash run_mysql_benchmarks.sh
#
echo Ensuring correct databases services are running
brew services stop postgresql@13
brew services start mysql

echo Creating database
mysql -u root < create_mysql.sql

echo Creating tables
pipenv run python3 create_mysql_tables.py

echo Loading data for benchmark test 1 - 1,000 records per table
# Load 10,000 records per table
pipenv run python3 load_data.py 1000

echo -------------------------------
echo Benchmarking MySQL test 1
pipenv run python3 benchmark_mysql.py
echo -------------------------------

echo Loading data for benchmark test 2 - 4,000 records per table
pipenv run python3 load_data.py 3000

echo -------------------------------
echo Benchmarking MySQL test 2
pipenv run python3 benchmark_mysql.py
echo -------------------------------

echo Loading data for benchmark test 3 - 7,000 records per table
pipenv run python3 load_data.py 3000

echo -------------------------------
echo Benchmarking MySQL test 3
pipenv run python3 benchmark_mysql.py
echo -------------------------------

echo Loading data for benchmark test 4 - 10,000 records per table
pipenv run python3 load_data.py 3000

echo -------------------------------
echo Benchmarking MySQL test 4
pipenv run python3 benchmark_mysql.py
echo -------------------------------
echo
echo Benchmark Complete
