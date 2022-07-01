from pymongo import MongoClient

# это для аудиторной level_up
# mongo_atlas_url = "mongodb+srv://user:user@cluster0.hthsl.mongodb.net"

# это для домашней
mongo_atlas_url = "mongodb+srv://user:user@cluster0.czqkb.mongodb.net"
cluster = MongoClient(mongo_atlas_url)

db = cluster["flights"]

airports_collection = db["airports"]
orders_collection = db["orders"]
directions_collection = db["directions"]
airplanes_collection = db["airplanes"]
schedules_collection = db["schedules"]
