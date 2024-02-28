import mysql.connector

# define tables to be created
tables = []
tables.append('''
    CREATE TABLE IF NOT EXISTS users (
        id INT NOT NULL AUTO_INCREMENT,
        PRIMARY KEY(id),
        name VARCHAR(255),
        email VARCHAR(255),
        phone_number VARCHAR(22),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
''')

tables.append('''
    CREATE TABLE IF NOT EXISTS vendors (
        id INT NOT NULL AUTO_INCREMENT,
        PRIMARY KEY(id),
        name VARCHAR(255),
        state VARCHAR(14),
        zip VARCHAR(5),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
''')

tables.append('''
    CREATE TABLE IF NOT EXISTS products (
        id INT NOT NULL AUTO_INCREMENT,
        PRIMARY KEY(id),
        vendor_id INT,
        CONSTRAINT fk_vendor FOREIGN KEY (vendor_id) REFERENCES vendors(id),
        name VARCHAR(255),
        description TEXT,
        price DECIMAL(10, 2),
        stock_quantity INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
''')

tables.append('''
    CREATE TABLE IF NOT EXISTS orders (
        id INT NOT NULL AUTO_INCREMENT,
        PRIMARY KEY(id),
        user_id INT,
        CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id),
        product_id INT,
        CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES products(id),
        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        total_product INT,
        shipping_address VARCHAR(255),
        payment_method VARCHAR(50),
        status VARCHAR(50) DEFAULT 'Pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
''')

payment_methods = ['Credit Card', 'Mailed Check', 'Paypal', 'Electronic Check']
statuses = ['Pending', 'Shipped', 'Cancelled', 'Delivered']

# Connect to PostgreSQL database
conn = mysql.connector.connect(
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
