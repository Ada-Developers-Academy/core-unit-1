# Defining Functions

## Introduction

A function is a reusable chunk of code. Every function is defined with a name and some logic.

If, in a given project, we want to **define** our own reusable chunks of code, then we can define our own functions. Then, any code that has access to our functions can invoke them. To define a function, we must use specific Python syntax.

## Learning Goals

- Define a function (function signature, function body, return)
- Demonstrate calling functions with and without arguments/parameters

## Vocabulary and Synonyms

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---
| Function | Lines of code (1 or more) that are related, grouped together, and named. Once defined, these lines of code are reusable and can be called over and over again. | Method | "I defined a function," "I used a function," "I wrote a function"
| Function definition, defining a function | How a function gets defined before it gets invoked | Function def, where the function is defined, a function you wrote | "I defined a function named `get_length`," "I defined the `get_length` function in this file," "I had bugs in my `get_length` function definition."
| Function Signature | A piece of syntax. A part of the function definition that determines function name and the parameter list | Method signature | "We can read the name from the function signature," "The function signature tells us what parameters there are."
| Parameter | The name of an expected argument for this function. This parameter name is the name of the local variable that will hold an argument value. Parameters and arguments at the time of function call are mapped positionally. | Argument. Param. What is passed into a function. | "This function has one parameter named `items`," "There are 3 parameters for this function," "The function doesn't take any parameters"

## Every Function Has a Responsibility

Remember, functions do things, and have a responsibility to do certain things when they are called.

Before we create a function, we should do our best to determine:

1. What is the kind of logic you want to put into a function?
    - What is this function _responsible for doing_?
1. What is the best name for this function? 
    - Ideally, the name of the function implies the responsibility of this function.
1. What kind of arguments should the function take in? 
    - How many arguments?
1. What one piece of data should the function return? 
    - What is its data type, and what does it represent?

For example, let's look at `len`:
- The responsibility of the `len` function is to return the length of a given value
- Its name `len` implies "get the length of the argument." Other good names include `length`, `get_length`, `calculate_length`.
- `len` should take in something with a length, like a string or list. It should take in one and only one argument.
- `len` should return an integer that represents the length of the argument.

### Considerations for Creating a Function

Sometimes, we make functions because we need to, because someone asks us to, because the requirements or tests say so, because a library or tool we're using forces us to.

Sometimes, we make functions because it makes our code more organized, readable, flexible, and higher quality.

Sometimes, making too many functions increases complexity in our code!

How should we consider creating a function?

Some considerations for creating a function:

- Will creating a function reduce the repetition in my code?
  - Is there a chunk of code that gets repeated over and over and over again?
- Will creating a function here increase the readability of this code? 
  - Is this chunk of code too complex or specialized, and needs a name?
- Will creating a function here better the organization of this code? 
  - Will my code be easier to navigate with this function?
- Can this function be reused in the future? 
  - Will future developers also benefit from this function, and not just me?

In general, the wisdom of when to create functions comes with time. As learners, we will have a bias towards creating and writing functions freely as practice.

## Syntax for Defining a Function

We must follow specific Python syntax to define a function. The syntax to create a function definition has two parts:

1. Function Signature
2. Function Body

## Define Name and Parameters in Function Signature

The first part of a function definition is the function signature. The function signature defines three things about the function:

1. That it's a function
2. The name of the function
3. The parameters of the function

The function signature is one line of code:
```python
def function_name(apples, oranges):
```

Read this table as it describes each piece of code in the function signature from left-to-right:

| Piece of Code | Notes
| --- | ---
| `def` |`def` is a special keyword in Python. Python interpreters read `def` and go "Hey! I'm beginning to define a function!", and reads the rest of the line as a function definition.
| `function_name` | **Replace this** part with the name of the function you are defining.
| `( ... )` | These round parentheses contain the parameter list. Ensure that it's inbetween the function name and colon(`:`)! Ensure that there is an ending `)`!
| `apples, oranges` | This is the function's parameter list. **Replace this!** Arguments named inside of a function signature are technincally called **parameters.** Here is a comma-separated list of the parameters of this function. There can be 0 parameters, in which case the parens would be empty, and the method signature would look like `def function_name():`
| `:` | This colon ends the function signature, and begins the function body. It's easy to not remember this colon!

Let's look at some examples of different function signatures:

```python
def sing_happy_birthday_to_everyone():
```

```python
def sing_happy_birthday(name):
```

```python
def calculate_bill(items, sales_tax, tip_percentage):
```

```python
def add(first_num, second_num):
```

```python
def len(s):
```

Callout: The parameter name `s` isn't a very descriptive one. Whatever you imagined `s` meaning... you're wrong! The argument `s` may be a string, byte, tuple, list, range, dictionary, set, or frozen set.

### More About Parameters

For every argument we want to pass into this function when we call it, we should define a parameter in the function signature.

Each parameter is a variable name. We can name each parameter anything we would name a variable... So our best parameter names are descriptive and readable.

This is where functions define the **position** of their parameters.

### Naming Conventions for Naming Your Functions

[PEP-8 (Style Guide for Python Code)](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names) describes the following for naming functions:

- lowercase
- words separated by underscores to help with readability

Tips:

- Since functions often _do_ things, it helps to name your functions starting with _verbs_
- Try to name things to imply meaning and how to use the function to others.


Short answer question: Look at this function signature.

```python
def calculate_bill(items, sales_tax, tip_percentage):
```

Based on the function signature, are you able to tell or predict:
- That it is a function? 
  - How are you able to tell?
- The name of the function?
- What the responsibility of this function is? 
  - How are you able to predict?
- How many parameters it takes in? 
  - How are you able to tell?
- Answer these questions for all three parameters:
  - What is its name? 
  - What is its implied meaning? 
  - What is its implied data type? 
  - How are you able to predict?


## Function Bodies: Python Logic Still Applies

The part after the function signature, and the second and final part of the function definition, is the function body. We use the function body to define the lines of code to execute when the function is called.

A function body can one line of code, or it can be 10000 lines of code.

The function body syntax has three things rules to keep in mind:

1. All lines of code inside a **function body must start at one deeper indentation level compared to the function signature.**
    - The function body ends when the indentation level returns back to the function signature.
1. All Python logic and syntax still applies. When this function is invoked, the code in the function body executes.
1. Every function definition defines a new level of variable scope. Variables declared in the function body can only be read and re-assigned inside the same function body. These variables are **local variables** that are **scoped** to this function.
    - **Parameters are local variables that can be read in the function body.**
    - All other normal Python syntax applies!
1. We optionally define a function's return value in the function body

Let's learn more details about parameters and return values, and then read some example function bodies.

## Parameters Are Variables We Can Read; Arguments Determine Their Values.

Every parameter is the name of a variable we can read in the function body.

**The value of this variable is the value that's passed in as an argument,** at the time of invoking the function.

Observe this function signature. Note its parameter list...
```python
def sing_happy_birthday(name):
```

And this line of code that invokes the function. Note its argument that it passed in. What is its data type and value?
```python
sing_happy_birthday("Aaisha")
```

Now finally, look at the full function definition:
```python
def sing_happy_birthday(name):
    print("Happy birthday to you...")
    print("Happy birthday to you...!")
    print(f"Happy birthday, dear {name}")
    print("Happy birthday to you!")
```

When our code runs, and it gets to the line that invokes the `sing_happy_birthday`, it passes in the argument `"Aaisha"`, which is a string.

This argument is the first and only argument, so it maps onto the parameter list as the first and only parameter, `name`. **The parameter `name` is given the value of the argument `"Aaisha"`.**

**Multiple arguments and parameters are mapped positionally.** The value of the first argument becomes the value of the first parameter. The value of the second argument becomes the second parameter, and so on.

Observe:

```python
def add(a, b):
    sum = a + b
    print(f"{a} + {b} = {sum}")
```

```python
add(15, 38)
```

The argument `15` is positionally first, and gets mapped to become the value of `a`. The argument `38` gets mapped to become the value of `b`.

### Exercise

Run this code to see what prints out as the value of. Change the arguments of the function call, and observe that the value of the variable in the function body reflects this change.

```python
def add(a, b):
    sum = a + b
    print(f"{a} + {b} = {sum}")

add(15, 38)
```

## Define Return Values with `return`

We define the return value of a function by writing a **return statement** in a function body. There are three rules to creating a return statement:

1. Syntax: use the keyword `return`, followed by expression or value to return
2. We can only return one value from a function every time it is invoked
3. When our program reaches a `return` statement, it will **end and exit the current function call**

### Syntax to Return Statements

The syntax to a return statement is this:
```python
return some_variable_or_expression_that_holds_the_return_value
```

Here, `return` is a keyword, followed by some variable or expression to return.

The return statement fits into a function body and gets its own separate line:
```python
def add(a, b):
    sum = a + b
    print(f"{a} + {b} = {sum}")
    return sum
```

In this example, the `add` function is returning the value of the variable `sum`.

### Return Statements End a Function Call

Return statements **always** end and exit a function call. When a program reaches a return statement, it will **immediately** take the return value, and return back to the line of code that invoked the function.

![Monopoly Card that reads "ADVANCE TO GO (COLLECT $200)"](assets/defining-functions-return-monopoly.jpg)

**Here's a Metaphor:** The `return` statement is like playing Monopoly, and getting the card that says "Advance to GO (Collect $200)". It means that the program should **immediately** pick up its bags (and the return value!) and head back to the code that invoked the function. **Don't even bother looking at the rest of the function!**

Read and run the code below to understand how `return` statements exit a function call, and that the rest of the function does not execute.

```python
def is_number_odd(num, message):
    if num % 2 != 0:
        print(f"The number passed in ({num}) is odd!")
        return True
    print(message)
    return False

is_number_odd(5, "This message will never print, because 5 is odd, and the function will return before printing message")
is_number_odd(8, "This message will print, because the function does not hit a return statement before printing this message")
```

## Example Function Bodies (with their signatures)

Function bodies can be short.
```python
def add(a, b):
    return a + b
```

Function bodies can be long.
```python
def add(a, b):
    print("Nothing could stop me from making this function a bazillion lines long!")
    print("Wow!")
    print("Wow! Wow!")
    print("Wow! Wow! Wow!")
    print("Wow! Wow!")
    print("Wow!")
    return a + b
```

Function bodies can read their parameters and use them like variables. They can use these variables and determine a return value.
```python
def add(a, b):
    doubled_a = a * 2
    smaller_b = b - 1
    sum = a + b
    print(f"Just for fun, I can print and use my variables {doubled_a} and {smaller_b}")
    return sum
```

Functions can have nested logic, and conditional return values.
```python
def add(a, b):
    if a < 0:
        print("I only want to add if a is greater than zero! I'll return false instead.")
        return false
    elif b == a:
        print("Did you know that a and b are the same value?")
    elif a % 2 == 0:
        print("Did you know that a is an even number?")
        if b % 2 == 0:
            print("Did you know that b is also an even number?!?!?!?")
            print("Jackpot!")
            return 777

    return a + b
```

Function bodies can choose to not return anything, and will instead return `None`.
```python
def add(a, b):
    print("I don't need to return anything.")
    print("If I don't, I'll return None automatically.")
    print("Instead, I'll just print some addition.")
    print(a + b)
    print("Great!")
    print("I did my job.")
    print("I'll get going now.")
```

### Functions With an Empty Body with `pass`

The `pass` statement is Python statement that executes no code. For example:

```python
def calculate_bill(items, sales_tax, tip_percentage):
    pass
```

[This is useful when we developers want to write function signatures that don't do anything at that moment](https://en.wikipedia.org/wiki/Method_stub), but Python syntax requires function bodies to be at least one line.

## Calling Your Functions In Your Python Code

Now that we can define functions, we can apply our knowledge about invoking functions to them!

Remember, invoking a function means:
- Knowing the function's name
- Knowing the function's parameters, and what arguments we want to pass into them
- Knowing the syntax to invoke the function: `()`!

```python
def sing_happy_birthday(name):
    print("Happy birthday to you...")
    print("Happy birthday to you...!")
    print(f"Happy birthday, dear {name}")
    print("Happy birthday to you!")

sing_happy_birthday("Melinda")
sing_happy_birthday("Kerry")
```

### Order Still Matters

Order still matters. We cannot invoke a function before our Python interpreter knows that it's defined.

Predict: What error we will see and why we will see it?

```python
sing_happy_birthday("Melinda")
sing_happy_birthday("Kerry")

def sing_happy_birthday(name):
    print("Happy birthday to you")
    print("Happy birthday to you")
    print(f"Happy birthday, dear {name}")
    print("Happy birthday to you")
```

Answer: We will get `NameError: name 'sing_happy_birthday' is not defined` because we try to invoke the `sing_happy_birthday` function before it's defined.

### Functions Can Invoke Other Functions

Code inside our function bodies can invoke other functions! (We've been calling the `print` function inside our functions quite a lot already.)

The rules about Python logic and functions logic still apply.

Reading and tracing this code takes patience and practice, and gets a lot easier over time!

```python
def sing_birthday_line():
    print("Happy birthday to you")

def sing_birthday_song(name):
    sing_birthday_line()
    sing_birthday_line()
    print(f"Happy birthday, dear {name}")
    sing_birthday_line()

sing_happy_birthday("Destiny")
```

### Making Sure Your Function Works

How do you know that your function works correctly, there are no syntax errors, and it produces the right results?

Every time we define a function, it will be healthy to ask:
- How can I make sure this function is doing the right thing?
- How can I make sure this function is giving back the right return value?
- What arguments should I pass in to get certain return values?

For the `sing_happy_birthday(name)` function, I could invoke this function with my name (or loved one) after I define it, and see what it prints out the birthday song I expect. 🎶

## Summary

- When we define our own functions, we can consider its responsibility
    - What should it take in?
    - What should it do?
    - What should it return?
- Function definitions have two parts: function signature and function body
- Function signatures define three parts:
    - Syntax to prove that it's a function: `def`, `():`
    - Function name
    - Parameter list
- We can invoke any function after it's defined

## Check for Understanding

Which of these has correct syntax in its function signature _and_ its function body?

```python
def convert_to_fahrenheit(deg_celsius)
    result = (deg_celsius * 1.8) + 32
    return result
```

```python
def convert_to_fahrenheit():
    result = (deg_celsius * 1.8) + 32
    return result
```

```python
def convert_to_fahrenheit(deg_celsius):
result = (deg_celsius * 1.8) + 32
return result
```

```python
def convert_to_fahrenheit(deg_celsius):
    result = (deg_celsius * 1.8) + 32
    return result
```
