import random
import os
from data import *


# Основные функции
# [0] - Генерация случайных записей в справочник
def record_generator(amount_record: int) -> None:
    '''Функция принимает на вход целое чило - количество генерируемых записей.
    В результате, текстовый файл очищается и заполняется сгенерированными записями.
    Выводится информация об генерации в консоль.'''
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
    result[0] = creator
    clear_input_records(result)
    os.system('cls')
    print(
        f'Вы создали текстовый файл с {amount_record} сгенерированными записями'
    )
    input('Нажмите [Enter] для перехода в основное меню')


# [1] - Вывод постранично записей из справочника на экран
def page_by_page(content: list) -> None:
    '''Функция принимает на вход список списков с данными.
    В результате, выводится на экран постранично записи из справочника.'''
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


# [2] - Добавление новой записи в справочник
def insert_new() -> None:
    '''Функция осуществляет интерфейс ввода новой записи.
    В результате, выводится на экран новая введенная запись.'''
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


# [3] - Редактирование записи в справочнике
def edit_dict(full_phone_dict: list) -> None:
    '''Функции на вход подается список списков с данными.
    Функция осуществляет интерфейс корректировки записи по номеру.
    В результате, выводится на экран скорректированная запись.'''
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


# [4] - Поиск записей по одной или нескольким характеристикам
def find_record(full_phone_dict: list) -> None:
    '''Функции на вход подается список списков с данными.
    Функция осуществляет интерфейс поиска вхождения введенных строк в телефонном справочнике.
    В результате, выводится на экран подходящие записи в виде таблицы.'''
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
    if result == []:
        print('│' + ' ' * ((width - 39) // 2) +
              'По вашему запросу ничего не найдено :-(')

    print('└' + '─' * (width - 2) + '┘')
    input('Нажмите [Enter] для выхода в основное меню')


# Второстепенные функции:
# Ошибка ввода
def input_error(key_str: list) -> None:
    '''Функции на вход подается строка, вызвавшая ошибку.
    Функция сообщает пользователю, что введена некорректная последовательность символов.'''
    print(
        f'Ошибка ввода({key_str}), для возврата в главное меню нажмите Enter')
    input()


# Запись строк в файл
def clear_input_records(record_list: list) -> None:
    '''Функции на вход подается список списков с данными.
    Функция очищает файл, и записывает в него все введенные данные.'''
    with open(text_file, 'w', encoding='utf-8') as file:
        for rl in record_list:
            file.write('\t\t\t'.join(rl))
            file.write('\n')


# Запись одной строки в конец файла
def add_record(record: list) -> None:
    '''Функции на вход подается спискок с данными.
    Функция записывает в конец файла приведенную запись.'''
    with open(text_file, 'r', encoding='utf-8') as file:
        last_id = file.readlines()[-2].split('\t\t\t')[0]
        record[0] = str(int(last_id) + 2)
    with open(text_file, 'a', encoding='utf-8') as file:
        file.write('\t\t\t'.join(record))
        file.write('\n')


# Чтение всех строк из файла
def get_from_file() -> list:
    '''Функция создает список списков из всех данных из файла.'''
    result = []
    with open(text_file, 'r', encoding='utf-8') as file:
        content = file.read().split('\n')
        result = [i.split('\t\t\t') for i in content if i != '']
    return result


# Вывод одной строки на экран
def formated_record_string(content: list) -> None:
    '''Функция на вход принимает список с записью.
    Функция выводит на экран форматированно запись в виде строки таблицы'''
    for l in content:
        print(l.ljust((width - 1) // len(title)), end='')
    print()


# Вывод шапки таблицы на экран
def title_print() -> None:
    '''Функция выводит на экран форматированно шапку таблицы в виде строки'''
    print('│', end='')
    for t in title:
        print(t.ljust((width - 1) // len(title)), end='')
    print()
