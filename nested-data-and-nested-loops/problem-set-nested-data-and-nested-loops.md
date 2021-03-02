# Problem Set: Nested Data and Nested Loops

## Directions

Complete all questions below.

## Practice

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: 8mavqk
* title: Nested Data and Nested Loops
##### !question

What is the syntax to get `"6501 Island St. SE"` from `restaurants`?

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
        "address": "6501 Island St SE"
    },
    {
        "name": "Toyoda",
        "cuisine": "Japanese",
        "address": "12543 Sushi Way NE"
    }
]
```

Use `[]` syntax with double-quotes where needed.

##### !end-question
##### !answer

restaurants[1]["address"]

##### !end-answer
##### !hint

Use `[]` syntax with double-quotes where needed.

Examples:

- `some_list[0]`
- `some_dictionary["some key"]`

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: WfX3l1
* title: Nested Data and Nested Loops
### !question

Implement `get_restaurant_addresses()`. This method takes in one parameter, `restaurants`. The method should return a list of restaurant addresses, which are strings.

Here are the tests:

```python
def test_get_restaurant_addresses():
    restaurants = [
        {
            "address": "1299 Dough Ave N"
        },
        {
            "address": "6501 Island St SE"
        },
        {
            "address": "12543 Sushi Way NE"
        }
    ]
    addresses = get_restaurant_addresses(restaurants)

    assert addresses == ["1299 Dough Ave N",
                         "6501 Island St SE", "12543 Sushi Way NE"]


def test_get_restaurant_addresses_no_restaurants():
    no_addresses = get_restaurant_addresses([])

    assert no_addresses == []
```

### !end-question
### !tests
```python
import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_get_restaurant_addresses(self):
        restaurants = [
            {
                "address": "1299 Dough Ave N"
            },
            {
                "address": "6501 Island St SE"
            },
            {
                "address": "12543 Sushi Way NE"
            }
        ]
        addresses = get_restaurant_addresses(restaurants)
        self.assertEqual(addresses, ["1299 Dough Ave N",
                                     "6501 Island St SE", "12543 Sushi Way NE"])

    def test_get_restaurant_addresses_no_restaurants(self):
        no_addresses = get_restaurant_addresses([])

        self.assertEqual(no_addresses, [])
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def get_restaurant_addresses(restaurants):
    addresses = []
    for restaurant in restaurants:
        addresses.append(restaurant["address"])
    return addresses
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 3 -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: 99WiYg
* title: Nested Data and Nested Loops
##### !question

What is the syntax to get `"Lizzie"` from `student_groups`?

```python
students = [
    ["Michelle", "Beyonce", "Kelly"],
    ["Luke", "Leia", "Han"],
    ["Gordon", "Lizzie", "Miranda"]
]
```

Use `[]` syntax with double-quotes where needed.

##### !end-question
##### !answer

students[2][1]

##### !end-answer
##### !hint

Use `[]` syntax with double-quotes where needed.

Examples:

- `some_list[0]`
- `some_dictionary["some key"]`

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 4 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: UOoCrY
* title: Nested Data and Nested Loops
##### !question

Implement `get_student_names()`. This method takes in one parameter, `student_groups`. The method should return a list of student names, which are strings.

Here are the tests:

```python
def test_get_student_names():
    students = [
        ["Michelle", "Beyonce", "Kelly"],
        ["Luke", "Leia", "Han"],
        ["Gordon", "Lizzie", "Miranda"]
    ]

    names = get_student_names(students)

    assert names == ["Michelle", "Beyonce", "Kelly", "Luke",
                     "Leia", "Han", "Gordon", "Lizzie", "Miranda"]


def test_get_student_names_no_names():
    no_names = get_student_names([])
    assert no_names == []
```

##### !end-question
##### !tests
```python
import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_get_student_names(self):
        students = [
            ['Michelle', 'Beyonce', 'Kelly'],
            ['Luke', 'Leia', 'Han'],
            ['Gordon', 'Lizzie', 'Miranda']
        ]
        names = get_student_names(students)
        self.assertEqual(
            names, ['Michelle', 'Beyonce', 'Kelly', 'Luke', 'Leia', 'Han', 'Gordon', 'Lizzie', 'Miranda'])

    def test_get_student_names_no_names(self):
        no_names = get_student_names([])

        self.assertEqual(no_names, [])
```
##### !end-tests
### !explanation

An example of a working implementation:

```python
def get_student_names(student_groups):
    names = []
    for group in student_groups:
        for student in group:
            names.append(student)
    return names
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 5 -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: 613ccf11-e7e6-4fad-a1b1-6a962bcd8967
* title: Nested Data and Nested Loops
##### !question

What is the syntax to get `"University of Washington"` from `schools`?

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
```

Use `[]` syntax with double-quotes where needed.

##### !end-question
##### !answer

schools["school 2"]["name"]

##### !end-answer
##### !hint

Use `[]` syntax with double-quotes where needed.

Examples:

- `some_list[0]`
- `some_dictionary["some key"]`

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 6 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: b54addb3-48b0-462a-9f6a-f9b749fba39f
* title: Nested Data and Nested Loops
##### !question

Implement `get_school_names()`. This method takes in one parameter, `schools`. The method should return a list of school names, which are strings.

Here are the tests:

```python
def test_get_school_names():
    schools = {
        "school 1": {
            "name": "Western Barkington University",
            "city": "Barkingham"
        },
        "school 2": {
            "name": "University of Barkington",
            "city": "Beattle"
        },
        "school 3": {
            "name": "Barkington State University",
            "city": "Pullbark"
        }
    }

    names = get_school_names(schools)

    assert names == ["Western Barkington University",
                     "University of Barkington", "Barkington State University"]


def test_get_school_names_no_names():
    no_names = get_school_names({})
    assert no_names == []
```

##### !end-question
##### !tests
```python
import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_get_school_names(self):
        schools = {
            "school 1": {
                "name": "Western Barkington University",
                "city": "Barkingham"
            },
            "school 2": {
                "name": "University of Barkington",
                "city": "Beattle"
            },
            "school 3": {
                "name": "Barkington State University",
                "city": "Pullbark"
            }
        }
        names = get_school_names(schools)
        self.assertEqual(
            names, ["Western Barkington University",
                    "University of Barkington", "Barkington State University"])

    def test_get_school_names_no_names(self):
        no_names = get_school_names({})

        self.assertEqual(no_names, [])
```
##### !end-tests
### !explanation

An example of a working implementation:

```python
def get_school_names(schools):
    names = []
    for school_num in schools:
        names.append(schools[school_num]["name"])
    return names
```

Another example of a working implementation:

```python
def get_school_names(schools):
    names = []
    for school_num, school in schools.items():
        names.append(school["name"])
    return names
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 7 -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: Q9vx6M
* title: Nested Data and Nested Loops
##### !question

It's karaoke night!

What is the syntax to get `"Jolene"` from `karaoke_queue`?

```python
karaoke_queue = {
  "Rajan": ["I Want It That Way", "Jolene"],
  "Akira": ["Return of the Mack", "Mr. Brightside"],
  "Linh": ["Say My Name", "Since You Been Gone"]
}
```

Use `[]` syntax with double-quotes where needed.

##### !end-question
##### !answer

karaoke_queue["Rajan"][1]

##### !end-answer
##### !hint

Use `[]` syntax with double-quotes where needed.

Examples:

- `some_list[0]`
- `some_dictionary["some key"]`

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 8 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: 1VNr86
* title: Nested Data and Nested Loops
##### !question

It's karaoke night!

Implement `get_song_list()`. This method takes in one parameter, `karaoke_queue`. The method should return a list of song titles, which are strings.

Here are the tests:

```python
def test_get_song_list():
    karaoke_queue = {
        "Rajan": ["I Want It That Way", "Jolene"],
        "Akira": ["Return of the Mack", "Mr. Brightside"],
        "Linh": ["Say My Name", "Since You Been Gone"]
    }

    song_list = get_song_list(karaoke_queue)

    assert song_list == ["I Want It That Way", "Jolene", "Return of the Mack",
                         "Mr. Brightside", "Say My Name", "Since You Been Gone"]


def test_get_song_list_no_songs():
    no_queue = get_song_list({})
    assert no_queue == []
```

##### !end-question
##### !tests
```python
import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_get_song_list(self):
        karaoke_queue = {
            "Rajan": ["I Want It That Way", "Jolene"],
            "Akira": ["Return of the Mack", "Mr. Brightside"],
            "Linh": ["Say My Name", "Since You Been Gone"]
        }
        song_list = get_song_list(karaoke_queue)
        self.assertEqual(
            song_list, ["I Want It That Way", "Jolene", "Return of the Mack",
                        "Mr. Brightside", "Say My Name", "Since You Been Gone"])

    def test_get_song_list_no_songs(self):
        no_queue = get_song_list({})

        self.assertEqual(no_queue, [])
```
##### !end-tests
### !explanation

An example of a working implementation:

```python
def get_song_list(karaoke_queue):
    song_list = []
    for performer, performer_queue in karaoke_queue.items():
        for song in performer_queue:
            song_list.append(song)
    return song_list
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->
