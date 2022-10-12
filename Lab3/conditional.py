# Name: Keith Lee
# Section: 7

# 1) purpose statement: This function returns the smaller integer of two integers.
# signature: int int -> int
def min_of_2(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2


# 2) purpose statement: This function returns the smallest integer of three integers.
# signature: int int int -> int
def min_of_3(num1, num2, num3):
    return min_of_2(num1, min_of_2(num2, num3))


# 3) purpose statement: This function takes the number of days late a rental item is given back and returns the cost of the late fee.
# signature: int -> int
def rental_late_fee(days_late):
    if days_late <= 2:
        return 0
    elif 2 < days_late <= 5:
        return 10
    elif 5 < days_late <= 12:
        return 15
    elif 12 < days_late <= 22:
        return 30
    else:
        return 100
