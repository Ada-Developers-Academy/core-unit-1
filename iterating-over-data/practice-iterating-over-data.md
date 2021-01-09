# Practice: Iterating Over Data

## Directions

Complete all questions below.

## Practice


### !challenge

* type: multiple-choice
* id: EJew-RW0t
* title: Which Range is Correct?

##### !question

Given a function called `stopwatch` that takes in the argument `22`, which of the following loops would  correctly start at `1` and increment all the way up to *and include* `22`?

##### !end-question

##### !options

* `for i in 22:`
* `for i in range(22)`
* `for i in range(1,22)`
* `for i in range(1,23)`

##### !end-options

##### !answer

`for i in range(1,23)`

##### !end-answer


##### !hint

##### !end-hint


##### !rubric

##### !end-rubric


##### !explanation

Python's `range` has an *exclusive nature*, meaning that it does not include the last integer in its range, ie the `stop` parameter. That's why we must use `23` instead of just `22`.

##### !end-explanation

### !end-challenge

<!-- CHALLENGE BREAK -->

### !challenge

* type: code-snippet
* language: python3.6
* id: EkdvU6Z0K
* title: Iterate Over a List

##### !question

Create a function named `sum_list` that takes a parameter `list` (a list of integers). Iterate through the list and sum up each integer. Then return the total.

##### !end-question

##### !placeholder

```python

def sum_list(list):
  pass

```

##### !end-placeholder

##### !tests
```python

import main
import unittest


class TestPython1(unittest.TestCase):
def test_sum_list(self):
  self.assertEqual(sum_list([3,5,7,9]),24)
  self.assertEqual(sum_list([0,-3,6,6]),9)

```
##### !end-tests


##### !hint

##### !end-hint


##### !rubric

##### !end-rubric


##### !explanation

An example of a working implementation:

``` python

def sum_list(list):
  sum = 0
  for i in list:
    sum += i
  return sum

```

##### !end-explanation

### !end-challenge

<!-- CHALLENGE BREAK -->


### !challenge

* type: checkbox
* id: N1iCy1fCF
* title: Choose the Best Option(s)


##### !question

Given this dictionary: 
``` python

my_profile = {"icecream_flavor": "chocolate", has_siblings: True}

```

Which loop(s) *can* I use if I want to print out each key?

##### !end-question

##### !options

* `for x in my_profile:`
* `for x in my_profile.keys()`
* `for x in my_profile.values()`
* `for x, y in my_profile.items()`


##### !end-options

##### !answer

* `for x in my_profile:`
* `for x in my_profile.keys()`
* `for x, y in my_profile.items()`

##### !end-answer


##### !hint

##### !end-hint


##### !rubric

##### !end-rubric


##### !explanation

##### !end-explanation

### !end-challenge

<!-- CHALLENGE BREAK -->

### !challenge

* type: checkbox
* id: NyhIeJG0K
* title: Choose the Best Option(s)


##### !question

Given this dictionary: 
``` python

my_profile = {"icecream_flavor": "chocolate", has_siblings: True}

```

Which loop(s) *can* I use if I want to print out each value?

##### !end-question

##### !options

* `for x in my_profile:`
* `for x in my_profile.keys()`
* `for x in my_profile.values()`
* `for x, y in my_profile.items()`


##### !end-options

##### !answer

* `for x in my_profile:`
* `for x in my_profile.values()`
* `for x, y in my_profile.items()`

##### !end-answer


##### !hint

##### !end-hint


##### !rubric

##### !end-rubric


##### !explanation

##### !end-explanation

### !end-challenge

<!-- CHALLENGE BREAK -->

### !challenge

* type: checkbox
* id: V1VRgkzAY
* title: Choose the Best Option(s)


##### !question

Given this dictionary: 
``` python

my_profile = {"icecream_flavor": "chocolate", has_siblings: True}

```

Which loop(s) *can* I use if I want to print out both keys and values?

##### !end-question

##### !options

* `for x in my_profile:`
* `for x in my_profile.keys()`
* `for x in my_profile.values()`
* `for x, y in my_profile.items()`


##### !end-options

##### !answer

* `for x in my_profile:`
* `for x, y in my_profile.items()`

##### !end-answer


##### !hint

##### !end-hint


##### !rubric

##### !end-rubric


##### !explanation

##### !end-explanation

### !end-challenge

<!-- CHALLENGE BREAK -->


### !challenge

* type: code-snippet
* language: python3.6
* id: NkbCNAWCF
* title: Match the Output

##### !question

Given a function named `search_dictionary` that takes two parameters: `dict` (a dictionary) and `check` (a string), check if the key `check` is found in `dict`, and then return the value at that key.

For example, given: `{"icecream_flavor": "chocolate", "lucky_nums": [7, 18, 34], has_pets: True}` and `has_pets`, return `True`.

##### !end-question

##### !placeholder

```python

def search_dictionary(dict,check):
  pass

```

##### !end-placeholder

##### !tests
```python

import main
import unittest

dict = {"icecream_flavor": "chocolate", "lucky_nums": [7, 18, 34], has_pets: True}
class TestPython1(unittest.TestCase):
def test_one(self):
  self.assertEqual(search_dictionary(dict, "has_dogs"),False)
  self.assertEqual(search_dictionary(dict, "icecream_flavor"),"chocolate")

```
##### !end-tests


##### !hint

##### !end-hint


##### !rubric

##### !end-rubric


##### !explanation

Two examples of working implementations:

``` python

def search_dictionary(dict,check):
  for i in dict:
    if i === check:
      return dict[i]

```
``` python

def search_dictionary(dict,check):
  for key, value in dict.items():
    if key === check:
      return value
  return

```

##### !end-explanation

### !end-challenge

<!-- CHALLENGE BREAK -->
