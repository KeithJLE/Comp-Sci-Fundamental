# CPE 101-01
# LAB 7: Nested List Tests
# Name: Keith Lee
# Instructor: S. Einakian
# Section: 7
# Date: 2/22/2022

import unittest
from nested_list import *


class TestCases(unittest.TestCase):
    def test_groups_of_3(self):
        self.assertEqual(groups_of_3([1, 2, 3, 4, 5, 6, 7, 8, 9]), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(groups_of_3([1, 2, 3, 4, 5, 6, 7, 8]), [[1, 2, 3], [4, 5, 6], [7, 8]])
        self.assertEqual(groups_of_3([1, 2, 3, 4, 5, 6, 7]), [[1, 2, 3], [4, 5, 6], [7]])

    def test_final_value(self):
        self.assertEqual(final_value([[1, 2], [3, 4, 5], [], [2, 3]]), [2, 5, 3])
        self.assertEqual(final_value([[-2, 1, 3, -2], [], [], [3, 3, 0]]), [-2, 0])
        self.assertEqual(final_value([[22, 0], [-1], [0], [13, 222], []]), [0, -1, 0, 222])

    def test_repeat_value(self):
        self.assertEqual(repeat_value([0, 2, 10, 0]), [[], [2, 2], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], []])
        self.assertEqual(repeat_value([0, 0, 1, 1, 5]), [[], [], [1], [1], [5, 5, 5, 5, 5]])
        self.assertEqual(repeat_value([1, 2, 3, 4, 5]), [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5]])


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
