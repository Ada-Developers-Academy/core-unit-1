# Invoking Functions

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=f3c374f1-0cf1-44f8-a5a8-acd3018b2ba0&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

## Learning Goals

- Demonstrate calling functions with and without arguments
- Use the return value in a function

## Introduction

A function is a reusable chunk of code. Every function is defined with a name and some logic. If in a given project, on a given line of code, we want to **execute** this logic and this reusable chunk of code, we need to **invoke** the function.

## Vocabulary and Synonyms

| Vocab               | Definition                                                                                                                                                       | Synonyms                                                                                              | How to Use in a Sentence                                                                                                                    |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Function            | Lines of code (1 or more) that are related, grouped together, and named. Once defined, these lines of code are reusable and can be called over and over again.   | -                                                                                                     | "I defined a function, " "I used a function, " "I wrote a function"                                                                         |
| Invoking a function | "Invoking a function" means "make the lines of code inside of a function definition happen now." We can invoke a function any number of times (even infinitely!) | Calling a function, executing a function, evaluating a function, running a function, using a function | "I invoked the function named `print` , " "I need to invoke `print` before the `if` statement, " "I need to call that function at the end." |
| Argument            | An argument is a piece of data delivered to a function when it's being invoked.                                                                                  | Parameter                                                                                             | "I passed in the argument `"orange"` ", "The function takes in two arguments"                                                               |
| Return value        | A return value is the piece of data that a function delivers to the code that invoked the function.                                                              | Return                                                                                                | "That function returned a dictionary, " "I need to use the return value of that function"                                                   |

## Every Function Has a Responsibility

Functions do things, and have a responsibility to do things when they are _invoked_.

We should fully understand the _responsibility_ of each function when we use it. Before using a function, we should be able to describe the following:

- the purpose of the function
- the data that _'goes into'_ the function
- the computations inside of the function
- the data that _'goes out'_ of the function

Python has defined a lot of functions for us to use, already. Let's look at some Python functions and their responsibilities.

| Name of function | Responsibility                                                                                                                                                                            |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `len`            | Based on the one given value, will calculate the length of the given value. The given value is typically either a string or list.                                                         |
| `print`          | Based on one given value, will display the given value to the "standard output" (like the console, terminal, bash, etc) as best it can.                                                   |
| `random.randint` | Based on two given values, generate a random integer in the range between the first given value and the second given value                                                                |
| `time.time`      | Calculates the number of seconds passed since [epoch. For Unix system, January 1, 1970, 00:00:00 at UTC is epoch (the point where time begins).](https://en.wikipedia.org/wiki/Unix_time) |

### !callout-info

## time and random are modules

Technically, `time.time` is a function named `time` inside a module `time` . Also, `random.randint` is a function named `randint` inside of a module named `random` . We won't worry about these details yet! What this means for us today is we will sometimes need these two lines of code at the top: `import random` and/or `import time`

### !end-callout

### !callout-info

## time.time and random.randint

Going forward, because technically `time` and `randint` are the names of the functions, and `time.time` and `random.randint` are how we must invoke them, we will notate it as such.

### !end-callout

## Invoke Functions with `function_name()`

Once we know a function's name and responsibility, we can invoke this function on a certain line of code. To do so, use this syntax:

```python
function_name()
```

... where `function_name` is replaced with the name of the function. We attach `()` to the right side of the function name.

Let's look at those Python functions and the syntax for how to invoke them.

| Name of function                       | Syntax to Invoke (With Zero Arguments) |
| -------------------------------------- | -------------------------------------- |
| `len`                                  | `len()`                                |
| `print`                                | `print()`                              |
| `randint` (inside the `random` module) | `random.randint()`                     |
| `time` (inside the `time` module)      | `time.time()`                          |

### Try It

Run this code, and see what it outputs.

```python
import time
time.time
```

Now, run this code, and observe the difference.

```python
import time
time.time()
```

`time.time()` (with `()` ) invokes the function, and gives us the number of seconds since epoch, fulfilling its responsibility. Without `()` , we are simply just acknowledging that `time.time` is a defined function.

## Functions Take In Arguments

Functions can "take in" 0 arguments, 1 argument, 2 arguments, 3 arguments, or more!

The `()` that we attached to the right of a name is actually how to invoke the function with _zero arguments._

To invoke a function with one or more arguments, we need to include the arguments **separated by commas** and **inside the `()` s.**

Let's look at those Python functions and the syntax for how to pass in arguments.

| Name of function | Line of code that invokes a function                 | Number of arguments passed in | Argument(s) passed in                           |
| ---------------- | ---------------------------------------------------- | ----------------------------- | ----------------------------------------------- |
| `len`            | `len(["Kelsea's Title", "Kelsea's Job Description])` | 1                             | `["Kelsea's Title", "Kelsea's Job Description]` |
| `print`          | `print("Garry's Models")`                            | 1                             | `"Garry's Models"`                              |
| `randint`        | `random.randint(0, 777)`                             | 2                             | `0` and `777`                                   |
| `time.time`      | `time.time()`                                        | 0                             | -                                               |

The number of arguments that a function accepts is determined by how it's defined. If we want to know how many arguments a function accepts, we should confirm through its documentation.

### Arguments are Positional

The arguments that we pass in to a function have a specific order, and the order matters.

- The correct order of arguments is **determined by whoever defined the function.**
- An incorrect order of arguments in a function is misusing the function, and will result in bugs/unexpected output.

#### Example with `random.randint`

Today, we've been working with functions defined by Python, so we'll find the correct order through Python documentation. Confirming with [this function's documentation](https://docs.python.org/3/library/random.html#random.randint), the function `random.randint` takes in two arguments: `a` and `b` :

> random.randint(a, b)

> Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

From the documentation, we should understand the following:

- The documentation calls the **first** argument `a`, and the **second** argument `b`. This is determined next to the name of the function, `random.randint(a, b)`
- The documentation says that the responsibility of this function relies on the logic of `a <= N <= b`. This means that the values of `a` should be the smallest number, and `b` should be the biggest number

When using the `randint` method, our smallest number should be positioned as the **first** argument, and our largest number should be positioned as the **second** argument. The output of this function will be a randomly generated integer between the values of a and b.

### Arguments Can Be Any Data Type

Arguments can be any data type:

- Strings
- Lists
- Dictionaries
- `None`
- Anything else!

Arguments can be:

- Literal values (such as `"apples"`)
- variables (such as `apples`, where `apples = "apples"` in a previous line of code)

In general, functions do not have rules about what _data type_ our _arguments_ are. However... considering the _responsibility_ of each function, arguments usually have an _implied_ expected data type.

We should rely on documentation, context clues, parameter names, and knowing the responsibility of a function, to infer what data type our arguments can or should be.

### Passing in the Wrong Number of Arguments

If we pass in the wrong number of arguments, we get errors, like this `TypeError` .

```bash
>>> len("Hello", "World")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: len() takes exactly one argument (2 given)
```

You can recreate the error here:

```python
len("Hello", "World")
```

Reading through our error messages, we should determine:

1. The type of error is `TypeError`
1. The details state `len() takes exactly one argument (2 given)`. This function takes in one argument, but we gave it two.
1. This error was traced to `line 1` from where this code was written.

To debug, we should...

1. re-run the code to make sure we can reproduce the error message
1. read the error message and see where the erroneous code is
1. find the line of code that calls this function
1. adjust how we call the function, with the proper number of arguments passed in

## Functions Return a Value Back to the Code that Invoked Them

Functions **_give back_** one value to the code that invoked the function. Often times, this value is the value that fulfills the function's responsibility.

The value that a function **gives back** to whoever called it is called its **return value**.

Return values can be any data type. They can even be `None` !

We can usually describe a return value by simply describing what it represents. Return values always have a _literal_ value after invoking a function, though.

Let's look at the return values for some functions we've observed, and some functions we can call.

| Name of function | Description of Return Value                            | Line of code that invokes a function                 | Arguments passed in                             | The literal Return Value |
| ---------------- | ------------------------------------------------------ | ---------------------------------------------------- | ----------------------------------------------- | ------------------------ |
| `len`            | length of the argument                                 | `len(["Kelsea's Title", "Kelsea's Job Description])` | `["Kelsea's Title", "Kelsea's Job Description]` | 2                        |
| `print`          | nothing                                                | `print("Garry's Models")`                            | `"Garry's Models"`                              | `None`                   |
| `randint`        | a random integer within the range of the two arguments | `random.randint(0, 777)`                             | `0` and `777`                                   | 419                      |
| `time`           | the number of seconds since epoch                      | `time.time()`                                        | -                                               | `1602720584.8029282`     |

### !callout-info

## print() returns None

`print` 's return value is always `None` ! This is intentional. The people who defined `print` (aka Python) said that the responsibility of `print` is to return `None` .

### !end-callout

How do we figure out what a return value is or should be?

The logic for determining the return value is inside of the function itself, so to figure out what the return value for any function is, we would need to do one of...

- look at how the function is defined
- read the function's documentation

### Calling Functions and Using Return Values is Our Job

When a function is invoked, the return value is used to pass back a value to the code that invoked the function.

Our logic will often rely on these return values of the functions we use.

**Setting Up a Pattern:** We will often...

1. _declare_ a variable
1. then invoke a function and _assign_ it to that variable on the right-hand side of the assignment operator (`=`).

Read these lines of code:

```python
kelseas_details = ["Kelsea's Title", "Kelsea's Job Description"]
details_length = len(kelseas_details)
```

Our Python interpreter reads this line of code from left to right like so:

1. On line 1, the _variable_ named `kelseas_details` is _assigned_ the value on the right: a _list_ with two elements: `"Kelsea's Title"` and `"Kelsea's Job Description"`
2. On line 2, the _value_ of the _variable_ named `details_length` is _assigned_ to the value on the right: `len(kelseas_details)`

   - What is the evaluated value of `len(kelseas_details)` ? Well, we are _invoking_ the function `len` , passing in one argument: `kelseas_details` . The **return value** of `len(kelseas_details)` is `2`

   - Therefore, the variable `details_length` is _assigned_ to the value `2` (the return value of `len(kelseas_details)` )

We should and will use those return values as:

- values we assign to other variables
- values that we pass to other functions
- values that we use in other data structures
- ... or more!

## Order Matters: Invoke Functions After It's Defined

We can only invoke functions after the function is defined.

### `NameError` on Undefined Functions

The function `time` is inside of the module named `time` , and the module (and thus the function) is undefined until we import the `time` module.

In this example, we _call_ the function `time.time()` after we load (and therefore define) `time` module with the line `import time` .

```python
import time
current_time = time.time()
print(current_time)
```

In this example, we call the function `time.time()` **before** we do `import time` .

```python
current_time = time.time()
import time
print(current_time)
```

We should get the following error:

```
Traceback (most recent call last):
  File "sandbox.py", line 1, in <module>
    current_time = time.time()
NameError: name 'time' is not defined
```

This error is Python telling us "Hey! On line 1, when we see `current_time = time.time()` , we see the name of _something_ called `'time'` , but I don't know what that is. I don't know anything with the name of `time` ."

To debug, we should...

1. Determine what line of code this error is occurring on (in this case, line 1)
1. Determine what name is giving us an error (in this case, `time`)
1. Determine how that name **should be** defined/loaded (in this case, the line `import time`)
1. Change our code so how we define this function is **before** where we call this function (in this case, moving the import line to above the function call)

## Check for Understanding

<!-- Question 1 -->

<!-- prettier-ignore-start -->
### !challenge

* type: checkbox
* id: ec392164-68de-4e37-a0c0-26ccd20f5cf6
* title: Invoking Synonyms

##### !question

Assume there is a function named `perform_show()` . Select all terms that mean invoking `perform_show()`

##### !end-question
##### !options

* Calling `perform_show()`
* Executing `perform_show()`
* Passing `perform_show()`
* Evaluating `perform_show()`

##### !end-options
##### !answer

* Calling `perform_show()`
* Executing `perform_show()`
* Evaluating `perform_show()`

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->

<!-- prettier-ignore-start -->
### !challenge

* type: multiple-choice
* id: a667287f-6322-490d-a5e3-fa32b8ef1d41
* title: Function Name

##### !question

``` python
performance = perform_show("Tyra's Magic Show", ["rabbit", "deck of cards"])`
```

What is the name of the function being called?

##### !end-question
##### !options

* performance
* perform_show
* "Tyra's Magic Show"
* ["rabbit", "deck of cards"]

##### !end-options
##### !answer

* perform_show

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 3 -->

<!-- prettier-ignore-start -->
### !challenge

* type: multiple-choice
* id: 5874f1be-0457-4d35-9f1e-f0876502eda1
* title: Function Arguments

##### !question

How many arguments are being passed into this function call?

``` python
performance = perform_show("Tyra's Magic Show", ["rabbit", "deck of cards"])
```

##### !end-question
##### !options

* 0
* 1
* 2
* 3

##### !end-options
##### !answer

* 2

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 4 -->

<!-- prettier-ignore-start -->
### !challenge

* type: multiple-choice
* id: 346c043f-969e-426d-afd1-15aafa603e45
* title: Functions and Variables

##### !question

What is `performance`?

``` python
performance = perform_show("Tyra's Magic Show", ["rabbit", "deck of cards"])
```

##### !end-question
##### !options

* A variable that invokes the `perform_show` function
* A variable that holds the `perform_show` function
* A variable that holds the return value of `perform_show("Tyra's Magic Show", ["rabbit", "deck of cards"])`
* A variable that is the `perform_show` function

##### !end-options
##### !answer

* A variable that holds the return value of `perform_show("Tyra's Magic Show", ["rabbit", "deck of cards"])`

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question Takeaway -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: qCXtbd
* title: Invoking Functions
##### !question

What was your biggest takeaway from this lesson? Feel free to answer in 1-2 sentences, draw a picture and describe it, or write a poem, an analogy, or a story.

##### !end-question
##### !placeholder

My biggest takeaway from this lesson is...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->
