def subsequence_sign(array):

    j = 0
    sign = 0

    for i in array:

        for zero in array:

            if zero == 0:
                array.remove(0)

        if j == len(array)-1:
            break

        if i < 0 < array[j+1] or i > 0 > array[j+1]:
            sign += 1
            j += 1

        elif i < 0 > array[j+1] or i > 0 < array[j+1]:
            j += 1

    return sign


# test = [1, -34, 8, 14, -5, -3, -4, 6, 9, -2, 0, 1, -2, 0, 0]
# print(subsequence_sign(test))


def average_double(array):

    pos_nums = [i for i in array if i > 0]
    neg_nums = [i for i in array if i < 0]

    pos_nums.append(sum(pos_nums))
    neg_nums.append(sum(neg_nums))

    pos_nums.append(len(pos_nums)-1)
    neg_nums.append(len(neg_nums)-1)

    new_array = pos_nums[len(pos_nums)-2:] + neg_nums[len(neg_nums)-2:]

    new_array.append(new_array[0] / new_array[1])
    new_array.append(new_array[2] / new_array[3])

    del new_array[:-2]

    return new_array


# print(average_double(test))

