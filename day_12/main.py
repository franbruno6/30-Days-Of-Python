#Day 12 - 30 Days of Python

import random
import string

def random_user_id():
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return random_chars

print(random_user_id())

def user_id_gen_by_user():
    user_input = int(input("Enter the length of the user id: "))
    user_input2 = int(input("Enter how many user id you want to generate: "))
    for i in range(user_input2):
        random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=user_input))
        print(random_chars)

user_id_gen_by_user()

def rgb_color_gen():
    random_rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return random_rgb
print(rgb_color_gen())

def list_of_hex_colors():
    hex_colors = []
    for i in range(3):
        hex_colors.append('#{:02x}{:02x}{:02x}'.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    return hex_colors
print(list_of_hex_colors())

def list_of_rgb_colors():
    rgb_colors = []
    for i in range(3):
        rgb_colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    return rgb_colors
print(list_of_rgb_colors())

def generate_colors(color_type):
    if color_type == 'hex':
        return list_of_hex_colors()
    elif color_type == 'rgb':
        return list_of_rgb_colors()
    else:
        return 'Invalid color type'
input_color = input("Enter the color type(hex or rgb): ") 
print(generate_colors(input_color))   
