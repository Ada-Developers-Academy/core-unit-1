# Problem Set: Higher Order Functions

## Directions

Complete all questions below.

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: multiple-choice
* id: 2a948f45-615e-4e79-8f90-260bd231ba28
* title: Higher Order Functions

##### !question

The following is the correct syntax for passing a keyword argument when calling a function.

##### !end-question

##### !options

a| function_name(argument1, parameter2)
b| [Option 2]
c| [Option 3, etc]

##### !end-options

##### !answer

b|

##### !end-answer

<!-- other optional sections -->
<!-- !hint - !end-hint (markdown, hidden, students click to view) -->
<!-- !rubric - !end-rubric (markdown, instructors can see while scoring a checkpoint) -->
<!-- !explanation - !end-explanation (markdown, students can see after answering correctly) -->

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: code-snippet
* language: python3.6
* id: 7bbe5762-40e2-40f3-8af5-b6d3786ea57d
* title: Higher Order Functions
<!-- * points: [1] (optional, the number of points for scoring as a checkpoint) -->
<!-- * topics: [python, pandas] (Checkpoints only, optional the topics for analyzing points) -->

##### !question

Imagine you have a list of dictionaries that represents the words and their score in the Adagrams game. Write a function `get_max_word` that takes a list of word dictionaries. You should use the `max` function with the `key` parameter such that the `get_max_word` function returns the word dictionary with the highest score. 

You should also write a named function `get_score` that is passed to the `key` parameter. In the next code challenge, you will be asked to use a lambda expression.

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
def get_score(word):
    pass

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
def get_score(word):
    return word["score"]

def get_max_word(words):
    if not words:
        return None
    
    return max(words, key=get_score)
```
##### !end-explanation

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: code-snippet
* language: python3.6
* id: f1b9b711-4a92-4612-9147-7e305cd89c17
* title: Higher Order Functions
<!-- * points: [1] (optional, the number of points for scoring as a checkpoint) -->
<!-- * topics: [python, pandas] (Checkpoints only, optional the topics for analyzing points) -->

##### !question

Imagine you have a list of dictionaries that represents the words and their score in the Adagrams game. Write a function `get_max_word` that takes a list of word dictionaries. You should use the `max` function with the `key` parameter such that the `get_max_word` function returns the word dictionary with the highest score. 

Your solution should use a lambda expression.

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
    
    return max(words, key=lambda word: word["score"])
```
##### !end-explanation

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->

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

Imagine you have a list of dictionaries that represents the words and their score in the Adagrams game. Write a function `sort_words` that takes a list of word dictionaries. You should use the `sorted` function with the `key` parameter such that the `sort_words` function returns a list of word dictionaries sorted alphabetically by `"word"`. 

In the case of an empty list, it should return `None`.

Example inputs and outputs:

| input | output | 
| -- | -- |
|`[{"word": "hi", "score": 5}, {"word": "how", "score": 9}, {"word": "are", "score": 3}, {"word": "you", "score": 6}]`|`[{"word": "are", "score": 3}, {"word": "hi", "score": 5}, {"word": "how", "score": 9}, {"word": "you", "score": 6}]`|
|`[{"word": "roar", "score": 4}, {"word": "ada", "score": 4}]`| `[{"word": "ada", "score": 4}, {"word": "roar", "score": 4}]`|
|`[{"word": "how", "score": 9}]`|`[{"word": "how", "score": 9}]`|
||
|`[]`| None|
##### !end-question

##### !placeholder

```py
def sort_words(words):
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

        result = [{"word": "are", "score": 3}, {"word": "hi", "score": 5}, {"word": "how", "score": 9}, {"word": "you", "score": 6}]

        self.assertEqual(result,p.sort_words(words))

    def test_single_word(self):
        words = [ {"word": "how", "score": 9}]

        result = [{"word": "how", "score": 9}]

        self.assertEqual(result,p.sort_words(words))

    def test_2_words(self):
        words = [{"word": "roar", "score": 4}, {"word": "ada", "score": 4}]

        result = [{"word": "ada", "score": 4}, {"word": "roar", "score": 4}]

        self.assertEqual(result,p.sort_words(words))

    def test_empty(self):
        words = []

        result = None

        self.assertEqual(result,p.sort_words(words))
```

##### !end-tests

<!-- other optional sections -->
<!-- !hint - !end-hint (markdown, hidden, students click to view) -->
<!-- !rubric - !end-rubric (markdown, instructors can see while scoring a checkpoint) -->
<!-- !explanation - !end-explanation (markdown, students can see after answering correctly) -->
##### !explanation
An example solution:

```py
def sort_words(words):
    if not words:
        return None
    
    return sorted(words, key=lambda word: word["word"])
```
##### !end-explanation

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->