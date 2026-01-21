def mask_account_card(type_number_or_account: str) -> str:
    """
    Функция принимает один аргумент - строку, содержащую тип и номер карты или счета
    Например: Visa Platinum 7000792289606361
              Maestro 7000792289606361
              Счет 73654108430135874305
    Возвращает строку с замаскированным номером.
    """
    if "Счет" in type_number_or_account:
        from src.masks import get_mask_account
        account_done_result: str = get_mask_account(int(type_number_or_account[-20: ]))
        return f'Счет {account_done_result}'
    else:
        from src.masks import get_mask_card_number
        return type_number_or_account.replace(type_number_or_account[-16:],get_mask_card_number(int(type_number_or_account[-16:])))


def get_date(date: str):
    """
    Функция принимает на вход дату в формате:
    "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате:
    "ДД.ММ.ГГГГ" ("11.03.2024")
    """
    return f'{date[8:10]}.{date[5:7]}.{date[0:4]}'
