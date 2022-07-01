from pymongo.cursor import Cursor

from utils import get_free_airplanes, randomize_time
from constants import airports, airplanes
from random import choice, randint
from datetime import datetime, timedelta
from infra import (
    airplanes_collection,
    airports_collection,
    orders_collection,
    directions_collection,
    schedules_collection
)


def create_airports():
    print("[debug] create airports")
    for airport in airports:
        country, city, icao = airport
        data = {"country": country, "city": city, "icao": icao}
        is_exist = airports_collection.count_documents(data)
        if is_exist > 0:
            print(f"[debug] Airport: {airport} already exists")
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
    icao_indexes: Cursor = airports_collection.find({}, {"_id": 0, "icao": 1})
    # {"icao": "UKDD", ...}
    icao_indexes: list = [index["icao"] for index in icao_indexes]
    # ["UKDD", "UKBB", "UKLL", "UKDE"]
    print(f"[debug] icao indexes: {icao_indexes}")

    # таким сетом списков мы создаем уникальные пары
    pairs = set([(_icao, icao) for icao in icao_indexes for _icao in icao_indexes])
    for orig, dest in pairs:
        data = {"origin": orig, "destination": dest}
        is_exist = directions_collection.count_documents(data)
        if is_exist > 0:
            print(f"Direction: {orig} -> {dest} already exists")
            continue
        res = directions_collection.insert_one(data)
        print(f"Direction: {orig} -> {dest} was created with _id: {res.inserted_id}")


def create_schedule(flight_date: datetime):
    for direction in directions_collection.find():

        airplane = get_free_airplanes(flight_date)

        if not airplane:
            return False

        flight_date_with_time = randomize_time(flight_date)

        data = {
            "airplane_id": airplane["_id"],
            "flight_date": flight_date_with_time,
            "direction_id": direction["_id"]
        }
        res = schedules_collection.insert_one(data)
        print(f"created schedule with _id: {res.inserted_id}")


if __name__ == '__main__':
    # create_airports()
    create_airplanes(5)
    # create_directions()

    days_ahead = 7
    tomorrow = datetime.today() + timedelta(days=1)
    dates = [tomorrow + timedelta(days=day) for day in range(days_ahead)]
    print(f"dates for schedule: {dates}")
    for date in dates:
        create_schedule(date)
