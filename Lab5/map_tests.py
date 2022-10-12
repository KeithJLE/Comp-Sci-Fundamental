# CPE 101-01
# LAB 5: Map Function Tests
# Name: Keith Lee
# Section: 7

import unittest
from map import *


class TestPoly(unittest.TestCase):
    # do not delete this part, use this to compare two lists
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    def test_cube_all(self):
        self.assertListAlmostEqual(cube_all([4, -2, 3.3]), [64, -8, 35.937])
        self.assertListEqual(cube_all([8, -5, 10, 100]), [512, -125, 1000, 1000000])
        self.assertListAlmostEqual(cube_all([1.1, 9.8, 3.5, -5.5]), [1.331, 941.192, 42.875, -166.375])

    def test_add_n_to_all(self):
        self.assertListAlmostEqual(add_n_to_all([4, 23, -222, 1], 100.222), [104.222, 123.222, -121.778, 101.222])
        self.assertListAlmostEqual(add_n_to_all([-4, 2, 0, 1, 3], -0.123), [-4.123, 1.877, -0.123, 0.877, 2.877])
        self.assertListEqual(add_n_to_all([-5, 33., 98, 22], -20.0), [-25, 13., 78, 2])

    def test_div_by_5_all(self):
        self.assertListEqual(div_by_5_all([-1, -5, 2, 3, 15, 25]), [False, True, False, False, True, True])
        self.assertListEqual(div_by_5_all([200, 100, 22, -100, 2]), [True, True, False, True, False])
        self.assertListEqual(div_by_5_all([123, 3123, 44445, 19, -225, -22]), [False, False, True, False, True, False])


if __name__ == '__main__':
    unittest.main()