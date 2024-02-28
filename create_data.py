from datetime import datetime
from random import choice, randint, uniform

from faker import Faker

class CreateData:
    def __init__(self):
        self.users = []
        self.vendors = []
        self.products = []
        self.orders = []

    def generate_data(self):
        faker = Faker()

        payment_methods = ['Credit Card', 'Mailed Check', 'Paypal', 'Electronic Check']
        statuses = ['Pending', 'Shipped', 'Cancelled', 'Delivered']

        # Generate fake data
        for i in range(1, 1001):
            # User data
            name = faker.name()
            email = faker.email()
            phone_number = faker.phone_number()
            self.users.append((name, email, phone_number))

            # Vendor data
            vendor_name = faker.company()
            vendor_state = faker.state()
            vendor_zip = faker.zipcode()
            self.vendors.append((vendor_name, vendor_state, vendor_zip))

            # Product data
            product_vendor_id = randint(1, i) # take random value from 1 to 1000
            product_name = faker.sentence(3)[:-1] # generate one to three words and remove the period
            description = " ".join([faker.sentence(15) for _ in range(10)])
            price = uniform(10, 1000)
            stock_quantity = randint(50, 10000)
            self.products.append((product_vendor_id, product_name, description, price, stock_quantity))

            # Order data
            order_user_id = randint(1, i)
            order_product_id = randint(1, i)
            order_date = faker.date_between_dates(date_start=datetime(2020, 1, 1), date_end=datetime(2024, 3, 1))
            order_total_product = randint(10, 1000) # this could be improved to check the product id to see how much stock there is, but it's not really necessary for benchmarking
            order_shipping_address = faker.address()
            order_payment_method = choice(payment_methods)
            order_status = choice(statuses)
            self.orders.append((order_user_id, order_product_id, order_date, order_total_product, order_shipping_address, order_payment_method, order_status))
