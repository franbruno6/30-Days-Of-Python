#Day 9 - 30 Days of Python

age = int(input('Enter your age: '))
if age>=18:
    print('You are old enough to learn to drive.')
else:
    print(f'You need {18-age} more years to learn to drive.')

my_age = 30
your_age = int(input('Enter your age: '))
if (your_age - 1) == my_age:
    print(f'You are {your_age-my_age} year older than me.')
elif your_age > my_age:
    print(f'You are {your_age-my_age} years older than me.')
elif your_age == my_age:
    print('We are of the same age.')
else:
    print(f'You are {my_age-your_age} years younger than me.')

a = int(input('Enter number a: '))
b = int(input('Enter number b: '))
if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}')

student_score = int(input('Enter your score: '))
if student_score >= 80 and student_score <= 100:
    print('A')
elif student_score >= 70 and student_score < 80:
    print('B')
elif student_score >= 60 and student_score < 70:
    print('C')
elif student_score >= 50 and student_score < 60:
    print('D')
elif student_score >= 0 and student_score < 50:
    print('F')

month = input('Enter month: ')
if month == 'September' or month == 'October' or month == 'November':
    print('The season is Autumn')
elif month == 'December' or month == 'January' or month == 'February':
    print('The season is Winter')
elif month == 'March' or month == 'April' or month == 'May':
    print('The season is Spring')
elif month == 'June' or month == 'July' or month == 'August':
    print('The season is Summer')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit: ')
if fruit in fruits:
    print(f'{fruit} is already in the list')
else:
    fruits.append(fruit)
    print(fruits)


person={
    'first_name': 'Francisco',
    'last_name': 'Bruno',
    'age': 25,
    'country': 'Argentina',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if 'skills' in person:
    skills_len = len(person['skills'])
    middle_index = skills_len // 2
    print(person['skills'][middle_index])
    if 'Python' in person['skills']:
        print('Python is in the skills')
    else:
        print('Python is not in the skills')
    if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print('He is a fullstack developer')
    elif 'Node' in person['skills'] and 'MongoDB' in person['skills'] and 'Python' in person['skills']:
        print('He is a backend developer')
    elif 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print('He is a front end developer')
    else:
        print('Unknown title')
if 'address' in person:
    print(f"{person['first_name']} lives in {person['address']['street']} and his zipcode is {person['address']['zipcode']}")
