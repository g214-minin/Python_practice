# Калькулятор приведённых/неприведенных уравнений общего вида и основных арифметических операции

print("перейти к калькулятору квадратных уравнений - 1")
print("перейти к калькулятору основных арифметических операции - 2")

solution = int(input("\nВведите 1 или 2: "))

if solution == 1:  # если 1 = 1 то переход к блоку кода квадратного уравнение

    coefficient_A = float(input("Введите старший коэффициент a: "))

    if coefficient_A > 0:  # когда коэффициент "a" > 0 идёт ввод других коэффициентов и вычисление "D"

        print(f"a = {coefficient_A}")
        coefficient_B = float(input("Введите средний коэффициент b: "))
        print(f"b = {coefficient_B}")

        coefficient_C = float(input("Введите свободным член c: "))
        print(f"c = {coefficient_C}")

        discriminant = coefficient_B ** 2 - 4 * coefficient_A * coefficient_C
        print(f"\nD = {discriminant}")

        if discriminant == 0:  # алгоритм сравнения значения "D" далее вычисление корней по правилам математики

            x1 = - coefficient_B / (2 * coefficient_A)
            print(f"\nx = {x1}")

        elif discriminant > 0:

            x1 = (- coefficient_B + discriminant ** 0.5) / (2 * coefficient_A)
            x2 = (- coefficient_B - discriminant ** 0.5) / (2 * coefficient_A)
            print(f"x1 = {x1}\nx2 = {x2}")

        else:

            print("Корней нет")

    else:

        print("Введите правильный коэффициент (a > 0)")

elif solution == 2:  # если 2 = 2 то переход к блоку кода основных арифметических операции

    addition = 1  # +
    subtraction = 2  # -
    division = 3  # /
    multiplication = 4  # *

    number_1 = float(input("Введите первое число: "))
    number_2 = float(input("Введите второе число: "))

    print("Инфо: сложение - 1, вычитание - 2, деление - 3, умножение - 4")

    sign = int(input("Введите (1, 2, 3, 4,) для определение операции: "))
    if sign == 1:

        result = number_1 + number_2
        print(f"Сумма чисел равна: {result}")

    elif sign == 2:

        result = number_1 - number_2
        print(f"Разность чисел равна: {result}")

    elif sign == 3:

        result = number_1 / number_2
        print(f"Частное чисел равна: {result}")

    elif sign == 4:

        result = number_1 * number_2
        print(f"Произведение чисел равна: {result}")

    else:

        print("Введите корректное значение")
