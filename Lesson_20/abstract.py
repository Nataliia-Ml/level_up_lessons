'''
Функции:
Когда мы объявляем функцию - объявляем параметры
Когда вывываем функцию - передаем аргументы

В классах:
функции становятся методами
все аргументы, параметры и аргументы уже называются атрибутами

3 постулата в классах:
Наследования
Полиморфизм
Инкапсуляция

Абстрактный класс - класс с абстрактными методами.
Это такой метод, который объявлен, но не реализован.
Его тело и действия могут быть прописаны для каждого подкласса.
Нам нужно классу сказать, что он абстрактным. Для этого есть библиотека - abc(abstract classes)
Асбтрактные классы по-разному представлены в пайтоне 2 и 3.
Мы рассматриваем только 3.
Метаклассы - очень высокие материи. Это инструкция для создания классов.
Если мы попытаемся созать экземпляр абстрактного класса - получим ошибку
Для создания экземпляра не может использоваться абстрактный класс!
Это исключение работает и для наследуемых классов,
так как в наследуемых классах все методы абстрактного класса должны быть реализованы
Все классы с родителем Proteus обязаны реализовывать все методы
Подвоя итог: АК определяет то, какие свойства и методы должны быть реализованы в подклассах.
Больше никаких требований (ни к аргументам, ни к значениям, как могло бы быть в других языках)

'''

# a - athribute, return_a - mathods
# class A:
#     a = 5
#
#     def return_a(self):
#         return self.a

from abc import (
    ABCMeta,
    abstractproperty,
    abstractmethod
)


class Proteus(metaclass=ABCMeta):
    def __init__(self, species):
        self.species = species

    @abstractmethod
    def eat(self):
        raise NotImplementedError

    @abstractmethod
    def breath(self):
        raise NotImplementedError

    @abstractmethod
    def sleep(self):
        raise NotImplementedError

    # пайтон разрешил создать в абс классе не асбтр метод.
    # Но это является методом того, как нужно заставить человека обязательно его переопределить, чтобы ним пользоваться.
    # Иначе - ошибка NotImplementedError
    def replication(self):
        raise NotImplementedError


class Bacteria(Proteus):
    def __init__(self, species):
        super().__init__(species)
        self.classname = self.__class__.__name__

    def eat(self):
        print(f"{self.classname} can eat via cell membrane")

    def sleep(self):
        print(f"{self.classname} doesn't sleep")

    def breath(self):
        print(f"{self.classname} some bacteria can breathe anaerobically, or without oxygen")

    def replication(self):
        print(f"{self.classname} can replicate by delf-division")


bacteria = Bacteria(species='bacteria')


class Vertebrate(Proteus):
    def __init__(self, species):
        super().__init__(species)
        self.classname = self.__class__.__name__

    def eat(self):
        print(f"{self.classname} eat with mouth")

    def sleep(self):
        print(f"{self.classname} should sleep")

    def breath(self):
        raise NotImplementedError

    def replication(self):
        raise NotImplementedError

    def move(self):
        raise NotImplementedError


class Fish(Vertebrate):
    def __init__(self, species):
        super().__init__(species)
        self.classname = self.__class__.__name__

    def breath(self):
        print(f"{self.classname} can breathe under water")

    def replication(self):
        print(f"{self.classname} can replicate by caviar")

    def move(self):
        print(f"{self.classname} can move under the water")


class Reptile(Vertebrate):
    def __init__(self, species):
        super().__init__(species)
        self.classname = self.__class__.__name__

    def breath(self):
        print(f"{self.classname} can breathe with oxygen")

    def replication(self):
        print(f"{self.classname} can replicate by eggs")

    def move(self):
        print(f"{self.classname} can move by land")

    def climb(self):
        print(f"{self.classname} can climb on vertical serface ")


class Amphibian(Fish, Reptile):
    def __init__(self, species):
        super().__init__(species)

    def breath(self):
        print(f"{self.classname} can breathe with oxygen and under water")


amphibian = Amphibian(species='amphibian')

'''
Amphibian.__mro__ - строка для просмотра множественного наследования 
Deep first left right
MRO
'''