from typing import Union, List


class Developer:
    def __init__(self, name, age, profile, salary):
        self.name = name
        self.age = age
        self.profile = profile
        self.salary = salary
        self.max_increase = self.calculate_max_increase()

    def calculate_max_increase(self):
        return self.salary * 0.1

    def salary_increase(self, increase_amount):
        if increase_amount > self.max_increase:
            return {'error': f"Max increase for person {self} is {self.max_increase}"}
        self.salary += increase_amount
        self.max_increase = self.calculate_max_increase()
        return {'msg': f"Increase {increase_amount} for person {self} done"}


class Junior(Developer):
    def __init__(self, name, age, profile, salary, mentor=None, plan=None):
        super().__init__(name, age, profile, salary)
        self._mentor = None
        self.change_mentor(mentor=mentor)
        self.plan = plan

    def change_mentor(self, mentor):
        if mentor and mentor != self._mentor:
            if not isinstance(mentor, Senior):
                raise ValueError(f"padavan must be instance of {Junior} not {type(padavan)}")
            self._mentor = mentor
            mentor.add_padavans(self)


class Senior(Developer):
    def __init__(self, name, age, profile, salary, padavans=None):
        super().__init__(name, age, profile, salary)
        self._padavans = list()
        self.add_padavans(padavans)

    def add_padavans(self, padavan: Union[Junior, List[Junior]]):
        if not padavan:
            return False

        padavans = []
        if isinstance(padavan, list):
            padavans.extend(padavan)
        else:
            padavans.append(padavan)

        if not all([isinstance(obj, Junior) for obj in padavans]):
            raise ValueError(f"padavan must be instance of {Junior} not {type(padavan)}")

        for padavan in padavans:
            if padavan and padavan not in self._padavans:
                self._padavans.append(padavan)
                padavan.change_mentor(self)


s = Senior("Bob", 18, "Python", 2800.0)
j1 = Junior("Fill", 19, "Python", 900)
j2 = Junior("Mary", 22, "Python", 900)
