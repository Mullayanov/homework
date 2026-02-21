import pytest

from src.processing import filter_by_state, sort_by_date
from tests.confest import list_dict_for_tests


# Используем параметризацию, для теста с разными значениями 'state'
@pytest.mark.parametrize(
    "state_for_test, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("EMPTY", []),
    ],
)
def test_filter_by_state(list_dict_for_tests, state_for_test, expected):
    assert filter_by_state(list_dict_for_tests, value_for_state=state_for_test) == expected


@pytest.mark.parametrize(
    "sorting_order, expected",
    [
        (
            True,
            [
                {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
                {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
                {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
                {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
                {"date": "2018-06-30T02:08:58.425572", "id": 939719572},
                {"date": "2018-06-30T02:08:58.425572", "id": 939714636},
            ],
        ),
        (
            False,
            [
                {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
                {"date": "2018-06-30T02:08:58.425572", "id": 939719572},
                {"date": "2018-06-30T02:08:58.425572", "id": 939714636},
                {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
                {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
                {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
            ],
        ),
    ],
)
def test_sort_by_date(list_dict_for_tests, sorting_order, expected):
    assert sort_by_date(list_dict_for_tests, is_sorting_order=sorting_order) == expected
