from datetime import datetime


def filter_by_state(list_dict_for_filtering: list, value_for_state: str = "EXECUTED") -> list:
    """
    Функция принимает список словарей и значение для ключа "state",
    и возвращает только те словари, в которых значение ключа "state", соответствует
    указанному значению
    """
    return [data for data in list_dict_for_filtering if data.get("state", "").upper() == value_for_state.upper()]


def sort_by_date(list_dict_for_sorting: list, is_sorting_order: bool = True) -> list:
    """
    Функция возвращает список словарей отсортированный по значеню "date".
    Порядок сортировки по умолчанию - убывание.
    """
    # Отфильтровать словари без ключа 'state'
    filtered = [item for item in list_dict_for_sorting if "state" and "date" in item]
    return sorted(filtered, key=lambda x: x["date"], reverse=is_sorting_order)


def parse_date(date_str: str) -> datetime:
    """Функция приводит дату к datetime, поддерживаем несколько форматов"""
    formats = ("%Y-%m-%d", "%d.%m.%Y", "%Y/%m/%d", "%d-%m-%Y")
    if not isinstance(date_str, str):
        return datetime.min  # Если дата не строка — считаем минимальной
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError, TypeError:
            continue
        # Если ни один формат не подошёл — считаем минимальной датой, чтобы сортировать в начале
    return datetime.min
