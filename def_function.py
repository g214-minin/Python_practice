def minimum(a, b, c): print(min(a, b, c))  # Минимум трёх чисел


minimum(31, 135, 12)


def amount(number): print(len(number))  # Вычисления кол-во цифр в числе


amount("123")


def sum_interval(n_0):  # Сумма чисел от 1 до n
    s = 0
    i = 1
    while i < n_0:
        s = i + s
        i = i + 1
    print(s)


sum_interval(10)


def factorial(n_1):  # Факториал n
    i = 0
    s = 1
    while i < n_1:
        i += 1
        s = i * s
    print(s)


factorial(5)
