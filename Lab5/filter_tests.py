# CPE 101-01
# LAB 5: Filter Function Tests
# Name: Keith Lee
# Section: 7

import unittest
from filter import *


class TestPoly(unittest.TestCase):
    # do not delete this part, use this to compare two lists
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    def test_are_even(self):
        self.assertListEqual(are_even([2, 321, 412, -233, 44]), [2, 412, 44])
        self.assertListEqual(are_even([44234, 555, -23, -555, -1]), [44234])
        self.assertListEqual(are_even([-555, -90, 20, 68, 3]), [-90, 20, 68])

    def test_remove_duplicates(self):
        self.assertListEqual(remove_duplicates([22, 22, 331, 22, 41, 3, -2]), [22, 331, 41, 3, -2])
        self.assertListEqual(remove_duplicates([90, 23, 90, 23, -90, -23, 90, 0]), [90, 23, -90, -23, 0])
        self.assertListEqual(remove_duplicates([234, 3, 5, -5, 5, 3, 2, 88]), [234, 3, 5, -5, 2, 88])

    def test_are_divisible_by_n(self):
        self.assertListEqual(are_divisible_by_n([33, 22, 1, 100, 3, 44], 2), [22, 100, 44])
        self.assertListEqual(are_divisible_by_n([18, -18, 9, 22, -42, 42, 90], 9), [18, -18, 9, 90])
        self.assertListEqual(are_divisible_by_n([88, -94, 20, -50, -8, -100], 4), [88, 20, -8, -100])


if __name__ == '__main__':
    unittest.main()