from src.masks import get_mask_account, get_mask_card_number

print(get_mask_card_number(7000792289606361))
print(get_mask_account(73654108430135874305))

list_arguments = ['Maestro 1596837868705199',
                  'Счет 64686473678894779589',
                  'MasterCard 7158300734726758',
                  'Счет 35383033474447895560',
                  'Visa Classic 6831982476737658',
                  'Visa Platinum 8990922113665229',
                  'Visa Gold 5999414228426353',
                  'Счет 73654108430135874305',
]

from src.widget import mask_account_card, get_date

for i in list_arguments:
    print(mask_account_card(i))

print(get_date("2024-03-11T02:26:18.671407"))