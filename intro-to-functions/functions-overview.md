# Functions: Overview

## Introduction

When we write code, we are creating sets of instructions.

Imagine this pseudocode for making a [peanut butter and jelly sandwich](https://en.wikipedia.org/wiki/Peanut_butter_and_jelly_sandwich):

```
Get ingredients
Get materials
Spread peanut butter on bread
Spread jelly on bread
Put the bread together
```

Sometimes, these sets of instructions are small, and get repeated and remixed:

```
Spread peanut butter on bread
Spread jelly on bread
```

Sometimes they are large and abstract, and contain sets of instructions inside them:

```
Get ingredients
  Get peanut butter
  Get jelly
  Get bread
```

Sometimes, those sets of instructions have sets of instruction inside them!

```
Get ingredients
  Get peanut butter
    Check if you have peanut butter at home
    If you don't have peanut butter at home, go to the store and buy a jar of peanut butter
```

How do programmers work with this large amount of code? We can keep our code flexible and organized by using the power of functions!

Functions give developers a way to think about writing code and reusing code.

## Learning Goals

- Define and distinguish between the terms function, function signature, function body, and the return keyword
- Apply Single Responsibility Principle to functions

## Vocabulary

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---
| Function | Lines of code (1 or more) that are related, grouped together, and named. Once defined, these lines of code are reusable and can be called over and over again. | Method | "I defined a function," "I used a function," "I wrote a function"
| Invoking a function | "Invoking a function" means "make the lines of code inside of a function definition happen now." We can invoke a function any number of times (even infinitely!) | Calling a function, executing a function, evaluating a function, running a function, using a function | "I invoked the function named `print`," "I need to invoke `print` before the `if` statement," "I need to call that function at the end."
| Function definition, defining a function | How a function gets defined before it gets invoked | Function def, where the function is defined, a function you wrote | "I defined a function named `get_length`," "I defined the `get_length` function in this file," "I had bugs in my `get_length` function definition."

## What are Functions?

Functions are lines of code that:
  - hold related, sequential logic
  - usually have a name
  - don't do anything, until we tell it to do something
  - take in data
  - return a result
  - are reusable

### Functions Hold Logic

Functions hold lines of logic!

This logic is typically related to each other.

**Look at this example:** Here is a chunk of pseudocode that describes the logic for converting a temperature in degrees from celsius to fahrenheit:

```python
# Put the degrees in celsius in a variable named deg_celsius
# deg_celsius = 85
# Then, multiply deg_celsius by 1.8, then add 32. Put this in a variable named deg_fahrhenheit
# deg_fahrenheit = (deg_celsius * 1.8) + 32
```

A function can hold logic such as this.

### Functions Usually Have Names

Almost every function has a name.

This name is how we will use, define, and talk about the method.

**Look at this example:** A function that holds the logic for converting degrees from celsius to fahrenheit could have any of these names:

- `convert_celsius_to_fahrenheit`
- `convert_temperature`
- `convert_to_f`

Or anything else!

### Invoking, Executing, Running Functions

We define and name functions. The logic that a function holds **never** executes... **until we write code that invokes the function**, or says, "Hey! Actually do the code inside of the function!"

**Look at this example:** We can define a function named `convert_temperature` that holds the logic that converts degrees to fahrenheit. However, it won't actually convert any temperature until we write code to "do" the function.

```python
# Define a function named convert_temperature
    # Inside the function:
    # Put the degrees in celsius in a variable named deg_celsius
    # deg_celsius = 85
    # Then, multiply deg_celsius by 1.8, then add 32. Put this in a variable named deg_fahrhenheit
    # deg_fahrenheit = (deg_celsius * 1.8) + 32

# The function named convert_temperature doesn't do anything
# unless I say "make it happen" outside of the function
```

### Functions Take in Data

Functions "take in" data.

When we **run the function**, we can **pass** data **into** the function.

This function **takes in** data. Then, the function uses the data inside of its logic.

**Look at this example:** For a function named `convert_temperature`, that converts **any** temperature in celsius to fahrenheit, we want the function `convert_temperature` to **take in** one piece of data: a temperature in celsius.

### Functions Return a Result

Functions return a result from the function. The result is a piece of data.

When a function **runs** and executes its logic, we can tell functions to do something special: return a result _back_ to the line of code that ran the function in the first place.

**Look at this example:** For our function `convert_temperature`, we want the function to **return the result** of one piece of data: a temperature in fahrenheit.

### Functions Are Reusable

Functions are reusable, and written generically so they can apply to more than one situation.

Functions hold logic, and ideally, that logic applies to many different situations. We want our function logic to be reusable. When we **run** functions, we can run functions more than once; we can run them infinitely!

**Look at this example:** For a function named `convert_temperature`, we want our function to convert **any** degrees in celsius to fahrenheit.

We should be able to **reuse** the exact same `convert_temperature` function logic to convert:
- 85 degrees celsius to 185 degrees fahrenheit
- 25 degrees celsius to 75 degrees fahrenheit
- 0 degrees celsius to 32 degrees fahrenheit

## Single Responsibility Principle on Functions

[Single Responsibility Principle](https://en.wikipedia.org/wiki/Single-responsibility_principle) is a **programming value/best practice,** or a belief that many/most developers value.

The Single Responsibility Principle (SRP) states that a function should have one, and only one primary responsibility. This is to say, when developers describe the purpose of a function, ideally, the function isn't trying to do more than one thing.

Callout: What is "one thing"? This principle intentionally relies on abstraction, design, and programmer personal opinion, so the answer to this question will differ per function.

We can talk about a function's responsibility with the sentence, "The responsibility of this function is to..."

**Look at this example:** Our `convert_temperature` function is responsible for converting a temperature in celsius to a temperature in fahrhenheit.
