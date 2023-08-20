import random

from data import *


def record_generator(amount_record: int):
    result = []
    for i in range(amount_record):
        telephone1: str = '79' + str(random.randint(10**8, 10**9 - 1))
        telephone2: str = '79' + str(random.randint(10**8, 10**9 - 1))
        organization = organizations.pop()
        record = ()
        is_male = random.randint(0, 1)
        if is_male:
            record = (names_male.pop(), surnames_male, patronymic_male,
                      organization, telephone1, telephone2)
            print(*record)
        else:
            record = (names_female.pop(), surnames_female, patronymic_female,
                      organization, telephone1, telephone2)
            print(*record)


def page_by_page():
    pass


def insert_new():
    pass


def edit_dict():
    pass


def find_record():
    pass


def read_error(key_str):
    print(
        f'Ошибка ввода( {key_str} ), для возврата в главное меню нажмите Enter'
    )
    input()