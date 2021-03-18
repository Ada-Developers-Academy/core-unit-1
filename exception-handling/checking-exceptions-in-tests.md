# Checking Exceptions in Tests

## Learning Goals

- Explain how to handle exceptions using try and except clauses

## Introduction

We've learned that raising exceptions stops the execution of our program to inform the developer about important errors.

Sometimes we will need to raise exceptions in our own projects at certain points. Raising an exception and stopping a program might prevent even bigger catastrophes down the line.

### !callout-info

## Example: Stop Money Transfers

For example, imagine writing a banking web app that allows customers to transfer money between accounts. Now imagine the customer Jordi. Unfortunately, her web browser doesn't allow web forms to enforce form validations. Jordi types in that she wants to withdraw $400 from her account. However, she makes a typo and inputs $4,000,000. That's more than she has!

The web form wouldn't stop her from doing this, and the Python language wouldn't throw a Runtime error. However, we can stop the program from withdrawing $4,000,000 by throwing an exception of our own.

### !end-callout

When it's important for us to raise errors, we should use unit tests to verify that we're raising errors as expected. `pytest` has syntax to help us expect raised exceptions.

## pytest Syntax

When preparing to write a test that expects a raised exception, we should determine two things:

1. What function call and input do we expect to raise the exception?
1. What kind of exception do we expect from this function call?

With those two pieces of info in mind, we can understand the pytest syntax:

```python
def test_exceptional_function():
    with pytest.raises(SomeTypeOfException):
        exceptional_function(exceptional_argument)
```

| <div style="min-width:485px; text-align:center;">Code</div>                   | <div style="min-width:220px;">Description</div>    |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <div style="text-align:center;">`with pytest.raises(...):`</div>              | pytest needs to know beforehand that we're expecting an exception. We use `with pytest.raises(...):` to begin a code block that will be able to handle it. If we don't, the test itself will crash! |
| <div style="text-align:center;">`SomeTypeOfException` </div>                        | **Replace this** with the exact kind of exception we're expecting. Examples include `TypeError`, `NotImplementedError`, or any other Python error. |
| `test_exceptional_function(exceptional_argument)` | **Replace this** with the function call that will raise the exception.                                                                                                                |

### Read This Example

Read this example and predict your answers for:

1. What function call will raise an exception?
1. What kind of exception will this function call raise?

```python
def divide_two_nums(apples, oranges):
    return apples / oranges

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide_two_nums(1, 0)
```

In the test `test_zero_division`, we can read and confirm:

1. The function we expect to raise an exception is `divide_two_nums`, specifically `divide_two_nums(1, 0)`.
1. The kind of exception we're expecting from this function call is `ZeroDivisionError`

## Check for Understanding

<!-- Question 1 -->

<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: 8HwyKa
* title: Checking Exceptions in Tests

##### !question

What is the function call that will raise an exception?

```python
def test_check_is_phone_num_valid():
    phone_num = 777-888-9999
    with pytest.raises(ValueError):
        is_valid = is_phone_num_valid(phone_num)
```

##### !end-question
##### !placeholder

function_name(args)

##### !end-placeholder
##### !answer

is_phone_num_valid(phone_num)

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->

<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: wrXI7Z
* title: Checking Exceptions in Tests

##### !question

What is the kind of exception we're expecting?

```python
def test_check_is_phone_num_valid():
    phone_num = 777-888-9999
    with pytest.raises(ValueError):
        is_valid = is_phone_num_valid(phone_num)
```

##### !end-question
##### !placeholder

NameOfException

##### !end-placeholder
##### !answer

ValueError

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 3 -->

<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: TmFBrt
* title: Checking Exceptions in Tests

##### !question

What is the function call that will raise an exception?

```python
def test_add_student_to_roster():
    roster = {}
    student = "Cordelia Wang"
    with pytest.raises(AttributeError):
        add_student_to_roster(roster, student)
```

##### !end-question
##### !placeholder

function_name(args)

##### !end-placeholder
##### !answer

add_student_to_roster(roster, student)

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 4 -->

<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: z4Qv6S
* title: Checking Exceptions in Tests

##### !question

What is the kind of exception we're expecting?

```python
def test_add_student_to_roster():
    roster = {}
    student = "Cordelia Wang"
    with pytest.raises(AttributeError):
        add_student_to_roster(roster, student)
```

##### !end-question
##### !placeholder

NameOfException

##### !end-placeholder
##### !answer

AttributeError

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->
