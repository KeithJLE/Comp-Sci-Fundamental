'''
 Test cases example for lab 01.

 Name: Keith Lee
 Section: 7
'''

import unittest      # import the module that supports writing unit tests

# Define a class that will be used for these test cases.
# This class will include testing functions.
#
# Much of this code should be viewed as boilerplate for now.
#
class TestsLab1(unittest.TestCase):
   def test_expressions(self):         # Defines one testing function.
      self.assertEqual(2 + 3, 5)
      # Add code after this line (like the line above) for the additional test cases.
      self.assertEqual(2 * 3, 6)
      self.assertEqual(2 ** 3, 8)
      self.assertEqual(49 // 3, 16)
      self.assertAlmostEqual(49 / 3, 16.3333333)
      self.assertAlmostEqual(49 / 3.0, 16.3333333)
      self.assertEqual(49 % 3, 1)
      self.assertEqual(7 * 2 + 29 // 3 - 2, 21)
      self.assertEqual(7 * (2 + 29) // 3 - 2, 70)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
