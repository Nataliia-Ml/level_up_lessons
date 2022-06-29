# Создадим класс. Ключевое слово - class

# class Person:
#     def __init__(self, gender, name, age):
#         self.gender = gender
#         self.name = name
#         self.age = age
#
#     def hello(self):
#         print(f'Hello, my name is {self.name}')
#
#
# person = Person("male", "Vasia", 40)
# person.hello()

# Создадим новый класс

# class Person:
#     def __init__(self, name, age, departament, salary):
#         self.name = name
#         self.age = age
#         self.departament = departament
#         self.salary = salary
#         self.max_increase = self.calculate_max_increase()
#
#     def calculate_max_increase(self):
#         return self.salary * 0.1
#
#     # Пропишем метод, который позволит отвергать единоразовое повышение ЗП больше, чем на 10%
#     def salary_increase(self, increase_amount):
#         if increase_amount > self.max_increase:
#             return {'error': f"Max increase for person {self} is {self.max_increase}"}
#         self.salary += increase_amount
#         self.max_increase = self.calculate_max_increase()
#         return {'msg': f"Increase {increase_amount} for person {self} done"}
#
#
# person = Person("Vasia", 40, "QA", 1500.0)

# Что мы рассмотрим в классах: Inheritance - наследования, Polymorphism - полиморфизм, Encapsulation
# Inheritance - наследования. Для их рассмотрения сделаем базовый класс Developer
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


# Допустим, мы хотим создать класс Junior. Он должен иметь все те же характеристики, что и класс Developer.
# Дополнительно у этого класса имеется характиристика mentor, plan. Если не учитывать наследования, наш код будет такой:
#
# class Junior:
#     def __init__(self, name, age, profile, salary, mentor, plan):
#         self.name = name
#         self.age = age
#         self.profile = profile
#         self.salary = salary
#         self.max_increase = self.calculate_max_increase()
#         self.mentor = mentor
#         self.plan = plan
#
# Если использовать наследование, нам нужно указывать родительский класс.
# Далее в методе __init__ передать все аргументы. А в первой строке прописать super().__init__(аргументы из родительского класса)

class Junior(Developer):
    def __init__(self, name, age, profile, salary, mentor=None, plan=None):
        super().__init__(name, age, profile, salary)
        self.mentor = mentor
        self.plan = plan

class Senior(Developer):
    def __init__(self, name, age, profile, salary, padavans=None):
        super().__init__(name, age, profile, salary)
        self.padavans = list()
        if padavans is not None:
            self.padavans.extend(padavans)

# person = Developer("Vasia", 40, "Go Lang", 1500.0)
# person = Developer("Margo", 20, "Python", 1800.0)
