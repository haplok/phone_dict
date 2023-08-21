import random
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


# [1]
def page_by_page(content: list):
    page = 1
    print('┌' + '─' * (width - 2) + '┐')
    print('│' + ' ' * ((width - 12) // 2) + f'Страница {page}' + ' ' *
          ((width - 12) // 2) + '│')
    print('│', end='')
    title = ('-НОМЕР-', '-ИМЯ-', '-ФАМИЛИЯ-', '-ОТЧЕСТВО-', '-ОРГАНИЗАЦИЯ-',
             '-ТЕЛЕФОН РАБ-', '-ТЕЛЕФОН ЛИЧНЫЙ-')
    for t in title:
        print(t.ljust((width - 1) // 7), end='')
    print()
    for i in content:
        print('│', end='')
        formated_record_string(i)
    print('│' + ' ' * (width - 2) + '│')
    print('└' + '─' * (width - 2) + '┘')


# [2]
def insert_new():
    pass


# [3]
def edit_dict():
    pass


# [4]
def find_record():
    pass


# Дополнительные функции:


# Ошибка ввода
def read_error(key_str: list):
    print(
        f'Ошибка ввода( {key_str} ), для возврата в главное меню нажмите Enter'
    )
    input()


# Запись строк в файл
def clear_input_records(record_list: list):
    with open(text_file, 'w', encoding='utf-8') as file:
        for rl in record_list:
            file.write('\t\t\t'.join(rl))
            file.write('\n')


# Чтение всех строк из файла
def get_from_file() -> list:
    result = []
    with open(text_file, 'r', encoding='utf-8') as file:
        content = file.read().split('\n')
        result = [i.split('\t\t\t') for i in content if i != '']
    return result


# вывод одной строки на экран
def formated_record_string(content: list):
    for l in content:
        print(l.ljust((width - 1) // 7), end='')
    print()


page_by_page(get_from_file())