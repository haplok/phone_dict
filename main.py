import os

from dict_functions import *

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
        if amount_record.isdigit():
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
        break

    else:
        input_error(select_key)
