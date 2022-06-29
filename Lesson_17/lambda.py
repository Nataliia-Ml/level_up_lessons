# def func(x):
#     return pow(x, 2)

# Lambda, map, filter
# map оператор, который выполняет работу со всеми элементами итерируемого объекта.
# Первый аргумент у мэпа - сама функция, второй - итерируемый объект.

# initial_l = [10, 20, 30, 101]

# пусть стоит задача выбрать элементы, который больше 100 - заменить на ноль
# первый способ
# new_list = []
# for el in initial_l:
#     if el>100:
#         new_list.append(el)
# print(new_list)


# второй способ

# создадим функцию-счетчик, которую мы обнуляем после 100

# def filter_func(x):
#     if x > 100:
#         return 0
#     else:
#         return x


# for el in new_l:
#     print(el)

# new_l = list(map(lambda x: 0 if x > 100 else x, initial_l))
# print(new_l)

# list comprehension
# new_list2 = [filter_func(x) for x in initial_l]
# print(new_list2)

# Map делает изменения с итерируемым объектом

# Filter - он работает с итер.объектом, но обязан возвращать тру/false. Если тру - объект останется

# users = {1: "Tom", 2: "Bob", 3: "Lui"}
# # users.items() >>> ((1, "Tom"), (2, "Bob"), (3, "Lui"))
# debts = {1: 10000.0, 2: 300.0, 3: 24000.0}

#
# def filter_debts(kv: tuple):
#     user_id, debt = kv #распакуем наш кортеж ((key, value), (key, value), (key, value), ...)
#     if debt > 5000.0:
#         return True #filter анализирует тру/фолс
#     else:
#         return False


# задача - отфильтровать. СОздать новый словарь
# debtors = dict(filter(lambda kv: kv[1] > 5000, debts.items()))   # ((key, value), (key, value), (key, value), ...)
# debtors = {kv[0]: kv[1] for kv in debts.items() if kv[1] > 5000}
#
# print(debtors)

# задание - составит список должник(имя) - долг
# users = {1: "Tom", 2: "Bob", 3: "Lui"}
# debts = {1: 10000.0, 2: 300.0, 3: 24000.0}

# # kv: tuple = (key, value) =>
# name_debt_map = dict(map(lambda kv: (users[kv[0]], kv[1]), debtors.items()))
# print(name_debt_map)

