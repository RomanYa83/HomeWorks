class ProcessingException(Exception):
    pass
"""Класс исключения при делении на '0'"""




class InvalidDataException(Exception):
    pass
"""Класс исключения при вводе неверного типа данных"""


def div(a, b):
    if b == 0:
        raise ProcessingException("Деление на ноль невозможно!!!")
    return a / b


def inputValue():
    try:
        x, y = map(int, input().split())
        div(x, y)
    except ProcessingException as exc:
        print(f'Error: {exc}')
    except ValueError:
        raise InvalidDataException




inputValue()

