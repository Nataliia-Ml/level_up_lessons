class BaseClass:
    def __new__(cls):
        print("BaseClass __new__ method")
        return super().__new__(cls)

    def __init__(self):
        print('BaseClass __init__ method run')

    def __del__(self):
        print("BaseClass __del__ method")


base = BaseClass()

'''
Почему по-разному работают del base и base.__del__() ?
'''

