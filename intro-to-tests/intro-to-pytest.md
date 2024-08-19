# Intro to pytest

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=3df8554d-2963-4ae9-a253-acd20023dc59&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

## Learning Goals

- Use automated unit tests to verify code correctness

## Introduction

When we understand that tests can verify code correctness, let's learn one way to use and write tests. The actual tools needed to use tests will depend on the language and technologies the project is in. Often, software teams have already decided their testing framework. In this curriculum, we've decided to test our Python code with `pytest`.

## Vocabulary and Synonyms

| Vocab     | Definition                        | Synonyms | How to Use in a Sentence |
| --------- | --------------------------------- | -------- | ------------------------ |
| Assertion | A statement that somethng is true |
| Assert    | Stating that something is true    | expect   |

## Installing `pytest`

[`pytest`](https://docs.pytest.org/en/stable/) is one of many testing tools for the Python language.



Before we install `pytest`, let's recall the steps we took in precourse the commands to install Python packages. First, we need to navigate to the directory that we want to step up our virtual environment in. You can use the `pwd` command to check if we are currently inside of the desired directory, if not then we can use the `cd` command to navigate to the correct one. After we are inside the correct directory we can the following commands to create and then activate our virtual environment:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

Remember that the first command creates a virtual environment under the name `venv` and the second command activates our virtual environment. After running the activation command, we should now see that each line of our terminal now begins with `(venv)`. This lets us know that our virtual environment has been activated. 

### !callout-info

## Virtual Environments

At high level, virtual environments are used to  install and manage packages separately from other projects that could be using the same packages. For instance, if project A requires an older version of `pytest` than project B, using a virtual environment allows both projects to exist on the same machine without have to upgrade/downgrade `pytest` to meet the conflicting version requirements. We will discuss virtual environments in greater detail later in Managing Packages and when discussing the Adagrams project.

### !end-callout


Now let's use the command below to install `pytest`:

```bash
(venv) pip3 install -U pytest
```

### !callout-danger

## pip3

Recall that we use `pip3` to designate `pip` for Python3.

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

`pytest` has a rule about naming individual tests: **It will only recognize test names begin with `test_` or end with `_test`**. The rest of the test name should imply the scenario you're testing.

Possible example test names include:

- `test_creates_chart` or `creates_chart_test`
- `test_returns_none_for_invalid_date` or `returns_none_for_invalid_date_test`
- `test_handles_yyyymmdd_date_format` or `handles_yyyymmdd_date_format_test`
- `test_raises_error_for_empty_location` or `raises_error_for_empty_location_test`

### `assert`

`assert` is a statement that will determine a test pass or failure. To the right of the `assert` should be an expression or comparison.

The `assert` statement checks if what's on the right is **truthy**. If the expression to the right is truthy, then the assertion will pass, and the test execution will move to the next line. If the expression is falsey, then the assertion will fail, the test execution will leave that test, and move on to the running the rest of the test suite.

We can use the wide range of Python comparisons in our `assert` statements.

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

<!-- available callout types: info, success, warning, danger, secondary, star  -->
### !callout-info

## `@pytest.mark.skip`

To skip a test we can place the _decorator_ `@pytest.mark.skip` above the unit test:

```python
@pytest.mark.skip
def test_my_func_returns_hello_world():
    result = my_func()
    assert result == "Hello, World!"
```

Python decorators are used to add functionality to a function or method. A python decorator uses the <code>@</code> symbol and is placed above the function that it decorates. Follow your curiosity to learn more about the [implementation of decorators](./intro-to-decorators.md).

### !end-callout

## Arrange, Act, Assert is Useful Test Structure

What do we put into the test (function) body? "Arrange, Act, Assert" is a useful pattern for reading and structuring tests.

| section | likely location in test | description                                                                                                                                                                                                                             |
| ------- | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Arrange | top                     | The top section of a test can include things to arrange, or set up. This can be creating variables, calling helper methods, or anything else depending on the context. Sometimes this section doesn't exist, because there is no setup. |
| Act     | middle                  | This section is where what needs to be tested _happens_. If we're writing a unit test for a function, this is where we invoke the function.                                                                                             |
| Assert  | end                     | The assert section is where any assert statements can be made.   |

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

| Code                      | Description                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------- |
| `import pytest`           | In order to check for raised exceptions, we need to import `pytest`.                          |
| `with pytest.raises(...)` | This syntax begins a block, checking for an exception to be raised within the block           |
| `ZeroDivisionError`       | The kind of exception we expect should be specified here                                      |
| `1 / 0`                   | In this code block, we should do our **Act** step, or invoke the function we're testing here. |

### !callout-info

## Testing Raised Exceptions?

This curriculum will go deeper into raising exceptions eventually! For now, awareness of syntax is our friend.

### !end-callout

### !callout-danger

## This Curriculum Uses unittest, Not pytest

This curriculum teaches pytest, a testing framework that has wide adoption in the Python community. This curriculum's projects will use pytest. However, **the code challenges within this curriculum will use unittest,** a different testing framework. This is due to a limitation in the curriculum tools.

---

Working with unittest, rather than pytest, will have some differences in syntax. However, conceptually, they are the exact same; the structure, error output, error messages, passed test messages, etc. will all be extremely alike.

This curriculum believes in a learner's ability to smoothly work with these differences.

### !end-callout

## Check for Understanding

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge
* type: ordering
* id: a1NxH7
* title: Intro to Pytest
##### !question

Rearrange these lines so they follow the logical order that a unit test is normally in.

##### !end-question
##### !answer

1. Test name
1. Arrange step, where setting up any variables is
1. Act step, where we call the tested function
1. Assert step, where we check that the result of the tested function is what we expected

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->
<!-- prettier-ignore-start -->
### !challenge
* type: ordering
* id: M9WsZl
* title: Intro to Pytest
##### !question

Rearrange these lines of code so they become a valid unit test. Assume that each line would be indented correctly.

##### !end-question
##### !answer

1. `def test_my_func_returns_hello_world():`
1. `result = my_func()`
1. `assert result == "Hello, World!"`

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 3 -->
<!-- prettier-ignore-start -->
### !challenge
* type: ordering
* id: lImr91
* title: Intro to Pytest
##### !question

Rearrange these lines of code so they become a valid unit test. Assume that each line would be indented correctly.

##### !end-question
##### !answer

1. `def test_zero_division():`
1. `with pytest.raises(ZeroDivisionError):`
1. `1 / 0`

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question Takeaway -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: RSsEpy
* title: Intro to Pytest
##### !question

What was your biggest takeaway from this lesson? Feel free to answer in 1-2 sentences, draw a picture and describe it, or write a poem, an analogy, or a story.

##### !end-question
##### !placeholder

My biggest takeaway from this lesson is...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->
