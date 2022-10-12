# Lab 2 Functions
# Name: Keith Lee
# Section: 7
from math import *


# 1) purpose statement:This function computes a given formula
# signature:int int -> float
def do_math(x, y):
    res_do_math = ((x * x) - ((3 / 5) * x * y * y)) / ((2 * x * x * y / 5) + 4)
    return res_do_math


# 2) purpose statement:This function computes the positive solution of a quadratic equation
# signature:int int int -> float
def quadratic_formula1(a, b, c):
    res_quadratic_formula1 = (((-b) + (sqrt((b * b) - (4 * a * c)))) / (2 * a))
    return res_quadratic_formula1


# 3) purpose statement:This function computes the negative solution of a quadratic equation
# signature:int int int -> float
def quadratic_formula2(a, b, c):
    res_quadratic_formula2 = (((-b) - (sqrt((b * b) - (4 * a * c)))) / (2 * a))
    return res_quadratic_formula2


# 4) purpose statement:This function computes the Manhattan distance between two points
# signature: int int int int -> int
def distance(x1, y1, x2, y2):
    res_distance = abs(x1 - x2) + abs(y1 - y2)
    return res_distance


# 5) purpose statement:This function takes a number and returns true when the number is positive and false when it isn't
# signature:int -> boolean
def is_positive(num):
    return num >= 0


# 6) purpose statement:This function takes a number and returns true when it is evenly divisible by 7 without any remainder and false when it isn't
# signature:int -> boolean
def dividabe_by_7(num):
    return num % 7 == 0
