from random import randint
from typing import Union, Type, List
import faker
from mentors_padavans import Senior, Junior


fake = faker.Faker()
SENIORS_AMOUNT = 3
JUNIORS_AMOUNT = 10
PADAVANS_PER_MENTOR = 3

devs_map = {Junior: JUNIORS_AMOUNT, Senior: SENIORS_AMOUNT}
devs = {} # {"Junior": [J1, J1, ...], "Senior": [S1, S2...]}


def create_devs(dev_type: Union[Type[Junior], Type[Senior]]):
    dev_amount = devs_map.get(dev_type, 0)
    dev_type_descr = dev_type.__name__ # "Junior", "Senior"

    for _ in range(dev_amount):
        dev_profile = fake.simple_profile()
        dev = dev_type(
            name=dev_profile['name'],
            dob=dev_profile['birthdate'],
            profile="Python",
            salary=randint(1500, 3500)
        )

        devs.setdefault(dev_type_descr, []).append(dev)
        # 1 -> []
        # n -> [jn]


def simulate_padavans_creation(mentor: Senior, padavans: List[Junior]):
    for _ in range(PADAVANS_PER_MENTOR):
        rnd_index = randint(0, len(padavans)-1)
        mentor.padavans = padavans.pop(rnd_index)



'''
TestCase1 - create Juniors and Seniors instance"
Will be created Junior and Senior
1 iteration dev = Junior
2 iteration  dev = Senior
'''

[create_devs(dev) for dev in devs_map]

# TestCase 2 - Simulate Padavan Creation

[simulate_padavans_creation(mentor=dev, padavans=devs["Junior"].copy()) for dev in devs["Senior"]]

# TestCase 3 - Simulate Padavan Dublication Creation

# TestCase 4 - Simulate Mentor Creation

# TestCase 3 - Simulate Padavan Dublication Creation

