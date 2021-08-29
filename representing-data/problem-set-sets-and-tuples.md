# Problem Set: Sets

## Directions

Complete all questions below.

## Practice

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: checkbox
* id: 2d93bfd4-1847-4514-9810-acb3f3db7d22
* title: Sets
<!-- * points: [1] (optional, the number of points for scoring as a checkpoint) -->
<!-- * topics: [python, pandas] (optional the topics for analyzing points) -->

##### !question

Check the expressions that evaluate to `{'apple', 'orange', 'banana'}` with the elements in any order.

##### !end-question

##### !options

* ```{'apple', 'apple', 'orange', 'orange', 'banana', 'banana'}```
* ```set(['apple', 'apple', 'orange', 'orange', 'banana', 'banana'])```
* ```{'apple', 'orange'}.union({'banana'})```
* ```{'apple', 'orange', 'banana'}.union({'melon', 'peach'})```
* ```{'apple', 'orange', 'banana'} | {'banana'}```
* ```{'apple', 'orange', 'banana', 'melon', 'peach'}.intersection({'apple', 'orange', 'banana'})```
* ```{'apple', 'orange', 'banana'} & {'melon', 'peach'}```

##### !end-options

##### !answer

* ```{'apple', 'apple', 'orange', 'orange', 'banana', 'banana'}```
* ```set(['apple', 'apple', 'orange', 'orange', 'banana', 'banana'])```
* ```{'apple', 'orange'}.union({'banana'})```
* ```{'apple', 'orange', 'banana'} | {'banana'}```
* ```{'apple', 'orange', 'banana', 'melon', 'peach'}.intersection({'apple', 'orange', 'banana'})```

##### !end-answer

##### !explanation

* `.union` and `|` are two syntax methods to create a set union.
* `.intersection` and `&` are two syntax methods to create a set intersection.

##### !end-explanation
<!-- !explanation - !end-explanation (markdown, students can see after answering correctly) -->``

<!-- other optional sections -->
<!-- !hint - !end-hint (markdown, hidden, students click to view) -->
<!-- !rubric - !end-rubric (markdown, instructors can see while scoring a checkpoint) -->
<!-- !explanation - !end-explanation (markdown, students can see after answering correctly) -->``

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: checkbox
* id: dc3885d4-35f0-4657-a574-f8ca79fac278
* title: Sets
<!-- * points: [1] (optional, the number of points for scoring as a checkpoint) -->
<!-- * topics: [python, pandas] (optional the topics for analyzing points) -->

##### !question

Check the expressions that evaluate to `True`.

##### !end-question

##### !options

* `{'apple', 'orange', 'banana'} < {'apple', 'orange', 'banana', 'melon', 'peach'} `
* `{'apple', 'orange', 'banana'} > {'apple', 'orange', 'banana', 'melon', 'peach'} `
* `{'apple', 'orange', 'banana'}.disjoint({'melon', 'peach'})`
* `{'apple', 'orange', 'banana'}.disjoint({'apple', 'orange', 'banana', 'melon', 'peach'})`

##### !end-options

##### !answer

* `{'apple', 'orange', 'banana'} < {'apple', 'orange', 'banana', 'melon', 'peach'} `
* `{'apple', 'orange', 'banana'}.disjoint({'melon', 'peach'})`

##### !end-answer

* `set_a < set_b` evaluates to `True` if `set_a` is a subset of `set_b`.
* A set is disjoint with another set if they have no overlapping elements.


### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->

### !challenge

* type: code-snippet
* language: python3.6
* id: 7dd15f30-291b-4d04-9560-b041c0718279
* title: sets

##### !question

Sandra is having a party and has three recipes she wants to make.  She has created a list of ingredients for each recipe:  

```python
bruschetta = ["bread", "olive oil", "garlic", "tomato", "basil", "balsamic vinegar", "salt"]
pesto_pasta = ["pasta", "olive oil", "garlic", "basil", "parmesan", "pine nuts"]
salsa = ["tomato", "onion", "garlic", "salt", "green onion", "cilantro", "jalapeno"]
```  

Write a function `shopping_list` that Sandra can use to create a shopping list of all of the ingredients that she will need to purchase.  She wants each item to show up only once in the list.  

| Example arguments | Example return value (order does not matter) |
| ----------------- | -------------------- |
| `bruschetta`, `pesto_pasta`, `salsa`              | `['parmesan', 'basil', 'bread', 'pine nuts', 'garlic', 'jalapeno', 'tomato', 'pasta', 'green onion', 'olive oil', 'cilantro', 'salt', 'onion', 'balsamic vinegar']`                |
| `[1, 2, 3, 4]`, `[5, 6, 7, 8]`, `[9, 10, 11, 12]`              | `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]`                  |

```

##### !end-question

##### !placeholder

```python

def shopping_list(recipe1, recipe2, recipe3):
    pass

```

##### !end-placeholder

##### !tests
```python

from main import shopping_list
import unittest

class TestPython1(unittest.TestCase):
    def test_example_recipes(self):
        bruschetta = ["bread", "olive oil", "garlic", "tomato", "basil", "balsamic vinegar", "salt"]
        pesto_pasta = ["pasta", "olive oil", "garlic", "basil", "parmesan", "pine nuts"]
        salsa = ["tomato", "onion", "garlic", "salt", "green onion", "cilantro", "jalapeno"]
        answer = ['parmesan', 'basil', 'bread', 'pine nuts', 'garlic', 'jalapeno', 'tomato', 'pasta', 'green onion', 'olive oil', 'cilantro', 'salt', 'onion', 'balsamic vinegar']
        result = shopping_list(bruschetta, pesto_pasta, salsa)
        result.sort()
        answer.sort()

        self.assertEqual(result, answer)

    def test_numbers(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [4, 5, 6, 7, 8]
        list3 = [7, 8, 9, 10, 11]
        result = shopping_list(list1, list2, list3)
        result.sort()
        answer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        answer.sort()
        self.assertEqual(result, answer)

    def test_all_equal(self):
        bruschetta = ["bread", "olive oil", "garlic", "tomato", "basil", "balsamic vinegar", "salt"]
        result = shopping_list(bruschetta, bruschetta, bruschetta)
        result.sort()
        bruschetta.sort()
        self.assertEqual(result, bruschetta)

    def test_no_overlap(self):
        list1 = [1, 2, 3, 4]
        list2 = [5, 6, 7, 8]
        list3 = [9, 10, 11, 12]
        result = shopping_list(list1, list2, list3)
        result.sort()
        answer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        answer.sort()

        self.assertEqual(result, answer)

```
##### !end-tests

<!--optional-->
##### !explanation

##### !end-explanation

One possible solution:
```python

def shopping_list(recipe1, recipe2, recipe3):
    set1 = set(recipe1)
    set2 = set(recipe2)
    set3 = set(recipe3)
    result = set1 | set2 | set3
    return(list(result))


### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->