# Exception Handling

## Learning Goals

- Define exceptions
- Explain how to handle exceptions using try and except clauses

## Introduction

If you didn't know, the absolute worst-case scenario for software is a crash caused by a syntax or runtime error*. The software has gone to a state where the program can't do anything, the user can't do anything, and possibly the program can't even restart into a usable state!

If software fails for one person, it's likely that software is failing for _many_ people. All of these consequences result in **chaos**.

![giphy](https://user-images.githubusercontent.com/16619004/103056684-748d8a80-4552-11eb-8705-2429df508339.gif) Source: [Giphy](http://gph.is/2lENCEI)


\* = Actually, there are plenty of other more severe worst-case scenarios.

## Vocabulary and Synonyms

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---
| Exception | An event or error that may cause your program to stop if not properly handled. | error | "The user provided the wrong data type causing the Traceback to throw a TypeError exception." | 

## Exceptions Are Python's Cry For Help

### Python Raises Exceptions at Runtime


## Common Exception Types

Exception Name | When it occurs
--- | ---
NameError | Raised when a local or global name is not found. 
ZeroDivisionError | Raised when the second argument of a division or modulo operation is zero.
OverflowError | Raised when the result of an arithmetic operation is too large to be represented.
SyntaxError | Raised when the parser encounters a syntax error. 
TypeError | Raised when an operation or function is applied to an object of inappropriate type.
KeyboardInterrupt | Raised when the user hits the interrupt key (normally Control-C or Delete).

## We Can Raise Exceptions

Python can raise exceptions under the hood... and other packages and tests can raise exceptions...

We can too! We use the `raise` keyword. We pair the `raise` keyword with the exception class (type) that we are expecting.

```python

```

### !callout-info
## Creating Error Messages
We can actually pass in our own error message when we raise an exception! If we pass in an error message, the exception will use that string as its error description when needed.
### !end-callout

```python
raise ZeroDivisionError('Tried to divide by zero flowers.')
```


## We Can Rescue Any Raised Exception

Remember, the worst case scenario for any program and programmer is a crash, especially from a raised exception.

What can we do to protect our program from crashes? Of course, the first step is to review the logic, and see if there's a way to write it that won't raise errors. However, Python also lets us catch raised exceptions before it crashes our program-- and then handle them! We use the `try ... except` syntax for this.

```python

```

Try Clause
If any exception is raised inside the `try` clause, the rest of the `try` clause is skipped, and code execution moves to the `except` clause
Except Clause, with Exception Type next to it
A raised exception from the `try` clause will check if it matches the exception type next to the `except` keyword. If it matches, the `except` clause executes
`as var_name:`
Inside the `except` clause, it might be helpful to refer to the Exception itself. For example, we might want to `print` it. We use `as var_name` to say the exception is in the variable `var_name`. `var_name` can be any name.

Example:

```python

```

The code execution of the code above is as follows:

1. First, the Python interpreter says "Okay, the function `calculate_circumference` is defined."
1. Then, the Python interpreter calls `calculate_circumference`.
1. We enter the `try` clause
1. Then, the Python interpreter executes `circumference = 2*3.14*radius`. This line of code raises an exception.
1. We skip the rest of the `try` clause, and then check if the exception is a `TypeError `.
1. The exception is a `TypeError`, so we enter the `except` clause. There is a new variable `err`, whose value is the Exception raised.
1. Then, we print the exception with a message. We could do other stuff too!
1. Finally, we exit this whole thing.

More Examples:

```python

```

```python

```

### Handle Many Types of Exceptions

If we need to handle more than one kind of exception, we can add an infinite number of `except` clauses. Much like the `if..elif` statements, the raised exception will check if it matches one-at-a-time, starting from the top.

This example will run the `try` clause. If an exception is raised, it will check if the exception is a `ZeroDivisionError ` first. If it isn't, then it will check if it's `UnboundLocalError`. Finally, if it isn't `UnboundLocalError`, then it will check if it's `NameError`. 

```python

```

## We Can Define Exceptions

If none of the built-in functions don't suit the logic and context of our code, what can we do? We can define custom exceptions, or exceptions with our own names and implementations.

We won't cover that material, but it's a cool piece of syntax! Follow your curiosity!

## Summary
Whether they're caused by programmers, insufficient memory, or user inputs errors are bound to happen. Raising and using the `try..except` clause are great ways to make our code more robust by handling errors before they crash our program. 
## Check for Understanding
