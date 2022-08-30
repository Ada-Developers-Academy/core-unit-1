# Activity: Exception Handling

## Goal

Our goal is to practice generating exceptions and writing tests to handle those exceptions.

## Activity Instructions

### In small groups

- Select one person as the "driver" to fork and clone the [Exception Handling Activity](https://github.com/AdaGold/ExceptionHandlingActivity) repo.
- The driver will share their screen and type, and everyone else will help "navigate".
- In the `main.py` file write a function that throws an exception with logic (not "raises Error".  See the note in the example below.)
- In the `test.py` file write a test for the function.

You can execute the code from the command line with:
` $ python activity/main.py `
Note: make sure to call your function inside your `main.py` file.

You can run the tests with:
` $ pytest `

### As a whole class

- Each group will share their exception and test code.

## Example 

Group A is assigned the exception ZeroDivisionError.

In their main.py they write:
```python

def div_zero(num):
    x = num / 0

div_zero(5)

```
NOTE: Group A has written code that throws the error, in this case a division problem with 0 as the divisor, rather than writing `raises ZeroDivisionError`.  In this activity make sure to write code that generates the error.

In their test.py Group A writes:
```python

def test_exception():
    # Arrange
    num = 5

    # Act
    with pytest.raises(ZeroDivisionError):
        div_zero(num)
```

## Exceptions

Work with the exception corresponding to your group number:
1. KeyError
1. IndexError
1. AttributeError
1. TypeError
1. NameError
1. ValueError
1. UnboundLocalError
1. OverflowError

Use the [Python Exception documentation](https://docs.python.org/3/library/exceptions.html) as a place to start researching about your group's exception.
