#Day 4: 30 Days of python programming

thirty = 'Thirty'
days = 'Days'
python = 'Python'
sentence = '{} {} Of {}'.format(thirty, days, python)
print(sentence)

coding = 'Coding'
_for = 'For'
all = 'All'
sentence = f'{coding} { _for} {all}'
print(sentence)

company = 'Coding For All'
print(company)
print(len(company))
print('Upper:',company.upper())
print('Lower:', company.lower())
print('Capitalize:', company.capitalize())
print('Title:', company.title())
print('Swapcase:', company.swapcase())

print(company[7:])
print('Index:', company.index('Coding'))
print('Replace:', company.replace('Coding', 'Python'))
print('Split:', company.split(' '))
companys = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print('Split:', companys.split(', '))
print(company[0])
print(len(company) - 1)
print(company[10])
print(company.index('C'))
print(company.index('F'))
company = 'Coding For All People'
print(company.rfind('l'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
print(sentence.rindex('because'))
print(sentence.replace('because ', ''))

print(company.startswith('Coding'))
print(company.startswith('coding'))

company = '   Coding For All    '
print(company.strip().rstrip())

print(('30DaysOfPython').isidentifier())
print(('thirty_days_of_python').isidentifier())

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(python_libraries))