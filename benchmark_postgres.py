"""
Script to benchmark postgres queries
"""

import time

import psycopg2

def run_query(cursor, query, iterations):
    runtimes = []

    for _ in range(iterations):
        start_time = time.time()
        cursor.execute(query)
        end_time = time.time()
        runtime_milliseconds = (end_time - start_time)*1000
        runtimes.append(runtime_milliseconds)
        # Clear the buffer for the next run
        cursor.fetchall()

    return runtimes

def benchmark_query(cursor, query, iterations):
    print(f"Benchmarking query: \n{query}\niterations: {iterations}")
    runtimes = sorted(run_query(cursor, query, iterations))
    # discard 100 lowest and 100 highest
    runtimes = runtimes [10:-10]
    print("Average runtime: ", sum(runtimes)/len(runtimes))

# Connect to PostgreSQL database and create cursor
postgres_conn = psycopg2.connect(
    host="localhost",
    user="benchmark_user",
    password="password",
    database="benchmark_db"
)
postgres_cursor = postgres_conn.cursor()

# Set iterations for benchmark
iterations = 100

# Benchmark queries that involve a single table
# Run with WHERE query, ORDER BY query, and WHERE with ORDER BY query
where_query = "SELECT * FROM users WHERE email LIKE '%gmail%'"
benchmark_query(postgres_cursor, where_query, iterations)

order_by_query = "SELECT * FROM users ORDER BY phone_number"
benchmark_query(postgres_cursor, order_by_query, iterations)

where_with_order_by_query = "SELECT * FROM users WHERE email LIKE '%gmail%' ORDER BY phone_number"
benchmark_query(postgres_cursor, where_with_order_by_query, iterations)

#
# Benchmark queries that involve a single join of two tables
#
single_inner_join_query = "SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id"
benchmark_query(postgres_cursor, single_inner_join_query, iterations)

single_left_join_query = "SELECT * FROM users LEFT JOIN orders ON users.id = orders.user_id"
benchmark_query(postgres_cursor, single_left_join_query, iterations)

single_right_join_query = "SELECT * FROM users RIGHT JOIN orders ON users.id = orders.user_id"
benchmark_query(postgres_cursor, single_right_join_query, iterations)

single_inner_join_query_with_where = "SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id WHERE email LIKE '%gmail%'"
benchmark_query(postgres_cursor, single_inner_join_query_with_where, iterations)

single_inner_join_query_with_order_by_query = "SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id ORDER BY phone_number"
benchmark_query(postgres_cursor, single_inner_join_query_with_order_by_query, iterations)

single_inner_join_query_with_where_and_order_by_query = "SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id WHERE email LIKE '%gmail%' ORDER BY phone_number"
benchmark_query(postgres_cursor, single_inner_join_query_with_where_and_order_by_query, iterations)

#
# Benchmark queries that involve two joins of three tables
#
double_inner_join_query = "SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id INNER JOIN products ON orders.product_id = products.id"
benchmark_query(postgres_cursor, double_inner_join_query, iterations)

double_left_join_query = "SELECT * FROM users LEFT JOIN orders ON users.id = orders.user_id LEFT JOIN products ON orders.product_id = products.id"
benchmark_query(postgres_cursor, double_left_join_query, iterations)

double_right_join_query = "SELECT * FROM users RIGHT JOIN orders ON users.id = orders.user_id RIGHT JOIN products ON orders.product_id = products.id"
benchmark_query(postgres_cursor, double_right_join_query, iterations)

double_inner_join_with_where_query = "SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id INNER JOIN products ON orders.product_id = products.id WHERE email LIKE '%gmail%'"
benchmark_query(postgres_cursor, double_inner_join_with_where_query, iterations)

double_inner_join_query_with_order_by_query = "SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id INNER JOIN products ON orders.product_id = products.id ORDER BY phone_number"
benchmark_query(postgres_cursor, double_inner_join_query_with_order_by_query, iterations)

double_inner_join_query_with_where_and_order_by_query = "SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id INNER JOIN products ON orders.product_id = products.id WHERE email LIKE '%gmail%' ORDER BY phone_number"
benchmark_query(postgres_cursor, double_inner_join_query_with_where_and_order_by_query, iterations)

#
# Benchmark queries that involve three joins of four tables
#
triple_inner_join_query = "SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id INNER JOIN products ON orders.product_id = products.id INNER JOIN vendors ON products.vendor_id = vendors.id"
benchmark_query(postgres_cursor, triple_inner_join_query, iterations)

triple_left_join_query = "SELECT * FROM users LEFT JOIN orders ON users.id = orders.user_id LEFT JOIN products ON orders.product_id = products.id LEFT JOIN vendors ON products.vendor_id = vendors.id"
benchmark_query(postgres_cursor, triple_left_join_query, iterations)

triple_right_join_query = "SELECT * FROM users RIGHT JOIN orders ON users.id = orders.user_id RIGHT JOIN products ON orders.product_id = products.id RIGHT JOIN vendors ON products.vendor_id = vendors.id"
benchmark_query(postgres_cursor, triple_right_join_query, iterations)

triple_inner_join_query_with_where_query = "SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id INNER JOIN products ON orders.product_id = products.id INNER JOIN vendors ON products.vendor_id = vendors.id WHERE email LIKE '%gmail%'"
benchmark_query(postgres_cursor, triple_inner_join_query_with_where_query, iterations)

triple_inner_join_query_with_order_by_query = "SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id INNER JOIN products ON orders.product_id = products.id INNER JOIN vendors ON products.vendor_id = vendors.id ORDER BY phone_number"
benchmark_query(postgres_cursor, triple_inner_join_query_with_order_by_query, iterations)

triple_innner_join_query_with_where_and_and_order_by_query = "SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id INNER JOIN products ON orders.product_id = products.id INNER JOIN vendors ON products.vendor_id = vendors.id WHERE email LIKE '%gmail%' ORDER BY phone_number"
benchmark_query(postgres_cursor, triple_innner_join_query_with_where_and_and_order_by_query, iterations)

postgres_cursor.close()
postgres_conn.close()
