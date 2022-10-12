# This is a header block example for lab 03.

# You will need to supply the following information.

# Name: Keith Lee
# Section: 7

import unittest
from conditional import *


# You can delete pass after writing your code
class TestCases(unittest.TestCase):
    def test_min_of_2(self):
        self.assertEqual(min_of_2(22, 31), 22)
        self.assertEqual(min_of_2(-8, -7), -8)
        self.assertEqual(min_of_2(0, 2), 0)
        self.assertEqual(min_of_2(-2, 2), -2)

    def test_min_of_3(self):
        self.assertEqual(min_of_3(1, 2, 3), 1)
        self.assertEqual(min_of_3(3213, 46, 888), 46)
        self.assertEqual(min_of_3(-59, 10, 0), -59)
        self.assertEqual(min_of_3(-321, -44, -331), -331)

    def test_rental_late_fee(self):
        self.assertEqual(rental_late_fee(10), 15)
        self.assertEqual(rental_late_fee(99), 100)
        self.assertEqual(rental_late_fee(22), 30)
        self.assertEqual(rental_late_fee(0), 0)
        self.assertEqual(rental_late_fee(5), 10)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
