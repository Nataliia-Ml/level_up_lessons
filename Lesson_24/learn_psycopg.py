import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="shop",
    user="postgres",
    password="postgres"
)
# cursor = conn.cursor()

# print(cursor)
# print(cursor.connection)

# cursor.execute("SELECT * FROM client")
# records = cursor.fetchall()
# print(f"Records from shop DB: \n{records}")

# for command in (cursor.fetchone, cursor.fetchall):
#     records = command()
#     print(f"Records from shop DB with command {command.__name__}: \n{records}")

# records = cursor.fetchmany(size=2)
# print(f"Records from shop DB with command fetchmany: \n{records}")

# for rec in cursor:
#     print(f"Record from shop DB: \n{rec}")

# cursor.close()
# conn.close()


# WITH AS - контексный менеджер
from psycopg2.extras import DictCursor
connection_data = {
    "host": "localhost",
    "dbname": "shop",
    "user": "postgres",
    "password": "postgres"
}

# with psycopg2.connect(**connection_data) as conn:
#     with conn.cursor() as cursor:
#         cursor.execute("SELECT * FROM client")
#         for rec in cursor:
#             print(f"Record from shop DB user name: \n{rec[1]}")

'''Чтобы вывести из строк какую-то одну колонку, можем пользоваться индексами (как на примере выше). 
А можно импортнуть from psycopg2.extras import DictCursor, и добавить курсору параметр cursor_factory=DictCursor,
а далее пользоваться названиями колонок, а не индексами.
'''

# with psycopg2.connect(**connection_data) as conn:
#     with conn.cursor(cursor_factory=DictCursor) as cursor:
#         cursor.execute("SELECT * FROM client")
#         for rec in cursor:
#             print(f"Record from shop DB user name: \n{rec['name']}")

"""
SQL injections
Так же тут пример кода для создания БД. Дополнительно нужно импортировать SOLATION_LEVEL_AUTOCOMMIT 
и дописать его
"""
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# connection_data = {
#     "host": "localhost",
#     "dbname": "shop",
#     "user": "postgres",
#     "password": "postgres"
# }
#
# conn = psycopg2.connect(**connection_data)
# conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# cursor = conn.cursor()
# cursor.execute("CREATE DATABASE injection_users")
# cursor.close()
# conn.close()

'''В коде выше мы создали БД injection_users. Дальше мы подключаемся к ней и работаем'''

connection_data = {
    "host": "localhost",
    "dbname": "injection_users",
    "user": "postgres",
    "password": "postgres"
}

# conn = psycopg2.connect(**connection_data)
# conn.set_session(autocommit=True)
# cursor = conn.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS users (username varchar(20), admin boolean)")
# cursor.execute("INSERT INTO users(username, admin) VALUES "
#                "('John', false), ('Tom', true);")
#
# cursor.close()
# conn.close()


# def check_if_admin(username):
#     with psycopg2.connect(**connection_data) as conn:
#         with conn.cursor() as cursor:
#             cursor.execute(f"SELECT admin FROM users where username = '{username}'")
#             res = cursor.fetchall()
#             print(f"Result: {res}")

""" Такой аргумент вернет тру в любом случае и отбросит все остальные запросы, это нарушает безопасность"""
# check_if_admin("'; select true; --")
""" По факту, такую инъекцию можно сделать именем при регистрации на сайте и у злоумышленника есть доступ к правам админа"""


# my_name = "'; update users set admin='true' where username='John'; select true; --"
# print(check_if_admin(my_name))
