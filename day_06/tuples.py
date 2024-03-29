#Day 6: 30 Days of python programming

empty_tpl = tuple()
brothers = ('Juan', 'Pedro', 'Carlos', 'Lucas')
sisters = ('Ana', 'Maria', 'Laura', 'Sofia')
siblings = brothers + sisters
print(len(siblings))
family_members = list(siblings)
family_members.append('Mama')
family_members.append('Papa')
family_members = tuple(family_members)
print(family_members)

family_members = list(family_members)
parents = family_members[-2:]
siblings = family_members[0:8]
print(parents)
print(siblings)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion')
animal_products = ('milk', 'meat', 'butter', 'yogurt')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_tp = list(food_stuff_tp)
middle_index = len(food_stuff_tp) // 2
middle_item = food_stuff_tp[middle_index]
food_stuff_tp.remove(middle_item)
print(food_stuff_tp)
print(middle_item)
food_stuff_tp = food_stuff_tp[3:-3]
print(food_stuff_tp)
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)