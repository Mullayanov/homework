def get_mask_card_number(card_number: int) -> str:
    """
    Принимает на вход номер карты и возвращает ее маску.
    Формат маски: XXXX XX** **** XXXX
    7000792289606361 - входной аргумент
    7000 79** **** 6361 - выход функции
    """
    number_musk: str = str(card_number).replace(str(card_number)[6:12], "*" * len(str(card_number)[6:12]))
    done_card_number: str = " ".join([number_musk[i : i + 4] for i in range(0, len(number_musk), 4)])
    return done_card_number


def get_mask_account(account_number: int) -> str:
    """
    Принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате: **XXXX
    73654108430135874305 - входной аргумент
    **4305 - выход функции
    """
    number: str = str(account_number)
    done_account_number = number.replace(number[:-4], "*" * 2)
    return done_account_number
