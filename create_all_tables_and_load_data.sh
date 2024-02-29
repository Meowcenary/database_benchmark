# Create users and databases within datagbase software
psql -h localhost -d postgres -U postgres -f create_postgres.sql
mysql -u root < create_mysql.sql

# Create tables for databases
pipenv run python3 create_postgres_tables.py
pipenv run python3 create_mysql_tables.py

# Load 1000 records
pipenv run python3 load_data.py 1000
