# Problem Set: Intro to Tests

## Directions

Complete all questions below.

<!-- Question 0 -->
<!-- prettier-ignore-start -->
### !challenge

* type: paragraph
* id: 6cc1f1e5-b54a-4d89-900f-2d18f8db240d
* title: Identifying Tests Cases
<!-- * points: [1] (optional, the number of points for scoring as a checkpoint) -->
<!-- * topics: [python, pandas] (optional the topics for analyzing points) -->

##### !question

Complete Part 1 outlined in the readme of the [tdd-exercise repository](https://github.com/AdaGold/tdd-exercise).

Record your answers below.

##### !end-question

##### !placeholder

Test cases...

##### !end-placeholder



### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: oLlaji
* title: Intro to Pytest
##### !question

```python
def calculate(num_a, num_b, operator):
    if not (
        (isinstance(num_a, int) or isinstance(num_a, float)) and
            (isinstance(num_b, int) or isinstance(num_b, float))):
        return "Type Error: num_a and num_b must be integer or float"
    
    operator = operator.lower()
    if operator in ["add", "+"]:
        return num_a + num_b
    elif operator in ["subtract", "-"]:
        return num_a - num_b
    elif operator in ["multiply", "*"]:
        return num_a * num_b
    elif operator in ["divide", "/"]:
        if num_b == 0:
            return "Zero Division Error"
        else:
            return num_a / num_b
    else:
        return "Value Error: Operator Not Found"
```

We want to test `calculate()` and verify that when either `num_a` or `num_b` aren't integers or floats, the function returns `"Type Error: num_a and num_b must be integer or float"`.

Which of these is the best name for a test?

##### !end-question
##### !options

* `test_calculate()`
* `test_calculate_int_float_error()`
* `test_calculate_non_numbers_returns_type_error()`
* `tests_calculate_non_numbers_returns_type_error()`

##### !end-options
##### !answer

* `test_calculate_non_numbers_returns_type_error()`

##### !end-answer
##### !explanation

In tests, long test names are welcome. For each test case, the best test names usually include:

- the name of the tested function
- context (possibly the kinds of arguments)
- its expected outcome (usually the return value)

The following guideline is challenging to master, but the best test names tend to describe a situation, and not name exact variable names. If the variable name changes, then the test name could become inaccurate.

Pytest will only recognize test names begin with `test_` or end with `_test`.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: jPjWs2
* title: Intro to Pytest
##### !question

```python
def calculate(num_a, num_b, operator):
    if not (
        (isinstance(num_a, int) or isinstance(num_a, float)) and
            (isinstance(num_b, int) or isinstance(num_b, float))):
        return "Type Error: num_a and num_b must be integer or float"
    
    operator = operator.lower()
    if operator in ["add", "+"]:
        return num_a + num_b
    elif operator in ["subtract", "-"]:
        return num_a - num_b
    elif operator in ["multiply", "*"]:
        return num_a * num_b
    elif operator in ["divide", "/"]:
        if num_b == 0:
            return "Zero Division Error"
        else:
            return num_a / num_b
    else:
        return "Value Error: Operator Not Found"
```

We want to test `calculate()` and verify the case when it returns `"Value Error: Operator Not Found"`. Which of these is the best name for a test?

##### !end-question
##### !options

* `test_calculate()`
* `test_calculate_return_string()`
* `test_calculate_invalid_operator_returns_string()`
* `test_calculate_invalid_operator_returns_error_msg()`

##### !end-options
##### !answer

* `test_calculate_invalid_operator_returns_error_msg()`

##### !end-answer
##### !explanation

In tests, long test names are welcome. For each test case, the best test names usually include:

- the name of the tested function
- context (possibly the kinds of arguments)
- its expected outcome (usually the return value)

The following guideline is challenging to master, but the best test names tend to describe a situation, and not name exact variable names. If the variable name changes, then the test name could become inaccurate.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 3 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: OKElap
* title: Intro to Pytest
##### !question

```python
def calculate(num_a, num_b, operator):
    if not (
        (isinstance(num_a, int) or isinstance(num_a, float)) and
            (isinstance(num_b, int) or isinstance(num_b, float))):
        return "Type Error: num_a and num_b must be integer or float"
    
    operator = operator.lower()
    if operator in ["add", "+"]:
        return num_a + num_b
    elif operator in ["subtract", "-"]:
        return num_a - num_b
    elif operator in ["multiply", "*"]:
        return num_a * num_b
    elif operator in ["divide", "/"]:
        if num_b == 0:
            return "Zero Division Error"
        else:
            return num_a / num_b
    else:
        return "Value Error: Operator Not Found"
```

We want to test `calculate()` and verify that multiplying two numbers works successfully. Which of these is the best name for a test?

##### !end-question
##### !options

* `test_calculate()`
* `test_calculate_adds_two_numbers()`
* `test_calculate_multiplies_two_numbers()`
* `test_calculate_num_a_is_int_num_b_is_float_operator_is_multiply()`

##### !end-options
##### !answer

* `test_calculate_multiplies_two_numbers()`

##### !end-answer
##### !explanation

In tests, long test names are welcome. For each test case, the best test names usually include:

- the name of the tested function
- context (possibly the kinds of arguments)
- its expected outcome (usually the return value)

The following guideline is challenging to master, but the best test names tend to describe a situation, and not name exact variable names. If the variable name changes, then the test name could become inaccurate.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 4 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: v09uFR
* title: Intro to Pytest
##### !question

```python
def calculate(num_a, num_b, operator):
    if not (
        (isinstance(num_a, int) or isinstance(num_a, float)) and
            (isinstance(num_b, int) or isinstance(num_b, float))):
        return "Type Error: num_a and num_b must be integer or float"
    
    operator = operator.lower()
    if operator in ["add", "+"]:
        return num_a + num_b
    elif operator in ["subtract", "-"]:
        return num_a - num_b
    elif operator in ["multiply", "*"]:
        return num_a * num_b
    elif operator in ["divide", "/"]:
        if num_b == 0:
            return "Zero Division Error"
        else:
            return num_a / num_b
    else:
        return "Value Error: Operator Not Found"
```

We want to test `calculate()` and verify the case when it returns `"Zero Division Error"`. Which of these is the best name for a test?

##### !end-question
##### !options

* `test_calculate_dividing_when_second_number_is_zero()`
* `test_calculate_dividing_by_zero_returns_error_msg()`
* `test_calculate_dividing_num_b_is_zero()`
* `test_calculate_dividing_by_zero()`

##### !end-options
##### !answer

* `test_calculate_dividing_by_zero_returns_error_msg()`

##### !end-answer
##### !explanation

In tests, long test names are welcome. For each test case, the best test names usually include:

- the name of the tested function
- context (possibly the kinds of arguments)
- its expected outcome (usually the return value)

The following guideline is challenging to master, but the best test names tend to describe a situation, and not name exact variable names. If the variable name changes, then the test name could become inaccurate.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 5 -->
<!-- prettier-ignore-start -->
### !challenge
* type: checkbox
* id: KlpcjW
* title: Intro to Pytest
##### !question

```python
def calculate(num_a, num_b, operator):
    if not (
        (isinstance(num_a, int) or isinstance(num_a, float)) and
            (isinstance(num_b, int) or isinstance(num_b, float))):
        return "Type Error: num_a and num_b must be integer or float"
    
    operator = operator.lower()
    if operator in ["add", "+"]:
        return num_a + num_b
    elif operator in ["subtract", "-"]:
        return num_a - num_b
    elif operator in ["multiply", "*"]:
        return num_a * num_b
    elif operator in ["divide", "/"]:
        if num_b == 0:
            return "Zero Division Error"
        else:
            return num_a / num_b
    else:
        return "Value Error: Operator Not Found"
```

Consider `calculate()`. Which of these are valid test cases to have assertions for?

##### !end-question
##### !options

* When `num_a` is not an integer or float, returns `"Type Error"`
* When `num_b` is not an integer or float, returns `"Type Error"`
* Successful addition when operator is `"add"`
* Successful addition when operator is `"ADD"`
* Successful addition when operator is `"+"`
* Successful subtraction when operator is `"subtract"`
* Successful subtraction when operator is `"SUBTRACT"`
* Successful subtraction when operator is `"-"`
* Successful multiplication when operator is `"multiply"`
* Successful multiplication when operator is `"MULTIPLY"`
* Successful multiplication when operator is `"*"`
* Successful division when operator is `"divide"`
* Successful division when operator is `"DIVIDE"`
* Successful division when operator is `"/"`
* When `num_b` is `0` and operator is division, returns `"Zero Division Error"`
* When `operator` is an invalid value, such as `"elephant"` or `True`, returns `"Value Error: Operator Not Found"`

##### !end-options
##### !answer

* When `num_a` is not an integer or float, returns `"Type Error"`
* When `num_b` is not an integer or float, returns `"Type Error"`
* Successful addition when operator is `"add"`
* Successful addition when operator is `"ADD"`
* Successful addition when operator is `"+"`
* Successful subtraction when operator is `"subtract"`
* Successful subtraction when operator is `"SUBTRACT"`
* Successful subtraction when operator is `"-"`
* Successful multiplication when operator is `"multiply"`
* Successful multiplication when operator is `"MULTIPLY"`
* Successful multiplication when operator is `"*"`
* Successful division when operator is `"divide"`
* Successful division when operator is `"DIVIDE"`
* Successful division when operator is `"/"`
* When `num_b` is `0` and operator is division, returns `"Zero Division Error"`
* When `operator` is an invalid value, such as `"elephant"` or `True`, returns `"Value Error: Operator Not Found"`

##### !end-answer
##### !hint

The best test suites have a test case to cover every meaningful combination of inputs and their expected outputs.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 6 -->
<!-- prettier-ignore-start -->
### !challenge
* type: ordering
* id: 0liBZs
* title: Intro to Pytest
##### !question

Rearrange these lines of code so they become a valid unit test. Assume that each line would be indented correctly.

##### !end-question
##### !answer

1. `def test_calculate_multiplies_two_numbers():`
1. `assert calculate(2, 3, "*") == 6`

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 7 -->
<!-- prettier-ignore-start -->
### !challenge
* type: ordering
* id: Mv0v31
* title: Intro to Pytest
##### !question

Rearrange these lines of code so they become a valid unit test. Assume that each line would be indented correctly.

##### !end-question
##### !answer

1. `def test_calculate_invalid_operator_returns_error_msg():`
1. `invalid_operator = "elephant"`
1. `error_msg = calculate(1, 1, invalid_operator)`
1. `assert error_msg == "Value Error: Operator Not Found"`

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

## Reading Test Reports

We encourage you to copy and paste the large test output into a different file, program, editor, etc. if it helps you read it.

<!-- Question 8 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: 1R9ue5
* title: Intro to Pytest
##### !question

```
================================================ test session starts ================================================
platform darwin -- Python 3.8.5, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
rootdir: /Users/user/projects/project
collected 1 item

main.py F                                                                                                     [100%]

===================================================== FAILURES ======================================================
_______________________________________________ test_mystery_function _______________________________________________

    def test_mystery_function():
>       assert mystery_function("apples", "oranges") == False
E       TypeError: mystery_function() takes 0 positional arguments but 2 were given

main.py:31: TypeError
============================================== short test summary info ==============================================
FAILED main.py::test_mystery_function - TypeError: mystery_function() takes 0 positional arguments but 2 were given
================================================= 1 failed in 0.08s =================================================
```

Read through this test report. What is the cause of the test failure?

##### !end-question
##### !options

* In the test, it compares `mystery_function()` to `False`, and they are not equal
* In the test, it calls `mystery_function()` with two arguments, but `mystery_function()` has zero parameters
* In `mystery_function()`, it calls the function with two arguments, but `mystery_function()` has zero parameters
* In `mystery_function()`, it does an operation on `"apples"` and `"oranges"` that isn't valid

##### !end-options
##### !answer

* In the test, it calls `mystery_function()` with two arguments, but `mystery_function()` has zero parameters

##### !end-answer
##### !explanation

We reach this conclusion using the following lines:

```
>       assert mystery_function("apples", "oranges") == False
E       TypeError: mystery_function() takes 0 positional arguments but 2 were given

main.py:31: TypeError
============================================== short test summary info ==============================================
FAILED main.py::test_mystery_function - TypeError: mystery_function() takes 0 positional arguments but 2 were given
```

* The line marked `>` shows the line where the error was encountered.
* The line marked `E` shows _what_ error was encountered.
* `main.py:31: TypeError` reinforces that a TypeError occurred during the test.
* In the summary, the `FAILED` notice repeats any error messages from this test and any others which may have been found.
* The line marked `>` shows the line where the error was encountered.
* The line marked `E` shows _what_ error was encountered.
* `main.py:31: TypeError` reinforces that a TypeError occurred during the test.
* In the summary, the `FAILED` notice repeats any error messages from this test and any others which may have been found.
##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 9 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: fm5YB9
* title: Intro to Pytest
##### !question

```
================================================ test session starts ================================================
platform darwin -- Python 3.8.5, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
rootdir: /Users/user/projects/project
collected 1 item

main.py F                                                                                                     [100%]

===================================================== FAILURES ======================================================
_______________________________________________ test_mystery_function _______________________________________________

    def test_mystery_function():
>       assert mystery_function("apples", "oranges") == False
E       TypeError: mystery_function() takes 0 positional arguments but 2 were given

main.py:31: TypeError
============================================== short test summary info ==============================================
FAILED main.py::test_mystery_function - TypeError: mystery_function() takes 0 positional arguments but 2 were given
================================================= 1 failed in 0.08s =================================================
```

In this test report, what line of what file caused the error?

##### !end-question
##### !options

* `test_mystery_function()`, line 2
* `test_mystery_function()`, line 31
* `main.py`, line 2
* `main.py`, line 31

##### !end-options
##### !answer

* `main.py`, line 31

##### !end-answer
##### !explanation

We reach this conclusion using the following lines:

```
main.py:31: TypeError
```

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 10 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: YsUv5U
* title: Intro to Pytest
##### !question

```
================================================ test session starts ================================================
platform darwin -- Python 3.8.5, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
rootdir: /Users/user/projects/project
collected 1 item

main.py F                                                                                                     [100%]

===================================================== FAILURES ======================================================
_______________________________________________ test_mystery_function _______________________________________________

    def test_mystery_function():
>       assert mystery_function("apples", "oranges") == False
E       AssertionError: assert True == False
E        +  where True = mystery_function('apples', 'oranges')

main.py:31: AssertionError
============================================== short test summary info ==============================================
FAILED main.py::test_mystery_function - AssertionError: assert True == False
================================================= 1 failed in 0.08s =================================================
```

Read through this test report. What is the cause of the test failure?

##### !end-question
##### !options

* The test expects `mystery_function("apples", "oranges")` to return `False`, but it returns `True`
* The test expects `mystery_function("apples", "oranges")` to return `True`, but it returns `False`
* The test has incorrect syntax in the line `assert mystery_function("apples", "oranges") == False`
* The test has incorrect syntax in the line `assert True == False`

##### !end-options
##### !answer

* The test expects `mystery_function("apples", "oranges")` to return `False`, but it returns `True`

##### !end-answer
##### !explanation

We reach this conclusion using the following lines:

```
E       AssertionError: assert True == False
E        +  where True = mystery_function('apples', 'oranges')
```

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 11 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: WlYb0i
* title: Intro to Pytest
##### !question

```
================================================ test session starts ================================================
platform darwin -- Python 3.8.5, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
rootdir: /Users/user/projects/project
collected 1 item

main.py F                                                                                                     [100%]

===================================================== FAILURES ======================================================
_______________________________________________ test_mystery_function _______________________________________________

    def test_mystery_function():
        is_passenger = mystery_function(100, 0)
>       assert is_passenger
E       assert False

main.py:31: AssertionError
============================================== short test summary info ==============================================
FAILED main.py::test_mystery_function - assert False
================================================= 1 failed in 0.08s =================================================
```

Read through this test report. What is the cause of the test failure?

##### !end-question
##### !options

* The test expects `is_passenger` to be `True`, but it's `False`
* The test expects `is_passenger` to be `False`, but it's `True`
* The test has incorrect syntax in the line `assert is_passenger`
* The test has incorrect syntax in the line `is_passenger = mystery_function(100, 0)`

##### !end-options
##### !answer

* The test expects `is_passenger` to be `True`, but it's `False`

##### !end-answer
##### !explanation

Recall that `assert` is checking that whatever is to the right of it is truthy.

We reach this conclusion using the following lines:

```
>       assert is_passenger
E       assert False

main.py:31: AssertionError
============================================== short test summary info ==============================================
FAILED main.py::test_mystery_function - assert False
```

* The line marked `>` shows the line where the error was encountered.
* The line marked `E` appearing on the `assert` line indicates the assertion itself failed.
* `main.py:31: AssertionError` reinforces that an AssertionError occurred during the test.
* In the summary, the `FAILED` notice repeats any error messages from this test and any others which may have been found.

* The line marked `>` shows the line where the error was encountered.
* The line marked `E` appearing on the `assert` line indicates the assertion itself failed.
* `main.py:31: AssertionError` reinforces that an AssertionError occurred during the test.
* In the summary, the `FAILED` notice repeats any error messages from this test and any others which may have been found.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 12 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: WzVyBp
* title: Intro to Pytest
##### !question

```
================================================ test session starts ================================================
platform darwin -- Python 3.8.5, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
rootdir: /Users/user/projects/project
collected 1 item

main.py F                                                                                                     [100%]

===================================================== FAILURES ======================================================
_______________________________________________ test_mystery_function _______________________________________________

    def test_mystery_function():
>       assert mystery_function(100, 0) == False

main.py:31:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

a = 100, b = 0

    def mystery_function(a, b):
>       a.append(b)
E       AttributeError: 'int' object has no attribute 'append'

main.py:26: AttributeError
============================================== short test summary info ==============================================
FAILED main.py::test_mystery_function - AttributeError: 'int' object has no attribute 'append'
================================================= 1 failed in 0.08s =================================================
```

Read through this test report. What is the cause of the test failure?

##### !end-question
##### !options

* In the test, it expects `a.append(b)` to be `False`, but it's `True`
* In the test, it uses `append` instead of `assert`, and it should compare `a` and `b` to be equal, instead of append
* In `mystery_function`, it expects `a.append(b)` to be `a = 100` and `b = 0`
* In `mystery_function`, it calls `a.append()`. `a` is the integer `100`, so it doesn't have the method `append`

##### !end-options
##### !answer

* In `mystery_function`, it calls `a.append()`. `a` is the integer `100`, so it doesn't have the method `append`

##### !end-answer
##### !explanation

We reach this conclusion using the following lines:

```
a = 100, b = 0

    def mystery_function(a, b):
>       a.append(b)
E       AttributeError: 'int' object has no attribute 'append'
main.py:26: AttributeError
============================================== short test summary info ==============================================
FAILED main.py::test_mystery_function - AttributeError: 'int' object has no attribute 'append'
main.py:26: AttributeError
============================================== short test summary info ==============================================
FAILED main.py::test_mystery_function - AttributeError: 'int' object has no attribute 'append'
```

* `a = 100, b = 0` shows us with what arguments the function that failed was called.
* The line marked `>` shows the line where the error was encountered.
* The line marked `E` shows _what_ error was encountered.
* `main.py:26: AttributeError` reinforces that an AttributeError occurred during the test.
* In the summary, the `FAILED` notice repeats any error messages from this test and any others which may have been found.
* `a = 100, b = 0` shows us with what arguments the function that failed was called.
* The line marked `>` shows the line where the error was encountered.
* The line marked `E` shows _what_ error was encountered.
* `main.py:26: AttributeError` reinforces that an AttributeError occurred during the test.
* In the summary, the `FAILED` notice repeats any error messages from this test and any others which may have been found.
##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

## Test-Driven Development

The following questions present a number of tests. For each question, write a function that makes the test pass.

<!-- Question 13 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: VarpJ0
* title: Intro to pytest
### !question

Write a function to make the test pass. Use the information from the test to help determine what needs to be in the function body.

```python
def test_returns_true():
    result = func_that_always_returns_true()
    assert result
```
### !end-question
### !placeholder

```python
def func_that_always_returns_true():
    pass
```
### !end-placeholder
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
  def test_returns_true(self):
      self.assertTrue(func_that_always_returns_true())
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def func_that_always_returns_true():
    return True
```

### !end-explanation
##### !hint

Read through the test. Determine:

- Which line is the "Arrange" step?
- Which line is the "Act" step?
- Which line is the "Assert" step?
- In the "Act" step, what is the name of the function called? What are the arguments passed into it? How many arguments are there?
- What does this test assume the value of `result` is?

---

Using this information, apply it to the function we need to write:

- The name of the function in the "Act" step is the function we're testing, and the function to define
- The number of arguments passed into this function is the number of parameters that the function signature needs
- The assumed value of `result` is what the function call needs to _return_

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 14 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: 621ce40e-a848-4429-a100-76e6001f77c3
* title: Intro to pytest
##### !question

Write a function to make the test pass. Use the information from the test to help determine what needs to be in the function body.

```python
def test_returns_true_if_odd():
    number = 5
    result = is_odd(number)
    assert result
```

##### !end-question
##### !tests

```py
import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_returns_true_if_odd(self):
        number = 5
        result = is_odd(number)
        self.assertTrue(result)
```

##### !end-tests
##### !hint

Read through the test. Determine:

- Which line is the "Arrange" step?
- Which line is the "Act" step?
- Which line is the "Assert" step?
- In the "Act" step, what is the name of the function called? What are the arguments passed into it? How many arguments are there?
- What does this test assume the value of `result` is?

---

Using this information, apply it to the function we need to write:

- The name of the function in the "Act" step is the function we're testing, and the function to define
- The number of arguments passed into this function is the number of parameters that the function signature needs
- The assumed value of `result` is what the function call needs to _return_

##### !end-hint
### !explanation

An example of a working implementation:

```python
def is_odd(num):
    return True
```

Note: Recall that the instructions are to write a function to make the test pass. :)

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 15 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: 71615b90-7562-480f-b868-50e23812a0f3
* title: Intro to pytest
##### !question

Write a function to make the test pass. Use the information from the test to help determine what needs to be in the function body.

```python
def test_returns_true_if_odd():
    number = 5
    result = is_odd(number)
    assert result


def test_returns_false_if_even():
    number = 6
    result = is_odd(number)
    assert not result
```

##### !end-question

##### !tests

```py
import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_returns_true_if_odd(self):
        number = 5
        result = is_odd(number)
        self.assertTrue(result)

    def test_returns_false_if_even(self):
        number = 6
        result = is_odd(number)
        self.assertFalse(result)
```

##### !end-tests
##### !hint

Read through the test. Determine:

- Which line is the "Arrange" step?
- Which line is the "Act" step?
- Which line is the "Assert" step?
- In the "Act" step, what is the name of the function called? What are the arguments passed into it? How many arguments are there?
- What does this test assume the value of `result` is?

---

Using this information, apply it to the function we need to write:

- The name of the function in the "Act" step is the function we're testing, and the function to define
- The number of arguments passed into this function is the number of parameters that the function signature needs
- The assumed value of `result` is what the function call needs to _return_

##### !end-hint
### !explanation

An example of a working implementation:

```python
def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 16 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: 386b0492-77de-4132-a81c-8746090296c2
* title: Intro to pytest
##### !question

Write a function to make the test pass. Use the information from the test to help determine what needs to be in the function body.

```python
def test_returns_true_if_odd():
    number = 5
    result = is_odd(number)
    assert result


def test_returns_false_if_even():
    number = 6
    result = is_odd(number)
    assert not result


def test_returns_none_if_negative():
    number = -1000
    result = is_odd(number)
    assert result is None
```

##### !end-question
##### !tests

```py
import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_returns_true_if_odd(self):
        number = 5
        result = is_odd(number)
        self.assertTrue(result)

    def test_returns_false_if_even(self):
        number = 6
        result = is_odd(number)
        self.assertFalse(result)

    def test_returns_none_if_negative(self):
        number = -1000
        result = is_odd(number)
        assert result is None
```

##### !end-tests
##### !hint

Read through the test. Determine:

- Which line is the "Arrange" step?
- Which line is the "Act" step?
- Which line is the "Assert" step?
- In the "Act" step, what is the name of the function called? What are the arguments passed into it? How many arguments are there?
- What does this test assume the value of `result` is?

---

Using this information, apply it to the function we need to write:

- The name of the function in the "Act" step is the function we're testing, and the function to define
- The number of arguments passed into this function is the number of parameters that the function signature needs
- The assumed value of `result` is what the function call needs to _return_

##### !end-hint
### !explanation

An example of a working implementation:

```python
def is_odd(num):
    if num < 0:
        return None
    elif num % 2 == 0:
        return False
    else:
        return True
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->