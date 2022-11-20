# from random import randint
#
# # 1)
# sps1 = []
# sps2 = []
#
# new_nechet = []
# new_chet = []
# for i in range(15):
#     random_num1 = randint(-100, 100)
#     random_num2 = randint(-100, 100)
#
#     sps1.append(random_num1)
#     sps2.append(random_num2)
#
# for i in sps1:
#     if i % 2 == 0:
#         new_chet.append(i)
# print(f"{new_chet} чёт")
#
# for i in sps2:
#     if i % 2 > 0:
#         new_nechet.append(i)
# print(f"{new_nechet} нечёт")
#
# # 2)
# i = 1
# j = 1
# while i < 10:
#     while j < 10:
#           print(i * j, end="\t")
#           j += 1
#     print("\n")
#     j = 1
#     i += 1
# # 3) 4)
#
# with open("D:\\test.txt", "w") as txt:
#     txt.write("1 строка \n2 строка\n3 строка\n4 строка\n5 строка\n6 строка\n7 строка")
#
# with open("D:\\test.txt", "r") as txt:
#     strs = txt.readlines()
#     strs = [line.rstrip() for line in strs]
#     result = strs[:4]
#     for line in result:
#         with open("D:\\result.txt", "a") as result_txt:
#             result_txt.write(line)
#
#     result = strs[4:5]
#     for line in result:
#         with open("D:\\result1.txt", "a") as result_txt1:
#             result_txt1.write(line)
# # 5)
# end_num = int(input("Введите конечное число: "))
# sum_num = sum(range(1, end_num))
# sum_num += end_num
# print(sum_num)
# # 6)
# list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(len(list_num), -1, -1):
#     print(i)