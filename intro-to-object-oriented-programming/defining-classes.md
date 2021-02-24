# Defining Classes

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=5ce55619-e5a5-450d-b92b-acd9004ddf8d&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

## Learning Goals

- Define a class
- Apply the ideas of "state" and "behavior" in OOP to classes

## Vocabulary and Synonyms

| Vocab       | Definition                                                                                                                                                                                                                                                              | Synonyms    | How to Use in a Sentence                                                                                                                                                                  |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Constructor | A method used when creating objects. Usually initializes an object's attributes.                                                                                                                                                                                        | Initializer | "The constructor gets called every time we make a new `User` instance," "The constructor has `username` as a parameter, so we need to pass in a username whenever we initialize a `User`" |
| `__init__`  | Name of the method used by Python as the constructor. Pronounced "dunder init." One of many "dunder" (double underscore) methods that are reserved by Python for specific tasks. Because `__init__` is so common, the "dunder" is often dropped in spoken conversation. | -           | "If I want to set up attributes, in my class definition I need to make an `__init__` method," "If I misspell `__init__`, my constructor won't work"                                       |
| `self`      | The conventional name for a parameter that refers to an instance itself within a method of a class.                                                                                                                                                                     | -           | "We access attributes through `self`," "We assign attributes through `self`"                                                                                                              |

## When Do We Make a Class?

Classes represent _things_, _ideas_, _concepts_, or _other kinds of nouns_ that are relevant to a problem we want to solve.

Developers define classes after realizing that encapsulating (bundling together) state and behavior into one data type will make problem-solving easier.

Developers define classes any time! We might define new classes:

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

Classes can be extremely big or extremely small. But while there is no one right size for a class, we should remember that the bigger the class we write the harder it becomes for others to understand it.

Classes can also follow the [Single Responsibility Principle](https://en.wikipedia.org/wiki/Single-responsibility_principle). Before we create a class, we should do our best to determine:

1. What concept is this class responsible for representing?
1. What is a descriptive name for this class?
   - The name should be singular, e.g., `Album` _not_ `Albums`

## Defining Classes

Once we've determined a class name and its responsibility, we can define a class with this syntax:

```python
class ClassName:
    pass
```

| Piece of Code | Notes                                                                                                                                                                                                                                                                                         |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `class`       | A keyword that indicates that a class definition is beginning                                                                                                                                                                                                                                 |
| `ClassName`   | **Replace this** with the name of the class you're defining. The [PEP-8](https://www.python.org/dev/peps/pep-0008/#class-names) style guide prefers CapitalCamel case for class names. Class names should be singular nouns.                                                                  |
| `:`           | Don't forget the colon to indicate the beginning of the class body                                                                                                                                                                                                                            |
| Class body    | Code that describes the class definition. It must be indented one level deeper than the `class` keyword. The class body can include attributes and methods to describe state and behavior. Here we used the `pass` directive as a syntax placeholder, resulting in an empty class definition. |

<!-- Question 1 -->

<!-- prettier-ignore-start -->
### !challenge

* type: code-snippet
* language: python3.6
* id: mpLd4O
* title: Define an Empty Class

##### !question

Define a class named "Driver". It will be responsible for representing a vehicle driver in a ride-share app. The class body should be empty, i.e., use `pass`.

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

An implementation that meets the requirements is:

```python
class Driver:
    pass
```

##### !end-explanation

### !end-challenge
<!-- prettier-ignore-end -->

## The Constructor

We will eventually use class definitions to _instantiate_ objects (i.e., create instances).

A class definition with an empty class body (indicated by using `pass`) will make an empty object. It still defines a new data type.

For many problems, we want to create object instances that have a customized _initial state_, or that perform other initialization logic as soon as they are created. When we need this behavior, we can define a **specific method** named `__init__` (pronounced formally as "dunder init", or casually as "init") as part of the class body.

```python
class ClassName:

    def __init__(self):
        pass
```

The `__init__` method:

- Uses the exact same syntax as what we have already seen for defining regular functions
- Must be named `__init__`. Python looks for this exact name!
- Runs whenever we instantiate (create a new instance of) this class
- Contains any logic that should be run whenever we instantiate (create a new instance of) this class
- **Must always take at least one parameter**
  - The first parameter **always** represents the instance itself. Details below.
  - This parameter is typically named `self`
- Does not need to return anything (and should not return anything)

For example, consider this `Album` class, that will print a message whenever an `Album` is instantiated:

```python
class Album:

    def __init__(self):
        print("Hello! I print whenever a new Album is instantiated")
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

An implementation that works is this:

```python
class Driver:
    def __init__(self):
        print("This init method runs every time a new Driver is instantiated!")
```

Actually, this test will pass as long as there's a `Driver` class; it's challenging to write a test that verifies that the `__init__` method exists.

##### !end-explanation

### !end-challenge
<!-- prettier-ignore-end -->

### !callout-info

## "init" Is For Initialize

We can describe the `__init__` method as a "class constructor," "constructor method," or "initializer." These names are used for any special method that runs once whenever an object is instantiated.

### !end-callout

## In Classes, We Can Access `self`

In class definitions, in `__init__` and other instance methods, Python always passes in at least one argument: the instance itself.

Why does it do this?

Python wants to give instances the ability to reference itself with a variable. For example, as we write code to define the `Album` class, we may think about the "Dirty Computer" album. If we want to write code for "Dirty Computer" having its own state and behavior, we want a variable that represents "Dirty Computer" itself.

By convention, this parameter is almost always named `self`. Technically, the parameter could have any name, but most Pythonists stick with `self`.

`self` must **always** be the first parameter to any instance method. `__init__` is an instance method. We'll see more examples of this when exploring instance methods.

### !callout-info

## An Analogy for `self`: The Pronoun "I"

In the English language, there is the pronoun "I." Each person uses the pronoun "I" to describe themselves. However, "I" doesn't refer to the same person in every context. "I" always means the person who is saying it!

Exactly like that, the `self` parameter exists for every instance method. However, the value of `self` always means the current instance itself.

### !end-callout

## Attributes: Variables on `self`

Recall that **attributes** hold pieces of data relevant to a class. These pieces of data are attached to particular object instances. The collection of attributes attached to an object holds that instance's _state_. We can add to the state any attributes that we feel are necessary to capture the important features of a class.

We define the attributes of an object instance in the instance methods of a class definition, usually in `__init__`.

All attributes have names. The values of attributes will differ between instances.

Here are some examples of attributes that could exist on classes:

| Class  | Attribute                    | Instance Example                                                                      | Value of Attribute for Example |
| ------ | ---------------------------- | ------------------------------------------------------------------------------------- | ------------------------------ |
| Driver | Total amount of money earned | A driver with ID `DR0004`, 3 rides, who has earned $35, has an average rating of 4.67 | `35`                           |
| Album  | Release date                 | Dirty Computer                                                                        | `"2018"`                       |

Attributes look and act exactly like variables. But because they are attached to an object instance, they are accessed through `self`. The syntax for both reading and writing attributes uses the `self` parameter.

Read through this example. Then, review the following sections for additional details.

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
self.attribute_name = value_expression
```

... where `attribute_name` is the name of the attribute, and `value_expression` is any expression resulting in the value to be assigned to the attribute.

We can assign and re-assign attributes in the `__init__` method and inside any other instance method (details in another lesson!).

In the above example, we set the attribute `title` to the value `"Purple Rain"` with:

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

In the example above, we read the attribute `title` in the string interpolation expression, reproduced here:

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
1. Set `total_earnings` to `35`

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

In addition to `self`, the constructor can take in more parameters . Additional parameters in the constructor mean that we expect additional arguments whenever we instantiate a new object. We pass in the specific arguments for our new object when we make the instance!

```python
class ClassName:

    def __init__(self, apples, oranges, bananas, mangos):
        print("At the time of instantiation, we will")
        print("need to pass in values for apples, oranges, bananas, and mangos.")
        print("We can read parameters just like any other parameters/variables:")
        print(f"Look! {apples}, {oranges}, {bananas}, {mangos}")
```

We can use any valid function definition syntax in the signature of the constructor, such as making optional arguments!

### Common Pattern: Initialize Attributes

There is a common initialization pattern in OOP where we do the following:

1. Define the parameters needed for every instance of a class
2. Use those parameters to make instance attributes in the constructor method

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
- Inside of `__init__`, we set these attributes to the parameter values
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
1. Inside the constructor, assign the appropriate value to each attribute.

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
   - Check your indentation! Everything inside a class body must start at one level of indentation in from the `class` keyword.

<!-- No CFU; this lesson has several questions throughout the lesson -->
