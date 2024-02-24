from datetime import datetime
from random import choice, randint, uniform

import psycopg2
from faker import Faker

faker = Faker()

# define tables to be created
tables = []
tables.append('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        phone_number VARCHAR(22),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

tables.append('''
    CREATE TABLE IF NOT EXISTS vendors (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        state VARCHAR(14),
        zip VARCHAR(5),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

tables.append('''
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        vendor_id INT,
        FOREIGN KEY (vendor_id) REFERENCES vendors(id),
        name VARCHAR(255),
        description TEXT,
        price DECIMAL(10, 2),
        stock_quantity INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

tables.append('''
    CREATE TABLE IF NOT EXISTS orders (
        id SERIAL PRIMARY KEY,
        user_id INT,
        FOREIGN KEY (user_id) REFERENCES users(id),
        product_id INT,
        FOREIGN KEY (product_id) REFERENCES products(id),
        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        total_product INT,
        shipping_address VARCHAR(255),
        payment_method VARCHAR(50),
        status VARCHAR(50) DEFAULT 'Pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

payment_methods = ['Credit Card', 'Mailed Check', 'Paypal', 'Electronic Check']
statuses = ['Pending', 'Shipped', 'Cancelled', 'Delivered']

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    user="benchmark_user",
    password="password",
    database="benchmark_db"
)
cursor = conn.cursor()

# Create tables
for table_def in tables:
    cursor.execute(table_def)

# Generate fake data
for i in range(1, 1001):
    # Generate and insert fake user data
    name = faker.name()
    email = faker.email()
    phone_number = faker.phone_number()
    cursor.execute("\
        INSERT INTO users (name, email, phone_number) \
        VALUES (%s, %s, %s)", (name, email, phone_number)
    )

    vendor_name = faker.company()
    vendor_state = faker.state()
    vendor_zip = faker.zipcode()
    cursor.execute("\
        INSERT INTO vendors (name, state, zip) \
        VALUES (%s, %s, %s)", (vendor_name, vendor_state, vendor_zip)
    )

    # take random value from 1 to 1000
    product_vendor_id = randint(1, i)
    # generate one to three words and remove the period
    name = faker.sentence(3)[:-1]
    description = " ".join([faker.sentence(15) for _ in range(10)])
    price = uniform(10, 1000)
    stock_quantity = randint(50, 10000)
    cursor.execute("\
        INSERT INTO products (vendor_id, name, description, price, stock_quantity) \
        VALUES (%s, %s, %s, %s, %s)", (product_vendor_id, name, description, price, stock_quantity)
    )

    order_user_id = randint(1, i)
    order_product_id = randint(1, i)
    order_date = faker.date_between_dates(date_start=datetime(2020, 1, 1), date_end=datetime(2024, 3, 1))
    # this could be improved to check the product id to see how much stock there is, but it's not really necessary for
    # benchmarking
    order_total_product = randint(10, 1000)
    order_shipping_address = faker.address()
    order_payment_method = choice(payment_methods)
    order_status = choice(statuses)
    cursor.execute("\
        INSERT INTO orders (user_id, product_id, order_date, total_product, shipping_address, payment_method, status) \
        VALUES (%s, %s, %s, %s, %s, %s, %s)", (order_user_id, order_product_id, order_date, order_total_product,
                                               order_shipping_address, order_payment_method, order_status)
    )

# Commit the changes and close the connection
conn.commit()
conn.close()
