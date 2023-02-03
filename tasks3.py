# 1) Да
# 2) -
# 3) #
# 4) int, str sets, tuples, boolean, list, dictionares, files
# 5) x = int(input(''))
# 6) int()
# 7) len()
# 8) -
# 9) Исходный код -> байт код -> PVM

# 3.
def parity(a, b):
    return (a + b) % 2 == 1


# print(parity(8, 8))


def mult_of_three(a, b, c):
    return (a % 3 == 0) == (b % 3 == 0) == (c % 3 == 0)


# print(mult_of_three(5, 9, 9))

# 1.
def dot(x, y):
    return y + 1 >= x and -y + 1 >= x and x + 1 >= y >= -x - 1


# print(dot(0.5, 0.5))
