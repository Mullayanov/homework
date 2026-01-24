from typing import Callable, Iterable

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
from src.widget import mask_account_card

mask_list = []

def foo(func: Callable, list_for: Iterable[list | str]):
    for item in list_arguments:
        mask_list.append(mask_account_card(item))
    print(mask_list)
print(foo(mask_account_card, list_arguments))
