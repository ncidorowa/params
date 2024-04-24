def test_func(*params):
     print("Тип:", type(params))
     print("Аргумент:", params)
     print('Строка', params)
     print('Числа', params)

test_func(5, 6, 7)

def fac(n):
    if n == 1:
        return 1
    return fac(n - 1) * n


print(fac(6))