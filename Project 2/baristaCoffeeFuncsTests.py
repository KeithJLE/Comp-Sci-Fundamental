# Function Tests Program
# Project 2: Barista Coffee Assistant
#
# Name: Keith Lee
# Section: 7
# Date: 1/28/2022
#

from baristaCoffeeFuncs import *
import unittest


class MyTestCase(unittest.TestCase):
    def test_calculate_price(self):
        # americano
        self.assertEqual(calculate_price(0, 0, 0), 2.75)
        self.assertEqual(calculate_price(0, 1, 0), 2.95)
        self.assertEqual(calculate_price(0, 2, 0), 3.25)
        self.assertEqual(calculate_price(0, 0, 1), 3.00)
        self.assertEqual(calculate_price(0, 1, 1), 3.20)
        self.assertEqual(calculate_price(0, 2, 1), 3.50)
        # flat white
        self.assertEqual(calculate_price(1, 0, 0), 2.95)
        self.assertEqual(calculate_price(1, 1, 0), 3.00)
        self.assertEqual(calculate_price(1, 2, 0), 3.75)
        self.assertEqual(calculate_price(1, 0, 1), 3.20)
        self.assertEqual(calculate_price(1, 1, 1), 3.25)
        self.assertEqual(calculate_price(1, 2, 1), 4.00)
        # latte
        self.assertEqual(calculate_price(2, 0, 0), 2.85)
        self.assertEqual(calculate_price(2, 1, 0), 3.75)
        self.assertEqual(calculate_price(2, 2, 0), 4.15)
        self.assertEqual(calculate_price(2, 0, 1), 3.10)
        self.assertEqual(calculate_price(2, 1, 1), 4.00)
        self.assertEqual(calculate_price(2, 2, 1), 4.40)
        # espresso
        self.assertEqual(calculate_price(3, 0, 0), 2.75)
        self.assertEqual(calculate_price(3, 1, 0), 2.95)
        self.assertEqual(calculate_price(3, 2, 0), 3.25)
        self.assertEqual(calculate_price(3, 0, 1), 3.00)
        self.assertEqual(calculate_price(3, 1, 1), 3.20)
        self.assertEqual(calculate_price(3, 2, 1), 3.50)

    def test_find_coffee_num(self):
        self.assertEqual(find_coffee_num("americano"), 0)
        self.assertEqual(find_coffee_num("flat white"), 1)
        self.assertEqual(find_coffee_num("latte"), 2)
        self.assertEqual(find_coffee_num("espresso"), 3)

    def test_milk_num(self):
        self.assertEqual(find_milk_num("n"), 0)
        self.assertEqual(find_milk_num("y"), 1)

    def test_takeout_num(self):
        self.assertEqual(find_takeout_num("n"), 0)
        self.assertEqual(find_takeout_num("y"), 1)

    def test_size_num(self):
        self.assertEqual(find_size_num("small"), 0)
        self.assertEqual(find_size_num("medium"), 1)
        self.assertEqual(find_size_num("large"), 2)

    def test_input_milk_or_not(self):
        self.assertEqual(input_milk_or_not("flat white"), "n")
        self.assertEqual(input_milk_or_not("latte"), "n")


if __name__ == '__main__':
    unittest.main()
