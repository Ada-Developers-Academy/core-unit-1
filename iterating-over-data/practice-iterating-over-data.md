# Practice: Iterating Over Data

## Directions

Complete all questions below.

## Practice

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: EJew-RW0t
* title: Iterating Over Data
##### !question

Given a function called `stopwatch` that takes in the argument `22`, which of the following loops would start at `1` and increment all the way up to *and include* `22`?

##### !end-question
##### !options

* `for i in 22:`
* `for i in range(22):`
* `for i in range(1, 22):`
* `for i in range(1, 23):`

##### !end-options
##### !answer

* `for i in range(1, 23):`

##### !end-answer
##### !explanation

Python's `range` has an *exclusive nature*, meaning that it does not include the last integer in its range, ie the `stop` parameter. That's why we must use `23` instead of just `22`.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: EkdvU6Z0K
* title: Iterating Over Data
##### !question

Create a function named `sum_list` that takes a parameter `list` (a list of integers). Iterate through the list and sum up each integer. Then return the total.

##### !end-question
##### !placeholder

```python

def sum_list(list):
    # Note: the word "list" may be highlighted because the Learn platform believes it's reserved
    # This should not affect our code
    pass

```

##### !end-placeholder
##### !tests
```python

import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_sum_list(self):
        self.assertEqual(sum_list([3,5,7,9]),24)
        self.assertEqual(sum_list([0,-3,6,6]),9)

```
##### !end-tests
##### !explanation

An example of a working implementation:

``` python

def sum_list(list):
  sum = 0
  for item in list:
    sum += item
  return sum

```

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 3 -->
<!-- prettier-ignore-start -->
### !challenge
* type: checkbox
* id: N1iCy1fCF
* title: Iterating Over Data
##### !question

Given this dictionary...

``` python
my_profile = {"icecream_flavor": "chocolate", "has_siblings": True}
```

Which of the loops below will produce the following output?

```
icecream_flavor
has_siblings
```

##### !end-question
##### !options

* 
```python
for x in my_profile:
    print(x)
```

* 
```python
for x in my_profile:
    print(my_profile[x])
```

* 
```python
for x in my_profile.keys():
    print(x)
```

* 
```python
for x, y in my_profile.items():
    print(y)
```


##### !end-options
##### !answer

* 
```python
for x in my_profile:
    print(x)
```

* 
```python
for x in my_profile.keys():
    print(x)
```

##### !end-answer
##### !hint

This question purposefully uses unreadable variable names. Replace the variable names `x` and `y` for more clarity.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 4 -->
<!-- prettier-ignore-start -->
### !challenge
* type: checkbox
* id: NyhIeJG0K
* title: Iterating Over Data
##### !question

Given this dictionary...

``` python
my_profile = {"icecream_flavor": "chocolate", "has_siblings": True}
```

Which of the loops below will produce the following output?

```
chocolate
True
```

##### !end-question
##### !options

* 
```python
for x in my_profile:
    print(x)
```

* 
```python
for x in my_profile:
    print(my_profile[x])
```

* 
```python
for x in my_profile.keys():
    print(x)
```

* 
```python
for x, y in my_profile.items():
    print(y)
```

##### !end-options
##### !answer

* 
```python
for x in my_profile:
    print(my_profile[x])
```

* 
```python
for x, y in my_profile.items():
    print(y)
```

##### !end-answer
##### !hint

This question purposefully uses unreadable variable names. Replace the variable names `x` and `y` for more clarity.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 5 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: NkbCNAWCF
* title: Iterating Over Data
##### !question

Create a function named `search_dictionary`. This function...

- Has two parameters, `dict` and `needle`
    - `dict` is a dictionary
    - `needle` is a string
- If `needle` is a key found in `dict`, then return the value at that key.

**Required**: Use a for-loop.

Here is the test:

```python
def test_search_dictionary_finds_value():
    dict = {"icecream_flavor": "chocolate",
            "lucky_nums": [7, 18, 34],
            "has_pets": True}
    assert search_dictionary(dict, "icecream_flavor") == "chocolate"
```

##### !end-question
##### !placeholder

```python
def search_dictionary(dict, needle):
    # Note: the word "dict" may be highlighted because the Learn platform believes it's reserved
    # This should not affect our code
    pass
```

##### !end-placeholder
##### !tests
```python

import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_search_dictionary_finds_value(self):
        dict = {"icecream_flavor": "chocolate",
                "lucky_nums": [7, 18, 34],
                "has_pets": True}
        self.assertEqual(search_dictionary(
            dict, "icecream_flavor"), "chocolate")

```
##### !end-tests
##### !explanation

Two examples of working implementations:

``` python
def search_dictionary(dict, needle):
    for item in dict:
        if item == needle:
            return dict[needle]
```

``` python
def search_dictionary(dict, needle):
    for key, value in dict.items():
        if key == needle:
            return dict[needle]
```

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 6 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: Ny72-sS0Y
* title: Iterating Over Data
##### !question

Continue the function named `search_dictionary` from above. This function still has two parameters, `dict` and `needle`, and returns the value if there is a key that matches `needle`.

Now, if `dict` does not contain the `needle` key, the function returns `False`.

**Required**: Use a for-loop.

Here are the tests:

```python
def test_search_dictionary_finds_value():
    dict = {"icecream_flavor": "chocolate",
            "lucky_nums": [7, 18, 34],
            "has_pets": True}
    assert search_dictionary(dict, "icecream_flavor") == "chocolate"


def test_search_dictionary_key_not_found_is_false():
    dict = {"icecream_flavor": "chocolate",
            "lucky_nums": [7, 18, 34],
            "has_pets": True}
    assert search_dictionary(dict, "has_dogs") == False
```

##### !end-question
##### !tests
```python
import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_search_dictionary_finds_value(self):
        dict = {"icecream_flavor": "chocolate",
                "lucky_nums": [7, 18, 34],
                "has_pets": True}
        self.assertEqual(search_dictionary(
            dict, "icecream_flavor"), "chocolate")

    def test_search_dictionary_key_not_found_is_false(self):
        dict = {"icecream_flavor": "chocolate",
                "lucky_nums": [7, 18, 34],
                "has_pets": True}
        self.assertEqual(search_dictionary(dict, "has_dogs"), False)
```
##### !end-tests
##### !hint

If you're stuck, consider reviewing the information on pairing an `else` statement with a `for loop`.

##### !end-hint
##### !explanation

Two examples of working implementations:

``` python
def search_dictionary(dict, needle):
    for item in dict:
        if item == needle:
            return dict[needle]
    return False
```
``` python
def search_dictionary(dict, needle):
    for item in dict:
        if item == needle:
            return dict[needle]
    else:
        return False
```
##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->
