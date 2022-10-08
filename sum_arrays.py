# Сумма двух массивов с отрицательными и положительными значениями
from random import randint

numbers_pos = []
numbers_neg = []

for i in range(15):

    random_number_pos = randint(1, 100)
    random_number_neg = randint(-100, -1)

    numbers_pos.append(random_number_pos)
    numbers_neg.append(random_number_neg)

print(f"Массив с положительными числами = {numbers_pos}\nМассив с отрицательными числами = {numbers_neg}")
sum_pos = sum(numbers_pos)
sum_neg = sum(numbers_neg)
print(f"Сумма положительного массива = {sum_pos}\nСумма отрицательного массива = {sum_neg}")
