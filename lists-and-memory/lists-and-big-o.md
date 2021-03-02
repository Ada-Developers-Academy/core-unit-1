# Lists and Big O

As our first data structure, lists can have a big impact on the time and space efficiency of our applications.  Lists allow us to pass arbitrary amounts of data into our functions so it becomes very important to learn to predict how our algorithms behave as the size of the input lists grow.

## Goals

- Explain how lists can impact time and space complexity
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

You might think that traversing a list, means that a function's time complexity is usually going to be O(n), but this is not the case.  

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

## Space Complexity

Lists can store an arbitrary amount of data and combined with dictionaries they will be our initial source of space complexity in our algorithms.  Remember however we measure how memory usage increases with increasing input size.  Space complexity is not a measurement of the input size, but rather how memory usage increases with larger input.

For example in our 1st example:

```python
def find(students, student_name):
    for student in students:
        if student["name"] == student_name:
            return student

    return None
```

The function takes an array as input, but it does not create a new list, and it does not increase the size of the given list.  So this function's space complexity is O(1).

Similarly the function below only ever increases the size of the list by one element.  It always adds one dictionary with two key-value pairs, no matter the size of the input.

```python
def add_student(students, name, class_name):
    students.append({
      "name": name,
      "class": class_name,
    })

    return students
```

On the other hand this function **does** allocate more memory as the size of the input increases.

```python
def even_numbers(numbers):
    even_nums = []
    for num in numbers:
        if num % 2 == 0:
            even_nums.append(num)
    
    return even_nums
```

This function will (worst-case) return a **new** list of equal size to the input list (n).  So the space complexity of this function is O(n).

<!-- available callout types: info, success, warning, danger, secondary  -->
### !callout-secondary

## Space Complexity - Things to Look for

With space complexity look for:

* New data structures like lists or dictionaries being created
* Repeated elements being added to input data structures

If a new data structure is being created or a loop repeatably adds elements to an existing data structure, the size of the result relative to the input length determines the space complexity.

### !end-callout

## Summary

Because lists are data structures they often contribute to the space or time complexity of our functions.  When our functions traverse a list, the size of the list will often determine the time complexity of our function.  When our function builds a list, the amount of data in the resulting data structure determines the space complexity.