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

<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: 36f0e6ef-3b85-4608-a8d2-89dca7c724c3
* title: Practice Nested Data II

##### !question
`restaurants` is a list of dictionaries. Modify `get_restaurant_info()` to print the following output:
```
Dough Zone
Bingos
Toyoda
```
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

def get_restaurant_info():
    pass
```
##### !end-placeholder
##### !tests
```python

import main
import unittest
from unittest.mock import patch 

@patch('builtins.print')
class TestInfo(unittest.TestCase):
  def test_restaurant_info(self, mock_print):
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
    get_restaurant_info(restaurants)
    mock_print.assert_called_with('Toyoda')
```
##### !end-tests
### !end-challenge
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: 38019b05-b160-44a2-87a1-e5680008e866
* title: Practice Nested Data III

##### !question
Modify `get_student_name()` to return `Lizzie` from the `students` list.
##### !end-question

##### !placeholder
```python
students = [
  ['Michelle', 'Beyonce', 'Kelly'],
  ['Luke', 'Leia', 'Han'],
  ['Gordon', "Lizzie", "Miranda"]
]

def get_student_name():
    pass
```
##### !end-placeholder
##### !tests
```python

import main
import unittest

class TestStudent(unittest.TestCase):
  def test_student_name(self):
    name = get_student_name()
    expected = "Lizzie"
    self.assertEqual(name, expected)
```
##### !end-tests
### !end-challenge
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: b54addb3-48b0-462a-9f6a-f9b749fba39f
* title: Practice Nested Data IV

##### !question
Modify `get_students()` to print all names from `students`.
##### !end-question

##### !placeholder
```python
students = [
  ['Michelle', 'Beyonce', 'Kelly'],
  ['Luke', 'Leia', 'Han'],
  ['Gordon', "Lizzie", "Miranda"]
]

def get_students():
    pass
```
##### !end-placeholder
##### !tests
```python

import main
import unittest
from unittest.mock import patch 

@patch('builtins.print')
class TestStudent(unittest.TestCase):
  def test_students(self, mock_print):
    get_students()
    mock_print.assert_called_with('Miranda')
```
##### !end-tests
### !end-challenge
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: 613ccf11-e7e6-4fad-a1b1-6a962bcd8967
* title: Practice Nested Data V

##### !question
Modify `get_school_name()` to return `University of Washington` from the `schools` list.
##### !end-question

##### !placeholder
```python
schools = {
    "school 1": {
        "name": "Western Washington University",
        "city": "Bellingham"
    },
    "school 2": {
        "name": "University of Washington",
        "city": "Seattle"
    },
    "school 3": {
        "name": "Washington State University",
        "city": "Pullman"
    }
}

def get_school_name():
    pass
```
##### !end-placeholder
##### !tests
```python

import main
import unittest

class TestSchool(unittest.TestCase):
  def test_school_name(self):
    name = get_school_name()
    expected = "University of Washington"
    self.assertEqual(name, expected)
```
##### !end-tests
### !end-challenge
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: b54addb3-48b0-462a-9f6a-f9b749fba39f
* title: Practice Nested Data VI

##### !question
Modify `get_schools` to print the name and city of each school from `schools`.
##### !end-question

##### !placeholder
```python
schools = {
    "school 1": {
        "name": "Western Washington University",
        "city": "Bellingham"
    },
    "school 2": {
        "name": "University of Washington",
        "city": "Seattle"
    },
    "school 3": {
        "name": "Washington State University",
        "city": "Pullman"
    }
}

def get_schools():
    pass
```
##### !end-placeholder
##### !tests
```python

import main
import unittest
from unittest.mock import patch 

@patch('builtins.print')
class TestSchools(unittest.TestCase):
  def test_schools(self, mock_print):
    get_schools()
    mock_print.assert_called_with("Pullman")
```
##### !end-tests
### !end-challenge
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: 279c4012-341e-4461-a716-f0c093c7faba
* title: Practice Nested Data VII

##### !question
It's Karoake night! Ada's karoake machine has a list of performers and Akira is up next with their second song. Modify `get_song_name()` to return `Mr. Brightside` from the `performers` list.
##### !end-question

##### !placeholder
```Python

performers = {
  "Rajan": ["I Want It That Way", "Jolene"],
  "Akira": ["Return of the Mack", "Mr. Brightside"],
  "Linh": ["Say My Name", "Since You Been Gone"]
}

def get_song_name():
    pass
```
##### !end-placeholder
##### !tests
```python

import main
import unittest

class TestSong(unittest.TestCase):
  def test_song_name(self):
    song = get_song_name()
    expected = "Mr. Brightside"
    self.assertEqual(name, expected)
```
##### !end-tests
### !end-challenge
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: b54addb3-48b0-462a-9f6a-f9b749fba39f
* title: Practice Nested Data VIII

##### !question
Adie's want to keep record of all the songs performed during Karoake Night. Modify `get_songs()` to print all the songs from the `performers` list.
##### !end-question

##### !placeholder
```Python

performers = {
  "Rajan": ["I Want It That Way", "Jolene"],
  "Akira": ["Return of the Mack", "Mr. Brightside"],
  "Linh": ["Say My Name", "Since You Been Gone"]
}

def get_songs():
    pass
```
##### !end-placeholder
##### !tests
```python

import main
import unittest
from unittest.mock import patch 

@patch('builtins.print')
class TestSchools(unittest.TestCase):
  def test_schools(self, mock_print):
    get_songs()
    mock_print.assert_called_with("Since You Been Gone")
```
##### !end-tests
### !end-challenge
<!-- prettier-ignore-end -->



<!-- Q1 Retrieve `restaurant address` from this list (nested list of objects)
- Q2 loop for values for above question 
- Q3 Retrieve `Jill` from nested list student names
- Q5 loop for id for above question
- Q6 Retrieve `University of WA` from nested object of lists (schools)
- Q7 loop for names in object for above
- Q8 Retrieve `Nguyen` from nested object of objects of performers
- Q9 loop for keys for above -->
