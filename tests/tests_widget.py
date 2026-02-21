import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "number_or_account, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Maestro 1249275120125", "Введен некорректный номер карты"),
        ("Счет 25298158105196", "Введен некорректный номер счета"),
        ("Visa Classic 46840624", "Введен некорректный номер карты"),
        ("", "Введены некорректные данные"),
    ],
)
def test_mask_account_card(number_or_account, expected):
    assert mask_account_card(number_or_account) == expected


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-01-30T02:26:18.671407", "30.01.2023"),
        ("2025-10-33T02:26:18.671407", "Введена некорректная дата"),
        ("3254-02-56T02:26:18.671407", "Введена некорректная дата"),
        ("2026-05-31", "31.05.2026"),
        ("02-05-2015", "Введена некорректная дата"),
        ("", "Введена некорректная дата"),
    ],
)
def test_get_date(date, expected):
    assert get_date(date) == expected
