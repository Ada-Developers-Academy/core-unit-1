# Problem Set: Representing Data

## Directions

Complete all questions below.

## Practice

### Using Lists

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: NwjaVq
* title: Representing Data
##### !question

What is the data type of `materials`?

```python
materials = ["Wood", "Paper", "Cardboard"]
```

##### !end-question
##### !options

* String
* None
* Boolean
* List

##### !end-options
##### !answer

* List

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: zOsSdd
* title: Representing Data
##### !question

Consider the list `["Wood", "Paper", "Cardboard"]`. Which of these is the most readable variable name?

##### !end-question
##### !options

* `material`
* `materials`
* `list`
* `l`

##### !end-options
##### !answer

* `materials`

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 3 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: bxveCY
* title: Representing Data
##### !question

Which of these is the best representation of a grocery list in Python?

##### !end-question
##### !options

* `"Spinach, Broccoli, Eggplant, Potatoes"`
* `[Spinach, Broccoli, Eggplant, Potatoes]`
* `["Spinach", "Broccoli", "Eggplant", "Potatoes"]`
* `[["Spinach"], ["Broccoli"], ["Eggplant"], ["Potatoes"]]`

##### !end-options
##### !answer

* `["Spinach", "Broccoli", "Eggplant", "Potatoes"]`

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

### Problem Statement to Representing Data

<!-- Question 4 -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: hDdbkg
* title: Representing Data
##### !question

Describe some ways you can recognize that a problem's solution might use a list. Explain it as if you're talking to a 10 year old in 2-4 sentences.

##### !end-question
##### !placeholder

After reading a problem statement, I can recognize it might use a list if...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 5 -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: qI4Mf6
* title: Representing Data
##### !question

Describe some ways you can recognize that a problem's solution might use a dictionary. Explain it as if you're talking to a 10 year old in 2-4 sentences.

##### !end-question
##### !placeholder

After reading a problem statement, I can recognize it might use a dictionary if...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 6 -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: xh0iTZ
* title: Representing Data
##### !question

| Date (YYYY-MM-DD format) | Number of Crows Spotted in the Parking Lot |
| ------------------------ | ------------------------------------------ |
| 2010-06-01               | 3                                          |
| 2010-06-02               | 5                                          |
| 2010-06-03               | 5                                          |
| 2010-06-04               | 6                                          |
| 2010-06-05               | 2                                          |
| 2010-06-06               | 2                                          |
| 2010-06-07               | 1                                          |
| 2010-06-08               | 0                                          |

Imagine this data is from an organization called "The Fellowship of Kiri's Neighborhood Friends" that collects data on Kiri's neighborhood friends.

Look through this data, and make a prediction about what this data represents. Describe it how you would explain it to a 10 year old in 2-4 sentences.

##### !end-question
##### !placeholder

This table represents...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 7 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: dZMTTi
* title: Representing Data
### !question

| Field        | Value      |
| ------------ | ---------- |
| date         | 2010-06-01 |
| location     | park       |
| crow_count   | 3          |
| dog_count    | 10         |
| cat_count    | 0          |
| pigeon_count | 31         |

Create a dictionary that contains all of the data in this table. Use context clues to understand what keys and values are expected (including running the test).

Put that dictionary in the function `get_friend_data()` as a dictionary literal and return it.

### !end-question
### !placeholder

```python
def get_friend_data():
    pass
```
### !end-placeholder
### !tests
```python
import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_get_friend_data(self):
        data = get_friend_data()

        self.assertEqual(data["date"], "2010-06-01")
        self.assertEqual(data["location"], "park")
        self.assertEqual(data["crow_count"], 3)
        self.assertEqual(data["dog_count"], 10)
        self.assertEqual(data["cat_count"], 0)
        self.assertEqual(data["pigeon_count"], 31)
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def get_friend_data():
    data = {
        "date": "2010-06-01",
        "location": "park",
        "crow_count": 3,
        "dog_count": 10,
        "cat_count": 0,
        "pigeon_count": 31
    }
    return data
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 8 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: KkABtU
* title: Representing Data
### !question

| Name   | Age |
| ------ | --- |
| Mae    | 31  |
| Brandi | 22  |
| Dane   | 44  |
| Neo    | 39  |
| Amara  | 36  |
| Jules  | 28  |

Using the data above, create a list of contestants' names. The names should be in the order of descending age, where the oldest contestant's name is first, and the youngest contestant's name is last.

Put that list in the function `sort_contestants_age_desc()` as a list literal and return it.

### !end-question
### !placeholder

```python
def sort_contestants_age_desc():
    pass
```
### !end-placeholder
### !tests
```python
import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_sort_contestants_age_desc(self):
        contestants = sort_contestants_age_desc()

        self.assertEqual(
            contestants, ["Dane", "Neo", "Amara", "Mae", "Jules", "Brandi"])
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def sort_contestants_age_desc():
    contestants = [
        "Dane", "Neo", "Amara", "Mae", "Jules", "Brandi"
    ]
    return contestants
```
### !end-explanation
### !end-challenge

<!-- Question 9 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: rmb4AO
* title: Representing Data
### !question

| Field                    | Expected Data Type | Value |
| ------------------------ | ------------------ | ----- |
| name                     | string             |       |
| is_morning_person        | boolean            |       |
| is_night_owl             | boolean            |       |
| fav_song_title           | string or `None`   |       |
| num_of_household_members | integer            |       |

Fill out this table's data.

Then, create a dictionary literal from the Field and Value columns in that table.

Put that dictionary in the function `get_my_preferences()` as a dictionary literal and return it.

### !end-question
### !placeholder

```python
def get_my_preferences():
    pass
```
### !end-placeholder
### !tests
```python
import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_get_my_preferences_has_valid_values(self):
        pref = get_my_preferences()

        self.assertIsInstance(pref["name"], str)
        self.assertIsInstance(pref["is_morning_person"], bool)
        self.assertIsInstance(pref["is_night_owl"], bool)
        fav_song = pref["fav_song_title"]
        self.assertTrue( isinstance(fav_song, str) or fav_song == None )
        self.assertIsInstance(pref["num_of_household_members"], int)
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def get_my_preferences():
    return {
        "name": "My Name",
        "is_morning_person": True,
        "is_night_owl": True,
        "fav_song_title": None,
        "num_of_household_members": 1
    }
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

### Modifying Data

<!-- Question 10 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: mHGBgU
* title: Representing Data
### !question

Implement the function `add_preference()`. This function takes in a `preferences` dictionary, a `category`, and a `value`.

This function should add a new key-value pair to `preferences`, where `category` is the key and `value` is the value. Then, it should return `preferences`.

The test for this function is:

```python
def test_add_preference():
    assert add_preference({}, "test cat", "test val") == {
        "test cat": "test val"}

    preferences = {
        "name": "My Name",
        "is_morning_person": True,
        "is_night_owl": True,
        "fav_song_title": None,
        "num_of_household_members": 1
    }

    updated_preferences = add_preference(preferences, "test cat", "test val")
    assert updated_preferences["test cat"] == "test val"
```

### !end-question
### !tests
```python
import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_add_preference(self):
        self.assertEqual(add_preference({}, "test cat", "test val"), {
                         "test cat": "test val"})

        preferences = {
            "name": "My Name",
            "is_morning_person": True,
            "is_night_owl": True,
            "fav_song_title": None,
            "num_of_household_members": 1
        }

        updated_preferences = add_preference(preferences, "test cat", "test val")

        self.assertEqual( updated_preferences["test cat"], "test val" )
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def add_preference(preferences, category, value):
    preferences[category] = value
    return preferences
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 11 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: 5LPH50
* title: Representing Data
### !question

Implement the function `add_grocery()`. This function takes in a `grocery_list` and a `new_item`. This function should append the new item to the end of the grocery list, and then return the grocery list.

The test for this function is:

```python
def test_add_grocery():
    assert add_grocery([], "Rice") == ["Rice"]
    assert add_grocery(["Rice"], "Beans") == ["Rice", "Beans"]
```

### !end-question
### !tests
```python
import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_add_grocery(self):
        self.assertEqual(add_grocery([], "Rice"), ["Rice"])
        self.assertEqual(add_grocery(["Rice"], "Beans"), ["Rice", "Beans"])
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def add_grocery(grocery_list, new_item):
    grocery_list.append(new_item)
    return grocery_list
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 12 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: LLU2tX
* title: Representing Data
### !question

Implement the function `copy_top_item()`. This function takes in two grocery lists, `my_groceries` and `their_groceries`. This function should:

1. Read the first element from the list `their_groceries`, and store it into a local variable.
1. Replace (re-assign) the first element in `my_groceries` with the stored value (the local variable) from step 1.
1. Return this modified list.

The test for this function is:

```python
def test_copy_top_item_reassigns_my_groceries():
    kiris_groceries = ["Spinach", "Broccoli", "Eggplants", "Potatoes"]
    tiegans_groceries = ["Avocados", "Oat Milk", "Mangoes"]

    new_groceries = copy_top_item(kiris_groceries, tiegans_groceries)

    assert new_groceries == ["Avocados", "Broccoli", "Eggplants", "Potatoes"]
    # Check that their_groceries wasn't modified
    assert tiegans_groceries == ["Avocados", "Oat Milk", "Mangoes"]
```

### !end-question
### !tests
```python
import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_copy_top_item_reassigns_my_groceries(self):
        kiris_groceries = ["Spinach", "Broccoli", "Eggplants", "Potatoes"]
        tiegans_groceries = ["Avocados", "Oat Milk", "Mangoes"]

        new_groceries = copy_top_item(kiris_groceries, tiegans_groceries)

        self.assertEqual(
            new_groceries, ["Avocados", "Broccoli", "Eggplants", "Potatoes"])
        # Check that their_groceries wasn't modified
        self.assertEqual(tiegans_groceries, ["Avocados", "Oat Milk", "Mangoes"])
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def copy_top_item(my_groceries, their_groceries):
    top_item = their_groceries[0]
    my_groceries[0] = top_item
    return my_groceries
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->
