import pytest

from src.decorators import log


@log()  # Тестирование без аргументов (вывод в консоль)
def add_numbers(a, b):
    """Складывает два числа."""
    return a + b


@log("test_log.txt")  # Тестирование с указанием файла
def multiply_numbers(a, b):
    """Умножает два числа."""
    return a * b


@log()
def divide_numbers(a, b):
    """Делит два числа, может вызвать ZeroDivisionError."""
    return a / b


@log("error_log.txt")
def subtract_numbers(a, b):
    """Вычитает два числа, может вызвать ValueError."""
    if b < 0:
        raise ValueError("Отрицательный делитель не допускается")
    return a - b


# --- Тесты ---


def test_log_decorator_console_success(capsys):
    """
    Тестирует декоратор log при выводе в консоль и успешном выполнении.
    """
    result = add_numbers(5, 3)
    assert result == 8

    captured = capsys.readouterr()

    # Проверяем, что в консоль был выведен лог
    # Ожидаем, что лог содержит имя функции, статус 'ok' и входные параметры
    assert "add_numbers ok" in captured.out


def test_log_decorator_file_success(tmp_path):
    """
    Тестирует декоратор log при записи в файл и успешном выполнении.
    """
    log_file = tmp_path / "test_log.txt"

    @log(str(log_file))  # Применяем декоратор с путем к файлу
    def square(x):
        return x * x

    result = square(7)
    assert result == 49

    # Читаем содержимое файла
    log_content = log_file.read_text()

    # Проверяем, что в файле есть запись о логе
    assert "square ok" in log_content


def test_log_decorator_console_error(capsys):
    """
    Тестирует декоратор log при выводе в консоль и возникновении ошибки.
    """
    with pytest.raises(ZeroDivisionError):
        divide_numbers(10, 0)  # Вызываем функцию, которая приведет к ошибке

    captured = capsys.readouterr()

    # Проверяем, что в консоль был выведен лог об ошибке
    assert "divide_numbers error: ZeroDivisionError" in captured.out


def test_log_decorator_file_error(tmp_path):
    """
    Тестирует декоратор log при записи в файл и возникновении ошибки.
    """
    error_log_file = tmp_path / "error_log.txt"

    @log(str(error_log_file))  # Применяем декоратор с путем к файлу
    def fail_function(data):
        if not isinstance(data, dict):
            raise TypeError("Ожидался словарь")
        return data.get("key")

    with pytest.raises(TypeError):
        fail_function([1, 2, 3])  # Вызываем функцию с некорректным типом данных

    # Читаем содержимое файла
    log_content = error_log_file.read_text()

    # Проверяем, что в файле есть запись об ошибке
    assert "fail_function error: TypeError" in log_content


def test_log_decorator_error_with_custom_exception(tmp_path):
    """
    Тестирует декоратор log с пользовательским исключением и записью в файл.
    """
    error_log_file = tmp_path / "custom_error_log.txt"

    @log(str(error_log_file))
    def process_data(value):
        if value < 0:
            raise ValueError("Значение не может быть отрицательным")
        return value * 2

    with pytest.raises(ValueError, match="Значение не может быть отрицательным"):
        process_data(-5)

    log_content = error_log_file.read_text()
    assert "process_data error: ValueError" in log_content


def test_log_decorator_preserves_function_metadata():
    """
    Проверяет, что декоратор сохраняет метаданные функции (имя и docstring).
    """

    @log()
    def my_function_with_meta():
        """Это тестовая функция с документацией."""
        pass

    assert my_function_with_meta.__name__ == "my_function_with_meta"
    assert my_function_with_meta.__doc__ == "Это тестовая функция с документацией."
