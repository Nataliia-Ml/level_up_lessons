import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

connection_data = {
    "host": "localhost",
    "dbname": "shop",
    "user": "postgres",
    "password": "postgres"
}

conn = psycopg2.connect(**connection_data)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()
cursor.execute("DROP DATABASE shop1")
cursor.execute("CREATE DATABASE shop1")
cursor.close()
conn.close()


connection_data = {
    'host': "localhost",
    'dbname': "shop1",
    'user': 'postgres',
    'password': 'postgres'
}


with psycopg2.connect(**connection_data) as conn:
    conn.set_session(autocommit=True)
    with conn.cursor() as cursor:
        # cursor.execute("DROP TABLE IF EXISTS client, products, orders, order_status, cart")
        # cursor.execute("DROP SEQUENCE IF EXISTS client_id_seq, products_id_seq, order_status_id_seq, orders_id_seq")

        cursor.execute(
            """
            CREATE TABLE client(
            id SERIAL PRIMARY KEY,
            name VARCHAR(15),
            dob TIMESTAMP,
            email VARCHAR(20))
            """
        )

        # cursor.execute("CREATE SEQUENCE client_id_seq")
        # cursor.execute("ALTER TABLE client ALTER COLUMN id SET DEFAULT nextval('client_id_seq')")

        cursor.execute(
            """
            CREATE TABLE products(
            id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            description TEXT,
            price FLOAT)
            """
        )

        # cursor.execute("CREATE SEQUENCE products_id_seq")
        # cursor.execute("ALTER TABLE products ALTER COLUMN id SET DEFAULT nextval('products_id_seq')")

        cursor.execute(
            """
            CREATE TABLE order_status(
            id SERIAL PRIMARY KEY,
            status VARCHAR(10))
            """
        )

        # cursor.execute("CREATE SEQUENCE order_status_id_seq")
        # cursor.execute("ALTER TABLE order_status ALTER COLUMN id SET DEFAULT nextval('order_status_id_seq')")

        cursor.execute(
            """
            CREATE TABLE orders(
            id SERIAL PRIMARY KEY,
            order_date TIMESTAMP NOT NULL DEFAULT NOW(),
            payday TIMESTAMP,
            client_id INTEGER REFERENCES client(id),
            status_id INTEGER REFERENCES order_status(id))
            """
        )

        # cursor.execute("CREATE SEQUENCE orders_id_seq")
        # cursor.execute("ALTER TABLE orders ALTER COLUMN id SET DEFAULT nextval('orders_id_seq')")

        cursor.execute(
            """
            CREATE TABLE cart(
            order_id INTEGER REFERENCES orders(id),
            product_id INTEGER REFERENCES products(id),
            quantity INTEGER DEFAULT 1,
            price_on_order FLOAT)
            """
        )

        cursor.execute("INSERT INTO order_status(status) VALUES('ordered'), ('shipped'),('delivered'), ('returned')")

        cursor.execute(
            """
            INSERT INTO client(name, dob, email) VALUES
            ('John Silver', timestamp '1980-09-01 12:00:00', 'silver@gmail.com'),
            ('Frank Silver', timestamp '1980-09-01 13:00:00', 'silver2@gmail.com'),
            ('Li Wong', timestamp '1980-09-01', 'wong@gmail.com'),
            ('Neal Murphy', '1978-01-04', 'murphy78@gmail.com'),
            ('Wilson Martin', '1989-05-21', 'wi_martin@gmail.com' ),
            ('Keith Hall', '1994-09-09', 'hallkeith@gmail.com'),
            ('Raul Williams', '1990-02-09', 'williams90@gmail.com'),
            ('Izabel Davis', '1993-07-25', 'izabel_93@gmail.com'),
            ('Oriana Harris', '1983-12-20', 'harris_o@gmail.com')
            """
        )

        cursor.execute(
            """
            INSERT INTO products(name, price, description) VALUES
            ('Shoes Nike', 110.00, 'white shoes'),
            ('Shoes Puma', 140.00, 'black shoes'),
            ('Jacket', 300.00, '-'),
            ('Reglan', 200.00, '-'),
            ('Hat', 50.00, '-'),
            ('Shirt', 55.00, 'blue'),
            ('Dress', 115.00, 'black')
            """
        )

        cursor.execute(
            """
            INSERT INTO orders(order_date, payday, client_id, status_id) VALUES
            ('27-05-2022', '27-05-2022', 4, 3),
            ('27-05-2022', NULL, 2, 2),
            ('25-05-2022', '26-05-2022', 5, 3),
            ('20-05-2022', NULL, 7, 4),
            ('01-06-2022', '01-06-2022', 6, 1)
            """
        )
        cursor.close()
