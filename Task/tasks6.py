

def matrix_generator(num):

    array = [[step * 0 for step in range(num)] for _ in range(num)]

    i = 0
    j = 1

    while i < num:
        array[i][-i-1] = 1
        i += 1

    while j < num:
        array[j][-j] = 2
        j += 1

    return array


# test = matrix_generator(8)
#
# for w in test:
#     print(w)