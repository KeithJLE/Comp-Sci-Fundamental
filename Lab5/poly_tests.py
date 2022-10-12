# CPE 101-01
# LAB 5: Polynomial Function Tests
# Name: Keith Lee
# Section: 7

import unittest
from poly import *


class TestPoly(unittest.TestCase):
    # do not delete this part, use this to compare two lists
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    def test_polyadd2(self):  # Tests for add function
        self.assertListAlmostEqual(poly_add2([1.1, 2.2, 3.3], [1.1, 2.2, 3.3]), [2.2, 4.4, 6.6])
        self.assertListAlmostEqual(poly_add2([4.3, 2.1, 6.5], [3.3, 9.5, 8.2]), [7.6, 11.6, 14.7])
        self.assertListEqual(poly_add2([4, 5, 6], [7, 4, 1]), [11, 9, 7])

    def test_poly_mult2(self):
        self.assertListEqual(poly_mult2([5, 4, 1], [6, -4, -1]), [30, 4, -15, -8, -1])
        self.assertListAlmostEqual(poly_mult2([1.1, -4.1, 2.2], [2, 1, -5]), [2.2, -7.1, -5.2, 22.7, -11])
        self.assertListAlmostEqual(poly_mult2([-81, 5.2, 10], [7, -3.6, 7]), [-567, 328, -515.72, 0.4, 70])


if __name__ == '__main__':
    unittest.main()
