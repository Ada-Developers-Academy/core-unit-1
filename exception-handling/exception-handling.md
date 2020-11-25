# Exception Handling

## Learning Goals

- Define exceptions
- Explain how to handle exceptions using try and except clauses

## Introduction

If you didn't know, the absolute worst-case scenario for software is a crash caused by a syntax or runtime error*. The software has gone to a state where the program can't do anything, the user can't do anything, and possibly the program can't even restart into a usable state!

If software fails for one person, it's likely that software is failing for _many_ people. All of these consequences result in 

\* = Actually, there are plenty of other more severe worst-case scenarios.

## Vocabulary and Synonyms

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---

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

callout:
We can actually pass in our own error message when we raise an exception! If we pass in an error message, the exception will use that string as its error description when needed.

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

1. First, the Python interpreter says "Okay, the function ` ` is defined."
1. Then, the Python interpreter calls ` `
1. We enter the `try` clause
1. Then, the Python interpreter executes ` `. This line of code raises an exception
1. We skip the rest of the `try` clause, and then check if the exception is a ` `
1. The exception is a ` `, so we enter the `except` clause. There is a new variable ` `, whose value is the Exception raised.
1. Then, we print the exception with a message. We could do other stuff too!
1. Finally, we exit this whole thing.

More Examples:

```python

```

```python

```

### Handle Many Types of Exceptions

If we need to handle more than one kind of exception, we can add an infinite number of `except` clauses. Much like the `if..elif` statements, the raised exception will check if it matches one-at-a-time, starting from the top.

This example will run the `try` clause. If an exception is raised, it will check if the exception is a ` ` first. If it isn't, then it will check if it's ` `. Finally, if it isn't ` `, then it will check if it's ` `. 

```python

```

## We Can Define Exceptions

If none of the built-in functions don't suit the logic and context of our code, what can we do? We can define custom exceptions, or exceptions with our own names and implementations.

We won't cover that material, but it's a cool piece of syntax! Follow your curiosity!

## Summary

## Check for Understanding

