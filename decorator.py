def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 1:
            for i in range(2, int(result * 0.5) + 1):
                if result % i == 0:
                    print('Composite number')
                    return result
            print('Prime number')
            return result
        else:
            print('Prime number')
            return result
    return wrapper


@is_prime
def sum_three(x, y, z):
    total = x + y + z
    return total


total = sum_three(150, 149, 8)
print(total)