'''
__init__ - инициализирует объект
__new__ - это конструктор экземпляра. Под капотом он работает при создании класса, а не init
Если прописать метод __new__, то метод __init__не отработает
'''
from datetime import time


# class MustExist:
#     def __init__(self):
#         print('MustExist Created')
#
#
# class BaseClass:
#     def __new__(cls):
#         # print(f'{cls}__new__ meth run')
#         # print(f'DIR: {dir()}\n')
#         # print(f'GLOBALS: {globals()}\n')
#         # print(f'LOCALS: {locals()}\n')
#         # return super().__new__(cls)
#         for var_name, var_value in globals().items():
#             if isinstance(var_value, MustExist):
#                 print(f"We found MustExist: {var_name}")
#                 return super().__new__(cls)
#         # raise Exception("MustExist should exist before create BaseClass")
#         # Можно вместо ошибки raise в случае отсутствия объекта из MustExist выдать сообщение:
#         print("MustExist should exist before create BaseClass. Creating MustExist")
#         # И создать самому объект:
#         return MustExist()
#
#     def __init__(self):
#         print('__init__ meth run')


# base = None
# while not isinstance(base, BaseClass)
#     print("Creating BaseClass")
#     base = BaseClass()


class BaseClass:
    def __new__(cls):
        print("BaseClass __new__ method")
        return super().__new__(cls)

    def __init__(self):
        print('BaseClass __init__ method run')

    def __del__(self):
        print("BaseClass __del__ method")


# must_exist = MustExist()
base = BaseClass()
# print(globals().get('must_exist'))
'''
base.__del__() -> BaseClass __del__ method
Удаления не произойдет, потому что мы переписали наш метод.
Однако del base сработает.
'''