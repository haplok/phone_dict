def page_by_page():
    pass


def insert_new():
    pass


def edit_dict():
    pass


def find_record():
    pass


while True:
    print('''Нажмите цифру для навигации по меню: 
[1] - Вывод постранично записей из справочника на экран, 
[2] - Добавление новой записи в справочник,
[3] - Возможность редактирования записей в справочнике,
[4] - Поиск записей по одной или нескольким характеристикам.''')
    select_key: str = input()
    if select_key == '1':
        page_by_page()
    elif select_key == '2':
        insert_new()
    elif select_key == '3':
        edit_dict()
    elif select_key == '4':
        find_record()

    else:
        print(
            f'Ошибка ввода( {select_key} ), для возврата в главное меню нажмите Enter'
        )
        input()
