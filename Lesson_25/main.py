from typing import Callable

import psycopg2
from psycopg2.sql import SQL, Identifier, Placeholder

from constants import DB, TABLES

"""
Задача на урок - создать декоратор, который будет создавать connection и курсор. 
Ним будем оборачивать функции, которые будут создавать там БД и таблицы.
Мы напишем продвинутый декоратор, который будет принимать аргументы для connection. 
Из-за этого он будет выглядеть не совсем обычно.
"""

def with_cursor(**connection_data):
    def with_cursor_decorator(f: Callable) -> Callable:
        def with_cursor_wrapper(*args, **kwargs):
            conn = psycopg2.connect(**connection_data)
            conn.autocommit = True
            cursor = conn.cursor()
            try:
                f(*args, **kwargs, cursor=cursor)
            except Exception as e:
                conn.rollback()
                print(f"SQL query failed with error: {e}")
                raise e
            else:
                conn.commit()
            finally:
                cursor.close()
                conn.close()
        return with_cursor_wrapper
    return with_cursor_decorator


@with_cursor(host="localhost", user="postgres", password="postgres")
def create_db_if_not_exist(db_name: str, cursor) -> None:
    query = SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname=%s")
    cursor.execute(query, (db_name, ))
    db_exists = cursor.fetchone()
    if not db_exists:
        query = SQL("CREATE DATABASE {db_name}").format(db_name=Identifier(db_name))
        """Этот принт покажет полный query, который полетел в БД"""
        print(query.as_string(cursor))
        cursor.execute(query)
    else:
        print(f"msg: database {db_name} already exists")


@with_cursor(host="localhost", dbname=DB, user="postgres", password="postgres")
def create_tables_if_not_exists(tables: dict, cursor) -> None:
    for table_name, columns in tables.items(): # columns -> ( ("id", "SERIAL PRIMARY KEY"), (), (), )
        fields = [SQL("{} {}").format(SQL(col[0]), SQL(col[1])) for col in columns] # col : ("id", "SERIAL PRIMARY KEY")
        query = SQL("CREATE TABLE IF NOT EXISTS {table_name} ({fields})").format(
            table_name=SQL(table_name),
            fields=SQL(', ').join(fields)
        )
        print(query.as_string(cursor))
        cursor.execute(query)


@with_cursor()
def fill_table():
    pass


if __name__ == "__main__":
    create_db_if_not_exist(DB)
    create_tables_if_not_exists(TABLES)
