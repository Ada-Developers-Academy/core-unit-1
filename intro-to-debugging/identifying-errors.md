# Identifying Errors with the Stack Trace

## Introduction

When we call `print("Hello World")` in our Python code, the text `Hello World` gets printed somewhere: the terminal.

When we call `print(variable_that_doesnt_exist)` in our Python code, we also get output in the terminal. We get error messages.

Learning about what these error messages are and how to read them will help us debug!

## Learning Goals

- Define Stack Trace (Traceback in Python)
- Explain how to read error messages in a stack trace
- Use the stack trace to identify the line of code that causes an error

## Vocabulary and Synonyms

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---
Stack Trace | A report of the active stack frames at a certain point in time during the execution of a program. Reports error messages and details about that error | Traceback | "When debugging that error, we should check the stack trace to see what line of code caused it," "The stack trace is very long, but we can see what test called this method here."

## The Stack Trace Delivers Error Messages

The stack trace is a report of all of the code running at a specific point. The stack trace will report error messages and details about that error, if the program runs into a syntax or runtime error.

For example, let's consider the following situation:
1. A Python script named `main.py`
1. A terminal that runs that file

```python
# main.py

apples_quantity = 888      # this is line 3
basket_capacity = 0        # this is line 4
apple_basket_quantity = number_of_apples / basket_capacity    # this is line 5
```

```bash
$ python3 main.py
```

In that same terminal window, we should see the following stack trace:

```bash
Traceback (most recent call last):
  File "main.py", line 5, in <module>
    apple_basket_quantity = number_of_apples / basket_capacity # this is line 5
ZeroDivisionError: division by zero
```

### !callout-info
## Terminal
Let's consider briefly **where** we see error messages, and in general all output. Right now, when we run Python code from the terminal, we see the output in the terminal. That's because our computers and terminals have configured a [standard stream for output](https://en.wikipedia.org/wiki/Standard_streams), or an "output channel." The output channel, or standard stream for output, for the terminal is the terminal itself by default.

We introduce this idea briefly because one day, the standard stream may change. :)
### !end-callout

We introduce this idea briefly because one day, the standard stream may change. :)

### Python Calls It The Traceback

Python programmers will often refer to the stack trace as the Traceback. [Traceback](https://docs.python.org/3/library/traceback.html) is the name of the Python-specific module that helps find and format the stack trace.

Practically speaking, only use the term "Traceback" in a Python context, and freely use the term "stack trace" in any programming context.

### Running Code Is Through "The Stack"

As our programs get bigger, we'll find that our stack trace outputs may get really long.

<details>

  <summary>
    Skim through this example to appreciate how long this stack trace is
  </summary>

```python
  Traceback (most recent call last):
  File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 2464, in __call__
    return self.wsgi_app(environ, start_response)
  File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 2450, in wsgi_app
    response = self.handle_exception(e)
  File "/usr/local/lib/python3.8/site-packages/flask_cors/extension.py", line 165, in wrapped_function
    return cors_after_request(app.make_response(f(*args, **kwargs)))
  File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1867, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.8/site-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 2447, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1952, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.8/site-packages/flask_cors/extension.py", line 165, in wrapped_function
    return cors_after_request(app.make_response(f(*args, **kwargs)))
  File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1821, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.8/site-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1950, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1936, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/Users/user/flask-api/app.py", line 126, in get_apples
    888/0
ZeroDivisionError: division by zero
```
</details>

Why is there so much output?

When we run a Python program, our machines need to run a lot of subroutines, including subroutines that parse and interpret the Python program, and subroutines that allocate computer memory for variables.

The details of these subroutines are typically hidden in high-level programming languages like Python. This is so Python programmers can focus on application code development.

The call stack, sometimes called "the stack," is a data structure that stores information about all the subroutines that start or finish. When a subroutine starts, the call stack _pushes_ information about that onto the stack. When a subroutine finishes, the call stack _pops_ that information off the stack.

### !callout-info
## Fun Fact 
This is where the phrase "stack overflow" comes from!
### !end-callout

## Finding The Good Stuff: How to Read Error Messages

When we come across errors, we should take notes of three things:

1. What is the description of the error
2. What is the name of the error
3. What is the line of code that caused the error, its file name and line number

### Finding the Line of Code that Causes the Error

Because each error is different, the information in a stack trace will vary.

However, let's consider this small example:

```bash
Traceback (most recent call last):
  File "main.py", line 5, in <module>
    apple_basket_quantity = number_of_apples / basket_capacity # this is line 5
ZeroDivisionError: division by zero
```

| Piece of the Stack Trace | Notes
| --- | ---
`Traceback (most recent call last):` | This is the beginning of the Traceback (Stack trace) being formatted and printed.
`File "main.py", line 5, in <module>` | This is information about the line of code described in the next line. This describes what file that line of code is in, the line number, and what module it is in.
`apple_basket_quantity = number_of_apples / basket_capacity # this is line 5` | This is the line of code that caused an error, or contains code that caused an error. **Note that it is indented** one level from the above line.
`ZeroDivisionError: division by zero` | This is the name of the error, and a description of the error. **Note that it is not indented at all** to emphasize that this is the ultimate error.

From our example, we can answer our three questions about errors:
1. The description of the error is `division by zero`
2. The name of the error is `ZeroDivisionError`
3. The line of code that caused the error is in `main.py` on line 5

### Check the Bottom First

As our code bases get larger and include more Python subroutines, our Traceback output will get longer. **As a general rule, the ultimate error is listed at the bottom, and line of code that raised that error is at the bottom.**

It is helpful to read the stack trace from the bottom, going up.

## Summary

With our above example, notice that the stack trace did **not** tell us that `basket_capacity` is `0`, or why `basket_capacity` might be `0`.

It's up to developers to use the information from the stack trace just as one piece to debug. However, checking and reading the stack trace is **always** the first step to debugging.

## Check for Understanding

Given this stack trace output, what is the description of the error?

```bash
  File "main.py", line 5
    if apple_quantity < 1
                        ^
SyntaxError: invalid syntax
```

* invalid syntax
* missing colon
* invalid if syntax

Given this stack trace output, what is the name of the error?

```bash
  File "main.py", line 5
    if apple_quantity < 1
                        ^
SyntaxError: invalid syntax
```

* ZeroDivisionError
* A Syntax Error
* SyntaxError

Given this stack trace output, what is the location of the line of code that caused the error?

```bash
  File "main.py", line 5
    if apple_quantity < 1
                        ^
SyntaxError: invalid syntax
```

* `example.py`
* line 5
* `main.py`, line 5
