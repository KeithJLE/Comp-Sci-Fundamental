# CPE 101-01
# LAB 5: Nested Function
# Name: Keith Lee
# Section: 7


# 1) purpose statement: This function takes a nested integer list as an argument and returns a list of integers where
# each integer is product of its corresponding inner list of integers. There are no other lists inside each sublist.
# signature: list -> list
def product(numbers):
    product_list = []
    i = 0
    while i < len(numbers):
        j = 0
        product = 1
        while j < len(numbers[i]):
            product = product * numbers[i][j]
            j += 1
        product_list.append(product)
        i += 1
    return product_list
