DB = "new_shop"
TABLES = {
    "client": (
        ("id", "SERIAL PRIMARY KEY"),
        ("name", "VARCHAR(20)"),
        ("dob", "TIMESTAMP"),
        ("email", "VARCHAR(40)"),
    ),
    "products": (
        ("id", "SERIAL PRIMARY KEY"),
        ("name", "VARCHAR(30)"),
        ("description", "VARCHAR(100)"),
        ("price", "FLOAT"),
    ),
    "order_status": (
        ("id", "SERIAL PRIMARY KEY"),
        ("status", "VARCHAR(10)"),
    ),
    "orders": (
        ("id", "SERIAL PRIMARY KEY"),
        ("client_id", "INTEGER REFERENCES client(id) on delete cascade"),
        ("status_id", "INTEGER REFERENCES order_status(id) on delete SET NULL"),
        ("order_date", "TIMESTAMP NOT NULL DEFAULT now()"),
        ("payment_date", "TIMESTAMP"),
    ),
    "cart": (
        ("order_id", "INTEGER REFERENCES orders(id) on delete cascade"),
        ("product_id", "INTEGER REFERENCES products(id) on delete SET NULL"),
        ("order_date", "TIMESTAMP NOT NULL DEFAULT now()"),
        ("quantity", "INTEGER"),
        ("price_on_order", "FLOAT"),
    ),
}
