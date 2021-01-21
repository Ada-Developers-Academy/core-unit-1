# Activity: Nested Loops 

## Directions

Complete all questions below.

## Practice

### Using Loops

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: 95d7ca55-984a-439c-8cd1-c3fb92212c89
* title: Practice Nested Loops I

##### !question
Using a nested loop, create a function that will print the following output:

```
1
-
-
-
2
-
-
-
3
-
-
-
```
##### !end-question
##### !placeholder
```python

nums = [1,2,3]
dashes = ["-", "-", "-"]

def loop_in_order(nums, chars):
  pass

loop_in_order(nums, dashes)

```
##### !end-placeholder
##### !tests
```python
import main
import unittest
from unittest.mock import patch 

@patch('builtins.print')
def test_loop_in_order(mock_print):
  loop_in_order([1,2,3],["-", "-", "-"])
  mock_print.assert_called_with('1 - - - 2 - - - 3 - - -')
  sys.stdout.write(str( mock_print.call_args ) + '\n')
```
##### !end-tests
##### !hint
Use a for in loop to loop through the lists.
##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: b990b092-7c30-481a-babb-55b253bb9db9
* title: Practice Nested Loops II

##### !question
Select the option that best describes the nested loops in this code:

``` Python
desserts = ["ice cream", "milkshake", "cake"]
flavors = ["vanilla", "chocolate", "strawberry"]

for dessert in desserts:
  print(dessert)
  for flavor in flavors:
    print(flavor)
```
##### !end-question
##### !options
* `for flavor in flavors:` is the *outer*  loop, `for dessert in desserts:` is the *inner*  loop. The *outer*  loop will iterate for the length of the `flavors` list (3) before starting the next iteration of the *inner* loop.
* `dessert in desserts:` is the *outer* loop, `for flavor in flavors:` is the *inner* loop. The *inner*  loop will iterate for the length of the `flavors` lists (3) before starting the next iteration of the *outer* loop. 
##### !end-options
##### !answer
* `dessert in desserts:` is the *outer* loop, `for flavor in flavors:` is the *inner* loop. The *inner*  loop will iterate for the length of the `flavors` lists (3) before starting the next iteration of the *outer* loop. 
##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 3 -->
<!-- prettier-ignore-start -->
### !challenge
* type: checkbox
* id: 4221aa42-6074-43aa-a083-749b1ca22a30
* title: Nested Loops Practice III 
##### !question

Select the option with the correct output for this nested loop.

``` Python
grid = []
for item in range(2):
  grid.append(["O"]* 3)
  for row in grid:
    print(f" ".join(row))
```

##### !end-question
##### !options

* 
```
 000
 000
```
* 
```
 000
 000
 000
```
* 
```
 000000
 000000
```
##### !end-options
##### !answer

* 
```
 000
 000
 000
```

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 4 -->
<!-- prettier-ignore-start -->
### !challenge

* type: code-snippet
* language: python3.6
* id: e44214b2-5a75-412e-a4e1-8a94523bdaaf
* title: Practice Nested Loops IV
* topics: python

##### !question
Desi's Desserts needs to display their online dessert menu. Desi created two lists: `desserts` and `flavors`. Use a nested loop to print out a menu of combined items from each list like this:

```
 vanilla ice cream
 chocolate ice cream
 vanilla milkshake
 chocolate milkshake
```
##### !end-question
##### !placeholder
```python

desserts = ["ice cream", "milkshake"]
flavors = ["vanilla", "chocolate"]

def combine_menu(flavors, desserts):
  pass

combine_menu(flavors, desserts)
```
##### !end-placeholder
##### !tests
```python
import main
import unittest
from unittest.mock import patch 

class TestMenuItems(unittest.TestCase):
  def test_combined_menu(self):
    menu = combine_menu(["ice cream", "milkshake"], ["vanilla", "chocolate"])
    mock_print.assert_called_with("vanilla ice cream chocolate ice cream vanilla milkshake chocolate milkshake")
```
##### !end-tests
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 5 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: 3417ddc6-cac6-4945-82b2-b4e27580355d
* title: Practice Nested Loops V
* topics: python

##### !question
Using a nested loop, create a function that will return the amount of vowels in a word. (Hint: The key value pair in `vowels` should look like this `{'a': 1, 'e': 2}`)
##### !end-question
##### !placeholder
```python

def check_vowels(word):
    vowel_list = ["a", "e", "i", "o", "u"]
    vowels = {}
return vowels
```
##### !end-placeholder
##### !tests
```python
import main
import unittest

class TestVowel(unittest.TestCase):
  def test_vowel(self):
    word = check_vowels("yellow")
    expected = {'e': 1, 'o': 1}
    self.assertEqual(word, expected)
```
##### !end-tests
### !end-challenge
<!-- prettier-ignore-end -->
