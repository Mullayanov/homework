def filter_by_state(list_dict_for_filtering: list, value_for_state: str = "EXECUTED") -> list:
    """
    Функция принимает список словарей и значение для ключа "state",
    и возвращает только те словари, в которых значение ключа "state", соответствует
    указанному значению
    """
    the_filtered_list: list = []
    for list_value in list_dict_for_filtering:
        if list_value["state"] == value_for_state.upper():
            the_filtered_list.append(list_value)
    return the_filtered_list


def sort_by_date(list_dict_for_sorting: list, is_sorting_order: bool = True) -> list:
    """
    Функция возвращает список словарей отсортированный по значеню "date".
    Порядок сортировки по умолчанию - убывание.
    """
    return sorted(list_dict_for_sorting, key=lambda list_dict: list_dict["date"], reverse=is_sorting_order)
