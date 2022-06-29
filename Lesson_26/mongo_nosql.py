"""
mongo-db - документно ориентированная БД.
SQL         NoSQL
db          db
table       collection
row         document
Установить pymongo:
pip install pymongo
pip install dnspython
При установке пайчарма нужно настроить пайтон-интерпретатор

'python.exe -m pip install "pymongo[srv]"'
pip install dnspython
"""
import random

from pymongo import MongoClient
from pymongo.cursor import Cursor
from pymongo.results import UpdateResult

# это для аудиторной level_up
# mongo_atlas_url = "mongodb+srv://user:user@cluster0.hthsl.mongodb.net"

# это для домашней
# mongo_atlas_url = "mongodb+srv://user:user@cluster0.czqkb.mongodb.net"
# cluster = MongoClient(mongo_atlas_url)

# all_db = cluster.list_database_names()
# print(f"All Mongo DBs: {all_db}")

# Создание БД
# clients_db = cluster["clients"]
# print(f"New DB: {clients_db}\n")

# account_collection = clients_db["account"]
# print(f"New Collection: {account_collection}\n")

# Mongo не добавляет БД, пока не будет добавлена запись
# Делаем запись в таблицу
# data = {"name": "john", "age": 33}
# res = account_collection.insert_one(data)
# print(f"Result: {res}")

# data = {"name": "George", "age": 22}
# res = account_collection.insert_one(data)

# data = {"name": "Bob", "age": "19"}
# res = account_collection.insert_one(data)
#
# data = {"name": "Lisa", "age": "25"}
# res = account_collection.insert_one(data)

# Выведем все данные из коллекции
# users: Cursor = account_collection.find()
# for user in users:
#     print(f"User: {user}")


# Чтобы вывести одного пользователя, нам нужно в find дать запрос query и пройтись циклом
# query = {"name": "john"}
# users: Cursor = account_collection.find(query)
# for user in users:
#     print(f"User: {user}")

# users_amount = account_collection.find()

# query = {"name": "john"}
# users: Cursor = account_collection.find(query)
# users: dict = account_collection.find_one(query)
# print(users)

# Посмотрим, что будет если вставим коллекции с различными типами данных. Вставим данные и посмотрим в компас.
# data = {"test": [1, 2, 3], "Test_02": {"test": "test"}}
# res = account_collection.insert_one(data)
# print(f"Result: {res.inserted_id}")

# Добавим поле, которого еще не было

# query = {"name": "john"}
# update_data = {"mail": "john@gmail.com"}
# update_cmd = {"$set": update_data}
#
# user: UpdateResult = account_collection.update_one(query,update_cmd)
# print(user.modified_count)


#  Задача - добавить всем строкам поле "is_admin" со значением False
# # Сначала делаем запрос, который найдет все строки, у которых имя подходит под определенное регулярное выражение.
# query = {"name": {"$regex": "^.*"}}
# update_data = {"is_admin": False}
# update_cmd = {"$set": update_data}
# user: UpdateResult = account_collection.update_many(query, update_cmd)
# print(user.modified_count)

# Задание - если в колонке age не число, сделать числом.
# users: Cursor = account_collection.find()
# for user in users:
#     if not isinstance(user['age'], int):
#         int_age = int(user['age'])
#         query = {"_id": user.upserted_id}
#         update_data = {"age": int_age}
#         update_cmd = {"$set": update_data}
#         user: UpdateResult = account_collection.update_one(query, update_cmd)


# Чтобы удалить коллекцию
# account_collection.drop()


