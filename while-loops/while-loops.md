# While Loops

## Learning Goals

* Practice using while loops to loop while a conditional is true 
* Apply a counter variable while using while loops

## Introduction

Imagine writing software that creates digital group greeting cards. Before the user can sign a digital group greeting card, they need to type in the specific password `AdaLovelaceCodesIt` . If they don't type in the correct password, then the app should ask them to type in the password again, and again, and again, until the user leaves or types in `AdaLovelaceCodesIt` .

How can we solve this problem using Python code?

for loops allow programmers to iterate over lists. Sometimes, we need to repeat lines of code, but not because we are iterating through a list. We can explore the while loop as an alternative!

## Vocabulary and Synonyms

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---
Infinite Loop | A loop that runs and never terminates or ends. Leads to a stack overflow error. | endless loop | "The loop kept going and going forever"
Counter variable | A variable solely used to representing a number that increments or decrements. Usually, it's used to count loops. It needs to be initialized outside of the loop. This is an informal, casual label! | - | "The counter variable `i` started at `0` and went up with each loop"

## While Loops Syntax

While loops are loops that run _while_ some condition is `True` or truthy.

``` python
while conditional_evaluates_to_true:
    print("I'm in the loop body")
```

| Piece of code                  | Notes                                                                                                                                              |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `while` | `while` is a keyword in Python that begins a while loop. It looks immediately to the right for a conditional expression, and a `:` to end the line |
| `conditional_evalutes_to_true` | **Replace this** with a conditional expression. When this expression is true, the loop body will run                                               |
| Loop body                      | **Replace this** with the code that should run in this while loop. This should be indented once inside the while loop.                             |

### Practicing Reading While Loops

Here, we use a while loop to print the numbers 1 through 5.

``` python
i = 1
while i <= 5:
    print(f"The value of i is {i}")
    i += 1

print("We are outside the while loop! Wooo!")
```

Here, we have a variable `i` . While `i` is less than or equal to 5, we will print `f"The value of i is {i}"` . Then, we will increment `i` by one.

`i` begins with a value of `1` . As the while loop loops, `i` grows bigger and bigger, since we're modifying the same `i` variable.

At some point, `i` will have a value of `6` . Then, `i <= 5` is falsey, and the while loop will exit. Our code execution moves on to the final `print` statement.

Another way to read this while loop is with a table:

| Value of `i` at the beginning of the loop | Is `i <= 10` ? | Value of `i` at the end of the loop body |
|-------------------------------------------|---------------|------------------------------------------|
| `1` | `True` | `2` |
| `2` | `True` | `3` |
| `3` | `True` | `4` |
| `4` | `True` | `5` |
| `5` | `True` | `6` |
| `6` | `False` | Loop body doesn't execute                |

Here, we should observe that at some point, `i` has a value of `6` , and the code asked "Is 6 <= 5? Is that true?" Because the answer is false, the code skips over the rest of the loop.

Callout: While loops can accidentally run infinitely! If the conditional for the while loop never becomes false, then the while loop and the program keep going, and going, and going... until something forces it to stop (such as a human closing down the program), or our machine cannot run it anymore. We call these cases **infinite loops, ** and are always a bug.

## Used While Problem-Solving

Let's explore different examples that apply while loops.

We can use a while loop even if we are decrementing a variable...

``` python
print("Preparing for blastoff in")

countdown = 10

while countdown > 0:
    print(f"{countdown}...")
    countdown -= 1

print("Launch!")
```

We can use a while loop that uses a function to calculate something...

``` python
flower_basket = []

while len(flower_basket) < 12:
    flower_basket.append("flower")

print("I have a very full flower basket with a dozen flowers:", flower_basket)
```

Callout: Note that this conditional uses `<` , _not_ `<=` , because we don't want to add another flower if the length of `flower_basket` is _equal_ to twelve. Watch out for an off-by-one error!

We can use a while loop that only checks if a variable is truthy!

``` python
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

``` python
i = 1
while i <= 5:
    print(f"The value of i is {i}")
    i += 1

print("We are outside the while loop! Wooo!")
```

A variable whose job it is to increment or decrement, specifically in a loop, is often called a _counter variable._

This counter variable is:

* used in the conditional expression for the while loop
* must eventually be modified in the while loop
* typically initialized before the loop

In this case, `i` is the counter variable. It gets setup before the while loop begins, and then increments inside the while loop. When we forget to change our counter variable, we often get infinite loops and bugs!

Callout: An alternative syntax is to use for loops with a range. The for loop syntax sets up and modifies something like a counter variable!

### `break` and `continue`

`break` is a keyword. When our code comes across `break` in a while loop, it will exit the entire while loop. The next line that runs is the line after the while loop.

``` python
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

* needing to find a specific element, then leave the iteration
* needing to leave the loop in case it comes across some invalid or error state

`continue` is a keyword that will stop executing the current iteration, and resume execution at the next iteration. When our code sees `continue` , it doesn't run anymore code in that iteration, but continues to the next loop.

``` python
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

* wanting a loop to "skip" in a special case

## Check for Understanding

<!-- Need to figure out the best, most meaningful way to do a question in Learn -->

<!-- question stubs -->

Fix this loop so it uses the counter variable `i` , and runs while `i` is less than `5` .

``` python
def loop_until_five():
    i = 0

    while False:
        i += 1

    return i

result = loop_until_five()
```

<!-- Answer: i should be 5 -->

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

<!-- Answer: This is the correct answer. False answers should toggle True/False on result, or be off-by-one on the i increments -->

| Value of `i` at the beginning of the loop | `i < 5` ? | `i` at the end of loop body | `result` at end of loop body |
|-------------------------------------------|----------|-----------------------------|------------------------------|
| `0` | `True` | `1` | `True` |
| `1` | `True` | `2` | `False` |
| `2` | `True` | `3` | `True` |
| `3` | `True` | `4` | `False` |
| `4` | `True` | `5` | `True` |
| `5` | `False` | Loop body doesn't execute   | -                            |

Read this code. The function `look_for_treasure` should exit after we find treasure. Add in the `break` keyword in the right line to make this happen and pass the test.

``` python
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

result = look_for_treasure()
```

<!-- Answer: i should be "Treasure" -->
