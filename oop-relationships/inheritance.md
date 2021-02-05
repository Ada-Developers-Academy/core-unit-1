# Inheritance

## Learning Goals

- Use Python syntax to create inheritance between two classes
- Recall that all objects inherit from Object
- Define overriding
- Use the super() function call in inheritance

## Introduction


## Vocabulary and Synonyms

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---
| Inheritance | A programming mechanism that allows classes to inherit attributes from another class. | ---      |"I'll use inheritance so the `Chocolate` class can inherit the `sugar serving` and `eat_in_one_sitting()` method from the `Candy` class. |
| Parent class | A class that contains variables and methods that can be inherited to other classes | base class, super class     |"`Candy` class is the parent class to `Chocolate` class." |
| Child class | A class that contains its own variables and methods but also inherits the variables and methods from a parent class | derived class, sub class     |"`Chocolate` class is the parent class to `Candy` class." |

## Syntax for Inheritance

To implement inheritance between two classes, we include the parent class in the definition of the child class:

```python
class ExampleChildClass(ExampleParentClass):
    pass
```

Compared to classes without explicit inheritance, this syntax:

- Adds `()`s to the right of the class name
- Puts the name of the parent class in the `()`s

Depending on how the project is organized, we may need to import the parent class so that Python is able to find the name. Like this:

```python
import ExampleParentClass

class ExampleChildClass(ExampleParentClass):
    pass
```

Recall that, unless the child class overrides it, the child class inherits the same implementation that the parent has for all methods and attributes, _including the `__init__` method_.

### Example: Button

Imagine that we have a `Button` class, which can be pressed. Also, we have a `SendPaymentButton` class, which is a `Button`. Our code could look like this:

```python
class Button:

    def __init__(self, label_text):
        print("I'm inside of Button's constructor!")
        self.label_text = label_text

    def on_button_press(self):
        print("I'm inside of Button's on_button_press method!")
```

```python
import Button

class SendPaymentButton(Button):
    pass
```

Imagine running this code in a file `main.py`:

```python
submit_btn = SendPaymentButton("Hello, World!")

print("This is submit_btn, our instance of SendPaymentButton:", submit_btn)

submit_btn.on_button_press()
```

Read through these observations, and then predict what the console output is from the above `main.py`.

- When we instantiate `SendPaymentButton`, we _must_ pass in `label_text`
    - `SendPaymentButton` did not define its own `__init__` method
    - Therefore, it looks to its parent class to see if it implements `__init__`
    - Because `Button` _does_ implement `__init__`, the child class will inherit it
- When we print `submit_btn`, our instance of `SendPaymentButton`, Python recognizes that it is type `SendPaymentButton`, not `Button`
- We can successfully invoke the instance method `on_button_press`
    - `SendPaymentButton` did not define `on_button_press`
    - `Button` _does_ define `on_button_press`
    - `SendPaymentButton` inherits `on_button_press` from the `Button` class

Let's look at some possible console output from the `main.py` above. Check to see if your predictions are in the right direction:

```
I'm inside of Button's constructor!
This is submit_btn, our instance of SendPaymentButton: <SendPaymentButton object at 0x10b8908e0>
I'm inside of Button's on_button_press method!
```

Take another minute to read through `main.py`. For each line, practice tracing the flow of code. Determine when each line gets printed to the console.

Tracing through this code should take us from `main.py`, then to the `SendPaymentButton` class, then to the `Button` class.

### Exercise: Pizza and FancyPizza

Create two classes, `Pizza` and `FancyPizza`.

- The `Pizza` class should...
    - define a constructor:
        - takes in `toppings` as a parameter
        - assigns an attribute named `toppings`
    - define an instance method `add_topping`:
        - takes in a `new_topping` parameter
        - appends `new_topping` to `toppings`

The `FancyPizza` class should...
    - inherit the exact same constructor from `Pizza`, which includes the `toppings` attribute
    - inherit the exact same `add_topping` method
    - define an additional instance method `get_fancy_first_topping`:
        - takes in no parameters
        - returns the string `f"Fancy {self.toppings[0]}"`
        - Example: if `toppings` is ["onions"], then this method returns `"Fancy onions"`


<!-- Question 1 -->

<!-- 

EXAMPLE IMPLEMENTATION

class Pizza:
    
    def __init__(self, toppings):
        self.toppings = toppings

    def add_topping(self, new_topping):
        self.toppings.append(new_topping)
        return new_topping

class FancyPizza(Pizza):

    def get_fancy_first_topping(self):
        return f"Fancy {self.toppings[0]}"



-->

<!--

EXAMPLE TESTS IN PYTEST


import pytest

def test_pizza():
    p = Pizza(["green peppers", "red peppers", "banana peppers"])
    assert len(p.toppings) is 3

    p.add_topping("mushrooms")

    assert len(p.toppings) is 4
    assert "mushrooms" in p.toppings

def test_fancy_pizza():
    fp = FancyPizza(["green onions", "red onions", "banana onions"])
    assert len(fp.toppings) is 3

    fp.add_topping("mushrooms")

    assert len(fp.toppings) is 4
    assert "mushrooms" in fp.toppings

    fancy_topping = fp.get_fancy_first_topping()

    assert fancy_topping == "Fancy green onions"


 -->

## Overriding Lets Us Replace Our Inheritance

If a child class needs to _replace_ the implementation of an inherited method, the child class can _override_ the method by redefining it with the same name.

```python
class ExampleParentClass:
    def example_instance_method(self):
        print("I'm inside of ExampleParentClass!")

class ExampleChildClass(ExampleParentClass):
    def example_instance_method(self):
        print("I'm inside of ExampleChildClass!")
```

Running this code...

```python
apple = ExampleParentClass()
apple.example_instance_method()

orange = ExampleChildClass()
orange.example_instance_method()
```

Produces this output:

```
I'm inside of ExampleParentClass!
I'm inside of ExampleChildClass!
```

Even though the child class inherits the parent class, the child and parent have different behaviors for `example_instance_method`. This is because the child class _overrode_ `example_instance_method` by redefining it.

### Exercise: Pizza Overriding

Continue the `Pizza` and `FancyPizza` classes.

- The `Pizza` class should implement the instance method `calculate_toppings_price`
    - takes no parameters
    - returns `0.75 * len(self.toppings)`

- The `FancyPizza` class should override that instance method
    - takes no parameters
    - returns `(2.50 * len(self.toppings)) + 5`

<!-- 

PLACEHOLDER

class Pizza:    
    def __init__(self, toppings):
        self.toppings = toppings

class FancyPizza(Pizza):
    pass



SOLUTION

class Pizza:
    
    def __init__(self, toppings):
        self.toppings = toppings

    def calculate_toppings_price(self):
        return 0.75 * len(self.toppings)

class FancyPizza(Pizza):

    def calculate_toppings_price(self):
        return (2.50 * len(self.toppings)) + 5

import pytest

def test_pizza():
    p = Pizza(["green peppers", "red peppers", "banana peppers"])

    toppings_price = p.calculate_toppings_price()

    assert toppings_price == pytest.approx(3.0)

def test_fancy_pizza():
    fp = FancyPizza(["green onions", "red onions", "banana onions"])

    toppings_price = fp.calculate_toppings_price()

    assert toppings_price == pytest.approx(15.0)
 -->


## Not Covered: `super()` and Multiple Inheritance

Python allows us to get a reference to any class's superclass with the special function `super()`. This would allow a child class to explicitly call things from the parent class's implementation, such as attributes or methods. The `super()` concept and syntax is out of scope for this lesson.

A majority of programming languages dictate that each class can only inherit from one other class; each class only has one parent class. Python supports multiple inheritance, or the ability for a class to inherit from more than one parent class. This concept and syntax is out of scope for this lesson.

As always, follow your curiosity!

## Check for Understanding
