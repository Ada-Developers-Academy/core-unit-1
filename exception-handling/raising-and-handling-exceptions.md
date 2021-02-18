# Raising and Handling Exceptions

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=ca96f679-b129-46fa-89f6-acd3003bd65d&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

## Learning Goals

- Define exceptions
- Explain how to handle exceptions using try and except clauses

## Introduction

The absolute worst-case scenario for software is a crash caused by a syntax or runtime error\*. The software has gone to a state where the program can't do anything, the user can't do anything, and possibly the program can't even restart into a usable state!

If software fails for one person, it's likely that software is failing for _many_ people. All of these consequences result in **chaos**.

![giphy](https://user-images.githubusercontent.com/16619004/103056684-748d8a80-4552-11eb-8705-2429df508339.gif) Source: [Giphy](http://gph.is/2lENCEI)

\* = Actually, there are plenty of other more severe worst-case scenarios.

## Vocabulary and Synonyms

| Vocab     | Definition                                                                     | Synonyms | How to Use in a Sentence                                                                      |
| --------- | ------------------------------------------------------------------------------ | -------- | --------------------------------------------------------------------------------------------- |
| Exception | An event or error that may cause your program to stop if not properly handled. | error    | "The user provided the wrong data type causing the Traceback to throw a TypeError exception." |

## Exceptions Are Python's Cry For Help

An exception is a type of _thing_ (we can say "data type") that holds information about an error that the program encounters. Exceptions hold data like specifically what error occured and which line of code caused it.

Python creates an exception whenever a syntax or runtime error occurs in a program. Python will then immediately try to stop the execution of the program and exit out of it. When an error happens, and we see details in the stack trace, we actually see details about the exception!

The act of creating an exception is often called **raising an exception.**

When an exception is raised, Python moves "up" through the stack of code execution. This act of the exception moving "up" is often called **throwing an exception** or **bubbling up.** We might imagine an exception raised in a deep layer of code getting thrown up through each layer above, eventually to the programmer's face.

Python raises exceptions because exceptions are Python's cry for help. Python only raises exceptions when some code says, "I can't do this! I can't go on!"

However, when Python surrenders and throws an exception, sometimes we can lend it a hand. While some exceptions really do represent irrecoverable conditions, others report situations that we might be able to handle so that Python can keep running our program normally!

Code that recognizes a thrown exception is often called **catching an exception.** Catching an exception and then handling the situation, setting things back in order, and making it possible to move on, is also often called **handling an exception.**

As we work with Python, we will encounter many types of exceptions. We will learn which kinds we tend to handle, and counterintuitively, which might actually be better to allow to crash our programs!

## Common Exception Types

| Exception Name    | When it occurs                                                          |
| ----------------- | ----------------------------------------------------------------------- |
| NameError         | A local or global name is not found.                                    |
| ZeroDivisionError | The second argument of a division or modulo operation is zero.          |
| OverflowError     | The result of an arithmetic operation is too large to be represented.   |
| SyntaxError       | The parser encounters a syntax error.                                   |
| TypeError         | An operation or function is applied to an object of inappropriate type. |
| KeyboardInterrupt | The user hits the interrupt key (normally Control-C or Delete).         |

## We Can Raise Exceptions

Python can raise exceptions under the hood... and other packages and tests can raise exceptions...

We can too! We use the `raise` keyword. We pair the `raise` keyword with the exception class name (type) that we want to report.

```python
x = -1
if x < 1:
    raise ValueError
```

When we run this code, we see the following output in the console:

```
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    raise ValueError
ValueError
```

Let's observe what our stack trace is telling us:

- There is a `ValueError` that stopped the code execution
- The line of code that caused this error is `raise ValueError`
- This line of code is in `"main.py"` on line 3

### Creating Error Messages

We can pass in our own error message when we raise an exception! If we pass in an error message, that message will be available to any exception handling code, which can provide additional details about the error.

```python
raise ZeroDivisionError('Tried to divide by zero flowers.')
```

When we run this code, we see the following output, which now has our message about flowers!

```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    raise ZeroDivisionError('Tried to divide by zero flowers.')
ZeroDivisionError: Tried to divide by zero flowers.
```

## We Can Handle Any Raised Exception

Crashes are annoying. Crashes interrupt our work and inconvenience users who run our software. But our programs don't run in isolation. We run software in a complicated environment, and sometimes things beyond our control go wrong. When this happens, crashing is sometimes the best thing to do!

But there are many cases where we can do something to fix a problematic situation before it becomes a catastrophe. What can we do to protect our program from crashes?

The first step is to review our logic, and see if there's a way to write it that won't raise errors. Additionally, Python lets us catch raised exceptions before they crash our program— and then handle them!

We use the `try ... except` syntax for this.

```python
try:
    any_number_of_python_lines_that_may_raise_an_error()
except ExampleError as error_as_a_variable:
    print(f"An exception occurred. Here are the error details: {error_as_a_variable}")
```

| Piece of Code             | Notes                                                                                                                                                                                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `try:`                    | This begins a _try-clause_. If any exception is raised by _any code_ executed inside the try-clause, the rest of the try-clause is skipped, and code execution moves to the `except` clause.                                                               |
| Body of the try-clause    | The try-clause should include all code that has the possibility of raising an exception that we want to handle. The try-clause is indented once from `try:`                                                                                                |
| `except`                  | A keyword that begins an _except-clause_. The except-clause will run if a matching exception is raised from the try-clause.                                                                                                                                |
| `ExampleError`            | **Replace this** with the type of exception that we are handling, such as `NameError` or `ZeroDivisionError`.                                                                                                                                              |
| `as`                      | A keyword that designates the caught exception (that matches the type of `ExampleError`) can be accessed as the local variable to the right.                                                                                                               |
| `error_as_a_variable`:    | **Replace this** with any valid variable name. This variable's value will be the exception data, and can be accessed inside of the except-clause. `err` is a common variable name. Don't forget the `:`!                                                   |
| Body of the except clause | The error clause should include code that needs to execute if an exception is raised. This code can be used for printing or logging details about `err`. More powerfully, this is where we can try handling the situation and helping the program move on. |

### !callout-info

## Error Specifications Are Optional

Technically, specifying the error type is optional. Specifying the local variable `err` is also optional. From the above syntax, we could omit `ExampleError as error_as_a_variable`, and it would still be valid code. Then, that except-clause would run if it catches _any_ exception. It's valuable to have the specificity and detail when handling exceptions, so this is a pattern we rarely see.

### !end-callout

### Walking Through an Example: Circumference

Consider this example. First, read through the code and its console output. Then, read through the explanation, and use it to trace the code.

```python
def calculate_circumference(radius):
    try:
        circumference = 2*3.14*radius
        print(f"Circumference of circle is: {circumference}")
        return circumference
    except TypeError as err:
        print(f"Calculation input has an incorrect data type, {err}.")


calculate_circumference("Some text that is definitely not a valid radius value.")

print("Notice how the program hasn't crashed. This is because exceptions change the flow of how programs execute rather than completely stop it.")
```

Running this code produces this console output:

```
Calculation input has an incorrect data type, can't multiply sequence by non-int of type 'float'.
Notice how the program hasn't crashed. This is because exceptions change the flow of how programs execute rather than completely stop it.
```

Here's a step-by-step explanation of how the code above runs:

1. First, the Python interpreter says "Okay, the function `calculate_circumference` is defined."
1. Then, the Python interpreter calls `calculate_circumference`.
1. We enter the try-clause
1. Then, the Python interpreter executes `circumference = 2*3.14*radius`. This line of code raises an exception.
1. We skip the rest of the try-clause, and then check if the exception is a `TypeError `.
1. The exception is a `TypeError`, so we enter the except-clause. There is a new variable `err`, whose value is the Exception raised.
1. Then, we print the exception with a message. We could do other stuff too, such as `return None`
1. Finally, we exit this whole thing.

### More Examples

For each example:

- Identify the function call that leads to the error condition, and describe what about it is problematic
- Identify what line of code inside the try-clause raises an error
- Observe what happens during each except-clause

1.
```python
def is_valid_int(input_num):
    try:
        x = int(input_num)
    except ValueError as error:
        print(f"{error}. Please enter a valid number.")


is_valid_int("Clearly not a valid int")
```

Output:

```
invalid literal for int() with base 10: 'Clearly not a valid int'. Please enter a valid number.
```

2.
```python
def enter_candy(candy_choice):
    candy_list = ["lollipops", "m&ms", "gummy bears"]
    try:
        print(f"Your candy choice is {candy_choice}")
        print(f"You selected {candy_list[candy_choice]}")
    except IndexError as error:
        print(f"A {error} was entered. Please enter 0, 1, or 2.")

enter_candy(9999)
```

Output:

```
Your candy choice is 9999
A list index out of range was entered. Please enter 0, 1, or 2.
```

### Handling Multiple Types of Exceptions

If we need to handle more than one kind of exception, we can add an infinite number of `except` clauses. Much like the `if..elif` statements, the raised exception will check if it matches one-at-a-time, starting from the top.

This example will run the `try` clause. If an exception is raised, it will check if the exception is a `ZeroDivisionError ` first. If it isn't, then it will check if it's `UnboundLocalError`. Finally, if it isn't `UnboundLocalError`, then it will check if it's `NameError`.

```python
def do_weird_number_math(apple):
    print("We're entering the do_weird_number_math function! Value of apple:", apple)

    try:
        if apple < 10:
            banana = apple / (apple - 3)

        print("Value of banana:", banana)
        print("Value of carrot:", carrot)
    except ZeroDivisionError as err:
        print(f"apple is 3, so it tried to divide by zero. {err}")
    except UnboundLocalError as err:
        print(f"apple is valid, but banana was never given a value, so we get an error. {err}")
    except NameError as err:
        print(f"We're trying to print carrot, but carrot is never defined before this. {err}")

    print("**************")

# The following line raises a ZeroDivisionError
do_weird_number_math(3)

# The following line raises an UnboundLocalError
do_weird_number_math(5555)

# This line raises a NameError
do_weird_number_math(8)
```

This code produces this console output:

```
We're entering the do_weird_number_math function! Value of apple: 3
apple is 3, so it tried to divide by zero. division by zero
**************
We're entering the do_weird_number_math function! Value of apple: 5555
apple is valid, but banana was never given a value, so we get an error. local variable 'banana' referenced before assignment
**************
We're entering the do_weird_number_math function! Value of apple: 8
Value of banana: 1.6
We're trying to print carrot, but carrot is never defined before this. name 'carrot' is not defined
**************
```

In our try-clause, different situations will raise different exceptions. Chaining except-clauses allows us to rescue them in specific ways.

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge
* type: ordering
* id: e45ab433-76f7-46b8-8203-92f7df1a7515
* title: try-except block
##### !question

Assume we have a function `process_list` which takes a list as an argument and performs an operation on it. If the function is passed something other than a list, it throws a `TypeError` exception. It may throw another type of exception if something else goes wrong.

Re-order the following lines of code into a working try-except block.

For this question, disregard proper indentation.

##### !end-question
##### !answer

1. `try:`
1. `process_list(my_list)`
1. `except TypeError:`
1. `print("Variable is not a list")`
1. `except:`
1. `print("Something else went wrong")`

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->


### !callout-secondary

## Multiple Exception Types with One Handler

Sometimes we have code that can trigger multiple exception types, but a single exception handler would be able to handle all of them. To catch multiple types with one handler, consider the following example syntax:

```python
try:
    # ...
except (ZeroDivisionError, UnboundLocalError, NameError) as err:
    print(f"Either a ZeroDivisionError, UnboundLocalError, or NameError happened. Details: {err}")
```

### !end-callout

## We Can Define Exceptions

If none of the built-in exception types are suitable for our code needs, what can we do? We can define custom exceptions, or exceptions with our own names and implementations.

We won't cover that material, but it's a cool piece of syntax! Follow your curiosity!

## Summary

Whether they're caused by programmers, insufficient memory, or user inputs, errors are bound to happen. Raising and using the `try...except` clause are great ways to make our code more robust by handling errors before they crash our program.

<!-- ## Check for Understanding -->

<!-- Use the questions in the checking exceptions in tests lessons, and reverse them, lol -->
