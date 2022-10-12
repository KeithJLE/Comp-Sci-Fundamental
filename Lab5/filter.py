# CPE 101-01
# LAB 5: Filter Functions
# Name: Keith Lee
# Section: 7

# 1) purpose statement: This function returns the even values from an input list.
# signature: list -> list
def are_even(numbers):
    evens = [i for i in numbers if i % 2 == 0]
    return evens


# 2) purpose statement: This function removes the duplicate numbers from an input list and returns a list without the
# duplicates. The first instance remains in original location.
# signature: list -> list
def remove_duplicates(numbers):
    new_numbers = []
    i = 0
    while i < len(numbers):
        if numbers[i] not in new_numbers:
            new_numbers.append(numbers[i])
        i += 1
    return new_numbers


# 3) purpose statement: This function takes an input list and a value 'n'. This function finds the integers in
# the input list that are divisible by the 'n' value and returns a new list with those values.
# signature: list int -> list
def are_divisible_by_n(numbers, n):
    new_numbers = []
    for i in range(len(numbers)):
        if numbers[i] % n == 0:
            new_numbers.append(numbers[i])
        i += 1
    return new_numbers
