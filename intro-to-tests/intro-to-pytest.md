# Intro to pytest

## Learning Goals

- Use automated unit tests to verify code correctness

## Introduction

When we understand that tests can verify code correctness, let's learn one way to use and write tests. The actual tools needed to use tests will depend on the language and technologies the project is in. Often, software teams have already decided their testing framework. In this curriculum, we've decided to test our Python code with `pytest`.

## Vocabulary and Synonyms

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---
Assertion | A statement that somethng is true |
Assert | Stating that something is true | expect |

## Installing `pytest`

[`pytest`](https://docs.pytest.org/en/stable/) is one of many testing tools for the Python language.

We can install (and upgrade) the `pytest` package with this command:

```bash
pip3 install -U pytest
```

### !callout-danger
## pip3
Callout in Red: Recall that we use `pip3` to designate `pip` for Python3.
### !end-callout


## Reworking Our Project Structure

When we use `pytest`, we will be creating more files. In order to anticipate more files, some future projects and assignments will follow this folder structure:

```bash
.
├── projectname
│   ├── __init__.py
│   └── somefile.py
└── tests
    ├── __init__.py
    ├── context.py
    └── test_somefile.py
```

Take care to notice the following:
1. In our project directory, there are 0 files, and 2 folders: `projectname` and `tests`.
    - We will replace the folder name `projectname` with our project's name
1. In our `projectname` folder, there is a file named `somefile.py`
    - This represents any Python files that include the functions we're writing
1. In our `tests` folder, there is a file named `test_somefile.py`
    - This represents a test file that is responsible for testing `projectname/somefile.py`
1. There are some other files: `__init__.py` and `context.py`
    - We will not focus on these files, but feel free to read through them

This folder structure isn't necessary to make `pytest` work; this folder structure:
1. Provides structure and organization to our projects
1. Mimics a project structure commonly used across technologies

### Tests Files go in the `tests` Directory

When we have test files, by convention, we'll organize them in the `tests` folder.

`pytest` has a rule about filenames: a test file's filename **must either** begin with `test_`, or end with `_test.py`.

A single test file will contain:

1. One or more unit tests
1. Any code that helps support these tests, such as helper methods or imports

## Running `pytest`

When we have `pytest` installed, and some test files, we can run the tests from the Terminal with the command `pytest`. When we change any code and want to see the new results of the test, we'll run `pytest` again!

### Reading the Results

After the tests run, the results of the tests will be printed to the terminal. The results read in this order:

```bash
========================================================= test session starts =========================================================
rootdir: /Users/user/projects/project
collected 2 items

tests/test_somefile.py F.                                                                                                         [100%]

============================================================== FAILURES ===============================================================
_________________________________________________________ test_true_is_false __________________________________________________________

    def test_true_is_false():
>       assert True is False
E       assert True is False

tests/test_somefile.py:5: AssertionError
======================================================= short test summary info =======================================================
FAILED tests/test_somefile.py::test_true_is_false - assert True is False
===================================================== 1 failed, 1 passed in 0.05s =====================================================
```

1. `test session starts` will print some facts about the tests, like how many tests there are. There will be a series of `.`s for passing tests, and `F` for failing tests.
1. `FAILURES` will print any tests that failed, the names of the test and what file and line it's on, and how these tests failed.
1. `short test summary info` will print a short test summary info, including overall how many tests passed or failed, and how long the tests took to run.

## Anatomy of a Unit Test

A single unit test will use the function syntax:

```python
def test_my_func_returns_hello_world():
    result = my_func()
    assert result == "Hello, World!"
```

The function name is the name of the test, and it should imply what the test is testing.

The function body contains the details of the test.

`pytest` has a rule about naming tests: **It will only recognize test names beginning with `test_`**. The rest of the test name should imply the scenario you're testing. Possible example test names include, `test_creates_chart`, `test_returns_none_for_invalid_date`, `test_handles_yyyymmdd_date_format`, or `test_raises_error_for_empty_location`.

### `assert`

`assert` is a statement that will determine a test pass or failure. To the right of the `assert` should be an expression or comparison.

The `assert` statement checks if what's on the right is **truthy**. If the expression to the right is truthy, then the assertion will pass, and the test execution will move to the next line. If the expression is falsey, then the assertion will fail, the test execution will leave that test, and move on to the running the rest of the test suite.

We can use comparisons, and the wide range of Python comparisons in our `assert` statements.

Read through these example `assert` statements as passing examples that prove we can compare numbers, strings, 

1. `assert True`
1. `assert 3+3`
1. `assert 3 == 3`
1. `assert 2 != 3`
1. `assert 2 < 3`
1. `assert (10/2) < (3*3)`
1. `assert ["a", "b", "c"] == ["a", "b", "c"]`
1. `assert "a" in ["a", "b", "c"]`
1. `assert some_variable == other_variable`
1. `assert some_variable is other_variable`
1. `assert some_variable != other_variable`
1. `assert 2 is not 3`
1. `assert "dragon" in "Once upon a time, there was a dragon queen..."`
1. `assert "foo" not in "Once upon a time, there was a dragon queen..."`

### !callout-info
## Python Operators
`is`, `not`, `is not`, and `in` are operators in Python. `is` returns true if both sides evaluate to the exact same object in memory. Feel free to keep diving into these operators!
### !end-callout


Tests should include at least one `assert` statement. There can be multiple assertions in a test.

## Arrange, Act, Assert is Useful Test Structure

What do we put into the test (function) body? "Arrange, Act, Assert" is a useful pattern for reading and structuring tests.

| section | likely location in test | description |
| --- | --- | --- |
Arrange | top | The top section of a test can include things to arrange, or set up. This can be creating variables, calling helper methods, or anything else depending on the context. Sometimes this section doesn't exist, because there is no setup.
Act | middle | This section is where what needs to be tested _happens_. If we're writing a unit test for a function, this is where we invoke the function.
Assert | end | The assert section is where any assert statements can be made.

### Expecting a Raised Exception

In contrast to `assert`, sometimes we need to assert that an exception gets raised during a function call.

To write a test that checks that an exception was raised, we need to follow this alternative syntax:

```python
import pytest

def test_zero_division():
    # Arrange steps go here

    # Assert
    with pytest.raises(ZeroDivisionError):
        1 / 0 # Act
```

| Code | Description |
| --- | --- |
`import pytest` | In order to check for raised exceptions, we need to import `pytest`.
`with pytest.raises(...)` | This syntax begins a block, checking for an exception to be raised within the block
`ZeroDivisionError` | The kind of exception we expect should be specified here
`1 / 0` | In this code block, we should do our **Act** step, or invoke the function we're testing here.

## Check for Understanding

Here, we are displaying the contents of the test.

Write a function to make the test pass. Use the information from the test to help determine what needs to be in the function body.

```python
def test_returns_true():
    result = func_that_always_returns_true()
    assert result
```


```python
def test_returns_true_if_odd():
    number = 5
    result = is_odd(number)
    assert result
```

```python
def test_returns_false_if_even():
    number = 6
    result = is_odd(number)
    assert not result
```

```python
def test_returns_None_if_negative():
    number = -1000
    result = is_odd(number)
    assert result is None
```

```python
def test_raises_runtime_error():
    with pytest.raises(RuntimeError):
        my_func()
```
