# Big O Analysis

## Learning Goals

- Apply time complexity analysis to arrays and operations on arrays
- Apply space complexity analysis to arrays and operations on arrays

## Introduction

When we read code, we can analyze an algorithm and come to a conclusion about its time and space complexity. This skill will let us check the efficiency of our code as we write it or review it!

This lesson is structured this way: We will...

- introduce some guidelines and some steps to take when analyzing complexity
- apply it to a small example, and give explanations
- apply it to a large example, and give explanations

We encourage you all to read through these sections. After each example, re-read the example and follow along the same thought process, so you can come to the same conclusions too.

## Time Complexity: Code to Big O

Recall that time complexity is the measurement of how the amount of time an algorithm takes to run as the size of the input changes. Also, time complexity is usually measured in _number of operations._ Therefore, our goal is to find a formula that captures how many operations an algorithm executes.

### Generic Steps

1. Read through the code, and identify all lists that have a variable size.
    - Typically, with one list, we say it has _n_ number of elements.
1. Identify all of the operations in the algorithm
1. Recognize which operations are related to the lists of size _n_
    - Typically, the operations inside of a for loop get multipled by _n_ times
    - This relationship will change depending on the kind of loop and the logic in the loop. Consider cases where the loop `break`s.
1. Create an equation that represents how many operations there are
    - This equation can use _n_ as a variable
1. Drop the constants (notes below)
1. Match this Big O to the most relevant complexity

### !callout-secondary

## What's an Operation?
One operation is when one operator is used. There are arithmetic operators (`+`, `-`, `*`, `%`, etc), assignment operators (`=`, `+=`, etc), comparison operators (`==`, `<`, `>=`, etc), logical operators (`and`, `or`, `not`), and more miscellaneous ones (`is`, `is not`, `in`, `not in`, etc)

### !end-callout

### Small Example

This is one implementation of the linear search algorithm. It takes in a list of _n_ element, and an item to search for. It's responsibility is to return the index of that item.

```python
def linear_search(array, item):
    for i in range(len(array)):
        if item == array[i]:
            return i
    return False
```

1. Identify all lists with variable size: There is one list with variable size, and it's a size of _n_.

2. Identify all operations in this algorithm:
    1. `if item == array[i]`
    1. `i in range(len(array))`

3. Recognize which operations have a relationship to list size:
    1. `if item == array[i]` can happen _n_ times
    1. `i in range(len(array))` can happen _n_ times
        - If this is not obvious, this is a detail that we can leave as an unknown. We may have other clues in the rest of the process that could help us. We can revisit this if we realize that this is crucial to our solution.

4. Create a formula that counts how many operations there are:
    1. Two operations can happen _n_ times. We can express this as _2 * n_, or _2n_

5. Drop the constants:
    1. In math, when looking at _2n_, `2` is a constant that we can drop
    1. After dropping the constant, our remaining formula is _n_

6. Match this formula with the most relevant complexity:
    1. _n_ matches _O(n)_ the most closely. This algorithm has linear time complexity.

### Large Example

This is one implementation of reversing the order of items in a list. It loops through an array, and starts looking at the first item (at index `i`) and the last item (at index `j`), and swaps their values, making use of a temporary variable `temp`. It will return a list in reverse order.

```python
def reverse(array):
    if len(array) <= 1:
        return array

    i = 0
    j = len(array) - 1

    while i < j:
        temp = array[i]
        array[i] = array[j]
        array[j] = temp

        i += 1
        j -= 1

    return array
```

1. Identify all lists with variable size: There is one list with variable size, and it's a size of _n_.

2. Identify all operations in this algorithm:
    1. `len(array) <= 1`
    1. `i = 0`
    1. `j = ...`
    1. `len(array) - 1`
    1. `i < j`
    1. `temp = ...`
    1. `array[i] = ...`
    1. `array[j] = ...`
    1. `i += 1`
    1. `j -= 1`

3. Recognize which operations have a relationship to list size:
    1. All 4 of the operations outside of the `while` loop will only happen once; they have no relationship to list size
    1. All 6 of the operations inside the `while` loop can happen _n_ times

4. Create a formula that counts how many operations there are:
    1. We can express this as _4 + (6 * n)_, or _4 + 6n_

5. Drop the constants:
    1. We are able to drop `4 +` and `6 *`
    1. After dropping the constants, our remaining formula is _n_

6. Match this formula with the most relevant complexity:
    1. _n_ matches _O(n)_ the most closely. This algorithm has linear time complexity.

### What is "Dropping the Constant," or Finding the Dominant Order?

In complexity analysis, programmers care about the dominant order, or the part of the complexity that affect the complexity _the most._

Mathematical constants are values that have a fixed value. Constants tend to be added, subtracted, multiplied, or divided in our formulas. In Big O, constants will affect our complexity (O(6n) is different than O(n))... but they do not affect the curve enough that is meaningful for complexity analysis.

Some examples:
- O(2n) is shortened to O(n)
- O(n/2) (or one half of _n_) is shortened to O(n)
- O(n + n<sup>2</sup>) is shortened to O(n<sup>2</sup>)

## Space Complexity: Code to Big O

```
# array is the input integer array to the algorithm

if array.length <= 1
  return # nothing to reverse

i = 0
j = array.length - 1

while i < j
  # swap values at i and j
  temp = array[i]
  array[i] = array[j]
  array[j] = temp

  increment i
  decrement j
```

You must have noticed the three memory allocations done by the program: i, j and temp. These are three integers created. Regardless of the size of the input array (be it 500 or 900,000), there will always be only and exactly three integers created. As such, the new memory allocations in this algorithm do not change as the size or value of the input changes. Such algorithms are said to have constant space complexity or O(1) space complexity.

## Example: Comparing Two Algorithms

These are two algorithms for the same thing. Consider the time and space complexity for each algorithm. Afterwards, we'll compare the two algorithms.

Algo 1

```
# array is the input integer array to the algorithm

if array.length <= 1
  return # nothing to reverse

i = 0
j = array.length - 1

while i < j
  # swap values at i and j
  temp = array[i]
  array[i] = array[j]
  array[j] = temp

  increment i
  decrement j
```

You must have noticed the three memory allocations done by the program: i, j and temp. These are three integers created. Regardless of the size of the input array (be it 500 or 900,000), there will always be only and exactly three integers created. As such, the new memory allocations in this algorithm do not change as the size or value of the input changes. Such algorithms are said to have constant space complexity or O(1) space complexity.

Algo 2

```
# array is the input integer array to the algorithm

if array.length <= 1
  return # nothing to reverse

i = 0
j = array.length - 1

# create a new array of the same size as input array
temp_array = new array of size array.length

while i < array.length
  # copy over the values in input array
  # into the temp array in reverse order
  temp_array[i] = array[j]
  increment i
  decrement j


i = 0
while i < array.length
  # copy over values from the temp array
  # into the input array
  array[i] = temp_array[i]

# array is reversed
```

The first while loop copies over each of the elements in the input array into a new array in reverse order of their position. The means, if there are 100 elements in the input array, then the loop will execute 100 times. If there are 700,000 elements in the input array, then the loop will execute 700,000 times and so on. Therefore, we can conclude that in the first loop, the number of operations performed are linearly changing in accordance with the size of the input.
The second loop copies for each element of the temporary array back into the input array. Following the same logic, in the second loop, the number of operations performed are linearly changing in accordance with the size of the input.
The time complexity of each loop is linear, or O(n) where n is the number of elements in the input array. Together, since they perform the operations one after another, the time complexity of the overall algorithm is linear or O(n), where n is the number of elements in the input array.

There are two integers, i and j that are used to index into the arrays. Each of these take up additional memory of the size of an integer each. Also, in addition to the input array, the algorithm creates a new array. This new array, temp_array takes up as much space as the size of the input array. If there are 100 elements in the input array, then the temp_array needs to be able to hold 100 elements. If the input array holds 900,000 elements, then the temp_array should also be able to hold 900,000 elements. In other words, the new temp_array created takes up space that is linearly proportional to the size of the input array. Therefore, the space complexity of this algorithm is linear or O(n), where n is the number of elements in the input array.

### Comparing

Time complexity: As we saw above, Algorithm 1 as well as Algorithm 2, both have the same time complexity. They both execute in linear time as compared to the size of the input, or are said to have O(n) time complexity, where n is the number of elements in the input array. From the view point of time complexity, both the algorithms are equally efficient.
Space complexity: We noted that Algorithm 1 above has a space complexity of O(1) or constant, since the amount of additional memory used does not change as the size of the input array changes. In contrast, Algorithm 2 creates a new array. The size of this new array created is the same as the input array. Therefore, Algorithm 2 has a space complexity of O(n), where n is the number of elements in the input array. Comparing Algorithm 1's constant space complexity with Algorithm 2's linear space complexity, we can conclude that Algorithm 1 is more space efficient than Algorithm 2.
In conclusion, although the two algorithms are equally time efficient, Algorithm 1 is more space efficient as compared to Algorithm 2 and hence, Algorithm 1 is a better choice.