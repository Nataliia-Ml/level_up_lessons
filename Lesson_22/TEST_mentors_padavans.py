import random
from faker import Faker
import mentors_padavans as file
'''
дз: по павдаванам
Создать 4 тест-сценарии, которые бы создавали синьоров и падванав
Написать различные сценарии тестов
1. Создать 4 синьоров, 12 джунов. 
2. добавить каждому синьору 3 джуна рандомно
3. попробовать дублицировать джунов синьорам (повторно добавить)
4. Джуну добавить рандомно синьоров
'''

def creation_seniors():
    list_seniors = []
    for _ in range(4):
        fake = Faker()
        name = fake.name()
        age = random.randint(18, 60)
        salary = random.randrange(500, 3000, 100)
        list_seniors.append(file.Senior(name=name, age=age, salary=salary))
    s1, s2, s3, s4 = list_seniors

# creation_juniors:
list_juniors = []
for _ in range(12):
    fake = Faker()
    name = fake.name()
    age = random.randint(18, 60)
    salary = random.randrange(250, 600, 50)
    list_juniors.append(file.Junior(name=name, age=age, salary=salary))
j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12 = list_juniors

print("Adding of padavans starts...")
print("~"*10)
for senior in list_seniors:
    for i in range(3):
        random_jun = random.choice(list_juniors)
        senior.padavans = random_jun
        print(f"Padavan {random_jun.name} was added for senior {senior.name}")
    print(f"List of padavans for senior {senior.name} is {senior.padavans}")

print("Adding of padavans ends...")
print("~"*10)
print("Adding of mentor starts...")
print("~"*10)
for junior in list_juniors:
    random_senior = random.choice(list_seniors)
    junior.mentor = random_senior
    print(f"Senior {random_senior.name} was added for padavan {junior.name}")
    print(f"Junior {junior.name} has {junior.mentor.name} as mentor.")
print("Adding of mentor ends...")
print("~"*10)