-- Drop the database if it exists
DROP DATABASE IF EXISTS benchmark_db;

-- Drop the database user if it exists
DROP USER IF EXISTS 'benchmark_user'@'localhost';

-- Create a new user
CREATE USER 'benchmark_user'@'localhost' IDENTIFIED BY 'password';

-- Create a new database
CREATE DATABASE benchmark_db;

-- Grant necessary privileges to the new user on the current database
GRANT ALL PRIVILEGES ON benchmark_db.* TO 'benchmark_user'@'localhost';

-- Connect to the target database
USE benchmark_db;

-- Grant permissions to create tables
GRANT CREATE, ALTER, INDEX, DROP, CREATE TEMPORARY TABLES, CREATE VIEW, EVENT, TRIGGER, SHOW VIEW ON benchmark_db.* TO 'benchmark_user'@'localhost';

-- Grant permissions to load data into tables
GRANT INSERT, SELECT, UPDATE, DELETE ON benchmark_db.* TO 'benchmark_user'@'localhost';
