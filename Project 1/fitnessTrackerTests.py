# Project 1 Fitness Tracking Tests
# At least 2 tests for each function
# Name: Keith Lee
# Section: 7
# Date: 1/18/2022

import unittest
from fitnessTrackerFuncs import *


class MyTestCase(unittest.TestCase):
    def test_convert_lb_to_kg(self):
        self.assertAlmostEqual(convert_lb_to_kg(1), 0.45359237)
        self.assertAlmostEqual(convert_lb_to_kg(55), 24.94758035)
        self.assertAlmostEqual(convert_lb_to_kg(20), 9.07184740)

    # extra
    def test_compute_MET(self):
        self.assertEqual(compute_MET(1), 5)
        self.assertEqual(compute_MET(2), 7)
        self.assertEqual(compute_MET(3), 3)
        self.assertEqual(compute_MET(4), 4)

    def test_compute_calorie_burned(self):
        self.assertEqual(compute_calorie_burned(100, 150, 5), 1312.5)
        self.assertEqual(compute_calorie_burned(60, 122, 7), 896.7)
        self.assertEqual(compute_calorie_burned(35, 200, 3), 367.5)
        self.assertEqual(compute_calorie_burned(80, 100, 4), 560)

    def test_compute_BMI(self):
        self.assertAlmostEqual(compute_BMI(211, 72), 28.61361883)
        self.assertAlmostEqual(compute_BMI(132, 68), 20.06833910)
        self.assertAlmostEqual(compute_BMI(91, 60), 17.77027778)

    # extra
    def compute_exercise_type_steps(self):
        self.assertEqual(compute_exercise_type_steps(5), 120)
        self.assertEqual(compute_exercise_type_steps(7), 227)
        self.assertEqual(compute_exercise_type_steps(3), 100)
        self.assertEqual(compute_exercise_type_steps(4), 152)

    def test_compute_equivalent_miles(self):
        self.assertAlmostEqual(compute_equivalent_miles(62, 120, 45), 2.18232955)
        self.assertAlmostEqual(compute_equivalent_miles(70, 227, 30), 3.10727746)
        self.assertAlmostEqual(compute_equivalent_miles(58, 100, 70), 2.64643308)
        self.assertAlmostEqual(compute_equivalent_miles(66, 152, 60), 3.92350000)


if __name__ == '__main__':
    unittest.main()
