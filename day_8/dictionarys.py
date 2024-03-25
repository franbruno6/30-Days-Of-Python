#Day 8 - 30 Days of Python

dog = {}
dog['name'] = 'Dog'
dog['breed'] = 'Bulldog'
dog['legs'] = 4
dog['age'] = 6
print(dog)

student = {
    'first_name': 'Pepe',
    'last_name' : 'Argento',
    'gender' : 'male',
    'age' : 50,
    'marital status' : 'married',
    'skills' : ['Python', 'Java', 'C++'],
    'country' : 'Argentina',
    'city' : 'Buenos Aires',
    'address' : 'Av. Pepe Argento 742',
}
print(len(student))
student['skills'].append('SQL')
student['skills'].append('HTML')
print(student)
keys_list = list(student.keys())
print(keys_list)
values_list = list(student.values())
print(values_list)
taple_student = tuple(student.items())
print(taple_student)
student.pop('skills')
print(student)
del student