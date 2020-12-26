# Defining Classes

## Learning Goals

- Define a class
- Apply the ideas of "state" and "behavior" in OOP to classes

## Vocabulary and Synonyms

| Vocab       | Definition                                                                                                                                       | Synonyms    | How to Use in a Sentence                                                                                                                                                                  |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Constructor | A special type of method that is used when creating objects. It does not give a `return` value. It usually initializes an object's attributes.   | Initializer | "The constructor gets called every time we make a new `User` instance," "The constructor has `username` as a parameter, so we need to pass in a username whenever we initialize a `User`" |
| `__init__`  | Python's specific method name for the constructor                                                                                                | -           | "If I want to set up attributes, in my class definition I need to make an `__init__` method," "If I mispell `__init__`, my constructor won't work"                                        |
| `self`      | The conventional name for a variable that refers to an instance itself. For instance methods in Python, this must always be the first parameter. | -           | "We access attributes through `self`," "We assign attributes through `self`"                                                                                                              |

## When Do We Make a Class?

Classes represent _things_, _ideas_, _concepts_, or _other kinds of nouns_ that are relevant to the problem at hand.

Developers define classes after realizing that encapsulating (organizing) state and behavior into one data type will make problem-solving easier.

Developers define classes any time:

- At the beginning of a project, after reading a problem statement
- In the middle of a project, after discovering that a deeper part of the problem needs a new class
- While refactoring, if seeing that attributes and methods can be better organized as a class

Some considerations for making a class:

- Is there a _concept_ that is used frequently in this project?
- Is there a major concept that holds a bunch of data?
- Is there a major concept that has certain behaviors?
- Will defining a class increase the readability?
- Will defining a class organize the code better?
- Can this class be reused in the future?

Classes can be extremely big or extremely small; there is no right size for a class.

Classes can also follow the [Single Responsibility Principle](https://en.wikipedia.org/wiki/Single-responsibility_principle). Before we create a class, we should do our best to determine:

1. What idea/concept is this class responsible for representing?
1. What is the best name for this class?
   - The name should be singular, ie `Album` _not_ Albums

## Defining Classes

Once we've determined a class name and its responsibility, we can define a class with this syntax:

```python
class ClassName:
    pass
```

| Piece of Code | Notes                                                                                                                                                                               |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `class`       | A keyword that indicates that a class definition is beginning                                                                                                                       |
| `ClassName`   | **Replace this** with the name of the class you're defining. The PEP-8 style guide prefers CapitalCamel case for class names. Class names should be singular nouns.                 |
| `:`           | Don't forget the colon to indicate the beginning of the class body                                                                                                                  |
| Class body    | Code that describes the class definition. It should be indented once into the class. The class body will include attributes and methods (functions) to describe state and behavior. |

<!-- Question 1 -->

<!-- prettier-ignore-start -->
### !challenge

* type: code-snippet
* language: python3.6
* id: mpLd4O
* title: Define an Empty Class

##### !question

Define a class named "Driver". It is responsible for representing a vehicle driver in a ride-share app. The class body should be empty, aka use `pass`

##### !end-question

##### !tests

```py
import unittest
from main import *

class TestDriverClass(unittest.TestCase):
  def test_driver_is_defined(self):
    self.assertTrue(Driver())
```

##### !end-tests

##### !explanation

The implementation we were expecting is this:

```python
class Driver:
    pass
```

##### !end-explanation

### !end-challenge
<!-- prettier-ignore-end -->

## The Constructor

We will eventually use class definitions to _instantiate_ objects (aka create instances).

A class definition with an empty class body will make an empty object (even if it's a new data type).

Many classes like to create objects with instances that have a customized, specific initial logic. In this situation, we may define a **special method** named `__init__()`, that will live inside the class definition.

```python
class ClassName:

    def __init__(self):
        pass
```

The `__init__` method:

- Uses the exact same syntax for defining a function
- Must be named `__init__`; Python looks for this exact name
- Runs whenever we instantiate ("use") this class
- Contains any logic that should be run whenever we instantiate ("use") this class
- **Must always take at least one parameter,** because it's special
  - The first parameter **always** represents an instance itself. Details below.
  - This parameter is typically named `self`
- Does not need to return anything (and should not return anything)

For example, consider this `Album` class, that will print a message whenever an `Album` is instantiated:

```python
class Album:

    def __init__(self):
        print("Hello! I print whenever a new Album is initialized")
```

<!-- Question 2 -->

<!-- prettier-ignore-start -->
### !challenge

* type: code-snippet
* language: python3.6
* id: Fshbd5
* title: Constructor method

##### !question

Replace `pass` and add in the `__init__` method for this `Driver` class. In the `__init__` method, print out the string `"This init method runs every time a new Driver is instantiated!"`

##### !end-question

##### !placeholder

```python
class Driver:
    pass
```

##### !end-placeholder

##### !tests

```py
import unittest
from main import *

class TestDriverClass(unittest.TestCase):
  def test_driver_is_defined(self):
    self.assertTrue(Driver())
```

##### !end-tests

#### !explanation

Actually, this test will pass as long as there's a `Driver` class; it's challenging to write a test that verifies that the `__init__` method exists.

##### !end-explanation

### !end-challenge
<!-- prettier-ignore-end -->

### !callout-info

## "init" Is For Initialize

We can describe the `__init__` method as a "class constructor," "constructor method," or "initializer." These names are used for any special method that runs once whenever an object is instantiated.

### !end-callout

## In Classes, We Can Access `self`

In class definitions, in the `__init__` method and other instance methods, we will need to use a _special_ variable named `self`.

Python wants to give instances the ability to reference itself with a variable. For example, as we write code to define the `Album` class, we may think about the "Dirty Computer" album. If we want to write code for "Dirty Computer" having its own state and behavior, we want a variable that represents "Dirty Computer" itself.

This variable is almost always named `self`. Technically, this variable can have any name, but most Pythonists will use `self`.

`self` must **always** be the first parameter to any instance method. `__init__` is an instance method. We'll see more examples of this when exploring instance methods.

### !callout-info

## An Analogy for `self`: The Pronoun "I"

In the English language, there is the pronoun "I." Each person uses the pronoun "I" to describe themselves. However, "I" doesn't point to the same person in every context; "I" always means the person who is saying it!

Exactly like that, the variable `self` will exist in every instance. However, the value of `self` will always mean the instance itself.

### !end-callout

## Attributes: Variables on `self`

Recall that **attributes** are pieces of data. In classes, they are pieces of data that become attached to each instance. Attributes maintain _state_. We want to write generic attributes in our class definitions.

All attributes have names. The values of attributes will differ between instances.

Here are some examples of attributes that could exist on classes:

| Class  | Attribute                    | Instance Example                                                                      | Value of Attribute for Example |
| ------ | ---------------------------- | ------------------------------------------------------------------------------------- | ------------------------------ |
| Driver | Total amount of money earned | A driver with ID `DR0004`, 3 rides, who has earned $35, has an average rating of 4.67 | `35`                           |
| Album  | Release date                 | Dirty Computer                                                                        | `"2018"`                       |

Because attributes have a close relationship to an instance, attributes will look and act exactly like variables... but they are assigned through `self`. Our syntax for reading and writing attributes will include `self`.

Read through this example. Then, read through the next sections to read about it in detail.

```python
class Album:

    def __init__(self):
        self.title = "Purple Rain"
        print(f"We can also read the value of the title attribute")
        print(f"by writing self.title: {self.title}")
```

When we make an instance of this class `Album`, it will print this:

```
We can also read the value of the title attribute
by writing self.title: Purple Rain
```

### Writing Attributes Inside of a Class

Inside of a class definition, we can assign values to an attribute with this syntax:

```python
self.attribute_name = new_value
```

... where `attribute_name` is the name of the attribute, and `new_value` is the new value.

We can assign and re-assign attributes in the `__init__` method and inside any other instance method (details in another lesson!).

In the above example, we assign the attribute `title` to `"Purple Rain"` with:

```python
self.title = "Purple Rain"
```

### Reading Attributes Inside of a Class

Inside of a class definition, we can read and use an attribute with this syntax:

```python
self.attribute_name
```

... where `attribute_name` is the name of the attribute. We call accessing a variable like this as using the _dot operator_.

We can read attributes in the `__init__` method and inside any other instance method.

In the above example, we read the attribute `title` when we interpolate it into a `print` statement:

```python
print(f"by writing self.title: {self.title}")
```

<!-- Question 3 -->

<!-- prettier-ignore-start -->
### !challenge

* type: code-snippet
* language: python3.6
* id: MqV7sl
* title: Attributes

##### !question

In this `Driver` class:

1. Create a constructor method, where `self` is the first parameter
1. Inside the constructor method, create an attribute named `total_earnings`
1. Assign `total_earnings` to `35`

##### !end-question

##### !placeholder

```py
class Driver:
    pass
```

##### !end-placeholder

##### !tests

```py
import unittest
from main import *

class TestDriverClass(unittest.TestCase):
  def test_driver_has_total_earnings_35(self):
    self.assertIs(Driver().total_earnings, 35)
```

##### !end-tests

##### !explanation

An implementation that works is this:

```python
class Driver:

    def __init__(self):
        self.total_earnings = 35
```

##### !end-explanation

### !end-challenge
<!-- prettier-ignore-end -->

## Revisiting the Constructor

We can combine attributes and constructors to make a really useful pattern.

### We Can Add More Parameters to the Constructor

The constructor can take in more parameters in addition to `self`. Additional parameters in the constructor will mean we'll expect arguments whenever we instantiate. We'll actually pass in real arguments at the time of making an instance!

```python
class ClassName:

    def __init__(self, apples, oranges, bananas, mangos):
        print("At the time of instantiation, we will")
        print("need to pass in values for apples, oranges, bananas, and mangos.")
        print("We can read parameters just like any other parameters/variables:")
        print(f"Look! {apples}, {oranges}, {bananas}, {mangos}")
```

We can use any valid syntax here, such as making optional arguments!

### Common Pattern: Initialize Attributes

A common pattern in OOP will use two things:

1. We'll define parameters needed for every instance of a class
2. We'll use those parameters and make them attributes in the constructor method

For our `Album` example, we might see this:

```python
class Album:

    def __init__(self, title, release_date, tracks):
        self.title = title
        self.release_date = release_date
        self.track_list = tracks
```

We should observe:

- Whenever we create an instance of `Album`, we'll need to pass in 3 things: `title`, `release_date`, and `tracks`
- Every instance of this class has three attributes: `title`, `release_date`, and `track_list`
  - We access these attributes with `self.title`, `self.release_date`, and `self.track_list`
- Inside of `__init__`, we assign these attributes to the parameters
- Note that there aren't rules about naming parameters:
  - The parameter `title` and the attribute `title` have the same name. The difference is that the parameter is a local variable, and the attribute is accessed with `self.title`
  - The parameter `tracks` and the attribute `track_list` do not have the same name.
- `self` must _still_ be the first parameter

<!-- Question 4 -->

<!-- prettier-ignore-start -->
### !challenge

* type: code-snippet
* language: python3.6
* id: wUph47
* title: Assign Attributes in the Constructor

##### !question

In this `Driver` class:

1. Create a constructor method with the following parameters in this exact order:
    - `self`
    - id
    - total earnings
    - list of trips
    - average rating
1. Inside the constructor, create the following attributes with these exact names:
    - `id`
    - `total_earnings`
    - `trips`
    - `avg_rating`
1. Inside the constructor, assign these attributes with the appropriate value

##### !end-question

##### !placeholder

```py
# Note: the word "id" may be highlighted because the Learn platform believes it's reserved
# This should not affect our code
class Driver:
    pass
```

##### !end-placeholder

##### !tests

```py
import unittest
from main import *

class TestDriverClass(unittest.TestCase):
  def test_driver_has_attributes(self):
    speed_racer = Driver("DR0004", 35, [], 4.67)
    self.assertIs(speed_racer.id, "DR0004")
    self.assertIs(speed_racer.total_earnings, 35)
    self.assertIs( len(speed_racer.trips), 0)
    self.assertIs(speed_racer.avg_rating, 4.67)

    racer_x = Driver("Racer X", 999, ["trip"], 10)
    self.assertIs(racer_x.id, "Racer X")
    self.assertIs(racer_x.total_earnings, 999)
    self.assertIs(len(racer_x.trips), 1)
    self.assertIs(racer_x.trips[0], "trip")
    self.assertIs(racer_x.avg_rating, 10)
```

##### !end-tests

##### !explanation

An implementation that works is this:

```python
class Driver:

    def __init__(self, id, total_earnings, trips, avg_rating):
        self.id = id
        self.total_earnings = total_earnings
        self.trips = trips
        self.avg_rating = avg_rating
```

##### !end-explanation

### !end-challenge
<!-- prettier-ignore-end -->

## Debugging Classes

Here are some common bugs to look out for when defining classes:

1. `NameError: name 'ExampleClassName' is not defined`
   - This suggests that the class named `ExampleClassName` hasn't been defined before trying to instantiate it
   - Check your class definition for typos
   - Check the line of code that instantiates this class for typos
   - Check that your class is defined before instantiating it
1. `AttributeError: 'ExampleClassName' object has no attribute 'missing_attribute_name'`
   - This suggests that we are trying to read an attribute from an instance of this class, but that attribute doesn't have a value
   - Check every place where the attribute is assigned for typos
   - Check the line of code that reads this attribute for typos
   - Ensure that the code uses `self` appropriately
   - Trace the code and ensure that the attribute is assigned before being read
1. `TypeError: __init__() takes 0 positional arguments but 1 was given`
   - This suggests that the constructor doesn't define the first parameter `self` (and Python automatically passes in a value for `self`)
   - Ensure that the `__init__` method takes in `self` as the first parameter
1. `IndentationError: expected an indented block`
   - This suggests that something in the class body is not indented, when it needs to be
   - Check your indentation! Everything inside a class body must start at one level of indentation in.

<!-- No CFU; this lesson has several questions throughout the lesson -->
