-- Drop the database if it exists
DROP DATABASE IF EXISTS benchmark_db;

-- Droper the database user if it exists
DROP ROLE IF EXISTS benchmark_user;

-- Create a new user
CREATE USER benchmark_user WITH PASSWORD 'password';

-- Grant the ability to create databases
ALTER USER benchmark_user CREATEDB;

-- Create a new database
CREATE DATABASE benchmark_db;

-- Connect to the default PostgreSQL database (usually 'postgres')
\c postgres;

-- Grant necessary privileges to the new user on the current database
GRANT ALL PRIVILEGES ON DATABASE benchmark_db TO benchmark_user;

-- Connect to the target database
\c benchmark_db;

-- Grant permissions to create tables
GRANT CREATE, CONNECT ON DATABASE benchmark_db TO benchmark_user;

-- Grant permissions to load data into tables
GRANT INSERT, SELECT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO benchmark_user;
