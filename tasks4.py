

def leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# print(leap_year(1804))

def penny(pen):

    pen_str = str(pen)

    for i in range(11, 15):
        if i == pen:
            return f'{pen} - копеек'

    for i in range(5, 10):
        if i == int(pen_str[-1]):
            return f'{pen} - копеек'

    if int(pen_str[-1]) == 0:
        return f'{pen} - копеек'

    for i in range(2, 5):
        if i == int(pen_str[-1]):
            return f'{pen} - копейки'

    if int(pen_str[-1]) == 1:
        return f'{pen} - копейка'
