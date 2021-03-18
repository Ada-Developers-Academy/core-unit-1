# Problem Set: Iterating Over Data

## Directions

Complete all questions below.

## Practice

<!-- Question 1 -->
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

<!-- Question 2 -->
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

<!-- Question 3 -->
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

<!-- Question 4 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: hGaZd5
* title: Iterating Over Data
### !question

Create a function named `listify_series` that takes one parameter `max_value` (an integer). Append each number in the range from `1` to `max_value` to a list. Then return that list.

**Required**: Use a for-loop and `range()`.

Here is the test:

```python
def test_listify_series():
    assert listify_series(3) == [1, 2, 3]
    assert listify_series(5) == [1, 2, 3, 4, 5]
    assert listify_series(10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### !end-question
### !placeholder

```python
def listify_series(max_value):
    pass
```
### !end-placeholder
### !tests
```python
import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_listify_series(self):
        self.assertEqual(listify_series(3), [1, 2, 3])
        self.assertEqual(listify_series(5), [1, 2, 3, 4, 5])
        self.assertEqual(listify_series(10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def listify_series(max_value):
    my_very_good_list = []
    for i in range(max_value):
        my_very_good_list.append(i + 1)
    return my_very_good_list
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 5 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: 7wMVtj
* title: Iterating Over Data
### !question

Create a function named `sum_series` that takes one parameter `max_value` (an integer). Starting with `1`, add each number in the range from `1` to `max_value` together. Then return that total.

**Required**: Use a for-loop and `range()`.

Here is the test:

```python
def test_sum_series():
    assert sum_series(3) == 6 # 1 + 2 + 3
    assert sum_series(5) == 15 # 1 + 2 + 3 + 4 + 5
    assert sum_series(10) == 55 # 1 + 2 + ... + 9 + 10
```

### !end-question
### !placeholder

```python
def sum_series(max_value):
    pass
```
### !end-placeholder
### !tests
```python
import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_sum_series(self):
        self.assertEqual(sum_series(3), 6)  # 1 + 2 + 3
        self.assertEqual(sum_series(5), 15)  # 1 + 2 + 3 + 4 + 5
        self.assertEqual(sum_series(10), 55)  # 1 + 2 + ... + 9 + 10
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def sum_series(max_value):
    sum = 0
    for i in range(max_value + 1):
        sum += i
    return sum
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 6 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: tTFqeV
* title: Iterating Over Data
### !question

Create a function named `sum_series` that takes two parameters: `min_value` and `max_value`. Starting with `min_value`, add each number in the range from `min_value` to `max_value` together. Then return that total.

**Required**: Use a for-loop and `range()`.

Here is the test:

```python
def test_sum_series_with_min_max_vals():
    assert sum_series(1, 3) == 6  # 1 + 2 + 3
    assert sum_series(2, 4) == 9  # 2 + 3 + 4
    assert sum_series(0, 5) == 15  # 1 + 2 + 3 + 4 + 5
    assert sum_series(3, 7) == 25  # 3 + 4 + 5 + 6 + 7
```

Assume that `min_value` and `max_value` are positive integers, where `min_value` is less than `max_value`

### !end-question
### !placeholder

```python
def sum_series(min_value, max_value):
    pass
```
### !end-placeholder
### !tests
```python
import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_sum_series_with_min_max_vals(self):
        self.assertEqual(sum_series(1, 3), 6)  # 1 + 2 + 3
        self.assertEqual(sum_series(2, 4), 9)  # 2 + 3 + 4
        self.assertEqual(sum_series(0, 5), 15)  # 1 + 2 + 3 + 4 + 5
        self.assertEqual(sum_series(3, 7), 25)  # 3 + 4 + 5 + 6 + 7
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def sum_series(min_value, max_value):
    sum = 0
    for i in range(min_value, max_value + 1):
        sum += i
    return sum
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 7 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: 1HUR7V
* title: Iterating Over Data
### !question

Create a function named `sum_even_nums_in_series` that takes two parameters: `min_value` and `max_value`. Starting with `min_value`, add each **even** number in the range from `min_value` to `max_value` together. Then return that total.

**Required**: Use a for-loop.

Here is the test:

```python
def test_sum_even_nums_in_series():
    assert sum_series(1, 3) == 2  # 2
    assert sum_series(2, 4) == 6  # 2 + 4
    assert sum_series(0, 5) == 6  # 0 + 2 + 4
    assert sum_series(3, 7) == 10  # 4 + 6
```

Assume that `min_value` and `max_value` are positive integers, where `min_value` is less than `max_value`

### !end-question
### !placeholder

```python
def sum_even_nums_series(min_value, max_value):
    pass
```
### !end-placeholder
### !tests
```python
import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_sum_even_nums_in_series(self):
        self.assertEqual(sum_even_nums_series(1, 3), 2)  # 2
        self.assertEqual(sum_even_nums_series(2, 4), 6)  # 2 + 4
        self.assertEqual(sum_even_nums_series(0, 5), 6)  # 2 + 4
        self.assertEqual(sum_even_nums_series(3, 7), 10)  # 4 + 6
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def sum_even_nums_series(min_value, max_value):
    sum = 0
    for i in range(min_value, max_value + 1):
        if i % 2 == 0:
            sum += i
    return sum
```

Another example of a working implementation:

```python
def sum_even_nums_series(min_value, max_value):
    sum = 0
    if min_value % 2 == 0:
        start_value = min_value
    else:
        start_value = min_value + 1

    for i in range(start_value, max_value + 1, 2):
        sum += i
    return sum
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 8 -->
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
            return value
```

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 9 -->
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
