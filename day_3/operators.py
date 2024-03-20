#Day 3: 30 Days of python programming

age = 1
heigth = 1.1
complex_number = 1 + 1j

base = int(input('Enter base: '))
heigth = int(input('Enter height: '))
print('Area of triangle is:', 0.5 * base * heigth)

side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))
print('Perimeter of triangle is:', side_a + side_b + side_c)

length = int(input('Enter length: '))
width = int(input('Enter width: '))
print('Area of rectangle is:', length * width)
print('Perimeter of rectangle is:', 2 * (length + width))

radius = int(input('Enter radius: '))
print('Area of circle is:', 3.14 * radius ** 2)
print('Circumference of circle is:', 2 * 3.14 * radius)

print(len('python'))
print(len('dragon'))
print(not(len('python') == len('dragon')))

print('on' in ('python' and 'dragon'))

print('jargon' in 'I hope this course is not full of jargon')

print('on' not in ('python' and 'dragon'))

python_length = len('python')
print ('Float', type(float(python_length)))
print ('String', type(str(python_length)))

print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)