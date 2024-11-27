def is_prime(func):
    def wrapper(a, b, c):
        res = func(a, b, c)
        for i in range(2, res - 1):
            if res % i == 0:
                return f'Составное - {res}'
        return f'Простое - {res}'
    return wrapper

@is_prime
def sum_three(a:int, b:int, c:int):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
