# CPE 101-01
# LAB 5: Map Functions
# Name: Keith Lee
# Section: 7


# 1) purpose statement: This function takes an input list and returns a new list with each value from the input list cubed.
# signature: list -> list
def cube_all(numbers):
    cube = [i ** 3 for i in numbers]
    return cube


# 2) purpose statement: This function takes an input list and float 'n' value. The function returns a new list with
# the value of 'n' added to each item from the input list.
# signature: list float -> list
def add_n_to_all(numbers, n):
    i = 0
    new_numbers = []
    while i < len(numbers):
        new_numbers.append(numbers[i] + n)
        i += 1
    return new_numbers


# 3) purpose statement: This function takes an input list and checks if each item in the input list is divisible by 5.
# Then the function returns a new list with True/False to each corresponding number and whether they are divisible by 5.
# signature: list -> list
def div_by_5_all(numbers):
    bools = []
    for i in range(len(numbers)):
        bools.append(numbers[i] % 5 == 0)
    return bools
