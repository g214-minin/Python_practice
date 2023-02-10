

def leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


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
    

def zodiac(d, m):
    if m == 3 and 21 <= d <= 31 or m == 4 and 1 <= d <= 20:
        return 'Овен'
    elif m == 4 and 21 <= d <= 30 or m == 5 and 1 <= d <= 20:
        return 'Телец'
    elif m == 5 and 21 <= d <= 31 or m == 6 and 1 <= d <= 21:
        return 'Близнецы'
    elif m == 6 and 22 <= d <= 30 or m == 7 and 1 <= d <= 22:
        return 'Рак'
    elif m == 7 and 23 <= d <= 31 or m == 8 and 1 <= d <= 23:
        return 'Лев'
    elif m == 8 and 24 <= d <= 31 or m == 9 and 1 <= d <= 23:
        return 'Дева'
    elif m == 9 and 24 <= d <= 30 or m == 10 and 1 <= d <= 23:
        return 'Весы'
    elif m == 10 and 24 <= d <= 31 or m == 11 and 1 <= d <= 22:
        return 'Скорпион'
    elif m == 11 and 23 <= d <= 30 or m == 12 and 1 <= d <= 21:
        return 'Стрелец'
    elif m == 12 and 22 <= d <= 31 or m == 1 and 1 <= d <= 20:
        return 'Козерог'
    elif m == 1 and 21 <= d <= 31 or m == 2 and 1 <= d <= 18:
        return 'Водолей'
    elif m == 2 and 19 <= d <= 29 or m == 3 and 1 <= d <= 20:
        return 'Рыбы'
