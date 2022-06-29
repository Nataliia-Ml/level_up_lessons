import random

from pymongo import MongoClient
from pymongo.cursor import Cursor
from pymongo.results import UpdateResult
from constants import airports, airplanes
from random import choice, randint
from datetime import datetime

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


def create_airports():
    for airport in airports:
        country, city, icao_idx = airport
        data = {"country": country, "city": city, "icao_idx": icao_idx}
        is_exist = airports_collection.count_documents(data)
        if is_exist > 0:
            print(f"Airport: {airport} already exists")
            continue
        res = airports_collection.insert_one(data)
        print(f"Airport: {airport} was created with _id: {res.inserted_id}")


def create_airplanes(airplanes_amount=1):
    data = []
    for _ in range(airplanes_amount):
        airplane = choice(airplanes)
        manufacturer, model, seats_range = airplane
        seats = randint(seats_range[0], seats_range[1])
        data.append({"manufacturer": manufacturer, "model": model, "seats": seats})

    res = airplanes_collection.insert_many(data)
    print(f"Airplanes: {data} was created with _ids: {res.inserted_ids}")


def create_directions():
    # mongo projection - такой запрос (как ниже) вернет только "icao_idx" со значением, если пройтись по icao_indexes циклом
    icao_indexes = airports_collection.find({}, {"_id": 0, "icao_idx": 1})
    icao_indexes = [index["icao_idx"] for index in icao_indexes]
    print(icao_indexes)

    pairs = set([(_icao, icao) for icao in icao_indexes for _icao in icao_indexes])
    for orig, dest in pairs:
        data = {"origin": orig, "destination": dest}
        is_exist = directions_collection.count_documents(data)
        if is_exist > 0:
            print(f"Direction: {orig} -> {dest} already exists")
            continue
        res = directions_collection.insert_one(data)
        print(f"Direction: {orig} -> {dest} was created with _id: {res.inserted_id}")


def create_schedule(flight_date: datetime):  # 17 June 00:00:00
    airports = airports_collection.find()
    for airport in airports:
        proper_airplane = False
        while not proper_airplane:
            # airplane = airplanes_collection.find_one()
            airplane = random.choice(list(airplanes_collection.find()))
            # airplane = airplanes_collection.aggregate([{"$sample": {"size": 1}}]) #- этот имеет тип <class 'pymongo.command_cursor.CommandCursor'>. Как дальше с ним работать?

            # query = {
            #     "airplane_id": airplane["_id"],
            #     "flight_date": {"$eq": flight_date}
            # }
            query = {
                "airplane_id": {"$eq": airplane["_id"]},
                "flight_date": {"$eq": flight_date}
            }
            # если самолет имеет вылеты на сегодня, он вернет 1. Иначе - 0
            airplane_flights_today = schedules_collection.count_documents(query)

            if airplane_flights_today > 0:
                print(f"Airplane: {airplane} already occupied for today: {flight_date}")
                continue
            proper_airplane = True
        direction = random.choice(list(directions_collection.find()))
        hour = randint(00, 23)
        minute = randint(00, 59)
        flight_date = flight_date.replace(hour=hour, minute=minute)
        # {"airplane_id": "", "flight_date": "", "direction_id": ""}
        data = {
            "airplane_id": airplane["_id"],
            "flight_date": flight_date,
            "direction_id": direction["_id"]
        }
        res = schedules_collection.insert_one(data)
        print(f"Created schedule with _id: {res.inserted_id}")


if __name__ == '__main__':
    # create_airports()
    # create_airplanes()
    # create_directions()
    create_schedule(datetime(2022, 7, 20))
