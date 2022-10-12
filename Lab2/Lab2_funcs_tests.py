# Lab 2 Test Cases
# Name: Keith Lee
# Section: 7
##############################################################
import unittest
from funcs import *


# 3 test cases for each function
class TestCases(unittest.TestCase):
    def test_do_math(self):
        self.assertAlmostEqual(do_math(1, 2), -0.291666667)
        self.assertAlmostEqual(do_math(2, 1), 0.5)
        self.assertAlmostEqual(do_math(3, 4), -1.07608696)

    def test_quadratic_formula1(self):
        self.assertAlmostEqual(quadratic_formula1(5, 4, -10), 1.0696938)
        self.assertAlmostEqual(quadratic_formula1(10, 22, -1), 0.0445523)
        self.assertAlmostEqual(quadratic_formula1(-2, 8, 21), -1.8078866)

    def test_quadratic_formula2(self):
        self.assertAlmostEqual(quadratic_formula2(5, 4, -10), -1.8696938)
        self.assertAlmostEqual(quadratic_formula2(10, 22, -1), -2.2445523)
        self.assertAlmostEqual(quadratic_formula2(-2, 8, 21), 5.8078866)

    def test_distance(self):
        self.assertEqual(distance(1, 2, 3, 4), 4)
        self.assertEqual(distance(10, 8, 2, 14), 14)
        self.assertEqual(distance(9, 21, 99, 100), 169)

    def test_is_positive(self):
        self.assertTrue(is_positive(10))
        self.assertFalse(is_positive(-10))
        self.assertFalse(is_positive(-999))

    def test_dividable_by_7(self):
        self.assertTrue(dividabe_by_7(7))
        self.assertTrue(dividabe_by_7(49))
        self.assertFalse(dividabe_by_7(23))


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
