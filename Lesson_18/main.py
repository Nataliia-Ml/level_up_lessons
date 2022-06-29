'''Threads - потоки
Processe - процессы
Поток запускается в рамках одного memory space. Пусть есть 3 потока, которые зависяь от переменных (a, name, c)
Процесс может запускаться в разных ядрах и имеет разные memory space.
Потоки имеют доступ к 1 ячейке памяти и запускаются на одном ядре.
Процесс - разные ядра и разные ячейки памяти.
Пайтон-интерпретатор работает с OS, а ОС работает с Hardware
Сам пайтон не может запускать процессы и потоки. Нужна инструкция ему
Минусы процессов:
1) IPC - inter process communication. Тут используется более сложные (Semaphors, Pipe)
Обмен данными в процессах довольно сложный.
2) Large memory footprint - много памяти сжирают

Минусы потоков:
GIL - global interpreter Lock
Гил - это механизм в пайтоне, который блокирует выполнение двух потоков одновременно.

'''
import sys
import time
from threading import Thread as th
import requests
from PIL import Image
from io import BytesIO
import os


# def thread_function(name):
#     print(f"Thread {name} starting\n")
#     time.sleep(7)
#     print(f"Thread {name} finishing")


# запуск только функции:
# thread_function("first")
# print(f"Main Thread waiting for to be finished")

# запуск через потоки:
# x = th(target=thread_function, args=("first",))
# x.start()
# print(f"Main Thread waiting for {x} to be finished")

# дополним окончанием
# x.join()
# print("All threads done. Program will be closed.")
# sys.exit()


"""
Пропишем код для сохранения изображений с ис
"""
HTTPBIN = 'https://httpbin.org/'
IMAGE_ENDPOINT = "image/jpeg"
IMAGE_URL = os.path.join(HTTPBIN, IMAGE_ENDPOINT)


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time() - start
        print(f"{func.__name__} works {end}")
    return wrapper


def download_save_image(idx):
    res = requests.get(IMAGE_URL)
    img = Image.open(BytesIO(res.content))
    img.save(f"img_from_httpbin_{idx}.jpeg")


@timeit
def download_save_images():
    threads = []
    for i in range(10):
        threads.append(th(target=download_save_image, args=(i,)))
    res = [th.start() for th in threads]
    print(res)


download_save_images()


@timeit
def download_save_images_loop():
    for i in range(10):
        download_save_image(i)


download_save_images_loop()



