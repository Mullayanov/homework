import random
from typing import Iterator


def filter_by_currency(transactions: list, currency_code: str) -> Iterator[list]:
    """
    Функция принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
    (например, USD).
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """
    Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Функция выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999
    """
    number: int = random.randint(start, stop)
    number_str: str = str(number).zfill(16)
    result: str = " ".join(number_str[i: i + 4] for i in range(0, 16, 4))
    yield result
