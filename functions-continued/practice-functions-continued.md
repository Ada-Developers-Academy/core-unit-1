# Practice: Functions, Continued

## Directions

Complete all questions below.

## Practice

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: bR7Zx6
* title: Functions, continued
### !question

Create a function named `adds_five`. It has one parameter, `num`. The function should add `5` to `num`, and return the sum.

| Example arguments | Example return value |
| ----------------- | -------------------- |
| `22`              | `27`                 |
| `0`               | `5`                  |

### !end-question
### !placeholder

```python
def adds_five(num):
    pass
```
### !end-placeholder
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
    def test_adds_five(self):
        self.assertEqual(adds_five(22), 27)
        self.assertEqual(adds_five(0), 5)
```
### !end-tests
### !explanation

Two examples of a working implementation:

```python
def adds_five(num):
    sum = num + 5
    return sum
```

```python
def adds_five(num):
    return num + 5
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: sDzsr2
* title: Functions, continued
### !question

Create a function named `doubles_and_adds_two`. It has one parameter, `num`. The function should add `num` + `num` + `2`, and return the sum.

| Example arguments | Example return value |
| ----------------- | -------------------- |
| `50`              | `102`                |
| `0`               | `2`                  |

### !end-question
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
    def test_doubles_and_adds_two(self):
        self.assertEqual(doubles_and_adds_two(50), 102)
        self.assertEqual(doubles_and_adds_two(0), 2)
```
### !end-tests
### !explanation

Two examples of a working implementation:

```python
def adds_five(num):
    sum = num + num + 2
    return sum
```

```python
def adds_five(num):
    return (num * 2) + 2
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 3 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: 3psiX0
* title: Functions, continued
### !question

Create a function named `doubles`. It has one parameter, `input`. If `input` is a number, the function should double `input` and return it. If `input` is a string, the function should concatenate `input` twice together.

| Example arguments | Example return value           |
| ----------------- | ------------------------------ |
| `3`               | `6`                            |
| `4`               | `8`                            |
| `"4"`             | `"44"`                         |
| `"Hello, World!"` | `"Hello, World!Hello, World!"` |

Note: In Learn code challenges, the phrase `input` is highlighted because it is the name of a Python function. We can still trust `input` to be a regular variable name in this context.

### !end-question
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
    def test_doubles(self):
        self.assertEqual(doubles(3), 6)
        self.assertEqual(doubles(4), 8)
        self.assertEqual(doubles("4"), "44")
        self.assertEqual(doubles("Hello, World!"), "Hello, World!Hello, World!")
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def doubles(input):
    return input + input
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 4 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: tRuqax
* title: Functions, continued
### !question

Create a function named `get_third_place`. It has one parameter, `finalists`. Assuming that the first item in `finalists` is first place and the second item in `finalists` is second place, return the finalist in third place.

| Example arguments                                   | Example return value |
| --------------------------------------------------- | -------------------- |
| `["Pikachu", "Bulbasaur", "Squirtle", "Charizard"]` | `"Squirtle"`         |
| `["Bulbasaur", "Squirtle", "Charizard"]`            | `"Charizard"`        |

### !end-question
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
    def test_get_third_place(self):
        self.assertEqual(get_third_place(["Pikachu", "Bulbasaur", "Squirtle", "Charizard"]), "Squirtle")
        self.assertEqual(get_third_place(["Bulbasaur", "Squirtle", "Charizard"]), "Charizard")
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def get_third_place(finalists):
    return finalists[2]
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 5 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: wrDWIg
* title: Functions, continued
### !question

Create a function named `get_third_place`. It has one parameter, `finalists`. If there are at least three finalists, return the finalist in third place. If there aren't at least three finalists, return `None`.

| Example arguments                                   | Example return value |
| --------------------------------------------------- | -------------------- |
| `["Pikachu", "Bulbasaur", "Squirtle", "Charizard"]` | `"Squirtle"`         |
| `["Squirtle", "Charizard"]`                         | `None`               |
| `[]`                                                | `None`               |

### !end-question
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
    def test_get_third_place(self):
        self.assertEqual(get_third_place(["Pikachu", "Bulbasaur", "Squirtle", "Charizard"]), "Squirtle")
        self.assertEqual(get_third_place(["Squirtle", "Charizard"]), None)
        self.assertEqual(get_third_place([]), None)
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def get_third_place(finalists):
    if len(finalists) < 3:
        return None
    else:
        return finalists[2]
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 6 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: dKxTe7
* title: Functions, continued
### !question

Create a function named `compare_votes`. It has two parameters, `candidate_a` and `candidate_b` (short for "candidate"). Both `candidate_a` and `candidate_b` will be dictionaries that look like this:

```python
{
    "name": "Mx. Candidate Name",
    "votes": 5
}
```

Compare the votes inside `candidate_a` and `candidate_b`. Find the candidate with more votes, and return their name.

| Example `candidate_a`              | Example `candidate_b`                | Example return value |
| ---------------------------------- | ------------------------------------ | -------------------- |
| `{"name": "Pikachu", "votes": 25}` | `{"name": "Bulbasaur", "votes": 24}` | `"Pikachu"`          |
| `{"name": "Pikachu", "votes": 0}`  | `{"name": "Bulbasaur", "votes": 1}`  | `"Bulbasaur"`        |

### !end-question
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
    def test_compare_votes(self):
        self.assertEqual(compare_votes({"name": "Pikachu", "votes": 25}, {"name": "Bulbasaur", "votes": 24}), "Pikachu")
        self.assertEqual(compare_votes({"name": "Pikachu", "votes": 0}, {"name": "Bulbasaur", "votes": 1}), "Bulbasaur")
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def compare_votes(candidate_a, candidate_b):
    if candidate_a["votes"] > candidate_b["votes"]:
        return candidate_a["name"]
    else:
        return candidate_b["name"]
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 7 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: 62GIlb
* title: Functions, continued
### !question

Create a function named `compare_ids`. It has two parameters, `candidate_a` and `candidate_b` (short for "candidate"). Both `candidate_a` and `candidate_b` will be dictionaries that look like this:

```python
{
    "id": 5
    "name": "Mx. Candidate Name",
}
```

Compare the IDs inside `candidate_a` and `candidate_b`. Find the candidate that has an ID with a smaller numerical value, and return the candidate dictionary itself.

| Example `candidate_a`                | Example `candidate_b`                  | Example return value             |
| ------------------------------- | --------------------------------- | -------------------------------- |
| `{"id": 25, "name": "Pikachu"}` | `{"id": 1, "name": "Bulbasaur"}`  | `{"id": 1, "name": "Bulbasaur"}` |
| `{"id": 25, "name": "Pikachu"}` | `{"id": 26, "name": "Bulbasaur"}` | `{"id": 25, "name": "Pikachu"}`  |

### !end-question
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
    def test_compare_ids(self):
        self.assertEqual(compare_ids({"id": 25, "name": "Pikachu"}, {"id": 1, "name": "Bulbasaur"}), {"id": 1, "name": "Bulbasaur"})
        self.assertEqual(compare_ids({"id": 25, "name": "Pikachu"}, {"id": 26, "name": "Pikachu"}), {"id": 25, "name": "Pikachu"})
```
### !end-tests
### !explanation

An example of a working implementation. Note how this solution does not have an `else` condition. With this particular logic, if `candidate_a["id"] < candidate_b["id"]` is `True`, it will exit the function by returning `candidate_a`. If `candidate_a["id"] < candidate_b["id"]` is `False`, then there is no other return value besides `candidate_b`.

```python
def compare_ids(candidate_a, candidate_b):
    if candidate_a["id"] < candidate_b["id"]:
        return candidate_a
    return candidate_b
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

### !callout-info

## Comparing Strings

Python supports comparing strings with `<`, `>`, etc. Python compares strings alphabetically. Strings that begin with `"A"` are less than `"Z"`. Python orders capital letters as less than lowercase letters, so `"A"` is less than `"a"`. Consider the table below.

| Code                 | Output  |
| -------------------- | ------- |
| `"Apple" < "Banana"` | `True`  |
| `"Apple" > "Banana"` | `False` |
| `"Banana" < "Apple"` | `False` |
| `"Banana" > "Apple"` | `True`  |
| `"Apple" < "apple"`  | `True`  |
| `"Apple" > "apple"`  | `False` |

What's going on? In modern computing, each character is given a numerical Unicode value. Unicode is a standard for representing all characters and emojis across different platforms. Follow your curiosity!

### !end-callout

<!-- Question 8 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: kULfEf
* title: Functions, continued
### !question

Create a function named `compare_alphabetically`. It has two parameters, `word_a` and `word_b`, which will be strings. Compare `word_a` and `word_b` and determine which one comes first alphabetically. Follow these rules:

- Assume all characters in both words use the English alphabet
- Order uppercase letters before lowercase letters

Return `word_a` if `word_a` comes first alphabetically. Return `word_b` if `word_b` comes first. Return either `word_a` or `word_b` if they are identical strings.

| Example `word_a` | Example `word_b` | Example return value |
| ---------------- | ---------------- | -------------------- |
| `"Pikachu"`      | `"Bulbasaur"`    | `"Bulbasaur"`        |
| `"Bulbasaur"`    | `"Pikachu"`      | `"Bulbasaur"`        |
| `"Pikachu"`      | `"Pikachu"`      | `"Pikachu"`          |
| `"Pikachu"`      | `"pikachu"`      | `"Pikachu"`          |

### !end-question
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
    def test_compare_alphabetically(self):
        self.assertEqual(compare_alphabetically("Pikachu", "Bulbasaur"), "Bulbasaur")
        self.assertEqual(compare_alphabetically("Bulbasaur", "Bulbasaur"), "Bulbasaur")
        self.assertEqual(compare_alphabetically("Pikachu", "Pikachu"), "Pikachu")
        self.assertEqual(compare_alphabetically("Pikachu", "pikachu"), "Pikachu")
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def compare_alphabetically(word_a, word_b):
    if word_a < word_b:
        return word_a
    else:
        return word_b
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 9 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: kJYUgL
* title: Functions, continued
### !question

Create a function named `compare_values`. It has two parameters, `a` and `b`, which will be numbers. Compare `a` against `b`. If `a` is less than `b`, return `-1`. If `a` is equal to `b`, return `0`. If `a` is greater than `b`, return `1`.

| Example `a` | Example `b` | Example return value |
| ----------- | ----------- | -------------------- |
| `999`       | `-999`      | `1`                  |
| `-5`        | `-5`        | `0`                  |
| `80.5`      | `80.6`      | `-1`                 |

### !end-question
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
    def test_compare_values(self):
        self.assertEqual(compare_values(999, -999), 1)
        self.assertEqual(compare_values(-5, -5), 0)
        self.assertEqual(compare_values(80.5, 80.6), -1)
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def compare_values(a, b):
    if a < b:
        return -1
    elif a == b:
        return 0
    else:
        return 1
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 10 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: Sl6onl
* title: Functions, continued
### !question

Create a function named `fizz_buzz`. It has one parameter, `num`.

If `num` is a multiple of 3, it should return `"Fizz"`. If `num` is a multiple of 5, it should return `"Buzz"`. If `num` is a multiple of 3 _and_ 5, it should return `"FizzBuzz"`. If `num` is _not_ a multiple of either 3 or 5, it should return `num`.

| Example `num` | Example return value |
| ------------- | -------------------- |
| `1`           | `1`                  |
| `2`           | `2`                  |
| `3`           | `"Fizz"`             |
| `327`         | `"Fizz"`             |
| `5`           | `"Buzz"`             |
| `560`         | `"Buzz"`             |
| `15`          | `"FizzBuzz"`         |
| `450`         | `"FizzBuzz"`         |

### !end-question
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz(1), 1)
        self.assertEqual(fizz_buzz(3), "Fizz")
        self.assertEqual(fizz_buzz(327), "Fizz")
        self.assertEqual(fizz_buzz(5), "Buzz")
        self.assertEqual(fizz_buzz(560), "Buzz")
        self.assertEqual(fizz_buzz(15), "FizzBuzz")
        self.assertEqual(fizz_buzz(450), "FizzBuzz")
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def fizz_buzz(num):
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->
