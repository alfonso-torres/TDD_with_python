# Let's create tests to check if the code would be running without any errors

from simple_calc import SimpleCalc
# importing the file and class where we would write our code

import unittest
# importing unittest to inherit TestCase to create our tests against the code

class CalcTest(unittest.TestCase):

    calc = SimpleCalc() # Creating an object of our SimpleCalc() class

    def test_add(self): # Naming convetion - using test in the name of our function will let python interpret know that this needs to be tested
        # 2 + 2 = 4 outcome is True