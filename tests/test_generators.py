import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency_code, expected",
    [
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
            ],
        ),
        (
            "RUB",
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
        ),
        ("TRY", []),
    ],
)
def test_filter_by_currency(for_tests_filter_by_currency: list[dict], currency_code: str, expected: list[dict]) ->\
        None:
    """
    Проводим тест filter_by_currency со списком словарей при помощи фикстуры в модуле confest
    """
    result = list(filter_by_currency(for_tests_filter_by_currency, currency_code))
    assert result == expected


@pytest.mark.parametrize("currency_code_1, expected", [("USD", []), ("RUB", [])])
def test_filter_by_currency_with_empty_list(empty_list: list, currency_code_1: str, expected: list) -> None:
    """
    Проводиим тест filter_by_currency с пустым списком словарей
    """
    result = list(filter_by_currency(empty_list, currency_code_1))
    assert result == expected


@pytest.mark.parametrize(
    "expected",
    [
        [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации",
            "Перевод организации",
        ]
    ],
)
def test_transaction_descriptions(for_tests_filter_by_currency: list[dict], expected: str) -> None:
    """
    Проверяет функцию transaction_descriptions списком словарей при помощи фикстуры в модуле confest
    """
    result = list(transaction_descriptions(for_tests_filter_by_currency))
    assert result == expected


@pytest.mark.parametrize("expected", [[]])
def test_transaction_descriptions_with_empty_list(empty_list: list, expected: str) -> None:
    """
    Проверяет функцию transaction_descriptions с пустым списком словарей
    """
    result = list(transaction_descriptions(empty_list))
    assert result == expected


def test_card_number_generator() -> None:
    """
    Проверяет функцию card_number_generator, на правильность номеров карт и корректный формат
    """
    gen = card_number_generator(1, 9999999999999999)
    card = next(gen)
    parts = card.split(" ")
    assert len(parts) == 4
    assert all(len(part) == 4 and part.isdigit() for part in parts)
    assert len(card.replace(" ", "")) == 16
    num = int(card.replace(" ", ""))
    assert 0o00000000000001 <= num <= 9999999999999999
