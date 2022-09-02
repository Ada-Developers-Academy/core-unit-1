# Problem Set: Higher Order Functions

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: code-snippet
* language: python3.6
* id: 36789c28-3e3c-4d4e-9a4c-456cd1cd691d
* title: Higher Order Functions
<!-- * points: [1] (optional, the number of points for scoring as a checkpoint) -->
<!-- * topics: [python, pandas] (Checkpoints only, optional the topics for analyzing points) -->

##### !question

Imagine you have a list of dictionaries that represents the words and their score in the Adagrams game. Write a function `get_max_word` that takes a list of word dictionaries. You should use the `max` function with the `key` parameter such that the `get_max_word` function returns the word dictionary with the highest score. 

In the case of a tie, the function should return the first element it sees.

In the case of an empty list, it should return `None`.

Example inputs and outputs:

| input | output | 
| -- | -- |
|`[{"word": "hi", "score": 5}, {"word": "how", "score": 9}, {"word": "are", "score": 3}, {"word": "you", "score": 6}]`|`{"word": "how", "score": 9}`|
|`[{"word": "ada", "score": 4}, {"word": "roar", "score": 4}]`| `{"word": "ada", "score": 4}`|
|`[{"word": "how", "score": 9}]`|`[{"word": "how", "score": 9}]`|
||
|`[]`| None|
##### !end-question

##### !placeholder

```py
def get_max_word(words):
    pass
```

##### !end-placeholder

##### !tests

```py
import unittest
import main as p

class test_max_word(unittest.TestCase):
    def test_nominal(self):
        words = [{"word": "hi", "score": 5}, {"word": "how", "score": 9}, {"word": "are", "score": 3}, {"word": "you", "score": 6}]

        result = {"word": "how", "score": 9}

        self.assertEqual(result,p.get_max_word(words))

    def test_single_word(self):
        words = [ {"word": "how", "score": 9}]

        result = {"word": "how", "score": 9}

        self.assertEqual(result,p.get_max_word(words))

    def test_tie(self):
        words = [ {"word": "ada", "score": 4}, {"word": "roar", "score": 4}]

        result = {"word": "ada", "score": 4}

        self.assertEqual(result,p.get_max_word(words))

    def test_empty(self):
        words = []

        result = None

        self.assertEqual(result,p.get_max_word(words))
```

##### !end-tests

<!-- other optional sections -->
<!-- !hint - !end-hint (markdown, hidden, students click to view) -->
<!-- !rubric - !end-rubric (markdown, instructors can see while scoring a checkpoint) -->
<!-- !explanation - !end-explanation (markdown, students can see after answering correctly) -->
##### !explanation
An example solution:

```py
def get_max_word(words):
    if not words:
        return None
    
    return max(words, key=lambda word:word["score"])
```
##### !end-explanation

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->