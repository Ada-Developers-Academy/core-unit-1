# Lists As References

## Goal

- Explain the impact of lists as references in a function call
- Identify functions with side effects
- Explain reasons to avoid side effects in our

## Introduction

Lists are our first data structure.  As we saw in the last lesson a list is a more sophisticated data structure storing references to each element indirectly.  In this lesson we will look at some of the implications we need to keep in mind as developers.

## Vocabulary and Synonyms

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---
|  Side Effect | Any lasting effect that occurs in a function, which is not through its return value. | - | A side-effect of our `find_product` function is that our list of products is put into alphabetical order. |
|  Mutable data type | Any type of variable which can be modified without changing the reference. | changable object | Lists and dictionaries can be modified inside function calls and so are mutable. |


## List As Arguments And Side-Effects

Integers and float variables cannot have side-effects when passed into a function as arguments.  Examine the example below:

```python
def calculate_total(subtotal, tax_rate):
    subtotal += subtotal * tax_rate
    return subtotal


products_total = 113

print(f"Before calculating the the total of the order, products_total is \
{products_total}")
bill_total = calculate_subtotal(products_total, 0.08)
print(f"The total bill is {bill_total}")
print(f"After calculating the the total of the order, products_total is \
{products_total}")
```

While the function `calculate_total` is running both the parameter `subtotal` and the argument `products_total` both refer to the same value in memory.  

![Integer references from above](../assets/lists-and-memory/lists-memory-int-references.png)


**Question:** When the line: `subtotal += subtotal * tax_rate` executes, subtotal changes in value.  Why doesn't `products_total` change?

<details style="max-width: 700px; margin: auto;">
    <summary>
      Our answer        
    </summary>

Because any operation using the equals sign `=` including `+=` changes the _reference_ for `subtotal` to a new location in memory.  Essentially Python performs the calculation (addition in this case) and creates a new integer in memory to store the result.  

Python then makes `subtotal` refer to that new location, leaving `products_total` unchanged.
</details>

This is the kind of behavior we want, because we do not want our arguments to have their values changed unexpectedly.  Most of the time we will use return values to get information back from a function call.

When re-assigning an entire list, things work the same as for integers.  However when the elements _inside_ a list are modified things get interesting.

```python
def shorten_names(names):
    index = 0
    while index < len(names):
        # truncate the strings to 0-5 characters
        name = names[index]
        names[index] = name[0:5]
        index += 1

    return names


friends = ["Simpson", "Burns", "Hibbert", "Bouvier"]

print(f"Before the function call friends is {friends}")
shorten_names(friends)
print(f"After the function call friends is {friends}")
```

The output of this Python code is:

```
Before the function call friends is ['Simpson', 'Burns', 'Hibbert', 'Bouvier']
After the function call friends is ['Simps', 'Burns', 'Hibbe', 'Bouvi']
```

After the function call the list `friends` has been modified!

This is because both `friends` and `names` refer to the same list in memory.

![Diagram of `names` and `friends` in memory](../assets/lists-and-memory/list-reference-example.png)

Following the reference to the specific elements with `names[index] = name[0:5]` will follow the reference to the specific element and then change the internal reference to a new value.  For example when `index` is 0.

![Changing a reference at an index](../assets/lists-and-memory/lists-and-memory-changing-index.png)

Notice that both `names` and `friends` refer to the same object, with updated items in the end.

Because list elements passed into a function can be modified during the function execution, lists are considered a _mutable_ data type.  Integers, strings and float arguments by contrast cannot have their values changed in a function call and are called _immutable data types_.

<!-- available callout types: info, success, warning, danger, secondary  -->
### !callout-info

## Side Effect

When a function has an effect, like changing a variable, outside of it's return value, it is said to have a side-effect.

### !end-callout

## Problems With Side Effects

Functions with side effects like this can be quite useful for some situation, for example if we wanted to read in a name from the terminal and append it to a list argument.

However functions with side effects, especially when they are unintened or not communicated among the team can be very problematic.

*  Functions with side effects especially when it is unintended could lead to a lot of potential bugs which are harder to debug.
*  It is easier to write tests for functions with no side-effects.
*  If the function is supposed to change anything in the environment, like modify a list parameter.  It must be clearly documented to avoid confusion.
*  Care must be taken in writing function definitions containing mutable data types (like Lists).

You can avoid introducing side effects by creating copies of mutable data types like lists and dictionaries and performing operations on the copies.

```python
def shorten_names(names):
    index = 0
    shortened_names = []
    while index < len(names):
        # truncate the strings to 0-5 characters
        name = names[index]
        shortened_names.append(name[0:5])
        index += 1
    
    return shortened_names
```

## Summary

Because lists internally contain references to the elements stored in them, it is possible for a parameter to modify the elements of a list passed as a parameter.  When this happens it is called a _side effect_.  Side effects can be useful, but they can also be problematic because they make our programs harder to test, and provide an avenue for subtle and hard to diagnose bugs enter our applications.  In general we try to avoid introducing side effects.

## Learning Comprehension



<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: code-snippet
* language: python3.6
* id: 9aadef70-ab5c-4ba0-8ea9-107ac2d0e4a3
* title: Eliminate Side Effects
* points: 1
* topics: python-lists

##### !question

The function below works fine, but introduces side effects.  Modify the function to avoid side effects.

##### !end-question

##### !placeholder

```py
def get_fire_students(students):
    '''
    INPUT: A list of dictionaries with the "name" and "class" key-value pairs.
    Example:  get_fire_students([{ "name": "Ada", "class": "fire"}, { "name": "Taylor", "class": "earth" }])
    RETURN VALUE: A list of dictionaries with **only** the students in the "fire" class.
    '''
    temp = []
    
    while students:
        student = students.pop()
        if student["class"] == "fire":
            temp.append(student)

    while temp:
        students.append(temp.pop())

    return students  
```

##### !end-placeholder

##### !tests

```py
import unittest
from main import get_fire_students

class TestGetFireStudents(unittest.TestCase):
  def test_empty_list(self):
    # Arrange
    input = []

    # Act
    answer = get_fire_students(input)

    # Assert
    self.assertEqual(0, len(answer), "If given an empty list it should return an empty list")
    self.assertEqual(0, len(input), "If given an empty list the argument should remain an empty list")

  def test_all_fire(self):
    # Arrange
    input = [
    {
        "name": "Chris",
        "class": "fire",
    },
    {
        "name": "Simon",
        "class": "fire",
    },
    {
        "name": "Claire",
        "class": "fire",
    },
    {
        "name": "Audrey",
        "class": "fire",
    },        
    {
        "name": "Jae",
        "class": "fire",
    },    
  ]

    # Act
    answer = get_fire_students(input)

    # Assert
    self.assertEqual(5, len(answer), "If given a list of 5 fire class students it should return the same list")
    self.assertEqual(5, len(input), "The input argument should remain unchanged")

    index = 0
    for student in answer:
        self.assertTrue(student in input, f"{student} should be in both lists")

  def test_all_not_fire(self):
    # Arrange
    input = [
    {
        "name": "Chris",
        "class": "water",
    },
    {
        "name": "Simon",
        "class": "water",
    },
    {
        "name": "Claire",
        "class": "water",
    },
    {
        "name": "Audrey",
        "class": "water",
    },        
    {
        "name": "Jae",
        "class": "water",
    },    
  ]

    # Act
    answer = get_fire_students(input)

    # Assert
    self.assertEqual(0, len(answer), "If given a list of 5 fire class students it should return the same list")
    self.assertEqual(5, len(input), "The input argument should remain unchanged")


  def test_one_fire(self):
    # Arrange
    input = [
    {
        "name": "Chris",
        "class": "fire",
    },
    {
        "name": "Simon",
        "class": "water",
    },
    {
        "name": "Claire",
        "class": "water",
    },
    {
        "name": "Audrey",
        "class": "water",
    },        
    {
        "name": "Jae",
        "class": "water",
    },    
  ]

    # Act
    answer = get_fire_students(input)

    # Assert
    self.assertEqual(1, len(answer), "If given a list of 5 fire class students it should return the same list")
    self.assertEqual(5, len(input), "The input argument should remain unchanged")

    for student in answer:
        self.assertEqual("fire", student["class"], f"All returned students should be in the fire class - {student} is not")

    
  def test_all_last_fire(self):
    # Arrange
    input = [
    {
        "name": "Chris",
        "class": "earth",
    },
    {
        "name": "Simon",
        "class": "water",
    },
    {
        "name": "Claire",
        "class": "water",
    },
    {
        "name": "Audrey",
        "class": "water",
    },        
    {
        "name": "Jae",
        "class": "fire",
    },    
  ]

    # Act
    answer = get_fire_students(input)

    # Assert
    self.assertEqual(1, len(answer), "If given a list of 5 fire class students it should return the same list")
    self.assertEqual(5, len(input), "The input argument should remain unchanged")

    for student in answer:
        self.assertEqual("fire", student["class"], f"All returned students should be in the fire class - {student} is not")
    
    self.assertEqual("Jae", answer[0]["name"], "Jae should be the only fire student")

    

```

##### !end-tests

<!-- other optional sections -->
<!-- !hint - !end-hint (markdown, hidden, students click to view) -->
<!-- !rubric - !end-rubric (markdown, instructors can see while scoring a checkpoint) -->
<!-- !explanation - !end-explanation (markdown, students can see after answering correctly) -->

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: checkbox
* id: 405c0a8c-d9b9-428e-8a72-3cf173bbff4a
* title: Why Side Effects Are Problematic
* points: 1
* topics: python-lists, python-side-effects

##### !question

Why are functions with side effects problematic?

##### !end-question

##### !options

* They make our functions harder to test
* They can introduce hard-to-find bugs in our programs
* Side effects mean we don't need return statements
* Functions with side effects require more communication among team members

##### !end-options

##### !answer

* They make our functions harder to test
* They can introduce hard-to-find bugs in our programs
* Functions with side effects require more communication among team members
##### !end-answer

<!-- other optional sections -->
##### !hint

Take a look at the bulleted list above.

##### !end-hint
<!-- !rubric - !end-rubric (markdown, instructors can see while scoring a checkpoint) -->
<!-- !explanation - !end-explanation (markdown, students can see after answering correctly) -->

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->