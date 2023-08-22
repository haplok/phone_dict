import random
import os
from data import *


# [0]
def record_generator(amount_record: int):
    result = []
    for i in range(amount_record):
        telephone1: str = '79' + str(random.randint(10**8, 10**9 - 1))
        telephone2: str = '79' + str(random.randint(10**8, 10**9 - 1))
        organization = organizations.pop()
        organizations.add(organization)
        record = ()
        is_male = random.randint(0, 1)
        if is_male:
            record = (str(i + 1), names_male.pop(), surnames_male,
                      patronymic_male, organization, telephone1, telephone2)

        else:
            record = (str(i + 1), names_female.pop(), surnames_female,
                      patronymic_female, organization, telephone1, telephone2)
        result.append(record)

    clear_input_records(result)
    os.system('cls')
    print(
        f'Вы создали текстовый файл с {amount_record} сгенерированными записями'
    )
    input('Нажмите [Enter] для перехода в основное меню')


# [1]
def page_by_page(content: list):
    page = 1
    while page <= len(content) // records_in_page + 1:
        os.system('cls')
        print('┌' + '─' * (width - 2) + '┐')
        print('│' + ' ' * ((width - 12) // 2) + f'Страница {page}' + ' ' *
              ((width - 12) // 2) + '│')
        title_print()
        for i in content[(page - 1) * records_in_page:page * records_in_page]:
            print('│', end='')
            formated_record_string(i)
        print('│' + ' ' * (width - 2) + '│')
        print('└' + '─' * (width - 2) + '┘')
        page += 1
        if page <= len(content) // records_in_page + 1:
            input('Нажмите [Enter] для просмотра следующей страницы')
    input('Нажмите [Enter] для перехода в основное меню')


# [2]
def insert_new():
    os.system('cls')
    new_record = [''] + [input(f'Введите {t}: ') for t in title[1:-2]]
    for t in title[-2:]:
        telef = input(f'Введите {t} (9 чисел): +79')
        if telef.isdigit() and len(telef) == 9:
            new_record.append('79' + telef)
        else:
            input_error(telef)
            return
    os.system('cls')
    print('┌' + '─' * (width - 2) + '┐')
    print('│' + ' ' * ((width - 22) // 2) + 'Вы ввели новую запись!')
    title_print()
    print('│', end='')
    formated_record_string(new_record)
    print('└' + '─' * (width - 2) + '┘')
    input('Нажмите [Enter] для выхода в основное меню')
    add_record(new_record)


# [3]
def edit_dict(full_phone_dict: list):
    os.system('cls')
    num = input('Введите номер записи, которую нужно редактировать: ')
    position = 0
    for i in range(len(full_phone_dict)):
        if full_phone_dict[i][0] == num:
            position = i
            print('┌' + '─' * (width - 2) + '┐')
            title_print()
            print('│', end='')
            print('│' + ' ' * ((width - 21) // 2) + 'Вы изменяете запись: ')
            formated_record_string(full_phone_dict[i])
            print('└' + '─' * (width - 2) + '┘')
    new_record = [str(position + 1)
                  ] + [input(f'Введите {t}: ') for t in title[1:-2]]
    for t in title[-2:]:
        telef = input(f'Введите {t} (9 чисел): +79')
        if telef.isdigit() and len(telef) == 9:
            new_record.append('79' + telef)
        else:
            input_error(telef)
            return
    full_phone_dict[position] = new_record
    clear_input_records(full_phone_dict)
    os.system('cls')
    print('┌' + '─' * (width - 2) + '┐')
    title_print()
    print('│', end='')
    print('│' + ' ' * ((width - 20) // 2) + 'Обновленная запись: ')
    formated_record_string(full_phone_dict[position])
    print('└' + '─' * (width - 2) + '┘')
    input('Нажмите [Enter] для выхода в основное меню')


# [4]
def find_record(full_phone_dict: list):
    os.system('cls')
    search_record = [input(f'{t} должен содержать: ') for t in title]
    result = []
    os.system('cls')
    print('┌' + '─' * (width - 2) + '┐')
    title_print()
    print('│' + ' ' * ((width - 15) // 2) + 'Фильтр поиска: ')
    print('│', end='')
    formated_record_string(search_record)
    print('│' + ' ' * ((width - 18) // 2) + 'Результаты поска: ')
    for f in full_phone_dict:
        flag = True
        for i in range(len(f)):
            if search_record[i].lower() not in f[i].lower():
                flag = False
        if flag:
            result.append(f)
            print('│', end='')
            formated_record_string(f)

    print('└' + '─' * (width - 2) + '┘')
    input('Нажмите [Enter] для выхода в основное меню')


# Дополнительные функции:


# Ошибка ввода
def input_error(key_str: list):
    print(
        f'Ошибка ввода({key_str}), для возврата в главное меню нажмите Enter')
    input()


# Запись строк в файл
def clear_input_records(record_list: list):
    with open(text_file, 'w', encoding='utf-8') as file:
        for rl in record_list:
            file.write('\t\t\t'.join(rl))
            file.write('\n')


# Запись одной строки в конец файла
def add_record(record: list):
    with open(text_file, 'r', encoding='utf-8') as file:
        last_id = file.readlines()[-2].split('\t\t\t')[0]
        record[0] = str(int(last_id) + 2)
    with open(text_file, 'a', encoding='utf-8') as file:
        file.write('\t\t\t'.join(record))
        file.write('\n')


# Чтение всех строк из файла
def get_from_file() -> list:
    result = []
    with open(text_file, 'r', encoding='utf-8') as file:
        content = file.read().split('\n')
        result = [i.split('\t\t\t') for i in content if i != '']
    return result


# Вывод одной строки на экран
def formated_record_string(content: list):
    for l in content:
        print(l.ljust((width - 1) // len(title)), end='')
    print()


# Вывод шапки таблицы на экран
def title_print():
    print('│', end='')
    for t in title:
        print(t.ljust((width - 1) // len(title)), end='')
    print()
