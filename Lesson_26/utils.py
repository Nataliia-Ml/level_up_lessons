from datetime import datetime
from random import randint

from infra import schedules_collection, airplanes_collection


def get_free_airplanes(flight_date: datetime):
    query = {"flight_date": {
        "$gte": flight_date.replace(hour=0, minute=1),
        "$lte": flight_date.replace(hour=23, minute=59)
        }
    }
    occupied_airplanes = schedules_collection.find(query, {"_id": 0, "airplane_id": 1})
    occupied_airplanes_id = [ap["airplane_id"] for ap in occupied_airplanes]
    """Код выше позволяет сделать список из айдишников самолетов, которые летят в дату  flight_date.
    Далее нам нужно каким-то образом выбрать такие айди самолетов из airplanes_collection, которых нет в occupied_airplanes_id.
    Это сделать сложно без применения функции агрегации в монго. 
    Агрегация - последовательность действий, где каждое следующее действие зависит от предыдущего.
    Яркий пример - несколько фильтров-параметров.
    """
    pipeline = [
        {"$match": {"_id": {"$nin": occupied_airplanes_id}}},
        {"$sample": {"size": 1}},
    ]

    try:
        return airplanes_collection.aggregate(pipeline).next()
    except StopIteration:
        print(f"[err] no free airplanes for this day: {flight_date}")
        return None


def randomize_time(flight_date: datetime):
    hour = randint(0, 23)
    minute = randint(0, 59)
    return flight_date.replace(hour=hour, minute=minute)
