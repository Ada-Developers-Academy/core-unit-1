# Practice: OOP Relationships

## Directions

Complete all questions below.

## Practice

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: 31f651e3-aa01-47f4-8e02-ece744f35515
* title: OOP Relationships
##### !question
Dino's Donut store is creating an online store using OOP. Dino has two classes: `DonutStore` and `Donuts`.

`DonutStore` can display donuts and provide images of each donut from the list of several instances of the `Donut` class.

Select the option that best describes this relationship.
##### !end-question
##### !options

* Composition
* Inheritance
* Composite

##### !end-options
##### !answer

* Composition

##### !end-answer
### !end-challenge
<!--prettier-ignore-end -->

<!-- Question 2 -->
<!-- prettier-ignore-start -->
### !challenge
* type: checkbox
* id: 8Mppv3
* title: Composition
##### !question
"Ada Bank" is a mobile app for users to keep track of their banking accounts. An `AccountSummary` class is responsible for displaying balances from a user's `SavingsAccount` and `CreditCardAccount`. Select the option(s) that accurately describe these relationships.
##### !end-question
##### !options
* `AccountSummary` is the parent class, while `Savings Account` and `Credit Card Account` are child classes
* `AccountSummary` has-a `SavingsAccount`
* `AccountSummary` has-a `CreditCardAccount`
* `SavingsAccount` and `CreditCardAccount` are component classes while `AccountSummary` is the composite class
##### !end-options

##### !answer
* `AccountSummary` has-a `SavingsAccount`
* `AccountSummary` has-a `CreditCardAccount`
* `SavingsAccount` and `CreditCardAccount` are component classes while `AccountSummary` is the composite class
##### !end-answer
### !end-challenge
<!--prettier-ignore-end -->

<!-- Question 3 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: 0375c3e0-7e50-49b4-bbbd-2d58951876c1
* title: Inheritance
##### !question
Imagine we are creating a virtual petting zoo named "Ada Animals" ("Adanimals" for short).

We have two classes so far: `Mammal` and `Bear`.

Select the option that best describes the parent-child relationship between the two classes.
##### !end-question
##### !options
* `Bear` inherits methods from `Mammal`.
* `Bear` inherits variables and methods from `Mammal`
* `Mammal` inherits variables and methods from `Bear`
##### !end-options
##### !answer
* `Bear` inherits variables and methods from `Mammal`
##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 4 -->
<!-- prettier-ignore-start -->
### !challenge
* type: checkbox
* id: 9247804e-3ef4-4995-b285-693d74dfdd04
* title: Inheritance
##### !question

Provided this code snippet, select the option that best describes how inheritance works between the `Bear` and `Mammal` class.

``` Python
class Mammal:
    def __init__(self, name, region):
        self.name = name
        self.region = region

    def make_noise():
        print("AHHHHHHH")

class Bear(Mammal):
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def make_appearance():
        print("ʕ •ᴥ• ʔ")
```
##### !end-question

##### !options
* `Bear` will inherit `name`, `region`, and `make_appearance()` from `Mammal`.
* `Mammal` will inherit `color`, `size`, and `make_appearance()` from `Mammal`.
* `Bear` will inherit `name`, `region`, and `make_noise()` from `Mammal`.
##### !end-options

##### !answer
* `Bear` will inherit `name`, `region`, and `make_noise()` from `Mammal`.
##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 5 -->
<!-- prettier-ignore-start -->
### !challenge
* type: checkbox
* id: 3963ffe6-78b6-47cd-8267-a4ff80ed0f47
* title: Inheritance

##### !question
Select the option that would generate the output:

```
ʕ •ᴥ• ʔ
ROOAAAR!!
```
##### !end-question
##### !options
* 
```python
class Mammal:
    def __init__(self, name, region):
        self.name = name
        self.region = region

    def make_noise(self):
        return "AHHHHHHH"

class Bear(Mammal):
    def make_appearance(self):
        return "ʕ •ᴥ• ʔ"

bear = Bear("bear", "wa")
print(bear.make_appearance())
print(bear.make_noise())
```

* 
```python
class Mammal:
    def __init__(self, name, region):
        self.name = name
        self.region = region

    def make_noise(self):
        return "AHHHHHHH"

class Bear(Mammal):
    def make_appearance(self):
        return "ʕ •ᴥ• ʔ"

    def make_noise(self):
        return "ROOAAAR!!"

bear = Bear("bear", "wa")
print(bear.make_appearance())
print(bear.make_noise())
```
* 
```python
class Mammal:
    def __init__(self, name, region):
        self.name = name
        self.region = region

    def make_noise(self):
        return "AHHHHHHH"

class Bear(Mammal):
    def make_appearance(self):
        return "ʕ •ᴥ• ʔ"

    def make_noise(self):
        return "ROOAAAR!!"

bear = Mammal("bear", "wa")
print(bear.make_appearance())
print(bear.make_noise())
```
##### !end-options

##### !answer
```python
class Mammal:
    def __init__(self, name, region):
        self.name = name
        self.region = region

    def make_noise(self):
        return "AHHHHHHH"

class Bear(Mammal):
    def make_appearance(self):
        return "ʕ •ᴥ• ʔ"

    def make_noise(self):
        return "ROOAAAR!!"

bear = Bear("bear", "wa")
print(bear.make_appearance())
print(bear.make_noise())
```
##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->
