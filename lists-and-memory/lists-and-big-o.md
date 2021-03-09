# Lists and Big O

As our first data structure, lists can have a big impact on the time and space efficiency of our applications.  Lists allow us to pass arbitrary amounts of data into our functions so it becomes very important to learn to predict how our algorithms behave as the size of the input lists grow.

## Learning Goals

- Explain how lists can impact time and space complexity.
- Accurately predict the time and space complexity of a function involving lists.  

## Time Complexity

Often when a function's input involves a list, the size of the input list becomes the `n` used to describe the function's time complexity.

Take a look at the function below.

```python
def find(students, student_name):
    for student in students:
        if student["name"] == student_name:
            return student

    return None
```

This function has a loop `for student in students:`,  which iterates through, worst-case, each item in the list.  Since the length of the loop depends on the size of the array (n), we can label this function with the time complexity O(n).

This isn't always the case:

```python
def add_student(students, name, class_name):
    students.append({
      "name": name,
      "class": class_name,
    })

    return students
```

The above function takes a list and a couple of arguments, but the function does not take any longer to execute as the list grows larger.

We might think that traversing a list, means that a function's time complexity is usually going to be O(n), but this is not always the case.  

The following function takes a list of numbers and puts them into sorted order, from smallest to greatest.  What do you think the time complexity is?

```python
def bubble_sort(numbers):
    length = len(numbers)
    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp

    return numbers
```

<details style="max-width: 700px; margin: auto;">
  <summary>Look at the loops, what do you think the time complexity is?</summary>

  If the size of `numbers` is `n`.  The outer loop will execute roughly `n` times.  Inside that loop is `for j in range(0, length - i - 1):` which will also execute roughly `n` times.  When you have a loop within a loop their time complexities multiply O(n * n) = O(n<sup>2</sup>)
</details>

<!-- available callout types: info, success, warning, danger, secondary  -->
### !callout-secondary

## Lists & Time Complexity - Things To Look For

When judging a function's time complexity look for:

* Loops which traverse the list
  * Do they iterate through the entire list, or do something else
  * Are there nested loops?
* Does the function call another function which performs any of the above actions?

### !end-callout

## Space Complexity

Lists can store an arbitrary amount of data and combined with dictionaries they will be our initial source of space complexity in our algorithms.  Remember, we measure space complexity by how memory usage increases with increasing input size.  

Space complexity is not a measurement of the input size, but rather how memory usage increases with larger input.

For example in our 1st example:

```python
def find(students, student_name):
    for student in students:
        if student["name"] == student_name:
            return student

    return None
```

The function takes an array as input, but it does not create a new list, and it does not increase the size of the given list.  So this function's space complexity is O(1).

Similarly the function below only ever increases the size of the list by one element.  It always adds one dictionary with two key-value pairs, no matter the size of the input. So this function's space complexity is also O(1).

```python
def add_student(students, name, class_name):
    students.append({
      "name": name,
      "class": class_name,
    })

    return students
```

On the other hand, this function **does** allocate more memory as the size of the input increases.

```python
def even_numbers(numbers):
    even_nums = []
    for num in numbers:
        if num % 2 == 0:
            even_nums.append(num)
    
    return even_nums
```

This function will (worst-case) return a **new** list of equal size to the input list (n).  So the space complexity of this function is O(n).  The key is how much **additional** memory will the function allocate as it executes.

<!-- available callout types: info, success, warning, danger, secondary  -->
### !callout-secondary

## Space Complexity - Things to Look for

With space complexity look for:

* New data structures like lists or dictionaries being created
* Repeated elements being added to input data structures

If a new data structure is being created or a loop repeatably adds elements to an existing data structure, the size of the result relative to the input length determines the space complexity.

### !end-callout

## Python Built-in Functions

Python has a number of [built-in functions](https://docs.python.org/3/tutorial/datastructures.html) for processing lists.  These functions **can** have an impact on the time or space complexity of any of your functions which use them.

For example:

* `clear()` - This function removes all elements of a list
  * Example:  `numbers.clear()`
  * Since this function must iterate through each element of the list and delete each element it has time complexity of O(n)
* `count()` - This function returns the number of elements with the specific value.
  * Example: `if sodas.count("Cherry Soda") == 3:`
  * Since this function must iterate through the entire list to find elements matching the argument, this function has O(n) time complexity.
* `index()` - This function returns the index of the first element to match the given argument.
  * Example: `location = sodas.index("Cherry Soda")
  * Since the function will iterate through the list until it finds the value or reaches the end of the list the time complexity is O(n).
* `copy()` - This function makes a copy of the given list.
  * Example: `duplicate_list = sodas.copy()`
  * Since this function iterates through the list and adds each element to a **new** list and then returns the new list, the time complexity is O(n) and the space complexity is also O(n).

<details style="max-width: 700px; margin: auto;">
    <summary>
        How can we identify the time or space complexity of a Python library function?
    </summary>

To identify the time/space complexity of a Python library function we can:

* Read the [Python Documentation entry on it](https://docs.python.org/3/tutorial/datastructures.html)
* Search for the answer in a web search engine (google it)
* Ask someone either in person or on a site like Stack Overflow

Regardless, we may need to make some educated guesses on the function's performance based on the description we read.  Consider, "How would I have to do this?"
</details>

## Summary

Because lists are data structures they often contribute to the space or time complexity of our functions.  When our functions traverse a list, the size of the list will often determine the time complexity of our function.  When our function builds a list, the amount of data in the resulting data structure determines the space complexity.
