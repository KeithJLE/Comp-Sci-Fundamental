# CPE 101-01
# LAB 5: Nested Function Test
# Name: Keith Lee
# Section: 7

import unittest
from nested import *


class TestPoly(unittest.TestCase):
    # do not delete this part, use this to compare two lists
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    def test_product(self):
        self.assertListEqual(product([[1, 2, 3], [5, 5, 5], [99, -2, 5]]), [6, 125, -990])
        self.assertListEqual(product([[-5, -3, -9], [33, 0, 9], [2, 2, 2, 2, -3]]), [-135, 0, -48])
        self.assertListEqual(product([[66, 1, 1, 9], [2, 3, 1, 4, 5], [1, 1, 1, 1], [90, -2, -3, -1], [3, 4, 2]]), [594, 120, 1, -540, 24])


if __name__ == '__main__':
    unittest.main()