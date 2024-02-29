'''
Script to create mutual data set to load into Postgres and Mysql databases for
benchmarking. Actual benchmarks are kept separate so they can be run again if necessary.
If changes to the data are needed modify CreateData class
'''
import sys

import mysql.connector, psycopg2

from create_data import CreateData

def load_data(cursor, create_data_instance, records_generated):
    for i in range(records_generated):
        cursor.execute("INSERT INTO users (name, email, phone_number) VALUES (%s, %s, %s)",
                       create_data_instance.users[i]
        )
        cursor.execute("INSERT INTO vendors (name, state, zip) VALUES (%s, %s, %s)",
                       create_data_instance.vendors[i]
        )
        cursor.execute("INSERT INTO products (vendor_id, name, description, price, \
                         stock_quantity) \
                       VALUES (%s, %s, %s, %s, %s)",
                       create_data_instance.products[i]
        )
        cursor.execute("\
            INSERT INTO orders (user_id, product_id, order_date, total_product, \
              shipping_address, payment_method, status) \
            VALUES (%s, %s, %s, %s, %s, %s, %s)",
            create_data_instance.orders[i]
        )



# Create data to be loaded into the databases
create_data_instance = CreateData()
# accept command line arg with number of record, default ot 10,000
records_to_generate = int(sys.argv[1]) or 10000
create_data_instance.generate_data(records_to_generate)

# Connect to PostgreSQL database
postgres_conn = psycopg2.connect(
    host="localhost",
    user="benchmark_user",
    password="password",
    database="benchmark_db"
)

# Load the Postgres data
load_data(postgres_conn.cursor(), create_data_instance, records_to_generate)

# Commit the changes and close the connection
postgres_conn.commit()
postgres_conn.close()

# Connect to MySQL database
mysql_conn = mysql.connector.connect(
    host="localhost",
    user="benchmark_user",
    password="password",
    database="benchmark_db"
)

# Load the MySQL data
load_data(mysql_conn.cursor(), create_data_instance, records_to_generate)

mysql_conn.commit()
mysql_conn.close()
