# While Loops

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=7868f1ce-2c0c-4074-aad7-ace501135410&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

## Learning Goals

- Practice using while-loops
- Practice using a counter variable in a while-loop

## Introduction

Imagine writing software that creates digital group greeting cards. Before the user can sign a digital group greeting card, they need to type in the specific password `AdaLovelaceCodesIt` . If they don't type in the correct password, then the app should ask them to type in the password again, and again, and again, until the user leaves or types in `AdaLovelaceCodesIt` .

How can we solve this problem using Python code?

`for` loops allow programmers to iterate over lists. Sometimes, we need to repeat lines of code, but not because we are traversing (iterating through) a list. We can explore the `while` loop as an alternative!

## Vocabulary and Synonyms

| Vocab            | Definition                                                                                                                                                                                                                   | Synonyms     | How to Use in a Sentence                                                                                        |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------------------------------------------------------------------------------------------------------- |
| Infinite loop    | A loop that runs and never terminates or ends. This leads to a program freezing or getting stuck doing the same thing forever.                                                                                               | endless loop | "The loop kept going and going forever, " "The program hit an infinite loop and I had to terminate it manually" |
| Counter variable | A variable solely used to represent a number that increments or decrements. Usually, counter variables are used to count loop iterations. It needs to be initialized outside of the loop. This is an informal, casual label! | -            | "The counter variable `i` started at `0` and incremented by 1 with each loop"                                   |

## `while` Loop Syntax

While-loops are loops that run _while_ some condition is `True` or truthy.

```python
while conditional_evaluates_to_true:
    print("I'm in the loop body")
```

| Piece of code                  | Notes                                                                                                                                              |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `while`                        | `while` is a keyword in Python that begins a while-loop. It looks immediately to the right for a conditional expression, and a `:` to end the line |
| `conditional_evalutes_to_true` | **Replace this** with a conditional expression. When this expression is true, the loop body will run                                               |
| Loop body                      | **Replace this** with the code that should run in this while-loop. This should be indented once inside the while-loop.                             |

### Practicing Reading While Loops

Here, we use a while-loop to print the numbers 1 through 5.

```python
i = 1
while i <= 5:
    print(f"The value of i is {i}")
    i += 1

print("We are outside the while-loop! Wooo!")
```

Here, we have a variable `i` . While `i` is less than or equal to 5, we will print `f"The value of i is {i}"` and then increment `i` by one.

`i` begins with a value of `1`. As the `while` loop iterates, `i` grows bigger and bigger, since we're modifying the same `i` variable.

At some point, `i` will have a value of `6` . The conditional, `i <= 5`, will evaluate to `False` and the while-loop will exit. Our code execution moves on to the final `print` statement.

Another way to read this while-loop is with a table:

| Value of `i` at the beginning of the loop iteration | Is `i <= 5` ? | Value of `i` at the end of the loop body |
| --------------------------------------------------- | ------------- | ---------------------------------------- |
| `1`                                                 | `True`        | `2`                                      |
| `2`                                                 | `True`        | `3`                                      |
| `3`                                                 | `True`        | `4`                                      |
| `4`                                                 | `True`        | `5`                                      |
| `5`                                                 | `True`        | `6`                                      |
| `6`                                                 | `False`       | Loop body doesn't execute                |

Here, we should observe that at some point, `i` has a value of `6` , and the code asked "Is 6 <= 5? Is that true?" Because the answer is no, the program does not execute the loop body again and exits the loop.

<!-- prettier-ignore-start -->
### !callout-danger

## Infinite Loops
While-loops can accidentally run infinitely! If the conditional for the while-loop never becomes false, then the while-loop and the program keep going, and going, and going... until something forces it to stop (such as a human closing down the program), or our machine cannot run it anymore. We call these cases **infinite loops,** and are often a bug.
### !end-callout
<!-- prettier-ignore-end -->

## Problem-Solving Using `while`

Let's explore different examples that apply while-loops.

We can use a while-loop even if we are decrementing a variable...

```python
print("Preparing for blastoff in")

countdown = 10

while countdown > 0:
    print(f"{countdown}...")
    countdown -= 1

print("Launch!")
```

We can use a while-loop that uses a function to calculate something...

```python
flower_basket = []

while len(flower_basket) < 12:
    flower_basket.append("flower")

print("I have a very full flower basket with a dozen flowers:", flower_basket)
```

### !callout-danger

## Operator Syntax

Note that this conditional uses `<` , _not_ `<=` , because we don't want to add another flower if the length of `flower_basket` is _equal_ to twelve. Watch out for an off-by-one error!

### !end-callout

We can use a while-loop that only checks if a variable is `True` or truthy!

```python
import random
coin_is_tails = True

while coin_is_tails:
    print("The coin flip is tails!")
    print("Will we get heads in the next coin flip?")
    coin_is_tails = bool(random.randint(0, 1))

print("We finally got heads.")
```

### Counter Variables

Let's return to our original example:

```python
i = 1
while i <= 5:
    print(f"The value of i is {i}")
    i += 1

print("We are outside the while-loop! Wooo!")
```

A variable that is only incremented or decremented, specifically in a loop, is often called a _counter variable._

A counter variable is:

- used in the conditional expression for the while-loop
- must be modified somewhere in the body of the while-loop
- must be initialized before the loop

In this case, `i` is the counter variable. It gets setup before the while-loop begins, and then increments inside the while-loop. When we forget to change our counter variable, we often get infinite loops and bugs!

### !callout-info

## `for` Loops

An alternative syntax is to use `for` loops with a range. The `for` loop syntax sets up and modifies something like a counter variable!

### !end-callout

### `break` and `continue`

`break` is a keyword. When our code comes across `break` in a while-loop, it will exit the entire while-loop. The next line that runs is the line after the while-loop.

```python
def demonstrate_break():
    i = 3

    while i < 10:
        if i == 7:
            print("i is seven! Let's get out of here!")
            break
        print(f"Counting: i is {i}")
        i += 1

demonstrate_break()
```

Possible example use cases:

- needing to find a specific element, then leave the iteration
- needing to leave the loop in case it comes across some invalid or error state

`continue` is a keyword that will stop executing the current iteration, and resume execution at the next iteration. When our code sees `continue`, it doesn't run anymore code in that iteration but continues to the next iteration of the loop.

```python
def demonstrate_continue():
    i = 3

    while i < 10:
        i += 1
        if i == 7:
            print("i is seven!")
            print("Let's print this special message, and then move on")
            print("*~*~*~* \o/ *~*~*~*")
            continue
        print(f"Counting: i is {i}")

demonstrate_continue()
```

Possible example uses cases:

- needing to "skip" the rest of a loop body in a special case

## Check for Understanding

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: AJC4nw
* title: While Loops
### !question

Fix this loop so it loops while `i` is less than `5` .

### !end-question
### !placeholder
``` python
def loop_until_five():
    i = 0

    while False:
        i += 1

    return i

result = loop_until_five()
```
### !end-placeholder
### !tests
```python
import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_loop_until_five(self):
        self.assertEqual(loop_until_five(), 5)
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def loop_until_five():
    i = 0

    while i < 5:
        i += 1

    return i
```

Here are the tests:

```python
def test_loop_until_five():
    assert loop_until_five() == 5
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: jMroBQ
* title: While Loops
##### !question

Think about the function named `loop_until_five()` from the previous question. What value does `loop_until_five()` return?

##### !end-question
##### !answer
5
##### !end-answer
##### !explanation

Even though the loop only ran while `i` was less than five, when `i` was the value `4`, it incremented to `5`.

Prove this to yourself by running this code!

```python
def loop_until_five():
    i = 0

    while i < 5:
        print("new loop")
        print("before inc, aka i < 5 is true:", i)
        i += 1
        print("after inc:", i)

    return i
```

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 3 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: UZgKoW
* title: While Loops
##### !question

Which of these loop table options most accurately describes this loop?

``` python
i = 0
result = None

while i < 5:
    if (i % 2) == 0:
        result = True
    else:
        result = False
    i += 1
```

### Loop Table Apple

| `i` at beginning of loop | `i < 5` ? | `i` at the end of loop body | `result` at end of loop body |
| ------------------------ | --------- | --------------------------- | ---------------------------- |
| `0`                      | `True`    | `1`                         | `False`                      |
| `1`                      | `True`    | `2`                         | `True`                       |
| `2`                      | `True`    | `3`                         | `False`                      |
| `3`                      | `True`    | `4`                         | `True`                       |
| `4`                      | `True`    | `5`                         | `False`                      |
| Loop doesn't execute     | -         | Loop body doesn't execute   | -                            |

### Loop Table Banana

| `i` at beginning of loop | `i < 5` ? | `i` at the end of loop body | `result` at end of loop body |
| ------------------------ | --------- | --------------------------- | ---------------------------- |
| `0`                      | `True`    | `1`                         | `True`                       |
| `1`                      | `True`    | `2`                         | `False`                      |
| `2`                      | `True`    | `3`                         | `True`                       |
| `3`                      | `True`    | `4`                         | `False`                      |
| `4`                      | `True`    | `5`                         | `True`                       |
| Loop doesn't execute     | -         | Loop body doesn't execute   | -                            |

### Loop Table Carrot

| `i` at beginning of loop | `i < 5` ? | `i` at the end of loop body | `result` at end of loop body |
| ------------------------ | --------- | --------------------------- | ---------------------------- |
| `0`                      | `True`    | `0`                         | `True`                       |
| `1`                      | `True`    | `1`                         | `False`                      |
| `2`                      | `True`    | `2`                         | `True`                       |
| `3`                      | `True`    | `3`                         | `False`                      |
| `4`                      | `True`    | `4`                         | `True`                       |
| Loop doesn't execute     | -         | Loop body doesn't execute   | -                            |

### Loop Table Durian

| `i` at beginning of loop | `i < 5` ? | `i` at the end of loop body | `result` at end of loop body |
| ------------------------ | --------- | --------------------------- | ---------------------------- |
| `0`                      | `True`    | `1`                         | `True`                       |
| `1`                      | `True`    | `2`                         | `False`                      |
| `2`                      | `True`    | `3`                         | `True`                       |
| `3`                      | `True`    | `4`                         | `False`                      |
| `4`                      | `True`    | `5`                         | `True`                       |
| `5`                      | `False`   | Loop body doesn't execute   | -                            |

##### !end-question
##### !options

* Loop Table Apple
* Loop Table Banana
* Loop Table Carrot
* Loop Table Durian

##### !end-options
##### !answer

* Loop Table Durian

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 4 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: SLx1UM
* title: While Loops
### !question

The function `look_for_treasure` has an error in it! `look_for_treasure` should exit after we find treasure. Add in the `break` keyword in the right location so the test passes.

### !end-question
### !placeholder

```python
import random


def check_if_treasure(item):
    is_treasure = random.randrange(100) < 25
    # The line below uses the ternary operator.
    return "Treasure!" if is_treasure else item + 1


def look_for_treasure():
    i = 0

    while True:
        if i == "Treasure!":
            print("We found treasure instead of a number!")
            print("Let's leave while we can.")
        print(f"Counting: i is {i}")
        i = check_if_treasure(i)

    print("I broke out of the loop!")
    return "I'm free!"
```
### !end-placeholder
### !tests
```python
import unittest
import random
from main import *

class TestPython2(unittest.TestCase):
    def test_look_for_treasure(self):
        self.assertEqual(look_for_treasure(), "I'm free!")
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def look_for_treasure():
    i = 0

    while True:
        if i == "Treasure!":
            print("We found treasure instead of a number!")
            print("Let's leave while we can.")
            break
        print(f"Counting: i is {i}")
        i = check_if_treasure(i)

    print("I broke out of the loop!")
    return "I'm free!"
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question Takeaway -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: MwC1Ik
* title: While Loops
##### !question

What was your biggest takeaway from this lesson? Feel free to answer in 1-2 sentences, draw a picture and describe it, or write a poem, an analogy, or a story.

##### !end-question
##### !placeholder

My biggest takeaway from this lesson is...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->
