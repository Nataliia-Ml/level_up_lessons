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
        self.mentor = mentor    #Setter _Junior__mentor
        self.plan = plan

    def is_mentor_exist(self, new_mentor):
        if getattr(self, "_Junior__mentor", None):
            if new_mentor == self.__mentor:
                return True
        return False

    def check_object_class(self, obj, class_to_check):
        if obj and not isinstance(obj, class_to_check):
            raise ValueError(
                f"padavan must be instance of {class_to_check} not {type(obj)}"
            )

    @property #Getter. If mentor is Getter => @mentor.setter, @mentor.deleter
    def mentor(self):
        print(f"My mentor is {self.__mentor}")
        return self.__mentor

    @mentor.setter
    def mentor(self, new_mentor):
        self.check_object_class(new_mentor, Senior)

        if new_mentor and not self.is_mentor_exist(new_mentor):
            new_mentor.add_padavans(self)
        self.__mentor = new_mentor

    @mentor.deleter
    def mentor(self):
        self.__mentor = None
        # Todo: Implement process of deleting this Junior from Senior's padavans


class Senior(Developer):
    # Todo: сделать проперти-логику для класса синьор. Предусмотреть все возможные ньансы.
    # Попытаться сделать код простым. Будет стресс-тест
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
                padavan.mentor = self


s = Senior("Bob", 18, "Python", 2800.0)
j1 = Junior("Fill", 19, "Python", 900)
j2 = Junior("Mary", 22, "Python", 900)
# дз : переделать синьйора, чтобы он работал по проперти
