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
    def __init__(self, name, age, salary, profile="Python", mentor=None, plan="Junior plan"):
        super().__init__(name, age, profile, salary)
        self.mentor = mentor    #Setter _Junior__mentor
        self.plan = plan

    def is_mentor_exist(self, new_mentor):
        if getattr(self, "_Junior__mentor", None):
            if new_mentor == self.__mentor:
                return True
        return False

    @staticmethod
    def check_object_class(obj, class_to_check):
        if obj and not isinstance(obj, class_to_check):
            raise ValueError(
                f"padavan must be instance of {class_to_check} not {type(obj)}"
            )

    @property #Getter. If mentor is Getter => @mentor.setter, @mentor.deleter
    def mentor(self):
        print(f"My mentor is {self.__mentor}")
        return self.__mentor

    @mentor.setter
    def mentor(self, new_mentor: "Senior"):
        self.check_object_class(new_mentor, Senior)

        if new_mentor and not self.is_mentor_exist(new_mentor):
            new_mentor.padavans = self

        self.__mentor = new_mentor

    @mentor.deleter
    def mentor(self):
        print(f"{self} delete mentor {self.__mentor}")
        # эта ошибка сработает только если будет удаление через синьора
        try:
            self.__mentor.padavans.remove(self)
        except ValueError:
            print(f"No such: {self} Padavan in mentor: {self.__mentor}")
        self.__mentor = None


class Padavans(list):   #list, MutableSequence
    def __init__(self, *args, **kwargs):
        super(Padavans, self).__init__(*args, **kwargs)

    def remove(self, value: Junior) -> None:
        print(f"Removing Padavan {value} from list")
        super(Padavans, self).remove(value)
        print(f"Removing Mentor {self} from Padavan Instance")
        del value.mentor


class Senior(Developer):
    def __init__(self, name, age, salary, profile="Python", padavans=None):
        super().__init__(name, age, profile, salary)
        self.__padavans = Padavans()
        self.padavans = padavans

    @property
    def padavans(self):
        print(f'{self} has padavans {self.__padavans}')
        return self.__padavans

    @padavans.setter
    def padavans(self, padavan: Union[Junior, List[Junior]]): #type hinting
        # if not padavan:
        #     return False

        padavans = []
        if isinstance(padavan, list):
            padavans.extend(padavan)
        elif padavan:
            padavans.append(padavan)

        if not all([isinstance(obj, Junior) for obj in padavans]):
            raise ValueError(f"padavan must be instance of {Junior} not {type(padavan)}")

        for padavan in padavans:
            if padavan and padavan not in self.__padavans:
                self.__padavans.append(padavan)
                padavan.mentor = self



