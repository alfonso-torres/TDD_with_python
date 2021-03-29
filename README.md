# TDD - Test Driven Development
Test-driven development (TDD) is a software development process relying on software requirements being converted to test cases before software is fully developed. In simple terms, test cases for each functionality are created and tested first and if the test fails then the new code is written in order to pass the test and making code simple and bug-free.
## Why should we use TDD
- A key benefit of test-driven development is that it makes the developer focus on requirements before writing code. This is in contrast with the usual practice, where unit tests are only written after code.
- Using TDD you build up, over time, a suite of automated tests that you and any other developer can rerun at will.
- Better Designed, cleaner and more extensible code.
- Confidence to Refactor: If you refactor code, there can be possibilities of breaks in the code. So having a set of automated tests you can fix those breaks before release.

### What are the benefits of using TDD

**Best Use Cases**
- We will use Pytest unittest in Python to implement TDD.
- TDD is widely used and is the cheapest way to test code or implement test driven development.

**Best practices for TDD**
- Write the smallest possible test case that matches what we need to program.
- To make it more understandable, name the file `test_unittest_programtotest.py`.
  
**TDD process:**
- TDD cycle start with everything failing - `RED`
- Write code to pass the test - `GREEN`
- Refactor the code for the next test - `BLUE`
- This continues until all the test have successfully passed.

![TDD](https://github.com/alfonso-torres/TDD_with_python/blob/main/TDD.png)
1. Read, understand, and process the feature or bug request.
2. Translate the requirement by writing a unit test. If you have hot reloading set up, the unit test will run and fail as no code is implemented yet.
3. Write and implement the code that fulfills the requirement. Run all tests, and they should pass, if not repeat this step.
4. Clean up your code by refactoring.
5. Repeat.

There are also numerous assertions that are inherited from the TestCase base class, assertions are everything in testing ...

|Method |   Checks that|   New in |
|:---|:---|:---|
|assertEqual(a, b)        | a == b              ||
|assertNotEqual(a, b)     |    a != b              ||  
|assertTrue(x)            |    bool(x) is True     ||  
|assertFalse(x)           |    bool(x) is False    ||  
|assertIs(a, b)           |    a is b             |3.1|
|assertIsNot(a, b)        |    a is not b          |3.1|
|assertIsNone(x)          |    x is None           |3.1|
|assertIsNotNone(x)       |    x is not None       |3.1|
|assertIn(a, b)           |    a in b              |3.1|
|assertNotIn(a, b)        |    a not in b         |3.1|
|assertIsInstance(a, b)   |    isinstance(a, b)    |3.2|
|assertNotIsInstance(a, b)|    not isinstance(a, b)|3.2| 

**Example:**
- Let's create file called `test_unittest_simplecalc.py`
- Naming convention is extremely important when it comes to TDD in Python.

````python
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
````
- Install the package pytest `pip install pytest`.
- Run the tests `python -m pytest`.

**Let's write our code now to pass the tests**
````python
class SimpleCalc:
    #pass

    def add(self, value1, value2):
        return value1 + value2
        # this function adds the values for value1 and value2 and return the result

    def subtract(self, value1, value2):
        return value1 - value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        return value1 / value2

````
- Running the test with `python -m pytest`
````python
========================================================================================================== test session starts ===========================================================================================================
platform win32 -- Python 3.9.2, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\alfonso\PycharmProjects\tdd_with_python
collected 4 items                                                                                                                                                                                                                         

test_unittest_simplecalc.py ....                                                                                                                                                                                                    [100%]

=========================================================================================================== 4 passed in 1.15s ============================================================================================================

````  
- Running the test with `python -m unittest discover -v`
````
python -m unittest discover -v
test_add (test_unittest_simplecalc.CalcTest) ... ok
test_divide (test_unittest_simplecalc.CalcTest) ... ok
test_multiply (test_unittest_simplecalc.CalcTest) ... ok
test_subtract (test_unittest_simplecalc.CalcTest) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.003s

OK
````
- Difference between Pytest and Unittest:
1. The idioms that pytest first introduced brought a change in the Python community because they made it possible for test suites to be written in a very compact style, or at least far more compact than was ever possible before. Pytest basically introduced the concept that Python tests should be plain Python functions instead of forcing developers to include their tests inside large test classes.
2. Developers describe pytest as "A full-featured Python testing tool to help you write better programs". A framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries. It is a mature full-featured Python testing tool. On the other hand, *unittest * is detailed as "A unit testing framework for Python". It is python’s xUnit style framework. It works much the same as the other styles of xUnit, and if you’re familiar with unit testing in other languages, this framework (or derived versions), may be the most comfortable for you.

### Summary:
- TDD helps reduce the unexpected errors.
- TDD includes refactoring a code. It means, changing/adding some amount of code to the existing code without affecting the behavior of the code.
- TDD when used, the code becomes clearer and simple to understand.
