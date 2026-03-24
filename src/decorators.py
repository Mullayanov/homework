def log(filename=None):
    """
    Декоратор для логирования работы функций.

    Принимает необязательный аргумент filename:
    - Если filename задан, логи записываются в указанный файл.
    - Если filename не задан, логи выводятся в консоль.

    Логирование включает:
    - Имя функции и результат выполнения при успешной операции.
    - Имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            args_repr_list = []
            for arg in args:
                args_repr_list.append(repr(arg))
            kwargs_repr_list = []
            for key, value in kwargs.items():
                kwargs_repr_list.append(f"{repr(key)}={repr(value)}")
            inputs_repr = ", ".join(args_repr_list + kwargs_repr_list)

            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)

                return result

            except Exception as error:
                error_type = type(error).__name__
                log_message = f"{func.__name__} error: {error_type}. Inputs: ({inputs_repr})"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)

                raise

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__

        return wrapper

    return decorator
