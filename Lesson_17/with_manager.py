"""
 os - библиотека, встроенная в пайтон. Она для работы с операционными системами.
os.getcwd() - вернет место, где мы находимся
touch file_{0..10}.wav

"""
import os
from pathlib import Path



# print(os.listdir("."))
# print(os.getcwd())
# os.chdir("test_folder")
# print(f"Directory now: {os.getcwd()}")
# print(f"List of file: {os.listdir('.')}")

# задача - переименовать файл
# os.rename("file_7.wav", "file_17.wav")
# print(os.listdir("."))


# задача: в папке test_folder файлы .wav переименовать на .mp3


# def rename_func(file_name):
#     os.rename(file_name, file_name.replace(".wav", ".txt"))
#
#
# list_file_names = os.listdir(".")
# print(f"list_file_names: {list_file_names}")
# new_name = map(rename_func, list_file_names)
# print(os.listdir("."))
# print(list(new_name))
# print(os.listdir("."))


"""
Решение от преподавателя. Сначала создаем список наших файлов, которые имеют расширение .wav. 
Затем применяем к этому списку нужные методы.
"""

# wav_files = [file for file in os.listdir(".") if file.endswith(".txt")]
# result = map(lambda f: os.rename(f, f.replace(".txt", ".wav")), wav_files)
# print(wav_files)
# print(list(result))
# print(os.listdir("."))


'''
У библиотеки OS есть модуль path, который предназначен для работы с путями.
Метод os.path.realpath() возвращает полный путь к папке/файлу.
Метод .path.dirname() отсекает название файла, а оставляет только путь
'''
# print(os.path.realpath("test_folder"))

# print(os.path.dirname("test_folder/file_1.txt"))


# Метод os.path.join() возвращает путь. Он складывается так: первый аргумент/второй аргумент/третий аргумент.
# new_path = os.path.join(".", "dir_01", "dir_02")
# print(new_path)         # -> ./dir_01/dir_02

# Метод os.makedirs(path) создаст все так, как указано в аргументе path.
# os.makedirs(new_path)

# Этим кодом в папке test_folder мы создали папку dir_01, а внутри нее dir_02
# Если мы второй раз запустим этот же код по созданию папок, то получим ошибку FileExistsError.
# Чтобы ее обойти, воспользуемся методом os.path.exists(), который возвращает True, если путь уже существует.
# Использование этого метода при создании директорий является best practise

# new_path = os.path.join(".", "dir_01", "dir_02")
# if not os.path.exists(new_path):
#     os.makedirs(new_path)
# else:
#     print(f"Warning!!! {new_path} already exists")


# Path(new_path).mkdir(parents=True, exist_ok=True)


"""
Контекстный менеджер
"""
# with smth [as var] - конструкция
# r - режим чтения
# with open("test.txt", "r") as file:
#     file.write("test string")

# r+ - режим чтения и записи
# with open("test.txt", "r+") as file:
#     file.write("test string")

# "w" - не дописывает, а переписывает
# with open("test.txt", "w") as file:
#     file.write("some new string")
#
# with open("test.txt", "a") as file:
#     file.write("some new string\n")


# with open("test_new.txt", "a") as file:
#     file.write("some new string\n")


# with open("test_new.txt", "w") as file:
#     for line in range(10):
#         file.write(f"New string {line}\n")


# with open("test_new.txt", "r+") as file:
#     print(file.readline())
#     print("~~~~~~~~~~")
#     print(file.readlines())


# def reader():
#     with open("test_new.txt", "r+") as file:
#         print(file.readlines())
#
# Создадим функцию для записи в файл
# def writer():
#     with open("test_new.txt", "r+") as file:
#         for line in range(10):
#             file.write(f"New line {line}\n")


# Допустим, нам нужно обрабатывать огромные файлы и искать в них ошибки. critical_issues - показатели наших ошибок
# critical_issues = ["[Error]", '[Warning]', 'Traceback']
#
#
# def reader():
#     with open("test_new.txt", "r+") as file:
#         lines = file.readlines()
#         lines_with_issues = [line for line in lines if any(issue in line for issue in critical_issues)]
#         print(lines_with_issues)


'''
дз. Представим функцию, которая принимает аргументом словарь, возвращает None.
Она должна открывать файл настроек (settings.cfg). Считаем, что этот файл существует и в нем есть какие-то настройки.
ip_address: 127.0.0.1
port: 8080
use_ssl:True
is_admin:False
Наполнение - на выбор.
Этот словарь прилетает с такими же параметрами-ключами. 
Прилетающий словарь может содержать все поля из конфигурационного файла, или только несколько.
На лишние элементы программа тоже не должна ругаться, а должна их игнорировать.
Наша функция должна работать со словарем-аргументом. Если прилетевшие данные отличаются от того, что записано в файле,
то перезаписать значения. 

'''


