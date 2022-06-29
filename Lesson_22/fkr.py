from faker import Faker
from faker.providers import DynamicProvider
from pprint import pprint
'''
основное назначение - генерация фейковых данных
python3 -m pip install Faker
'''

# fake = faker.Faker("en_US")

# for _ in range(20):
#     pprint(fake.name())

# for _ in range(20):
#     pprint(fake.phone_number())

fake = Faker()

developer_prof_providers = DynamicProvider(
    provider_name="developer_professions",
    elements=["QA", "Python Developer", "Go Developer", "JavaScript Developer"]
)

fake.add_provider(developer_prof_providers)

for _ in range(5):
    print(fake.developer_professions())
