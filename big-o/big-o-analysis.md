# Big O Analysis

## Learning Goals

## Introduction

## Time Complexity: Code to Big O

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

### Always Looking for the Biggest Big O

Constants are dropped. Constants only shift our graph slightly, but do not affect the overall look of the graph by much. O(2n) is shortened to O(n). O(1⁄2 n) is shortened to O(n).
Usually when an algorithm's growth rate is a mix of orders, the dominant order is shown, and the rest are dropped. O(n^2) + O(n) or O(n^2 + n) would be shortened to O(n^2). This is because O(n^2) + O(n) is smaller than O(n^2) + O(n^2).In other words, O(n^2) + O(n) is in the order of O(n^2) + O(n^2). O(n^2) + O(n^2) can be simplified to O(n^2) _ 2 or O(2 _ n^2). Then, we can drop the constant, and simply state that the complexity is O(n^2).

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