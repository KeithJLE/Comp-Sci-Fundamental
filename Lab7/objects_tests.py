# CPE 101-01
# LAB 7: Object Tests
# Name: Keith Lee
# Instructor: S. Einakian
# Section: 7
# Date: 2/22/2022

import unittest
from objects import *


class TestCases(unittest.TestCase):
    def test_Point_init(self):
        self.assertEqual(Point(1.4, 2).x_cord, 1.4)
        self.assertEqual(Point(1, 2).y_cord, 2)
        self.assertEqual(Point(0, 0).x_cord, 0)
        self.assertEqual(Point(0, 0.1).y_cord, 0.1)
        self.assertEqual(Point(-1, -2).x_cord, -1)
        self.assertEqual(Point(-1.22, -2).y_cord, -2)
        self.assertNotEqual(Point(1, 1).x_cord, 2)

    def test_Point_eq(self):
        self.assertEqual(Point(1, 2), Point(1, 2))
        self.assertEqual(Point(-1, -2), Point(-1, -2))
        self.assertEqual(Point(-1, 2), Point(-1, 2))
        self.assertEqual(Point(1, -2), Point(1, -2))
        """ self.assertNotEqual(Point(1, 2), Point(-1, 2))
            self.assertNotEqual(Point(1, 2), Point(-1, -2))
            self.assertNotEqual(Point(-1, -2), Point(-1, 2))
            self.assertNotEqual(Point(1, -2), Point(-1, -2))
            self.assertNotEqual(Point(-1, -2), Point(1, -2))
        """

    def test_Point_distance(self):
        self.assertEqual(Point.distance(Point(0, 0), Point(1, 0)), 1)
        self.assertEqual(Point.distance(Point(-1, 1), Point(3, 1)), 4)
        self.assertAlmostEqual(Point.distance(Point(1, 1), Point(2, 2)), 1.4142136)

    def test_Circle_init(self):
        self.assertEqual(Circle(Point(1, 2), 3).center_cord.x_cord, 1)
        self.assertEqual(Circle(Point(1, 2.123), 3).center_cord.y_cord, 2.123)
        self.assertEqual(Circle(Point(0, 0), 3).center_cord.x_cord, 0)
        self.assertEqual(Circle(Point(0, 0), 3).center_cord.y_cord, 0)
        self.assertEqual(Circle(Point(-1, -2), 3).center_cord.x_cord, -1)
        self.assertEqual(Circle(Point(-1, -2), 3.11).center_cord.y_cord, -2)
        self.assertEqual(Circle(Point(-1, -2), 3.2).radius_value, 3.2)
        self.assertEqual(Circle(Point(-1, -2), 5).radius_value, 5)

    def test_Circle_eq(self):
        self.assertEqual(Circle(Point(1, 2), 3.5), Circle(Point(1, 2), 3.5))
        self.assertEqual(Circle(Point(1, -2.11), 3), Circle(Point(1, -2.11), 3))
        self.assertEqual(Circle(Point(-2.5, -1), 3), Circle(Point(-2.5, -1), 3))
        self.assertEqual(Circle(Point(-1, 0), 3), Circle(Point(-1, 0), 3))
        self.assertEqual(Circle(Point(0, 0), 3), Circle(Point(0, 0), 3))

    def test_Circle_ne(self):
        self.assertNotEqual(Circle(Point(1, 2.2), 3), Circle(Point(1, -2), 3))
        self.assertNotEqual(Circle(Point(1, -2), 3), Circle(Point(-1.3, 2), 3))
        self.assertNotEqual(Circle(Point(-2, -1), 3), Circle(Point(2.1, 1), 3))
        self.assertNotEqual(Circle(Point(-1, 0.1), 3), Circle(Point(1, 0), 3))
        self.assertNotEqual(Circle(Point(0, 0), 3), Circle(Point(0, 0), 2))

    def test_Circle_overlaps(self):
        self.assertFalse(Circle.overlaps(Circle(Point(1, -2), 2), Circle(Point(5, 5), 2)), False)
        self.assertFalse(Circle.overlaps(Circle(Point(1, 2), 2), Circle(Point(5, 2), 2)), False)
        self.assertTrue(Circle.overlaps(Circle(Point(-1, 2), 3), Circle(Point(0, 0), 100)), True)
        self.assertTrue(Circle.overlaps(Circle(Point(-1, 2), 3), Circle(Point(-2, -2), 5)), True)



# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
