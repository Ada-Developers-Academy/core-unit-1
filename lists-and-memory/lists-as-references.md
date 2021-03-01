# Lists As References

## Goal

- Explain the impact of lists as references in a function call
- Identify functions with side effects
- Explain reasons to avoid side effects in our

## Introduction



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

print(f"Before calculating the the total of the order, products_total is {products_total}")
bill_total = calculate_subtotal(products_total, 0.08)
print(f"The total bill is {bill_total}")
print(f"After calculating the the total of the order, products_total is {products_total}")
```

While the function `calculate_total` is running both the parameter `subtotal` and the argument `products_total` both refer to the same value in memory.  

![Integer references from above](../assets/lists-and-memory/lists-memory-int-references.png)


<details>
<summary>
  When the line:

  `subtotal += subtotal * tax_rate`

  executes, subtotal changes in value.  Why doesn't `products_total` change?
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

Because list arguments passed into a function can be modified during the function execution, they are considered a _mutable_ data type.  Integers, strings and float arguments by contrast cannot have their values changed in a function call and are called _immutable data types_.

<!-- available callout types: info, success, warning, danger, secondary  -->
### !callout-info

## Side Effect

When a function has an effect, like changing a variable, outside of it's return value, it is said to have a side-effect.

### !end-callout

## Problems With Side Effects

Functions with side effects like this can be quite helpful, for example if we wanted to read in and add a name to our list.  

However functions with side effects, especially when they are unintened or not communicated can be very problematic.


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
            temp.push(student)

    while temp:
        students.push(temp.pop())

    return students  

#   return 1
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
        self.assertEqual(student, input[index], f"input[{index}]  ({input[index]}) should equal answer[{index}]  ({answer[index])")

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
    
    assertEqual("Jae", answer[0]["name"], "Jae should be the only fire student")

    

```

##### !end-tests

<!-- other optional sections -->
<!-- !hint - !end-hint (markdown, hidden, students click to view) -->
<!-- !rubric - !end-rubric (markdown, instructors can see while scoring a checkpoint) -->
<!-- !explanation - !end-explanation (markdown, students can see after answering correctly) -->

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->
