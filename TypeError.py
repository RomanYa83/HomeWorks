def all_what_you_want (a, b):

    try:
        result = a + b
    except TypeError as exc:
        result = str(a) + str(b)
        print(f'Странные аргументы {exc}, но результат таков: {result}')
    else:
        print(result)
    finally:
        print(f'Фуууухх, вроде всё срослось!')

print(all_what_you_want(10.11, '11'))
