# Time and Space Complexity

## Learning Goals

- Define time and space complexity

## Introduction

Fraction of a second
Tiny bit of memory
Limits

Considered to be efficient

## Vocabulary and Synonyms

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---
Algorithm
| **Time Complexity**      | A measurement of how the amount of time an algorithm takes to run as the size of the input changes.       |
| **Space Complexity**   |  A measurement of how much memory algorithm uses as the size of the input changes        |

## Considering the Algorithm

We could consider performance of an algorithm in three different scenarios: best-case, worst-case and average case.

Consider the task of performing a sequential search on some sort of list, i.e. an array. Best-case would be that your target value was found in the first element. Worst-case would be that the value was not there at all (so all elements would have to be compared and tested, including the last). Average-case would be mid-way between the two, and still dependent on the length of the list.

In Computer Science, we care about worst case and average case. This is because we rely on our software systems to run our lives and infrastructure and we need applications which perform well under difficult circumstances. Further most solutions will perform well in best-case scenarios. The differences become noticable under average and worst-case scenarios.

Worst case consideration: It is important to consider the worst case scenario when the response time is critical. e.g. the shutdown program for a nuclear power plant.
Average case consideration: If an algorithm is to be used many times on many different instances, it may be more important to know the average execution time. e.g. calculating total cost for all the items in the shopping cart for a user for an e-commerce website like etsy.com or amazon.com

## Time Complexity is How Long It Takes

While quantitatively representing the speed of an algorithm, we are looking to share the rate of change of number of operations in an algorithm as the either the size or the value of the input to the algorithm changes.

### Examples

O(1) – Find a random person's phone number by flipping open any page in the phone book.
O(log n) – Given a person's name, find the corresponding phone number. This is using a binary search for a person's phone number.
O(n) – Find all people whose phone numbers contain the digit "5". This will require linear scaning through the phone book.
O(n log n) – Sort a phone book's pages by looking at the first name on each page. See the merge sort for understanding this further.

## Space Complexity is How Much Memory is Required

Similarly, while quantitatively sharing memory utilizaton of an algorithm, we are interested in sharing the rate of change of amount of memory or space needed by an algorithm as compared to either the size or the value of the input.

### Examples



## We Compare Efficiency Between Algorithms

An efficient algorithm is one that runs as fast as possible and requires as little computer memory as possible. We often have to settle for a trade-off between these two goals, compromising memory to make things faster, or speed to use less memory.

## Check for Understanding


