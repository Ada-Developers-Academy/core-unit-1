# Question moved from Intro to Tests topic, may be useful in Exception Handling topic

<!-- Question 17 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: a18259ec-848d-4ec4-99c1-c6a71ec1fab7
* title: Intro to pytest

##### !question

Write a function to make the test pass. Use the information from the test to help determine what needs to be in the function body.

```python
def test_raises_zerodiv_error():
    with pytest.raises(ZeroDivisionError):
        run_mystery_algorithm()
```

##### !end-question
##### !tests

```py
import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_raises_zerodiv_error(self):
        with self.assertRaises(ZeroDivisionError):
            run_mystery_algorithm()
```

##### !end-tests
##### !hint

Read through the test. Determine:

- Which line is the "Act" step?
- What are the "Arrange" and "Assert" steps?
- In the "Act" step, what is the name of the function called? What are the arguments passed into it? How many arguments are there?
- What does this test assert?

Using this information, apply it to the function we need to write:

- The name of the function in the "Act" step is the function we're testing, and the function to define
- The number of arguments passed into this function is the number of parameters that the function signature needs
- Use the clues from the test syntax to understand what the intended outcome of this function is

##### !end-hint
### !explanation

An example of a working implementation:

```python
def run_mystery_algorithm():
    return 5/0
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->
