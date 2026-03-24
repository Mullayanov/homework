from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_number_or_account: str = "") -> str:
    """
    Функция принимает один аргумент - строку, содержащую тип и номер карты или счета
    Например: Visa Platinum 7000792289606361
              Maestro 7000792289606361
              Счет 73654108430135874305
    Возвращает строку с замаскированным номером.
    """
    if not type_number_or_account:
        return "Введены некорректные данные"

    parts = type_number_or_account.strip().split()
    if not parts:
        return "Введены некорректные данные"

    card_type = parts[0]
    number = parts[-1]

    if card_type == "Счет":
        if number.isdigit() and len(number) == 20:
            account_done_result: str = get_mask_account(str(number))
            return f"Счет {account_done_result}"
        else:
            return "Введен некорректный номер счета"

    elif number.isdigit() and len(number) == 16:
        return type_number_or_account.replace(number, get_mask_card_number(str(number)))
    else:
        return "Введен некорректный номер карты"


def get_date(date: str = "") -> str:
    """
    Функция принимает на вход дату в формате:
    "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате:
    "ДД.ММ.ГГГГ" ("11.03.2024")
    """
    if not date:
        return "Введена некорректная дата"
    elif (
        date[0:4].isdigit()
        and date[5:7].isdigit()
        and date[0:4].isdigit()
        and 1950 <= int(date[0:4]) <= 2050
        and 1 <= int(date[5:7]) <= 12
        and 1 <= int(date[8:10]) <= 31
    ):
        return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
    else:
        return "Введена некорректная дата"
