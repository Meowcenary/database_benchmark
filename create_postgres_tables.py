import psycopg2

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

# Commit the changes and close the connection
conn.commit()
conn.close()
