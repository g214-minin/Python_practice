# 1 a)
result_0 = (101 + 0) / 3
print(f"1. a) {result_0}")
# b)
result_0 = 3.0e-6 * 10000000.1
print(f"1. b) {result_0}")
# 2
number_0 = 1  # int(input("Введите 1 число: "))
number_1 = 1  # int(input("Введите 2 число: "))
number_2 = 1  # int(input("Введите 3 число: "))
number_3 = 1  # int(input("Введите 4 число: "))
result_1 = number_0 == number_1 == number_2 == number_3
print(f"2. {result_1}")
# 3
arr = [312, 322, 122, 397, 444, 900, 12, 331, 567]
max_0 = max(arr)
print(f"3. {max_0}")
# 4
min_0 = min(arr)
print(f"4. {min_0}")
# 5
medium_number = sum(arr) / len(arr)
arr.append(medium_number)
print(f"5. {[i for i in arr if i > medium_number]}")
# 6
number_0 = 5  # int(input("Введите 1 число: "))
number_1 = 7  # int(input("Введите 2 число: "))
s = 0
for i in range(number_1):
    s += number_0
print(f"6. {s}")
# 7
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = 0
for i in arr:
    s += 1
    i = i % 2
    if i == 0:
        print(f"7. Чётное число {s}")
    else:
        print(f"7. Не чётное {s}")
# 8
far = 321.75  # float(input("Введите температуру по Фарангейту: "))
cel = 5/9 * (far - 32)
print(f"8. Температура по цельсию: {cel}")
# 9
growth = 170  # float(input("Введите свой рост: "))
weight = 70  # float(input("Введите свой вес: "))
growth /= 100
BMI = weight / (growth**2)
if BMI < 16:
    print(f"9. Выраженный дефицит массы тела, ИМТ = {BMI}")
elif BMI < 18.5:
    print(f"9. Недостаточная (дефицит) масса тела, ИМТ = {BMI}")
elif BMI < 25:
    print(f"9. Норма, ИМТ = {BMI}")
elif BMI < 30:
    print(f"9. Избыточная масса тела (предожирение), ИМТ = {BMI}")
elif BMI < 35:
    print(f"9. Ожирение 1 степени, ИМТ = {BMI}")
elif BMI < 40:
    print(f"9. Ожирение 2 степени, ИМТ = {BMI}")
elif BMI > 40:
    print(f"9. Ожирение 3 степени, ИМТ = {BMI}")
# 10
number_0 = 5
print(f"10. {number_0**2}, {number_0**3}, {number_0**4}")
# 11
a = 20  # int(input("Сторона a = "))
b = 20  # int(input("Сторона b = "))
c = 45  # int(input("Сторона c = "))
if a + b > c and a + c > b and b + c > a:
    print("11. Треугольник существует")
else:
    print("11. Треугольник не существует")
