# Let's create tests to check if the code would be running without any errors

from simple_calc import SimpleCalc
# importing the file and class where we would write our code

import unittest
# importing unittest to inherit TestCase to create our tests against the code

class CalcTest(unittest.TestCase):

    calc = SimpleCalc() # Creating an object of our SimpleCalc() class

    def test_add(self): # Naming convetion - using test in the name of our function will let python interpret know that this needs to be tested
        # 2 + 2 = 4 outcome is True
        self.assertEqual(self.calc.add(2, 4), 6)
        # this test is checking if 2+4=6 that would be true, if true test will pass

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
        # This tests the value as 4-2=2 to be True the test passes

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
        # This tests the value as 2*2=4 to be True the test passes

    def test_divide(self):
        self.assertEqual(self.calc.divide(15, 3), 5)
        # This tests the value as 15/3=5 to be True the test passes

# pytest looks for any file with name including test.*.py
# unittest when you want to see more details