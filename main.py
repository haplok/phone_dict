# Структура проекта:
# 1. main.py - текущий, основной файл, отвечает за интерфейс меню.
# 2. dict_functions.py - все основные и второстепенные функции программы.
# 3. data.py - все настройки программы и общие 'константы' программы.
# 4. phone_dict.txt - файл для хранения данных программы.
import os

from dict_functions import *

print(logo)
input('Нажмите [Enter] для перехода в основное меню')

while True:
    os.system('cls')
    print(''' 
[0] - Генерация случайных записей в справочник,
[1] - Вывод постранично записей из справочника на экран, 
[2] - Добавление новой записи в справочник,
[3] - Редактирование записи в справочнике,
[4] - Поиск записей по одной или нескольким характеристикам,
[x] - Выход из программы.''')
    select_key: str = input('Введите цифру для навигации по меню: ')
    if select_key == '0':
        os.system('cls')
        print('Введите количество генерируемых записей:', end=' ')
        amount_record = input()
        if amount_record.isdigit() and amount_record != '0':
            record_generator(int(amount_record))
        else:
            input_error(amount_record)

    elif select_key == '1':
        page_by_page(get_from_file())
    elif select_key == '2':
        insert_new()
    elif select_key == '3':
        edit_dict(get_from_file())
    elif select_key == '4':
        find_record(get_from_file())
    elif select_key == 'x' or select_key == 'X':
        os.system('cls')
        print('Программу создал Артем Ершов')
        break

    else:
        input_error(select_key)
