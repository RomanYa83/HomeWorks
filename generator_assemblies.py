print("Задача 1: Фабрика Функций")
def operations(operation):
    if operation == "mult":
        def mult(a, b):
            return a * b
        return mult
    elif operation == "divide":
        def divide(a, b):
            return a / b
        return divide


my_choice_mult = operations("mult")
print(my_choice_mult(2, 8))
my_choice_divide = operations("divide")
print(my_choice_divide(17, 8))

print("Задача 1: Фабрика Функций_2")

def sum(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multi(a, b):
    return a * b


def div(a, b):
    return a / b


def select_operation(choice):
    if choice == "plus":
        return sum
    elif choice == "minus":
        return subtract
    elif choice == "multiply":
        return multi
    else:
        return div


operation = select_operation("plus")
print(operation(5, 7))
operation = select_operation("minus")
print(operation(7, 95))
operation = select_operation("multiply")
print(operation(312, 475))
operation = select_operation("div")
print(operation(5, 7))


print("Задача 2: Возведение в квадрат (Лямбда-функции)")

square = lambda a: a ** 2
print(square(4))

print("Задача 2: Возведение в квадрат (с использованием def)")


def square(a):
    return a ** 2

print(square(4))

print("Задача 3: Вызываемые Объекты")

class Area:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __call__(self, *args, **kwargs):
        return self.a * self.b


area = Area(5, 6)
print(f'Площадь равна: {area()}')