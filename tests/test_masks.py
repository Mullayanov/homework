import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number, expected",
    [
        (7000792289606361, "7000 79** **** 6361"),
        (25902605674, "Введен некорректный номер карты"),
        ("", "Введен некорректный номер карты"),
    ],
)
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected


@pytest.mark.parametrize(
    "account, expected",
    [
        (73654108430135874305, "**4305"),
        (94569246428564024096240624, "Введен некорректный номер счета"),
        ("", "Введен некорректный номер счета"),
    ],
)
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected
