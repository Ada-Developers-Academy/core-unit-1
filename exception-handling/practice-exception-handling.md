# Practice: Exception Handling

## Directions

Complete all questions below.

## Practice

<!-- Question 1 -->

<!-- prettier-ignore-start -->
### !challenge

* type: code-snippet
* language: python3.6
* id: XwJz6l
* title: Exception Handling

### !question

Given these tests, provide the function body that will make them pass. Assume that the only invalid, claimed code school name is `"Ada Developers Academy"`.

```python
def test_valid_name():
    result = claim_unreserved_code_school_name("Some Code School")
    assert result is True


def test_invalid_name():
    with pytest.raises(ValueError):
        claim_unreserved_code_school_name("Ada Developers Academy")
```

### !end-question
### !placeholder

```python
def claim_unreserved_code_school_name(name):
    pass
```
### !end-placeholder
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
    def test_valid_name(self):
        result = claim_unreserved_code_school_name("Some Code School")
        self.assertTrue(result)

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            claim_unreserved_code_school_name("Ada Developers Academy")
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def claim_unreserved_code_school_name(name):
    if name == "Ada Developers Academy":
        raise ValueError
    return True
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->

<!-- prettier-ignore-start -->
### !challenge

* type: code-snippet
* language: python3.6
* id: SkMsOl
* title: Exception Handling

### !question

Given these tests, provide the function body that will make them pass. Assume that any phone number that is a string is valid.

Hint: The function `type(phone_num)` will return `str` if `phone_num` is a string.

```python
def test_valid_phone_nums_return_true():
    phone_num = "777-888-9999"
    is_valid = is_phone_num_valid(phone_num)
    assert is_valid

def test_invalid_phone_nums_raise_error():
    phone_num = 777-888-9999
    with pytest.raises(ValueError):
        is_valid = is_phone_num_valid(phone_num)
```

### !end-question
### !placeholder

```python
def is_phone_num_valid(phone_num):
    pass
```
### !end-placeholder
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
    def test_valid_phone_nums_return_true(self):
        phone_num = "777-888-9999"
        is_valid = is_phone_num_valid(phone_num)
        self.assertTrue(is_valid)

    def test_invalid_phone_nums_raise_error(self):
        phone_num = 777-888-9999
        with self.assertRaises(ValueError):
            is_phone_num_valid(phone_num)
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def is_phone_num_valid(phone_num):
    if type(phone_num) is not str:
        raise ValueError
    return True
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 3 -->

<!-- prettier-ignore-start -->
### !challenge

* type: code-snippet
* language: python3.6
* id: VLwvhu
* title: Exception Handling

### !question

Given these tests, refactor this function to make them pass. Use `try ... except` syntax.

- If no error is raised, return `cost_per_person`
- If a `ZeroDivsionError` is raised, catch it, and return `0`

```python
def test_split_cost_evenly():
    cost = split_cost_evenly(100, 4, .5)
    assert cost == pytest.approx(37.5)


def test_caught_zerodivisionerror_returns_zero():
    cost = split_cost_evenly(100, 0, .5)
    assert cost == 0
```

### !end-question
### !placeholder

```python
def split_cost_evenly(total_cost, num_of_people, tip_percentage):
    cost_with_tip = total_cost * (1 + tip_percentage)
    cost_per_person = cost_with_tip / num_of_people
    return cost_per_person
```
### !end-placeholder
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
    def test_split_cost_evenly(self):
        cost = split_cost_evenly(100, 4, .5)
        self.assertAlmostEqual(cost, 37.5)

    def test_caught_zerodivisionerror_returns_zero(self):
        cost = split_cost_evenly(100, 0, .5)
        self.assertEqual(cost, 0)
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def split_cost_evenly(total_cost, num_of_people, tip_percentage):
    try:
        cost_with_tip = total_cost * (1 + tip_percentage)
        cost_per_person = cost_with_tip / num_of_people
        return cost_per_person
    except ZeroDivisionError:
        return 0
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 4 -->

<!-- prettier-ignore-start -->
### !challenge

* type: code-snippet
* language: python3.6
* id: j9kUX9
* title: Exception Handling

### !question

Given these tests, refactor **_only_** the **`get_celebration_treat`** function to make them pass. Use `try ... except` syntax.

In `get_celebration_treat`...

- If no error is raised, then `get_celebration_treat` returns `"celebration {thirteenth_donut}!"`, where `thirteenth_donut` is the result of `grab_thirteenth_donut()`
- If an `IndexError` is raised because of accessing something missing in `donuts`, then `get_celebration_treat` returns `"no donut :("`

```python
def test_get_celebration_treat():
    bakers_dozen = [
        "glazed donut", "old-fashioned", "jelly donut", "bear claw", "classic donut with pink frosting and sprinkles on top", "donut hole", "another glazed donut", "yet another glazed donut?", "cruller", "maple donut", "powdered sugar donut", "doughnut", "thirteenth donut"
    ]
    # Run this assert as part of the "Arrange" step to ensure we're set up correctly
    assert len(bakers_dozen) == 13

    thirteenth_donut = get_celebration_treat(bakers_dozen)
    assert thirteenth_donut == "celebration thirteenth donut!"


def test_no_celebration_treat():
    empty_donut_box = []
    # Run this assert as part of the "Arrange" step to ensure we're set up correctly
    assert len(empty_donut_box) != 13

    no_donut = get_celebration_treat(empty_donut_box)
    assert no_donut == "no donut :("


def test_dont_grab_thirteenth_donut():
    # This test is for checking that grab_thirteenth_donut raises the error
    empty_donut_box = []
    with pytest.raises(IndexError):
        grab_thirteenth_donut(empty_donut_box)
```

### !end-question
### !placeholder

```python
def grab_thirteenth_donut(donuts):
    return donuts[12]


def get_celebration_treat(treats):
    thirteenth_donut = grab_thirteenth_donut(treats)
    return f"celebration {thirteenth_donut}!"
```
### !end-placeholder
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
    def test_get_celebration_treat(self):
        bakers_dozen = [
            "glazed donut", "old-fashioned", "jelly donut", "bear claw", "classic donut with pink frosting and sprinkles on top", "donut hole", "another glazed donut", "yet another glazed donut?", "cruller", "maple donut", "powdered sugar donut", "doughnut", "thirteenth donut"
        ]
        self.assertEqual(len(bakers_dozen), 13)
        thirteenth_donut = get_celebration_treat(bakers_dozen)
        self.assertEqual(thirteenth_donut, "celebration thirteenth donut!")

    def test_no_celebration_treat(self):
        empty_donut_box = []
        self.assertNotEqual(len(empty_donut_box), 13)
        no_donut = get_celebration_treat(empty_donut_box)
        self.assertEqual(no_donut, "no donut :(")

    def test_dont_grab_thirteenth_donut(self):
        # This test is for checking that grab_thirteenth_donut raises the error
        empty_donut_box = []
        with self.assertRaises(IndexError):
            grab_thirteenth_donut(empty_donut_box)
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def get_celebration_treat(treats):
    try:
        thirteenth_donut = grab_thirteenth_donut(treats)
        return f"celebration {thirteenth_donut}!"
    except IndexError:
        return "no donut :("
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 5 -->

<!-- prettier-ignore-start -->
### !challenge

* type: code-snippet
* language: python3.6
* id: UlAHwy
* title: Exception Handling

### !question

Given these tests, refactor **_only_** the **`prepare_meal`** function to make them pass. Use `try ... except` syntax.

In `prepare_meal`...

- If no error is raised, then `food` should be the result of `make_breakfast(pantry)`
- If a `KeyError` is raised because of accessing something missing in `pantry`, then `food` should be `"nothing"`

```python
def test_makes_breakfast_on_a_plate():
    pantry = {
        "waffles": "blueberry waffles",
        "juice": "orange juice"
    }
    breakfast = prepare_meal("breakfast", pantry)
    assert breakfast == "blueberry waffles and orange juice on a plate!"


def test_missing_pantry_items_gets_nothing_on_a_plate():
    empty_pantry = {}
    missing_breakfast = prepare_meal("breakfast", empty_pantry)
    assert missing_breakfast == "nothing on a plate!"


def test_make_breakfast_with_empty_pantry():
    # This test is for checking that make_breakfast raises the error
    empty_pantry = {}
    with pytest.raises(KeyError):
        make_breakfast(empty_pantry)
```
### !end-question
### !placeholder

```python
def make_breakfast(pantry):
    breakfast = f"{pantry['waffles']} and {pantry['juice']}"
    return breakfast

def serve_food(food):
    return food + " on a plate!"

def prepare_meal(meal_type, pantry):
    if meal_type == "breakfast":
        food = make_breakfast(pantry)
    meal = serve_food(food)
    return meal
```
### !end-placeholder
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
    def test_makes_breakfast_on_a_plate(self):
        pantry = {
            "waffles": "blueberry waffles",
            "juice": "orange juice"
        }
        breakfast = prepare_meal("breakfast", pantry)
        self.assertEqual(
            breakfast, "blueberry waffles and orange juice on a plate!")

    def test_missing_pantry_items_gets_nothing_on_a_plate(self):
        empty_pantry = {}
        missing_breakfast = prepare_meal("breakfast", empty_pantry)
        self.assertEqual(
            missing_breakfast, "nothing on a plate!")

    def test_make_breakfast_with_empty_pantry(self):
        # This test is for checking that make_breakfast raises the error
        empty_pantry = {}
        with self.assertRaises(KeyError):
            make_breakfast(empty_pantry)
```
### !end-tests
### !hint
Try putting the line `food = make_breakfast(pantry)` inside the try-clause. If a `KeyError` is caught, then assign `food` to `"nothing"`.
### !end-hint
### !explanation

An example of a working implementation:

```python
def prepare_meal(meal_type, pantry):
    if meal_type == "breakfast":
        try:
            food = make_breakfast(pantry)
        except KeyError:
            food = "nothing"
    meal = serve_food(food)
    return meal
```

It's completely valid to have more code inside the try-clause.

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->
