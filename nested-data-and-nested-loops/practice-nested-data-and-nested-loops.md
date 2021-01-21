# Activity: Nested Data and Nested Loops

## Directions

Complete all questions below.

## Practice

### Using nested data and nested loops 

<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: 21148e80-6a8d-4c69-ab99-2e7fd11c6aa5
* title: Practice Nested Data I

##### !question
Modify `get_restaurant_address()` so it returns the value `6501 Bongo St. SE`.
##### !end-question

##### !placeholder

```python
restaurants = [
  {
    "name": "Dough Zone",
    "cuisine": "Chinese",
    "address": "1299 Dough Ave N"
  },
  {
    "name": "Bingos",
    "cuisine": "Carribean",
    "address": "6501 Bongo St. SE"
  },
  {
    "name": "Toyoda",
    "cuisine": "Japanese",
    "address": "12543 Sushi Way NE"
  }
]

def get_restaurant_address():
    pass

```

##### !end-placeholder

##### !tests
```python

import main
import unittest
class TestAddress(unittest.TestCase):
  def test_loop_in_order(self):
    address = get_restaurant_address()
    expected = "6501 Bongo St. SE"
    self.assertEqual(address, expected)
```
##### !end-tests
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Q1 Retrieve `restaurant address` from this list (nested list of objects)
- Q2 loop for keys for above question 
- Q3 Retrieve `Jill` from nested list student names
- Q5 loop for id for above question
- Q6 Retrieve `University of WA` from nested object of lists (schools)
- Q7 loop for names in object for above
- Q8 Retrieve `Nguyen` from nested object of objects of performers
- Q9 loop for keys for above -->
