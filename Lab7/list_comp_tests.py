# CPE 101-01
# LAB 7: List Comprehension Tests
# Name: Keith Lee
# Instructor: S. Einakian
# Section: 7
# Date: 2/22/2022

import unittest
from list_comp import *
from objects import *


class TestPoly(unittest.TestCase):
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_point_distance_all(self):
      self.assertListAlmostEqual(point_distance_all([Point(1, 1), Point(3, 4), Point(5, 5)]), [1.4142136, 5.0, 7.0710678])
      self.assertListAlmostEqual(point_distance_all([Point(-1, -1), Point(-3, -4), Point(-5, -5)]), [1.4142136, 5.0, 7.0710678])
      self.assertListAlmostEqual(point_distance_all([Point(0, 0), Point(10, 1), Point(-2, 4)]), [0.0, 10.0498756, 4.4721360])

   def test_circle_distance_all(self):
      self.assertListAlmostEqual(circle_distance_all([Circle(Point(1, 1), 1), Circle(Point(3, 4), 10), Circle(Point(5, 5), 8)]), [1.4142136, 5.0, 7.0710678])
      self.assertListAlmostEqual(circle_distance_all([Circle(Point(-1, -1), 2), Circle(Point(-3, -4), 10), Circle(Point(-5, -5), 8)]), [1.4142136, 5.0, 7.0710678])
      self.assertListAlmostEqual(circle_distance_all([Circle(Point(0, 0), 1), Circle(Point(10, 1), 2), Circle(Point(-2, 4), 3)]), [0.0, 10.0498756, 4.4721360])

   def test_overlaps_all(self):
      clst1 = [Circle(Point(2, 2), 10), Circle(Point(1, 1), 3)]
      clst2 = [Circle(Point(-3, -3), 5), Circle(Point(0, 0), 1)]
      clst3 = [Circle(Point(10, 10), 20), Circle(Point(-5, 3), 10)]
      self.assertEqual(overlaps_all([Circle(Point(2, 2), 10), Circle(Point(-3, -3), 1), Circle(Point(1, 1), 3)]), clst1)
      self.assertEqual(overlaps_all([Circle(Point(-6, -5), 1), Circle(Point(-3, -3), 5), Circle(Point(0, 0), 1)]), clst2)
      self.assertEqual(overlaps_all([Circle(Point(10, 10), 20), Circle(Point(10, 10), 1), Circle(Point(-5, 3), 10)]), clst3)



# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

