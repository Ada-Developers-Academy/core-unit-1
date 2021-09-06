# Problem Set: Sets and Tuples

## Directions

Complete all questions below.

## Practice

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- prettier-ignore-start -->

### !challenge

* type: checkbox
* id: 2d93bfd4-1847-4514-9810-acb3f3db7d22
* title: Sets and Tuples
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

<!-- prettier-ignore-end -->

<!-- ======================= END CHALLENGE ======================= -->

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- prettier-ignore-start -->

### !challenge

* type: checkbox
* id: dc3885d4-35f0-4657-a574-f8ca79fac278
* title: Sets and Tuples
<!-- * points: [1] (optional, the number of points for scoring as a checkpoint) -->
<!-- * topics: [python, pandas] (optional the topics for analyzing points) -->

##### !question

Check the expressions that evaluate to `True`.

##### !end-question

##### !options

* `{'apple', 'orange', 'banana'} < {'apple', 'orange', 'banana', 'melon', 'peach'} `
* `{'apple', 'orange', 'banana'} > {'apple', 'orange', 'banana', 'melon', 'peach'} `
* `{'apple', 'orange', 'banana'}.isdisjoint({'melon', 'peach'})`
* `{'apple', 'orange', 'banana'}.isdisjoint({'apple', 'orange', 'banana', 'melon', 'peach'})`

##### !end-options

##### !answer

* `{'apple', 'orange', 'banana'} < {'apple', 'orange', 'banana', 'melon', 'peach'} `
* `{'apple', 'orange', 'banana'}.isdisjoint({'melon', 'peach'})`

##### !end-answer

* `set_a < set_b` evaluates to `True` if `set_a` is a subset of `set_b`.
* A set is disjoint with another set if they have no overlapping elements.


### !end-challenge

<!-- prettier-ignore-end -->

<!-- ======================= END CHALLENGE ======================= -->

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- prettier-ignore-start -->

### !challenge

* type: code-snippet
* language: python3.6
* id: 7dd15f30-291b-4d04-9560-b041c0718279
* title: Sets and Tuples

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
| `[1, 2, 3, 4]`, `[5, 6, 7, 8]`, `[9, 10, 11, 12]`              | `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]`                  |

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

One possible solution:

```python
def shopping_list(recipe1, recipe2, recipe3):
    # build a unique set from each input (inputs are expected to be lists)
    set1 = set(recipe1)
    set2 = set(recipe2)
    set3 = set(recipe3)

    # find the union of all three sets
    result = set1 | set2 | set3

    # build a list from the result set to return
    return list(result)
```

##### !end-explanation

### !end-challenge

<!-- prettier-ignore-end -->

<!-- ======================= END CHALLENGE ======================= -->

### Gotta Catch (and Release) 'Em All!

In some parts of the world, bug collecting is very popular among children. Mady and Lesha live in such a region, and they love to explore their neighborhoods looking for interesting creepy-crawlies. Being good friends, they have a healthy rivalry, and are always trying to find rarer, more interesting bugs than the other!

It can be difficult to keep track of all the bugs they've encountered. Clearly, they can't keep all the bugs they find, so they keep notes about each bug as they find them, and then let the bugs go again. Being avid collectors, they have found _a lot_ of bugs!

Since they keep track of the bugs they find in lists (making note of each bug as it's caught), they have lots of duplicate information in their records, and it can be hard to compare their records about who has caught which bugs.

_We_ know that sets can help us manage data containing duplicates, so let's offer to write some code to help them manage their data!

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- prettier-ignore-start -->

### !challenge

* type: code-snippet
* language: python3.6
* id: 5e945f7a-fa92-423e-8b55-6a1dd2b22f87
* title: Sets and Tuples

##### !question

Mady and Lesha track their bug information in lists. They would love to know which unique bugs each has caught. They'd like to get some sort of insect index, sort of an InsectDex containing that unique information.

Assuming Mady and Lesha have caught the following bugs:

```python
mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]
lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]
```  

Write a function `make_insect_dex` that they can use to make an InsectDex for each of them. Remember that in the InsectDex, each insect should appear only once.

| Example arguments | Example return value (order does not matter) |
| ----------------- | -------------------- |
| `mady_bugs` | `{'lightning bug', 'caterpillar', 'ladybug', 'monarch butterfly', 'june bug', 'carpenter ant'}` |
| `lesha_bugs` | `{'stag beetle', 'earwig', 'millipede', 'pill bug', 'june bug', 'lightning bug', 'dragonfly'}`  |

##### !end-question

##### !placeholder

```python
def make_insect_dex(bug_list):
    pass
```

##### !end-placeholder

##### !tests

```python
import unittest
import main
from main import make_insect_dex

class TestMakeInsectDex(unittest.TestCase):

  def test_make_insect_dex_for_mady(self):
    mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]

    self.assertEqual(make_insect_dex(mady_bugs), {'lightning bug', 'caterpillar', 'ladybug', 'monarch butterfly', 'june bug', 'carpenter ant'})

  def test_make_insect_dex_for_lesha(self):
    lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]
    self.assertEqual(make_insect_dex(lesha_bugs), {'stag beetle', 'earwig', 'millipede', 'pill bug', 'june bug', 'lightning bug', 'dragonfly'})
```

##### !end-tests

##### !hint

Pay close attention to the types that are expected. Notice the literals used for `mady_bugs` and `lesha_bugs`, as well as the literals used to display the example return values. What is each type? Make sure the function is handling the expected input type and producing the expected result type.

##### !end-hint

##### !explanation

An example of a working implementation:

```python
def make_insect_dex(bug_list):
    # build a new unique set from the input
    # bug_list is expected to be a list possibly containing duplicates
    return set(bug_list)
```

##### !end-explanation

### !end-challenge

<!-- prettier-ignore-end -->

<!-- ======================= END CHALLENGE ======================= -->

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- prettier-ignore-start -->

### !challenge

* type: code-snippet
* language: python3.6
* id: 1df7dc4e-7858-470b-83c5-7e619a31cb18
* title: Sets and Tuples

##### !question

Mady and Lesha would love to know which bugs each has caught that the other hasn't!

Assuming Mady and Lesha have caught the following bugs:

```python
mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]
lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]
```  

Write a function `caught_only_by_first` that they can use to compare the bugs each has caught, so they can see the bugs that have only been caught by the first one of their data passed to the function.

| Example arguments | Example return value (order does not matter) |
| ----------------- | -------------------- |
| `mady_bugs, lesha_bugs` | `{'ladybug', 'monarch butterfly', 'carpenter ant', 'caterpillar'}` |
| `lesha_bugs, mady_bugs` | `{'millipede', 'stag beetle', 'earwig', 'pill bug', 'dragonfly'}`  |

##### !end-question

##### !placeholder

```python
def caught_only_by_first(first_list, second_list):
    pass
```

##### !end-placeholder

##### !tests

```python
import unittest
import main
from main import caught_only_by_first

class TestCaughtOnlyByFirst(unittest.TestCase):

  def test_caught_only_by_first_when_mady_is_first(self):
    mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]
    lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]

    self.assertEqual(caught_only_by_first(mady_bugs, lesha_bugs), {'ladybug', 'monarch butterfly', 'carpenter ant', 'caterpillar'})

  def test_caught_only_by_first_when_lesha_is_first(self):
    mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]
    lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]

    self.assertEqual(caught_only_by_first(lesha_bugs, mady_bugs), {'millipede', 'stag beetle', 'earwig', 'pill bug', 'dragonfly'})
```

##### !end-tests

##### !hint

Pay close attention to the types that are expected. Notice the literals used for `mady_bugs` and `lesha_bugs`, as well as the literals used to display the example return values. What is each type? Make sure the function is handling the expected input type and producing the expected result type.

##### !end-hint

##### !explanation

An example of a working implementation:

```python
def caught_only_by_first(first_list, second_list):
    # build a new unique set from each input
    # inputs are expected to be lists possibly containing duplicates
    first_set = set(first_list)
    second_set = set(second_list)

    # find result by removing anything from the second set from the first
    # notice this is order-dependent
    result = first_set - second_set

    # return the result set
    return result
```

##### !end-explanation

### !end-challenge

<!-- prettier-ignore-end -->

<!-- ======================= END CHALLENGE ======================= -->

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- prettier-ignore-start -->

### !challenge

* type: code-snippet
* language: python3.6
* id: e7a154a4-1f4d-4c2c-bb04-b88d978f3aba
* title: Sets and Tuples

##### !question

Mady and Lesha's bug excitement continues unabated! They know which bugs they caught that were distinct from one another, but would like to know which bugs they caught in common.

Assuming Mady and Lesha have caught the following bugs:

```python
mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]
lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]
```  

Write a function `caught_by_both` that they can use to find out which bugs were caught both by Mady and by Lesha.

| Example arguments | Example return value (order does not matter) |
| ----------------- | -------------------- |
| `mady_bugs, lesha_bugs` | `{'lightning bug', 'june bug'}` |
| `lesha_bugs, mady_bugs` | `{'lightning bug', 'june bug'}`  |

##### !end-question

##### !placeholder

```python
def caught_by_both(first_list, second_list):
    pass
```

##### !end-placeholder

##### !tests

```python
import unittest
import main
from main import caught_by_both

class TestCaughtByBoth(unittest.TestCase):

  def test_caught_by_both_when_mady_is_first(self):
    mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]
    lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]

    self.assertEqual(caught_by_both(mady_bugs, lesha_bugs), {'lightning bug', 'june bug'})

  def test_caught_by_both_when_lesha_is_first(self):
    mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]
    lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]

    self.assertEqual(caught_by_both(lesha_bugs, mady_bugs), {'lightning bug', 'june bug'})
```

##### !end-tests

##### !hint

Pay close attention to the types that are expected. Notice the literals used for `mady_bugs` and `lesha_bugs`, as well as the literals used to display the example return values. What is each type? Make sure the function is handling the expected input type and producing the expected result type.

##### !end-hint

##### !explanation

An example of a working implementation:

```python
def caught_by_both(first_list, second_list):
    # build a new unique set from each input
    # inputs are expected to be lists possibly containing duplicates
    first_set = set(first_list)
    second_set = set(second_list)

    # find result by finding where the sets intersect (overlap)
    result = first_set & second_set

    # return the result set
    return result
```

##### !end-explanation

### !end-challenge

<!-- prettier-ignore-end -->

<!-- ======================= END CHALLENGE ======================= -->

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- prettier-ignore-start -->

### !challenge

* type: code-snippet
* language: python3.6
* id: c43f2ad4-b5b4-428b-8899-438decd86d2f
* title: Sets and Tuples

##### !question

Mady and Lesha are really enjoying comparing their adventures! But now they'd love to know how many kinds of bugs they've caught in combination. They're pretty sure that they've caught a lot more bugs together than they have individually!

Assuming Mady and Lesha have caught the following bugs:

```python
mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]
lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]
```  

Write a function `caught_together` that they can use to find all the bugs that they've caught: either only by Mady, only by Lesha, or by both of them!

| Example arguments | Example return value (order does not matter) |
| ----------------- | -------------------- |
| `mady_bugs, lesha_bugs` | `{'pill bug', 'stag beetle', 'ladybug', 'monarch butterfly', 'caterpillar', 'earwig', 'lightning bug', 'dragonfly', 'millipede', 'june bug', 'carpenter ant'}` |
| `lesha_bugs, mady_bugs` | `{'pill bug', 'stag beetle', 'ladybug', 'monarch butterfly', 'caterpillar', 'earwig', 'lightning bug', 'dragonfly', 'millipede', 'june bug', 'carpenter ant'}`  |

##### !end-question

##### !placeholder

```python
def caught_together(first_list, second_list):
    pass
```

##### !end-placeholder

##### !tests

```python
import unittest
import main
from main import caught_together

class TestCaughtTogether(unittest.TestCase):

  def test_caught_together_when_mady_is_first(self):
    mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]
    lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]

    self.assertEqual(caught_together(mady_bugs, lesha_bugs), {'pill bug', 'stag beetle', 'ladybug', 'monarch butterfly', 'caterpillar', 'earwig', 'lightning bug', 'dragonfly', 'millipede', 'june bug', 'carpenter ant'})

  def test_caught_together_when_lesha_is_first(self):
    mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]
    lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]

    self.assertEqual(caught_together(lesha_bugs, mady_bugs), {'pill bug', 'stag beetle', 'ladybug', 'monarch butterfly', 'caterpillar', 'earwig', 'lightning bug', 'dragonfly', 'millipede', 'june bug', 'carpenter ant'})
```

##### !end-tests

##### !hint

Pay close attention to the types that are expected. Notice the literals used for `mady_bugs` and `lesha_bugs`, as well as the literals used to display the example return values. What is each type? Make sure the function is handling the expected input type and producing the expected result type.

##### !end-hint

##### !explanation

An example of a working implementation:

```python
def caught_together(first_list, second_list):
    # build a new unique set from each input
    # inputs are expected to be lists possibly containing duplicates
    first_set = set(first_list)
    second_set = set(second_list)

    # find result by finding the contents of both sets combined
    result = first_set | second_set

    # return the result set
    return result
```

##### !end-explanation

### !end-challenge

<!-- prettier-ignore-end -->

<!-- ======================= END CHALLENGE ======================= -->

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- prettier-ignore-start -->

### !challenge

* type: code-snippet
* language: python3.6
* id: 3b751423-f9d1-41b6-852d-6735e457bd0f
* title: Sets and Tuples

##### !question

Mady and Lesha made a great discovery! Their local library had a journal written by one of the greatest bug catchers ever known! It claims to have a list of all known bugs in the area. Mady and Lesha want to know how many are left for them to find!

Assuming Mady and Lesha have caught the following bugs:

```python
mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]
lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]
```  

And that the great bug catcher journal lists the following bugs:

```python
journal_bugs = ["pill bug", "damselfly", "stag beetle", "ladybug", "honey bee", "monarch butterfly", "moth", "caterpillar", "earwig", "lightning bug", "dragonfly", "stag beetle", "millipede", "june bug", "carpenter ant"]
```  

Write a function `left_to_catch` that they can use to find out which bugs each of them has left to catch.

Was the great bug catcher journal correct? Only time will tell! Mady and Lesha are excited for their adventures to continue!

| Example arguments | Example return value (order does not matter) |
| ----------------- | -------------------- |
| `mady_bugs, journal_bugs` | `{'pill bug', 'earwig', 'dragonfly', 'millipede', 'damselfly', 'stag beetle', 'honey bee', 'moth'}` |
| `lesha_bugs, journal_bugs` | `{'damselfly', 'monarch butterfly', 'honey bee', 'carpenter ant', 'moth', 'ladybug', 'caterpillar'}`  |

##### !end-question

##### !placeholder

```python
def left_to_catch(caught_list, all_list):
    pass
```

##### !end-placeholder

##### !tests

```python
import unittest
import main
from main import left_to_catch

class TestLeftToCatch(unittest.TestCase):

  def test_left_to_catch_for_mady(self):
    mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]
    journal_bugs = ["pill bug", "damselfly", "stag beetle", "ladybug", "honey bee", "monarch butterfly", "moth", "caterpillar", "earwig", "lightning bug", "dragonfly", "stag beetle", "millipede", "june bug", "carpenter ant"]

    self.assertEqual(left_to_catch(mady_bugs, journal_bugs), {'pill bug', 'earwig', 'dragonfly', 'millipede', 'damselfly', 'stag beetle', 'honey bee', 'moth'})

  def test_left_to_catch_for_lesha(self):
    lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]
    journal_bugs = ["pill bug", "damselfly", "stag beetle", "ladybug", "honey bee", "monarch butterfly", "moth", "caterpillar", "earwig", "lightning bug", "dragonfly", "stag beetle", "millipede", "june bug", "carpenter ant"]

    self.assertEqual(left_to_catch(lesha_bugs, journal_bugs), {'damselfly', 'monarch butterfly', 'honey bee', 'carpenter ant', 'moth', 'ladybug', 'caterpillar'})
```

##### !end-tests

##### !hint

Pay close attention to the types that are expected. Notice the literals used for `mady_bugs` and `lesha_bugs`, as well as the literals used to display the example return values. What is each type? Make sure the function is handling the expected input type and producing the expected result type.

##### !end-hint

##### !explanation

An example of a working implementation:

```python
def left_to_catch(caught_list, all_list):
    # build a new unique set from each input
    # inputs are expected to be lists possibly containing duplicates
    caught_set = set(caught_list)
    all_set = set(all_list)

    # find result by removing the caught set from the all set
    # notice this is the same approach as for caught_only_by_first
    # the difference is the order
    result = all_set - caught_set

    # return the result set
    return result
```

##### !end-explanation

### !end-challenge

<!-- prettier-ignore-end -->

<!-- ======================= END CHALLENGE ======================= -->

### For Certain Definitions of Interesting

Carmelo is a math fanatic. They especially love mathematical sequences: lists of numbers with interesting properties. Some sample sequences include:

- Counting numbers: 1, 2, 3, 4, 5, 6, 7, 8, ...
- Positive even numbers: 2, 4, 6, 8, 10, 12, 14, 16, ...
- [Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number): 1, 1, 2, 3, 5, 8, 13, 21, ...
- [Triangular numbers](https://en.wikipedia.org/wiki/Triangular_number): 1, 3, 6, 10, 15, 21, 28, 36, ...

It turns out that there are many, many interesting sequences of numbers (depending on your definition of interesting!), and Carmelo is having a tough time keeping track of the ones they know about. For a sense of the scale of their problem, check out [The On-Line Encyclopedia of Integer Sequences](http://oeis.org/)!

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- prettier-ignore-start -->

### !challenge

* type: code-snippet
* language: python3.6
* id: 8847d1ad-0ce1-43db-aa82-33f9f744aecb
* title: Sets and Tuples

##### !question

Carmelo has built a set of tuples, where each tuple holds the first eight values in a sequence. They need our help to write a function that can tell them whether a new sequence is one they've already seen. (Take a moment and think about why they used tuples to store their sequences in the set!)

Assuming Carmelo has the following sequences in their collection of sequences:

```python
carmelo_sequences = {
    (1, 2, 3, 4, 5, 6, 7, 8),
    (2, 4, 6, 8, 10, 12, 14, 16),
    (1, 1, 2, 3, 5, 8, 13, 21),
    (1, 3, 6, 10, 15, 21, 28, 36),
}
```  

And that we have the following sequences defined:

```python
fibonacci_sequence = [1, 1, 2, 3, 5, 8, 13, 21]
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
```  

Write a function `is_known_sequence` that Carmelo can use to find out whether they've seen this sequence before.

| Example arguments | Example return value |
| ----------------- | -------------------- |
| `fibonacci_sequence, carmelo_sequences` | `True` |
| `prime_numbers, carmelo_sequences` | `False`  |

##### !end-question

##### !placeholder

```python
def is_known_sequence(sequence, known_sequences):
    pass
```

##### !end-placeholder

##### !tests

```python
import unittest
import main
from main import is_known_sequence

class TestIsKnownSequence(unittest.TestCase):

  def test_is_known_sequence_with_fibonacci(self):
    fibonacci_sequence = [1, 1, 2, 3, 5, 8, 13, 21]
    carmelo_sequences = {
        (1, 2, 3, 4, 5, 6, 7, 8),
        (2, 4, 6, 8, 10, 12, 14, 16),
        (1, 1, 2, 3, 5, 8, 13, 21),
        (1, 3, 6, 10, 15, 21, 28, 36),
    }

    self.assertEqual(is_known_sequence(fibonacci_sequence, carmelo_sequences), True)

  def test_is_known_sequence_with_primes(self):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
    carmelo_sequences = {
        (1, 2, 3, 4, 5, 6, 7, 8),
        (2, 4, 6, 8, 10, 12, 14, 16),
        (1, 1, 2, 3, 5, 8, 13, 21),
        (1, 3, 6, 10, 15, 21, 28, 36),
    }

    self.assertEqual(is_known_sequence(prime_numbers, carmelo_sequences), False)
```

##### !end-tests

##### !hint

Describe the type of `carmelo_sequences`. What is the outer type? What is the inner type? Notice the type of the sequences being passed in. Can they be compared directly to the contents of `carmelo_sequences`? How can we build a new copy of the data that we _can_ compare?

##### !end-hint

##### !explanation

An example of a working implementation:

```python
def is_known_sequence(sequence, known_sequences):
    # we expect known_sequences to be a set of tuples, where each tuple is a mathematical sequence
    # we expect sequence to be a list
    
    # we need to build a new tuple from the list so that we can see whether it's in the set
    sequence_tuple = tuple(sequence)

    # return the result of checking whether the input sequence is in the known set
    return sequence_tuple in known_sequences
```

##### !end-explanation

### !end-challenge

<!-- prettier-ignore-end -->

<!-- ======================= END CHALLENGE ======================= -->

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- prettier-ignore-start -->

### !challenge

* type: code-snippet
* language: python3.6
* id: 76b680cf-c278-44ca-bdda-146c3c3866ea
* title: Sets and Tuples

##### !question

Carmelo is always looking for new, interesting properties of their sequences. They've recently been wondering whether the first and last values they stored in each of their sequences has anything interesting about them.

Assuming Carmelo is currently interested in the following sequences:

```python
fibonacci_sequence = [1, 1, 2, 3, 5, 8, 13, 21]
positive_even_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
triangular_numbers = [1, 3, 6, 10, 15, 21, 28, 36]
```  

They would like to get the first and last value returned as two values.

Write a function `get_first_and_last` that Carmelo can use to retrieve the pair of values from the start and end of the sequence. Note that they would like to be able to use the function as follows:

```python
first, last = get_first_and_last(fibonacci_sequence)
```

| Example arguments | Example return value |
| ----------------- | -------------------- |
| `fibonacci_sequence` | `(1, 21)` |
| `positive_even_numbers` | `(2, 16)` |
| `prime_numbers` | `(2, 19)` |
| `triangular_numbers` | `(1, 36)` |

##### !end-question

##### !placeholder

```python
def get_first_and_last(sequence):
    pass
```

##### !end-placeholder

##### !tests

```python
import unittest
import main
from main import get_first_and_last

class TestGetFirstAndLast(unittest.TestCase):

  def test_get_first_and_last_with_fibonacci(self):
    fibonacci_sequence = [1, 1, 2, 3, 5, 8, 13, 21]

    self.assertEqual(get_first_and_last(fibonacci_sequence), (1, 21))

  def test_get_first_and_last_with_even_numbers(self):
    positive_even_numbers = [2, 4, 6, 8, 10, 12, 14, 16]

    self.assertEqual(get_first_and_last(positive_even_numbers), (2, 16))

  def test_get_first_and_last_with_primes(self):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]

    self.assertEqual(get_first_and_last(prime_numbers), (2, 19))

  def test_get_first_and_last_with_triangular_numbers(self):
    triangular_numbers = [1, 3, 6, 10, 15, 21, 28, 36]

    self.assertEqual(get_first_and_last(triangular_numbers), (1, 36))
```

##### !end-tests

##### !explanation

An example of a working implementation:

```python
def get_first_and_last(sequence):
    # we expect sequence to be a non-empty list (Carmelo always stores 8 values)
    
    # return the first (position 0) and last (position -1) values from the sequence
    # Python treats bare comma-separated values as a tuple!
    return sequence[0], sequence[-1]
```

##### !end-explanation

### !end-challenge

<!-- prettier-ignore-end -->

<!-- ======================= END CHALLENGE ======================= -->

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- prettier-ignore-start -->

### !challenge

* type: code-snippet
* language: python3.6
* id: 2a510580-ed13-4150-b591-0619d4b0ab74
* title: Sets and Tuples

##### !question

Carmelo has a way to get the first and last elements of any of their sequences. They wonder whether it would be interesting if they found the product of each of those pairs. They'd like to store the results in a dictionary so that they can keep track of the products of all of the first and last elements from all of their sequences.

They start with an empty dictionary for the product table:

```python
product_table = {}
```

Then they'll use the `get_first_and_last` function we wrote for them to get the first and last element of each of their very interesting sequences. Then they'll pass the `product_table` and the first and last elements in to a new function they'd like us to write.

Write a function `store_product_of_pairs` that Carmelo can use to build up their `product_table` using each of the pairs. Consider the following examples. Notice that the call returns the product as the return value, and also stores it in the `product_table` using the pair of input numbers as the dictionary key.

| Example arguments | Example return value | Contents of `product_table` |
| ----------------- | -------------------- | --------------------------- |
| `product_table, 1, 21` | `21` | `{ (1, 21): 21 }`
| `product_table, 2, 16` | `32` | `{ (1, 21): 21, (2, 16): 32 }`
| `product_table, 2, 19` | `38` | `{ (1, 21): 21, (2, 16): 32, (2, 19): 38 }`
| `product_table, 1, 36` | `36` | `{ (1, 21): 21, (2, 16): 32, (2, 19): 38, (1, 36): 36 }`

The previous examples would be the result of calling something like the following code:

```python
product_table = {}
store_product_of_pairs(product_table, 1, 21)
store_product_of_pairs(product_table, 2, 16)
store_product_of_pairs(product_table, 2, 19)
store_product_of_pairs(product_table, 1, 36)
```

##### !end-question

##### !placeholder

```python
def store_product_of_pairs(product_table, first, last):
    pass
```

##### !end-placeholder

##### !tests

```python
import unittest
import main
from main import store_product_of_pairs

class TestStoreProductOfPairs(unittest.TestCase):

  def test_store_product_of_pairs_with_1_21(self):
    product_table = {}

    self.assertEqual(store_product_of_pairs(product_table, 1, 21), 21)
    self.assertEqual(product_table, {(1, 21): 21})

  def test_store_product_of_pairs_with_2_16(self):
    product_table = {}

    self.assertEqual(store_product_of_pairs(product_table, 2, 16), 32)
    self.assertEqual(product_table, {(2, 16): 32})

  def test_store_product_of_pairs_with_2_19(self):
    product_table = {}

    self.assertEqual(store_product_of_pairs(product_table, 2, 19), 38)
    self.assertEqual(product_table, {(2, 19): 38})

  def test_store_product_of_pairs_with_1_36(self):
    product_table = {}

    self.assertEqual(store_product_of_pairs(product_table, 1, 36), 36)
    self.assertEqual(product_table, {(1, 36): 36})


  def test_store_product_of_pairs_with_all_four_pairs(self):
    product_table = {}

    self.assertEqual(store_product_of_pairs(product_table, 1, 21), 21)
    self.assertEqual(product_table, {(1, 21): 21})
    self.assertEqual(store_product_of_pairs(product_table, 2, 16), 32)
    self.assertEqual(product_table, {(1, 21): 21, (2, 16): 32})
    self.assertEqual(store_product_of_pairs(product_table, 2, 19), 38)
    self.assertEqual(product_table, {(1, 21): 21, (2, 16): 32, (2, 19): 38})
    self.assertEqual(store_product_of_pairs(product_table, 1, 36), 36)
    self.assertEqual(product_table, {(1, 21): 21, (2, 16): 32, (2, 19): 38, (1, 36): 36})
```

##### !end-tests

##### !hint

If we want to store a pair of numbers (a collection with two values) as the key of a dictionary, what type can we use? What requirements are there about what types can be used as keys in dictionaries? What types do we know about that meet those requirements?

It may seem surprising that we can pass a dictionary into a function, make changes to it, and have those changes affect the dictionary outside the function. This ability is closely related to how Python works with data and variables, which will be discussed in more detail in other lessons. For now, we can decide to accept that this is the way that Python works, and later we'll understand more deeply why!

Be sure to both update the `product_table` and _then_ return the result value.

##### !end-hint

##### !explanation

An example of a working implementation:

```python
def store_product_of_pairs(product_table, first, last):
    # product_table is expected to be a dictionary mapping number pairs to numeric products
    # first and last are expected to be numbers

    # calculate the product
    product = first * last

    # store the product in the product_table under the pair made from first and last
    product_table[first, last] = product

    # finally, return the product
    return product
```

##### !end-explanation

### !end-challenge

<!-- prettier-ignore-end -->

<!-- ======================= END CHALLENGE ======================= -->
