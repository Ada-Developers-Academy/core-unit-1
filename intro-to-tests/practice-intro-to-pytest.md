1
Which of these is the best name for a test?


```python
def calculate(num_a, num_b, operator):
    if (isinstance(num_a, int) or isinstance(num_a, float)) and (isinstance(num_b, int) or isinstance(num_b, float)):
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

test_calculate()
test_calculate_int_float_error()
test_calculate_non_numbers_returns_type_error()
tests_calculate_non_numbers_returns_type_error()


In tests, long test names are welcome. For each test case, the best test names usually include:

- the name of the tested function
- context (possibly the kinds of arguments)
- its expected outcome (usually the return value)

The following guideline is challenging to master, but the best test names tend to describe a situation, and not name exact variable names. If the variable name changes, then the test name could become inaccurate.


We want to test `calculate()` and verify the case when it returns `"Value Error: Operator Not Found"`. Which of these is the best name for a test?

test_calculate()
test_calculate_return_string()
test_calculate_invalid_operator_returns_string()
test_calculate_invalid_operator_returns_error_msg()


We want to test `calculate()` and verify that multiplying two numbers works successfully. Which of these is the best name for a test?

test_calculate()
test_calculate_adds_two_numbers()
test_calculate_multiplies_two_numbers()
test_calculate_num_a_is_int_num_b_is_float_operator_is_multiply()

We want to test `calculate()` and verify the case when it returns `"Zero Division Error"`. Which of these is the best name for a test?

test_calculate_dividing_when_second_number_is_zero()
test_calculate_dividing_by_zero_returns_error_msg()
test_calculate_dividing_num_b_is_zero()
test_calculate_dividing_by_zero()

Consider `calculate()`. Which of these are valid test cases to have assertions for?

When `num_a` is not an integer or float, returns `"Type Error"`
When `num_b` is not an integer or float, returns `"Type Error"`
Successful addition when operator is `"add"`
Successful addition when operator is `"ADD"`
Successful addition when operator is `"+"`
Successful subtraction when operator is `"subtract"`
Successful subtraction when operator is `"SUBTRACT"`
Successful subtraction when operator is `"-"`
Successful multiplication when operator is `"multiply"`
Successful multiplication when operator is `"MULTIPLY"`
Successful multiplication when operator is `"*"`
Successful division when operator is `"divide"`
Successful division when operator is `"DIVIDE"`
Successful division when operator is `"/"`
When `num_b` is `0` and operator is division, returns `"Zero Division Error"`
When `operator` is an invalid value, such as `"elephant"` or `True`, returns `"Value Error: Operator Not Found"`

2


Logical Arrange Act Assert ordering

def test_calculate_invalid_operator_returns_error_msg():
invalid_operator = "elephant"
error_msg = calculate(1, 1, invalid_operator)
assert error_msg == "Value Error: Operator Not Found"


def test_calculate_multiplies_two_numbers():
assert calculate(2, 3, "*") == 6

6


Arrange Act Assert ordering

Rearrange these lines so they follow the logical order that a unit test is normally in.

Test name
Arrange step, where setting up any variables is
Act step, where we call the tested function
Assert step, where we check that the result of the tested function is what we expected

1


Rearrange these lines of code so they become a valid unit test. Assume that each line would be indented correctly.


def test_my_func_returns_hello_world():
result = my_func()
assert result == "Hello, World!"

4

Rearrange these lines of code so they become a valid unit test. Assume that each line would be indented correctly.

def test_zero_division():
with pytest.raises(ZeroDivisionError):
1 / 0

5 Read this test failure



```bash
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

In the test, it compares `mystery_function()` to `False`, and they are not equal
In the test, it calls `mystery_function()` with two arguments, but `mystery_function()` has zero parameters
In `mystery_function()`, it calls the function with two arguments, but `mystery_function()` has zero parameters
In `mystery_function()`, it does an operation on `"apples"` and `"oranges"` that isn't valid


In this test report, what line of what file caused the error?

`test_mystery_function()`, line 2
`test_mystery_function()`, line 31
`main.py`, line 2
`main.py`, line 31


```bash
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

The test expects `mystery_function("apples", "oranges")` to return `False`, but it returns `True`
The test expects `mystery_function("apples", "oranges")` to return `True`, but it returns `False`
The test has incorrect syntax in the line `assert mystery_function("apples", "oranges") == False`
The test has incorrect syntax in the line `assert True == False`


```bash
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

The test expects `is_passenger` to be `True`, but it's `False`
The test expects `is_passenger` to be `False`, but it's `True`
The test has incorrect syntax in the line `assert is_passenger`
The test has incorrect syntax in the line `is_passenger = mystery_function(100, 0)`


```bash
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

In the test, it expects `a.append(b)` to be `False`, but it's `True`
In the test, it uses `append` instead of `assert`, and it should compare `a` and `b` to be equal, instead of append
In `mystery_function`, it expects `a.append(b)` to be `a = 100` and `b = 0`
In `mystery_function`, it calls `append()`. `a` is the integer `100`, so it doesn't have the method `append`


3 imagine another test case







3 imagine another test case



