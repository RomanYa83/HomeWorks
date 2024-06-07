"""******с помощью функций высших порядков*******"""
def square(x):
    return x ** 2


def odd(x):
    return x % 2

numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

res = map(square, filter(odd, numbers))

print(list(res))

"""**************или с помощью списковой сборки****************"""

res = [x ** 2 for x in numbers if x % 2]

print(res)