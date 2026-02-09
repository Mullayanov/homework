from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

# Список вводных данных для проверки ДЗ 9.2
list_arguments = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
]
# Цикл подставляет вводные данные в функцию mask_account_card
for i in list_arguments:
    print(mask_account_card(i))
# Проверка работы функции get_date
print(get_date("2024-03-11T02:26:18.671407"))
# Список вводных данных для проверки ДЗ 10.1
list_dict = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
# Проверка работы функции filter_by_state
print(filter_by_state(list_dict, 'canceled'))
# Проверка работы функции sort_by_date.
# Для сортировки по убыванию, второй аргумент не указываем, либо указываем True.
# Для сортиировки по возрастанию, второй аргумент указываем False.
print(sort_by_date(list_dict, False))
