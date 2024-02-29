import time

import mysql.connector, psycopg2

def run_query(cursor, query, iterations):
    runtime_totals = 0.0

    for _ in range(iterations):
        start_time = time.time()
        cursor.execute(query)
        end_time = time.time()
        runtime_totals += (end_time - start_time)
        # Clear the buffer for the next run
        cursor.fetchall()

    return runtime_totals / iterations

def benchmark_query(mysql_cursor, postgres_cursor, query, iterations):
    print(f"Benchmarking query: \n{query}\niterations: {iterations}")
    print("Average runtime MySQL: ", run_query(mysql_cursor, query, iterations))
    print("Average runtime Postgres: ", run_query(postgres_cursor, query, iterations))

# Connect to PostgreSQL database and create cursor
postgres_conn = psycopg2.connect(
    host="localhost",
    user="benchmark_user",
    password="password",
    database="benchmark_db"
)
postgres_cursor = postgres_conn.cursor()

# Connect to MySQL database and create cursor
mysql_conn = mysql.connector.connect(
    host="localhost",
    user="benchmark_user",
    password="password",
    database="benchmark_db"
)
mysql_cursor = mysql_conn.cursor()

# Set iterations for benchmark
iterations = 1000

# Benchmark queries that involve a single table
# Run with WHERE query, ORDER BY query, and WHERE with ORDER BY query
where_query = "SELECT * FROM users WHERE email LIKE '%gmail%'"
benchmark_query(mysql_cursor, postgres_cursor, where_query, iterations)

order_by_query = "SELECT * FROM users ORDER BY phone_number"
benchmark_query(mysql_cursor, postgres_cursor, order_by_query, iterations)

where_with_order_by_query = "SELECT * FROM users WHERE email LIKE '%gmail%' ORDER BY phone_number"
benchmark_query(mysql_cursor, postgres_cursor, where_with_order_by_query, iterations)

# Benchmark queries that involve a single table
single_inner_join_query = "SELECT * FROM users INNER JOIN orders ON users.id = orders.id"
benchmark_query(postgres_cursor, single_left_join_query, iterations)

single_left_join_query = "SELECT * FROM users LEFT JOIN orders ON users.id = orders.id"
benchmark_query(mysql_cursor, postgres_cursor, single_left_join_query, iterations)

single_right_join_query = "SELECT * FROM users RIGHT JOIN orders ON users.id = orders.id"
benchmark_query(mysql_cursor, postgres_cursor, single_right_join_query, iterations)
# single_full_join_query = "SELECT * FROM users FULL JOIN orders ON users.id = orders.id"
# benchmark_query(mysql_cursor, postgres_cursor, single_full_join_query, iterations)

# Benchmark queries that involve a single table

# Benchmark queries that involve a single table

# Close connections and cursors
