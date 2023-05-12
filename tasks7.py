def task1(*arg):
    return arg
    

one = 1
two = 2

# print(task1(one, two))

def name_age(name: str, age: int):
    return f'Ваше имя - {name} Возраст - {age}'
    

# print(name_age('test', 12))


def calculation(num_one: int, num_two: int, operation: str):
    if operation == '+':
        result_sum = num_one + num_two
        return result_sum
    elif operation == '-':
        result_sub = num_one - num_two
        return result_sub
    elif operation == '+-':
        result_sum = num_one + num_two
        result_sub = num_one - num_two
        return result_sum, result_sub
        
        
# print(calculation(5, 5, '+-'))

def task3(a: int, b: int, c: int, d: int):
    if a == c-1 and b == d-1:
        return 'YES'
    else:
        return 'NO'
        

# print(task3(1, 2, 3, 4))
