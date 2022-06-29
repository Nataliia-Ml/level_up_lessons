'''
дз. Представим функцию, которая принимает аргументом словарь, возвращает None.
Она должна открывать файл настроек (settings.cfg). Считаем, что этот файл существует и в нем есть какие-то настройки.
ip_address: 127.0.0.1
port: 8080
use_ssl: True
is_admin: False

Наполнение - на выбор.
Этот словарь прилетает с такими же параметрами-ключами.
Прилетающий словарь может содержать все поля из конфигурационного файла, или только несколько.
На лишние элементы программа тоже не должна ругаться, а должна их игнорировать.
Наша функция должна работать со словарем-аргументом. Если прилетевшие данные отличаются от того, что записано в файле,
то перезаписать значения.
Почитать больше о with open. Может придется писать 2 with open.
'''
# a_file = open("sample.txt", "r")
# list_of_lines = a_file.readlines()
# print(list_of_lines)
# list_of_lines[1] = "Line2\n"
# print(list_of_lines)
#
#
# a_file = open("sample.txt", "w")
# a_file.writelines(list_of_lines)
# a_file.close()
# Идея такова. Открываем файл настроек в режиме чтения, считываем все строки.
# Затем нужно как-то понять, что изменить в соответствии с начальными настройками.
# Далее открываем файл через запись и через метод .writelines() заменяем строки.


settings = [{"ip_address": "127.0.0.1", "port": "8080", "use_ssl": False, "is_admin": True},
            {"ip_address": "127.77.0.1", "port": "8080"},
            {"ip_address": "192.0.0.1", "debag_mode": False}
            ]

settings_one = {"ip_address": "192.0.0.1", "port": "8080", "use_ssl": False, "is_admin": True}


def change_settings(new_settings: dict):
    '''
    Если важно, чтобы настройки из нашего файла settings.cfg были по умолчанию,
    то в начале функции перезапишем в нее начальные значения.
    '''
    # with open('settings.cfg', 'w') as file:
    #     file.writelines(['ip_address: 127.0.0.1\n', 'port: 8080\n', 'use_ssl: True\n', 'is_admin: False\n'])

    with open('settings.cfg', 'r') as file:
        old_settings_list = file.readlines()
        print(f'old_settings_list: {old_settings_list}')

        old_settings_dict = {el.split(": ")[0]: el.split(": ")[1][:-1] for el in old_settings_list}
        # old_settings_dict["use_ssl"] = True
        # old_settings_dict["is_admin"] = False
        print(f'old_settings_dict: {old_settings_dict}')
        print(f'new_settings: {new_settings}')

        for k1, v1 in old_settings_dict.items():
            for k2, v2 in new_settings.items():
                if k1 == k2:
                    old_settings_dict[k1] = v2
        print(f'old_settings_dict: {old_settings_dict}')

        new_settings_list = []
        for k, v in old_settings_dict.items():
            new_settings_list.append(f"{k}: {v}\n")
        print(new_settings_list)

    with open('settings.cfg', 'w') as file:
        file.writelines(new_settings_list)


for setting in settings:
    change_settings(setting)
