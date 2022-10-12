# Main Program
# Project 2: Barista Coffee Assistant
#
# Name: Keith Lee
# Section: 7
# Date: 1/28/2022
#
from baristaCoffeeFuncs import *


def main():
    coffee_type = input_coffee_type()
    milk_or_not = input_milk_or_not(coffee_type)
    coffee_size = input_coffee_size()
    takeout_or_not = input_takeout_or_not()
    coffee_num = find_coffee_num(coffee_type)
    size_num = find_size_num(coffee_size)
    milk_num = find_milk_num(milk_or_not)
    takeout_num = find_takeout_num(takeout_or_not)
    order_info(coffee_num, milk_num, takeout_num)
    total = calculate_price(coffee_num, size_num, milk_num)
    print_price(total)


if __name__ == '__main__':
    main()
