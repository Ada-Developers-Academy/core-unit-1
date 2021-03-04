# Problem Set: While Loops

## Directions

Complete all questions below.

## Practice

<!-- prettier-ignore-start -->
### !challenge

* type: multiple-choice
* id: 31402b5a-5d5a-409f-b5cd-a5c1a7f845d7
* title: While Loops

##### !question

How many times will the body of this `while` loop run?

```python
counter = 0
while counter < 5:
    print('in the loop body')
    counter += 1
```

##### !end-question

##### !options

* 0
* 4
* 5
* 6
* it runs forever
* impossible to predict

##### !end-options

##### !answer

* 5

##### !end-answer

### !end-challenge
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
### !challenge

* type: multiple-choice
* id: ce90bffc-5966-4486-8c2f-4d1d10ca58d3
* title: While Loops

##### !question

How many times will the body of this `while` loop run?

```python
counter = 4
while counter >= 0:
    print('in the loop body')
    counter -= 1
```

##### !end-question

##### !options

* 0
* 4
* 5
* 6
* it runs forever
* impossible to predict

##### !end-options

##### !answer

* 5

##### !end-answer

##### !explanation

A loop like this, running from some value all the way down to 0, might be used to access the entries in a list in reverse order. This loop iterates from 4 down to 0, which are the indices of a list with 5 items.

<br />

Because this "off by one" can be confusing, we often prefer `for` loops in a situation like this rather than a `while` loop.

##### !end-explanation

### !end-challenge
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
### !challenge

* type: multiple-choice
* id: 5fa25950-37c3-48d9-ae6c-81d41d85e85a
* title: While Loops

##### !question

How many times will the body of this `while` loop run?

```python
counter = 0
while counter < 10:
    print('in the loop body')

    if counter < 5:
        continue

    counter += 1
```

##### !end-question

##### !options

* 0
* 1
* 5
* 10
* it runs forever
* impossible to predict

##### !end-options

##### !answer

* it runs forever

##### !end-answer

##### !explanation

Even though this loop has a statement to increment `counter`, it also has a condition in the loop body that skips it! Imagine how hard this might be to spot if it were buried in very complicated logic!

<br />

Infinite `while` loops don't always happen from forgetting to write a line that updates the loop control variable. Sometimes our own code gets in the way. This is why we often prefer `for` loops if we know how many times we want a loop to run ahead of time!

##### !end-explanation

### !end-challenge
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
### !challenge

* type: multiple-choice
* id: 9401f1e3-778d-4559-a1ef-dee071d4db90
* title: While Loops

##### !question

How many times will the body of this `while` loop run?

```python
import random

num = random.randint(1, 10)
while num <= 5:
    print('in the loop body')
    num = random.randint(1, 10)
```

##### !end-question

##### !options

* 0
* 1
* 5
* 10
* it runs forever
* impossible to predict

##### !end-options

##### !answer

* impossible to predict

##### !end-answer

##### !explanation

This loop has a 50/50 chance of executing the loop body each time the condition is checked. We don't know for certain how many times it will run! Now, this isn't really a very useful loop, but image instead of a random number, we ask for user input. If some value of that input lets us decide to terminate the loop, then we also can't say for certain how many times _that_ loop will run. This is the most typical use for a `while` loop: loops that run an indeterminate number of times.

##### !end-explanation

### !end-challenge
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
### !challenge

* type: multiple-choice
* id: 9016d79a-4d74-459f-a714-ca38bf9a176c
* title: While Loops

##### !question

How many times will the body of this `while` loop run?

```python
while counter < 5:
    print('in the loop body')
    counter += 1
```

##### !end-question

##### !options

* 0
* 4
* 5
* 6
* it runs forever
* impossible to predict

##### !end-options

##### !answer

* 0

##### !end-answer

##### !explanation

We forgot to initialize `counter`! This causes a `NameError` in the loop condition, so we don't run the loop body. In fact, this code will crash!

<br />

There are many things we have to remember when setting up `while` loops: initializing loop control variables, getting the loop condition right, properly updating the loop control variable, and that doesn't even consider the actual _logic_ we want to do in our loop! For these reasons, when possible, we often try to replace `while` loops with `for` loops. The next few questions explore this.

##### !end-explanation

### !end-challenge
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
### !challenge

* type: multiple-choice
* id: 0a8cfa41-b770-4e80-8af0-f4d5127c8424
* title: While Loops

##### !question

Which of the `for` loops below is equivalent to this `while` loop?

```python
counter = 0
while counter < 5:
    print(counter)
    counter += 1
```

##### !end-question

##### !options

* ```python
for counter in range(4):
    print(counter)
```

* ```python
for counter in range(5):
    print(counter)
```
* ```python
for counter in range(5, 0):
    print(counter)
```

* ```python
for counter in range(5, 0, -1):
    print(counter)
```

##### !end-options

##### !answer

* ```python
for counter in range(5):
    print(counter)
```

##### !end-answer

##### !explanation

The `while` loop runs from 0 to 4 (less than 5), printing each value. Recall that the `range` function

##### !end-explanation

### !end-challenge
<!-- prettier-ignore-end -->



















### REWRITE FOR THE MULTIPLE HELPERS
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

