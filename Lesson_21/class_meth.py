"""
1.Static meth - это обычный метод, который включается в пространство имен класса. Но он не оперирует экземпляром класса.
Стат методу мы передаем self, но не используем. Для объявления стат метода используемся @staticmethod.
Если метод обернуть декоратором, то self из аргументов можно убрать.
В этом случае у метода нет доступа к информации об экземпляре класса.

2.Class meth

Они оба не связаны с экземпляром класса. И они не требуют создания экземпляра. Их можно вызывать напрямую через класс.
"""


class Pet:
    _class_info = "Pet Animal"
    created_pets = 0

    # def __new__(cls):
    #     print(f"Class is {cls}")
    #     print(super())
    #     if Pet.created_pets >= 3:
    #         print("Max amount of Pets")
    #         return None
    #     else:
    #         return super().__new__(cls)

    def __init__(self):
        self._init_class_info = "Pet Animal from __init__"
        Pet.created_pets += 1

    @staticmethod
    def static_about():
        print(f"[static meth] This class is about {Pet._class_info}")

    @classmethod
    def class_about(cls):
        print(f"[class meth]This class is about {cls._class_info}")


class Dog(Pet):
    _class_info = "Dog Pet Animal - man's best friend"


class Cat(Pet):
    _class_info = "Cat Pet Animal - meow"


# for num in range(3):
#     pet_instance = Pet()
#     print(Pet.created_pets)
#     print(pet_instance.created_pets)

for pet in [Pet, Cat, Dog]:
    pet.static_about()
    pet.class_about()
