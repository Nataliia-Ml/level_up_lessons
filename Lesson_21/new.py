class Name:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.full_name = self.first_name + " " + self.last_name
        self.initials = self.first_name[0] + "." + self.last_name[0]


class Calculator:
    # def __init__(self, num_one: int, num_two: int):
    #     self.num_one = num_one
    #     self.num_two = num_two

    @staticmethod
    def add(num_one, num_two):
        return num_one + num_two

    @staticmethod
    def subtract(num_one, num_two):
        return num_one - num_two

    @staticmethod
    def multiply(num_one, num_two):
        return num_one * num_two

    @staticmethod
    def divide(num_one, num_two):
        return num_one / num_two


class Employee:
    def __init__(self, first_name: str, last_name: str, salary: int):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @classmethod
    def from_string(cls, name: str):
        first_name, last_name, salary = name.split("-")
        return cls(first_name=first_name, last_name=last_name, salary=salary)


emp1 = Employee.from_string("John-Smith-400")
