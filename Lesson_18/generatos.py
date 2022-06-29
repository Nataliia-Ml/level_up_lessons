'''
Итератор работает с готовым объектом.
Генератом сам генерирует объект согласно какой-то логике

'''

#  Так выглядит функция
# def countdown(n):
#     while n >= 0:
#         print(n)
#         n -= 1


# print(type(countdown)) #<class 'function'>

#  Так выглядит генератор

# def countdown(n):
#     while n >= 0:
#         yield n
#         n -= 1
#
#
# gen = countdown(10)
# print(type(gen)) # <class 'generator'>

# писать генератор, который принимает строку в себя, выдавал по одной букве из строки, пока не встретит пробел
# тогда выдает стоп итерейшнс


# def print_letters(string: str):
#     n = 0
#     while string[n] != " ":
#         yield string[n]
#         n += 1
#
#
# gen_1 = print_letters("Hello, world!")

import cProfile
print(cProfile.run('[i **2 for i in range(1000000) if i % 3 == 0 or i % 5 == 0]'))