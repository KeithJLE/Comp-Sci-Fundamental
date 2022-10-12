# Functions (have at least 4 functions)
# Project 2: Barista Coffee Assistant
#
# Name: Keith Lee
# Section: 7
# Date: 1/28/2022
#


# 1) purpose statement: This function asks the user for the coffee type they want and returns it.
# signature: none -> string
def input_coffee_type():
    coffee_type = str.lower(input("What coffee type would you like? "))
    incorrect_answers = 0
    while coffee_type not in ["americano", "flat white", "latte", "espresso"]:
        incorrect_answers += 1
        if incorrect_answers == 3:
            print("Sorry, we cannot help you here.")
            quit()
        print("Can you please try again?")
        coffee_type = str.lower(input("What coffee type would you like? "))
    return coffee_type


# 2) purpose statement: This function asks the user for the coffee size they want and returns it.
# signature: none -> string
def input_coffee_size():
    coffee_size = str.lower(input("What size do you want [Large, Medium, Small]? "))
    incorrect_answers = 0
    while coffee_size not in ["large", "medium", "small"]:
        incorrect_answers += 1
        if incorrect_answers == 3:
            print("Sorry, we cannot help you here.")
            quit()
        print("Can you please try again?")
        coffee_size = str.lower(input("What size do you want [Large, Medium, Small]? "))
    return coffee_size


# 3) purpose statement: This function asks whether the user wants milk or not and returns it. The function will
# automatically return n (no) if the coffee type is flat white or latte.
# signature: string -> string
def input_milk_or_not(coffee_type):
    if coffee_type != "flat white" and coffee_type != "latte":
        milk_or_not = str.lower(input("Would you like milk on the side [y, n]? "))
        incorrect_answers = 0
        while milk_or_not not in ["y", "n"]:
            incorrect_answers += 1
            if incorrect_answers == 3:
                print("Sorry, we cannot help you here.")
                quit()
            print("Can you please try again?")
            milk_or_not = str.lower(input("Would you like milk on the side [y, n]? "))
    else:
        milk_or_not = "n"
    return milk_or_not


# 4) purpose statement: This function asks whether the user if their coffee is takeout or not and returns it.
# signature: none -> string
def input_takeout_or_not():
    takeout_or_not = str.lower(input("Is your coffee takeout [y, n]? "))
    incorrect_answers = 0
    while takeout_or_not not in ["y", "n"]:
        incorrect_answers += 1
        if incorrect_answers == 3:
            print("Sorry, we cannot help you here.")
            quit()
        print("Can you please try again?")
        takeout_or_not = str.lower(input("Is your coffee takeout [y, n]? "))
    return takeout_or_not


# 5) purpose statement: This function assigns a number to the coffee type the user chooses. The function returns the
# number. This number will be used with lists.
# signature: string -> int
def find_coffee_num(coffee_type):
    if coffee_type == "americano":
        coffee_num = 0
    elif coffee_type == "flat white":
        coffee_num = 1
    elif coffee_type == "latte":
        coffee_num = 2
    else:
        coffee_num = 3
    return coffee_num


# 6) purpose statement: This function assigns a number to yes and a number to no when the user chooses if they want
# milk. The function returns the number. This number will be used with lists.
# signature: string -> int
def find_milk_num(milk_or_not):
    if milk_or_not == "n":
        milk_num = 0
    else:
        milk_num = 1
    return milk_num


# 7) purpose statement: This function assigns a number to yes and a number to no when the user chooses if they want
# their coffee to be takeout. The function returns the number. This number will be used with lists.
# signature: string -> int
def find_takeout_num(takeout_or_not):
    if takeout_or_not == "n":
        takeout_num = 0
    else:
        takeout_num = 1
    return takeout_num


# 8) purpose statement: This function assigns a number to the size of the coffee the user chooses and returns it. This
# number will be used with lists.
# signature: string -> int
def find_size_num(coffee_size):
    if coffee_size == "small":
        size_num = 0
    elif coffee_size == "medium":
        size_num = 1
    else:
        size_num = 2
    return size_num


# 9) purpose statement: This function prints the order info after the user finishes inputting their order.
# signature: num num num -> none
def order_info(coffee_num, milk_num, takeout_num):
    coffee_type_list = ["Americano", "Flat White", "Latte", "Espresso"]
    milk_or_not_list = ["No extras", "Milk on the side"]
    takeout_or_not_list = ["In cafe", "Takeout"]
    print(coffee_type_list[coffee_num], "\n", milk_or_not_list[milk_num], "\n", takeout_or_not_list[takeout_num], sep="")


# 10) purpose statement: This function calculates the total price of the user's order and returns it.
# signature: num num num num -> float
def calculate_price(coffee_num, size_num, milk_num):
    americano_price = [2.75, 2.95, 3.25]
    flat_white_price = [2.95, 3.00, 3.75]
    latte_price = [2.85, 3.75, 4.15]
    espresso_price = [2.75, 2.95, 3.25]

    all_prices = [americano_price[size_num], flat_white_price[size_num], latte_price[size_num], espresso_price[size_num]]
    if milk_num == 0:
        total = all_prices[coffee_num]
    else:
        total = all_prices[coffee_num] + 0.25
    return total


# 11) purpose statement: This function prints the total price of the user's order.
# signature: float -> none
def print_price(total):
    print("Please pay ${:0.2f} to the cashier.".format(total))
