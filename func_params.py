def print_params(a=1, b='String', c=True):
    print(a, b, c)


print_params()

def print_params(a=1, b='String', c=True):
    print(a, b)


print_params()


def print_params(a=1, b='String', c=True):
    print()


print_params()


def print_params(a=1, b='String', c=True):
    print(a, b, c)


print_params(b = 25, c = [1, 2, 3])


values_list = [5.5, False, 1]
values_dict = {'a': True, 'b': 111.1, 'c': 14}
values_list_2 = [2, True]


print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)