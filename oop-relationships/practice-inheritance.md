# Practice: Inheritance

## Directions

Complete all questions below.

## Practice

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge
* type: checkbox
* id: 85c8a657-1907-418a-9020-7b7baf02b9d1
* title: Inheritance
##### !question

What is a key difference between inheritance and composition?

##### !end-question
##### !options

* Composition is an extension of a parent class, and inheritance is more of a distant cousin twice removed.
* Inheritance describes an **is-a** relationship. Composition describes a **has-a** relationship.
* Inheritance can be described as an extension of a parent class. Composition adds supportive logic to a class.

##### !end-options

##### !answer
* Inheritance describes an **is-a** relationship. Composition describes a **has-a** relationship.
* Inheritance can be described as an extension of a parent class. Composition adds supportive logic to a class.
##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->
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
