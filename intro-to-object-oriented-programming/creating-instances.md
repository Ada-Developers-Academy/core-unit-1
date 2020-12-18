# Creating Instances

## Learning Goals

- Define instances in Object-Oriented Programming
- Practice creating instances of classes in Python

## Introduction

Instances are concrete manifestations of classes.

## Vocabulary and Synonyms

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---

## Creating Instances

The following expression creates an instance of a class:

```python
ExampleClassName()
```

We take the exact class name and attach `()` to the right of it, as if invoking it like a function.

This tells Python to start a series of processes, such as running the `__init__` method. The expression turns into a new instance.

We can create multiple, different instances with the same syntax. The code below will make three different instances:

```python
ExampleClassName()
ExampleClassName()
ExampleClassName()
```

The following code will instantiate two different `Album`s, as long as the class `Album` is defined before it:

```python
Album()
Album()
```

### Pass in Required Params

The syntax above assumed that there were no required arguments to pass in.

The _constructor_ inside of the class determines what arguments are needed whenever we instantiate the class. During instantiation, we pass in arguments with the same syntax as calling a function.

Assuming that the `Album` class is defined like this...

```python
class Album:

    def __init__(self, title):
        self.title = title
```

We can make two separate instances of `Album` with the following code:

```python
Album("Dirty Computer")
Album("Purple Rain")
```

### !callout-info

## Don't Pass in `self`
**We do not need to pass in a value for the first `self` argument.** When we instantiate a class, Python will automatically pass in the correct value for `self`.

### !end-callout

It's worth it to recognize that, even if the arguments are the same, calling `Album(...)` will _always_ make another instance. The following code still makes _two_ instances of `Album`:

```python
Album("Dirty Computer")
Album("Dirty Computer")
```

### Storing in Variables

Just like with strings, lists, dictionaries, numbers, and other kinds of data, if we want to keep a reference to data, we should assign it to a variable.

```python
dirty_computer = Album("Dirty Computer")
purple_rain = Album("Purple Rain")
```

In the above example...

1. First, we make an instance of `Album` with the title `"Dirty Computer"` with `Album("Dirty Computer")`
1. Then, we store that instance in the variable `dirty_computer`
1. In the next line, we make a different instance of `Album` with `Album("Purple Rain")`
1. ... and we store it in the variable `purple_rain`

<!-- Question 1 -->

<!-- prettier-ignore-start -->
### !challenge

* type: code-snippet
* language: python3.6
* id: taH7s5
* title: Creating Instances

##### !question

Do not modify the `Driver` class.

Inside of the `get_specific_driver_instance` function:

- Make an instance of `Driver`. This instance should have an ID of `"DR0002"`.
- Return this instance

##### !end-question

##### !placeholder

```py
class Driver:
    
    def __init__(self, id):
        self.id = id

def get_specific_driver_instance():
    pass
```

##### !end-placeholder

##### !tests

```py
import unittest
from main import *

class TestDriverClass(unittest.TestCase):
  def test_get_specific_driver_instance(self):
    driver_DR0002 = get_specific_driver_instance()
    self.assertIs(driver_DR0002.id, "DR0002")
```

##### !end-tests

##### !explanation

An implementation that works is this:

```python
class Driver:

    def __init__(self, id):
        self.id = id


def get_specific_driver_instance():
    specific_driver_instance = Driver("DR0002")
    return specific_driver_instance
```

##### !end-explanation

### !end-challenge
<!-- prettier-ignore-end -->

### Reading Instances

We can read and use an instance of a class just like any other variable.

```python
name_of_instance
```

We can use this variable in a lot of different ways, such as printing it, or passing it into a function:

```python
class Album:

    def __init__(self, title):
        self.title = title

# After the class definition...

purple_rain = Album("Purple Rain")
print( type(purple_rain) )
```

When we run the above code, we'll get output similar to this:

```
<class '__main__.Album'>
```

We can call `type()` and pass in `purple_rain` in order to see what data type `purple_rain` is. It prints out `<class '__main__.Album'>`, which indicates that it's of class `Album` (located inside a namespace named `__main__`. This detail is less relevant).

### Reading Attributes

We can read an attribute from an instance using the dot-operator:

```python
example_instance.name_of_attribute
```

... where `example_instance` is an instance of a class, and `name_of_attribute` is the name of an attribute defined in that class.

To get the value of the `title` attribute from the album "Purple Rain," we need to...

1. Make an instance of Album with a title attribute
1. Read it

```python
purple_rain = Album("Purple Rain")
print( purple_rain.title )
```

This example outputs `Purple Rain`.

Of course, we can assign this value to yet another local variable:

```python
purple_rain = Album("Purple Rain")
album_title = purple_rain.title
print( album_title )
```

<!-- Question 2 -->

<!-- prettier-ignore-start -->
### !challenge

* type: code-snippet
* language: python3.6
* id: 2P7iOr
* title: Reading Attributes

##### !question

Do not modify the `Driver` class.

Inside of the `get_specific_second_trip` function:

- Make an instance of `Driver`. This instance should have an list of trips with this value: `["trip 1", "trip 2", "trip 3"]`.
- Return the second trip of this instance
    - Practice the syntax of accessing items from the attribute `trips`

##### !end-question

##### !placeholder

```py
class Driver:
    def __init__(self, trips):
        self.trips = trips

def get_specific_second_trip():
    pass
```

##### !end-placeholder

##### !tests

```py
import unittest
from main import *

class TestDriverClass(unittest.TestCase):
  def test_get_specific_driver_instance(self):
    second_trip = get_specific_second_trip()
    self.assertEqual(second_trip, "trip 2")
```

##### !end-tests

##### !explanation

An implementation that works is this:

```python
class Driver:
    def __init__(self, trips):
        self.trips = trips


def get_specific_second_trip():
    driver = Driver(["trip 1", "trip 2", "trip 3"])
    return driver.trips[1]
```

##### !end-explanation

### !end-challenge
<!-- prettier-ignore-end -->

### Re-assigning Attributes on Instances

We can re-assign the values of attributes on instances. We do so with the assignment operator:

```python
example_instance.attribute_name = new_attribute_value
```

When looking at our `Album` example:

```python
class Album:
    def __init__(self, title):
        self.title = title

album = Album("Purple Rain")
print( album.title )

album.title = "Dirty Computer"
print( album.title )
```

What will the output be? We should see that the `title` attribute of the instance on `album` goes from `"Purple Rain"` to `"Dirty Computer"`.

```
Purple Rain
Dirty Computer
```

## Multiple Instances in One Program

Not only do we want to make one or two `Album`s and `Driver`s, we may want to make hundreds of them, all within one program.

Understanding instances requires us to understand that instances will occupy separate places in memory, and will keep track of different values for attributes.

### Experiment: Printing Objects and Seeing Different IDs

Let's run a small experiment to prove this to ourselves:

Python gives each object a unique ID. Sometimes, this unique ID is the memory address for this object. Regardless, we can use this unique ID to differentiate objects from each other, because they will have different IDs.

Let's see what happens when we print (the ID of) one instance of `Album`...

```python
class Album:

    def __init__(self, title):
        self.title = title

purple_rain = Album("Purple Rain")
print(f"This is what happens when we print purple_rain: {purple_rain}")
```

The output `<__main__.Album object at 0x1020fcaf0>` is Python's default behavior for how to print and represent an `Album` object. The `0x1020fcaf0` is a unique identifier.

Now, observe this code. When looking at the output, we should count how many unique instances there are, how many unique IDs there are, and to see if any of these IDs change over the duration of the program.

```python
class Album:
    def __init__(self, title):
        self.title = title


purple_rain = Album("Purple Rain")
dirty_computer = Album("Dirty Computer")

another_album = Album("Purple Rain")

print(f"Purple Rain: {purple_rain}")
print(f"Another album named Purple Rain: {another_album}")
print(f"Dirty Computer: {dirty_computer}")
```

We should get output similar to this:

```
Purple Rain: <__main__.Album object at 0x10b28caf0>
Another album named Purple Rain: <__main__.Album object at 0x10b31c0a0>
Dirty Computer: <__main__.Album object at 0x10b28c850>
```

Note that even though two instances of `Album` both have the same title, `"Purple Rain"`, they are separate instances that have different IDs.

## Check for Understanding

