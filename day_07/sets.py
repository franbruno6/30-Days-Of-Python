# Day 7: 30 Days of Python

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Tesla', 'SpaceX', 'GitHub'])
print(it_companies)
it_companies.remove('GitHub')
del it_companies

C = A.union(B)
print(C)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
A_B = A.symmetric_difference(B)
print(A_B)
del A_B, A, B

age_set = set(age)
print(len(age_set))
print(len(age))

string = 'I am a teacher and I love to inspire and teach people.'
sentence = string.split()
sentence = set(sentence)
print(len(sentence))
print(sentence)