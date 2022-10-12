# Name: Keith Lee
# Section: 7

# 1) purpose statement: This function tells you whether your integer is odd or not.
# signature: int -> bool
def is_odd(num):
    return num % 2 != 0

# 2) purpose statement: This function tells you whether your integer is in the specified interval or not.
# signature: int -> bool
def in_an_interval(num):
    return -10 <= num < -4 or -2 <= num <= 8 or 27 < num < 52 or 10 < num <= 22 or 110 <= num <= 237

# 3) purpose statement: This function tells you whether your two integers are in their specified intervals and also if the first integer is evenly divisible by the second integer.
# signature: int int -> bool
def is_divisible_in_interval(num1, num2):
    return 75 <= num1 <= 140 and 30 < num2 <= 200 and num1 % num2 == 0

