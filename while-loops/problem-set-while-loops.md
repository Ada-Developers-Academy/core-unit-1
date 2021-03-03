# Problem Set: While Loops

## Directions

Complete all questions below.

## Practice

Some of the following coding questions use a helper function `input_int`.  It works just like the [`input`](https://docs.python.org/3/library/functions.html#input) function that we've seen before, except that instead of returning a string, we will assume that it returns an integer.

In the question blocks below, we don't need to define `input_int`. We can just assume that it is available.

But to experiment with the coding questions in VS Code or repl.it, we will need an implementation for `input_int`. In Python, safely converting from a string to an integer requires handling exceptions. For anyone who has read ahead, or who would like to do some extra research, we can try implementing it ourselves! Otherwise, here's a working implementation.

<details style="max-width: 700px; margin: auto;">
    <summary>A working implementation of `input_int`</summary>
```python
# accept a variable number of positional parameters
def input_int(*args):
    # loop forever (until we get valid input)
    while True:
        # get string input
        user_input = input(*args)
        try:
            # try converting to an int (will return if successful)
            return int(user_input)

            # if the conversion succeeded, we will have returned already
        except ValueError:
            # could not convert the input, so show an error message
            print('Try again.')
```
</details>


<!-- prettier-ignore-start -->
### !challenge

* type: code-snippet
* language: python3.6
* id: 0fdaf2f7-0573-4e0a-8fd2-46f15076de24
* title: While Loops

##### !question

We would like to prompt a user for a number of integers to sum, and then get each number, one by one, and return the sum of the input values.

Provide the implementation for `calculate_sum` so that it
- prompts the user for the number of values to input (be sure to use `input_int`)
- reads as many numbers from the user as they originally entered (again, use `input_int`)
- returns the sum of the entered integers

##### !end-question

##### !placeholder

```python
def calculate_sum():
    # be sure to call input_int when you need an integer from the user
    # a default implementation is provided above for experimenting in VS Code or repl.it
    pass
```

##### !end-placeholder

##### !tests

```py
import unittest
import main

num_src = None

def read_ints(nums):
    for num in nums:
        yield num

def input_int(_):
    return next(num_src)

# inject into main
main.input_int = input_int

class TestPython1(unittest.TestCase):

    def test_one(self):
        global num_src
        num_src = read_ints([6, 1, 1, 2, 3, 5, 8])
        self.assertEqual(20, main.calculate_sum())

    def test_two(self):
        global num_src
        num_src = read_ints([10, 0, 1, 2, 3, 4, 5, 6,7, 8, 9])
        self.assertEqual(45, main.calculate_sum())
```

##### !end-tests

#### !hint

A possible interaction with a user could look like this:
>How many numbers should we sum? 3<br />
>Enter an integer: 1<br />
>Enter an integer: 2<br />
>Enter an integer: 3<br />
>The sum of the numbers is 6


#### !end-hint

#### !explanation

An example of a working implementation:

```python
def calculate_sum():
    loop_count = input_int('How many numbers should we sum? ')
    counter = 0
    my_sum = 0

    while counter < loop_count:
        num = input_int('Enter an integer: ')
        my_sum += num
        counter += 1

    print(f'The sum of the numbers is {my_sum}')
    return my_sum
```

#### !end-explanation

### !end-challenge
<!-- prettier-ignore-end -->

