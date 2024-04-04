def example(value, *args, z=15, **kwargs):
    print(value)
    print(args)
    print(z)
    print(kwargs)


example('eat some more of these sweet buns and drink some tea', 14, 13, 15, 8, z=10, name='James', surname='Bond')

#
print('----------------------')
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(9))
