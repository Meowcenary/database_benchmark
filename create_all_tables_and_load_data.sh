psql -h localhost -d postgres -U postgres -f create_postgres.sql
mysql -u root < create_mysql.sql
pipenv run python3 create_postgres_tables.py
pipenv run python3 create_mysql_tables.py
pipenv run python3 load_data.py
