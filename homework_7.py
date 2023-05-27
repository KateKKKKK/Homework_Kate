
def math_operations(num_1, num_2, operation):
    if operation == "+":
        return num_1 + num_2
    elif operation == "-":
        return num_1 - num_2
    elif operation == "/":
        return num_1 / num_2
    elif operation == "*":
        return num_1 * num_2
    else:
        print(f"Not known operation: {operation}")
print(math_operations(10,3, "-"))

import math

def square(side: float()):
    perimeter = 4 * side
    area = side ** 2
    diagonal = side * math.sqrt(2)
    return perimeter, area, diagonal
result = square(5)
print(result)
#

import math

def is_prime(num):
    if num < 2:
        return False
    for item in range(2, math.isqrt(num) + 1):
        if num % item == 0:
            return False
    return True
print(is_prime(970))
#
import re

def remove_numbers_from_file(file_):
    with open(file_, 'r') as file:
        lines = file.readlines()
    updated_lines = []
    for line in lines:
        updated_line = re.sub(r'\d+', '', line)
        updated_lines.append(updated_line)

    with open(file_, 'w') as file:
        file.writelines(updated_lines)

def calculate_sum(*args):
    total_sum = sum(args)
    return total_sum
print(calculate_sum(1,2,3,4,5))

def remove_vowels(string):
    vowels = ["A", "E", "I", "O", "U", "Y", "a", "e", "i", "o", "u", "y"]
    result = ""
    for item in string:
        if item not in vowels:
            result += item
    return result
result = remove_vowels("hello Kate")
print(result)


def display_box(width, height, character = str("*")):
    if width < 2 or height < 2:
        return
    top_line = character * width
    middle_line = character + " " * (width - 2) + character
    print(top_line)
    for item in range(height - 2):
        print(middle_line)
    print(top_line)
print(display_box(5, 4, 'x'))
