import os

from dict_functions import *

while True:
    print('''Нажмите цифру для навигации по меню: 
[0] - Генерация случайных записей в справочник,
[1] - Вывод постранично записей из справочника на экран, 
[2] - Добавление новой записи в справочник,
[3] - Редактирование записи в справочнике,
[4] - Поиск записей по одной или нескольким характеристикам.''')
    select_key: str = input()
    if select_key == '0':
        os.system('cls')
        print('Введите количество генерируемых записей:', end=' ')
        amount_record = input()
        if amount_record.isdigit():
            record_generator(int(amount_record))
        else:
            input_error(amount_record)
        input()
    elif select_key == '1':
        page_by_page(get_from_file())
    elif select_key == '2':
        insert_new()
    elif select_key == '3':
        edit_dict()
    elif select_key == '4':
        find_record()

    else:
        input_error(select_key)
