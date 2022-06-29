class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am {self.__class__.__name__}. Polymorphism is working")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am {self.__class__.__name__}. Polymorphism is working indeed")

    def make_sound(self):
        print("Bar")


animals = [Cat("Cat", 5), Dog("Dog", 4)]

for animal in animals:
    animal.make_sound()
    animal.info()
