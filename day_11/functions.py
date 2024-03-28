# Day 11 - 30 Days of Python

def add_two_numbers(num1, num2):
    return num1 + num2
print(add_two_numbers(3, 4))

def area_of_circle(r):
    return 3.14 * r ** 2
print(area_of_circle(10))

def sum_of_numbers(*args):
    total = 0
    for num in args:
        if isinstance(num, int):
            total += num
        else:
            return '{} is not a valid input'.format(num)
    return total
print(sum_of_numbers(1, 2, 'Arg', 4, 5))

def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32
print(convert_celsius_to_fahrenheit(36))

def check_season(month):
    if month.lower() in ['september', 'october', 'november']:
        return 'Autumn'
    elif month.lower() in ['december', 'january', 'february']:
        return 'Winter'
    elif month.lower() in ['march', 'april', 'may']:
        return 'Spring'
    elif month.lower() in ['june', 'july', 'august']:
        return 'Summer'
    else:
        return 'Invalid month'
print(check_season('April'))

def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)
print(calculate_slope(1, 2, 9, 10))

def solve_quadratic(a, b, c):
    d = b ** 2 - 4 * a * c
    x1 = (-b + d ** 0.5) / 2 * a
    x2 = (-b - d ** 0.5) / 2 * a
    return x1, x2
print(solve_quadratic(1, -5, 6))

def print_list(*args):
    for i in args:
        print(i)
lst = [1, 2, 3, 4, 5]
print_list(*lst)

def reverse_list(lst):
    for i in range(len(lst) - 1, -1, -1):
        print(lst[i])
reverse_list([1, 2, 3, 4, 5])

def capitalize_list_items(lst):
    return [i.capitalize() for i in lst]
print(capitalize_list_items(['python', 'numpy', 'pandas', 'django', 'flask']))

def add_item(lst, item):
    lst.append(item)
    return lst
lst = [1, 2, 3, 4, 5]
print(add_item(lst, 6))

def remove_item(lst, item):
    lst.remove(item)
    return lst
print(remove_item(lst, 6))

def sum_of_numbers(num):
    total = 0
    for i in range(num + 1):
        total += i
    return 'Sum of all numbers in the range of {} = {}'.format(num,total)
print(sum_of_numbers(100))

def sum_of_odds(num):
    total = 0
    for i in range(num + 1):
        if i % 2 != 0:
            total += i
    return 'Sum of all odd numbers in the range of {} = {}'.format(num,total)
print(sum_of_odds(100))

def sum_of_evens(num):
    total = 0
    for i in range(num + 1):
        if i % 2 == 0:
            total += i
    return 'Sum of all even numbers in the range of {} = {}'.format(num,total)
print(sum_of_evens(100))

def evens_and_odds(num):
    evens = 0
    odds = 0
    for i in range(num + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return 'The number of evens are {}\nThe number of odds are {}'.format(evens, odds)
print(evens_and_odds(100))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
print(is_prime(11))

def are_items_unique(lst):
    return len(lst) == len(set(lst))
print(are_items_unique([1, 2, 3, 4, 5]))

def are_items_same_type(lst):
    return len(set([type(i) for i in lst])) == 1
print(are_items_same_type([1, 2, 3, 4.7, 5]))