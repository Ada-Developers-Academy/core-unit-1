# Problem Set: Big(O)

## Directions

Complete all questions below.

## Practice

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: rhpVnF
* title: Big O
##### !question

What is the time complexity of the following piece of code?

```python
def does_value_exist(input_list, value):
    for item in input_list:
        if item == value:
            return True
    return False
```

##### !end-question
##### !options

* O(1)
* O(log n)
* O(n)
* O(n log n)
* O(n<sup>2</sup>)
* O(n<sup>3</sup>)

##### !end-options
##### !answer

* O(n)

##### !end-answer
##### !explanation

The provided code _linearly_ searches through each item in the list to check if the value is found. In the worst case scenario, all items in the list are searched. This means if there are _n_ items in the list, all _n_ items will be checked. In the best case scenario, the value to be found would be the first item in the list. In the average cases, the number of times the loop will run will be somewhere in between best case and worst case but still dependent on the number of items in the list i.e. _n_.

<br />

The time complexity of this algorithm is therefore _linear_ or _O(n)_ where _n_ is the length of the input_list.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: fFOaNl
* title: Big O
##### !question

What is the time complexity of the following piece of code?

```python
def repeat_four_times(value):
    for count in range(4):
        print("The value is", value)
```

##### !end-question
##### !options

* O(1)
* O(log n)
* O(n)
* O(n log n)
* O(n<sup>2</sup>)
* O(n<sup>3</sup>)

##### !end-options
##### !answer

* O(1)

##### !end-answer
##### !explanation

Independent of the input parameter value, the loop in this method will always run four times. Because the number of iterations in the loop is constant and independent of input parameter size or value, the time complexity will be _constant_ or _O(1)_.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 3 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: 2sHTBq
* title: Big O
##### !question

What is the time complexity of the following piece of code?

```python
def repeat_multiple_times(value, num_of_repetitions):
    for count in range(num_of_repetitions):
        print("The value is", value)
```

##### !end-question
##### !options

* O(1)
* O(log n)
* O(n)
* O(n log n)
* O(n<sup>2</sup>)
* O(n<sup>3</sup>)

##### !end-options
##### !answer

* O(n)

##### !end-answer
##### !explanation

This method executes the `print` instruction `num_of_repetitions` number of times. If the value of `num_of_repetitions` changes, the number of times the `print` instruction is repeated will change _linearly_.

<br />

Therefore, the time complexity of this algorithm is _linear_ or _O(n)_ where _n_ is multiple.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 4 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: BAKq4K
* title: Big O
##### !question

What is the time complexity of the following piece of code?

```python
def greet_friends(input_list):
    for num in range(len(input_list)):
        print(f"Hello, Friend #{num + 1}!")
```

##### !end-question
##### !options

* O(1)
* O(log n)
* O(n)
* O(n log n)
* O(n<sup>2</sup>)
* O(n<sup>3</sup>)

##### !end-options
##### !answer

* O(n)

##### !end-answer
##### !explanation

This method will execute the `print` statement as many times as is the length of the `input_list`. If the size of the `input_list` changes, the number of times the `print` statement gets executed will change to match the size.

<br />

Since the number of times the `print` statement gets executed is _linearly_ proportional to the length of the `input_list`, the time complexity is _linear_ or _O(n)_ where _n_ is the length of the `input_list`.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 5 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: SULbFB
* title: Big O
##### !question

What is the time complexity of the following piece of code?

```python
def greet_friends(input_list):
    i = 0
    while i < 17:
        print(f"Hello, Friend #{i + 1}!")
        i += 1
```

##### !end-question
##### !options

* O(1)
* O(log n)
* O(n)
* O(n log n)
* O(n<sup>2</sup>)
* O(n<sup>3</sup>)

##### !end-options
##### !answer

* O(1)

##### !end-answer
##### !explanation

The loop in this method gets run 17 times regardless of the size or value of the input list.

<br />

Hence, the time complexity of _constant_ or _O(1)_.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 6 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: 4w506R
* title: Big O
##### !question

What is the time complexity of the following piece of code?

```python
def greet_friends(input_list):
    count = len(input_list)
    i = 0
    while i < count:
        print(f"Hello, Friend #{i + 1}!")
        i += 1
```

##### !end-question
##### !options

* O(1)
* O(log n)
* O(n)
* O(n log n)
* O(n<sup>2</sup>)
* O(n<sup>3</sup>)

##### !end-options
##### !answer

* O(n)

##### !end-answer
##### !explanation

The loop in this method gets run `count` number of times. `count` is the length of `input_list`. As the length of `input_list` changes, so will the number of times the loop gets executed. The execution of the loop is _linearly_ proportional to the length of `input_list`.

<br />

So, the time complexity is _linear_ or _O(n)_ where n is the length of the input parameter, `input_list`.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 7 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: bfvZeu
* title: Big O
##### !question

What is the time complexity of the following piece of code?

```python
def greet_friends(input_list):
    count = len(input_list)
    i = 0
    while i < 17:
        for j in range(count):
            print(f"Hello, Friend #{i+1} in {j+1}!")
        i += 1
```

##### !end-question
##### !options

* O(1)
* O(log n)
* O(n)
* O(n log n)
* O(n<sup>2</sup>)
* O(n<sup>3</sup>)

##### !end-options
##### !answer

* O(n)

##### !end-answer
##### !explanation

There are two nested loops in this method. The outer `while` loop gets run 17 times. The inner `for` loop gets run `count` number of times where `count` is the length of `input_list`. Since the loops are nested, for each iteration of the outer loop, the complete inner loop gets run once. That means, the `print` statement will get executed (17 * `count`) number of times.

<br />

In Big O terms, the `print` statement will get executed _(17 * n)_ number of times, where _n_ is the length of `input_list`. While determining time complexity, we drop the constants. So, the time complexity of this algorithm is _O(n)_, where n is the length of `input_list`. In other words, the time complexity is linearly proportional to the input size.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 8 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: 5qCZ8q
* title: Big O
##### !question

What is the time complexity of the following piece of code?

```python
def greet_friends(input_list):
    count = len(input_list)
    i = 0
    while i < count:
        for j in range(count):
            print(f"Hello, Friend #{i+1} in {j+1}!")
        i += 1
```

##### !end-question
##### !options

* O(1)
* O(log n)
* O(n)
* O(n log n)
* O(n<sup>2</sup>)
* O(n<sup>3</sup>)

##### !end-options
##### !answer

* O(n<sup>2</sup>)

##### !end-answer
##### !explanation

There are two nested loops in this method. Each loop runs _n_ number of times where _n_ is the length of `input_list`. Since the loops are nested, the loop will run _n * n_ number of times.

So, the times complexity of this algorithm is _O(n ^ 2)_ where _n_ is the length of the input test_array. In other words, the time complexity is _quadratic_, which is a _polynomial_ time complexity.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 9 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: rkV75c
* title: Big O
##### !question

What is the time complexity of the following piece of code?

```python
def greet_friends(input_list):
    count = len(input_list)
    k = 0
    while k != count:
        i = 0
        while i < count:
            for j in range(count):
                print(f"Hello, Friend #{i+1} in #{j+1}!")
            i += 1
        k += 1
```

##### !end-question
##### !options

* O(1)
* O(log n)
* O(n)
* O(n log n)
* O(n<sup>2</sup>)
* O(n<sup>3</sup>)

##### !end-options
##### !answer

* O(n<sup>3</sup>)

##### !end-answer
##### !explanation

There are three nested loops in this method, each running _n_ times where _n_ is the length of `input_list`. The time complexity will therefore be _n * n * n_ or in Big O terms _O(n ^ 3)_. In other words, the time complexity will be _cubic_, which is a _polynomial_ time complexity.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 10 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: b9HqKs
* title: Big O
##### !question

What is the time complexity of the following piece of code?

```ruby
def search(input_list, value):
    low = 0
    high = len(input_list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if input_list[mid] > value:
            high = mid - 1
        elif input_list[mid] < value:
            low = mid + 1
        else:
            return mid

    if input_list[low] == value:
        return low

    return None
```

##### !end-question
##### !options

* O(1)
* O(log n)
* O(n)
* O(n log n)
* O(n<sup>2</sup>)
* O(n<sup>3</sup>)

##### !end-options
##### !answer

* O(log n)

##### !end-answer
##### !explanation

There is one loop in this method. The loop is run proportional to the length of `input_list`. With each iteration through the loop, half of the items in `input_list` are eliminated (either first half or second half) until either the value is found or the loop ends. Since with each iteration through the loop, half of the values in the remaining sub-array are eliminated, the time complexity of this algorithm is _logarithmic_ or _O(log n)_ where _n_ is the length of the input parameter, test_array.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 11 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: RIvnUW
* title: Big O
##### !question

Imagine a password of length _n_ that can contain only digit values (numbers).

What will be the time complexity for [a brute force solution](https://en.wikipedia.org/wiki/Brute-force_attack) to break the password?

##### !end-question
##### !options

* O(1)
* O(log n)
* O(n)
* O(n log n)
* O(n<sup>2</sup>)
* O(n<sup>3</sup>)
* O(n!)
* O(10<sup>n</sup>)

##### !end-options
##### !answer

* O(10<sup>n</sup>)

##### !end-answer
##### !explanation

To break the password of size _n_ where each value could be one of ten, 0-9 digits, we will need to try out each possibility starting with all n values being _0_. Then change one of the values to remaining 9 possibilities. For each of these, change another value to each of the remaining possibilities and so on.

<br />

The first of the n values could be any of 0 through 9. For each of these, we try the 10 possible values for the second of the n values and so on. This would lead to _10 * 10 * ... n times_ or in other words _10 ^ n_ possibilities to explore. Hence the time complexity will be _O(10 ^ n)_ or _exponential_.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 12 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: GdZGf5
* title: Big O
##### !question

A traveling salesperson wants to visit _n_ cities. They can start the journey at any city and must visit each city once.

How many different possibilities exist of the order in which they could visit all the _n_ cities?

##### !end-question
##### !options

* O(1)
* O(log n)
* O(n)
* O(n log n)
* O(n<sup>2</sup>)
* O(n<sup>3</sup>)
* O(n!)
* O(10<sup>n</sup>)

##### !end-options
##### !answer

* O(n!)

##### !end-answer
##### !explanation

We start with choosing one of the _n_ cities to be the starting cities. There _n_ possible options for this. For each such choice of first cities, the are _n - 1_ options to select the second city to visit. Then, _n - 2_ options to select the third city to vist and so on until only one city remains to visit.

<br />

Let's consider an example: Let's say _n_ is 3 and the possible cities are Atlanta, Boston and Chicago. Here's how we can explore the problem. We pick one of the three cities to be the first city. Let's say Atlanta. Then, for the next city to visit, there are two options, Boston or Chicago. Let's say we pick Boston then only one city remains unvisited i.e. Chicago. To try out all possible such options would look like to following:

1. Atlanta  -> Boston -> Chicago
1. Atlanta -> Chicago -> Boston
1. Boston -> Atlanta -> Chicago
1. Boston -> Chicago -> Atlanta
1. Chicago -> Atlanta -> Boston
1. Chicago -> Boston -> Atlanta

<br />

This is a total of 6 possibilities, which is the same as _3 * 2 * 1_ or _3!_ i.e. _3 factorial_.

<br />

Generalizing to _n_ cities, this would be _n * (n-1) * (n-2) * ... * 1_ or _n!_ i.e. _n factorial_. In Big O terms, the time complexity will be _O(n!)_ or _factorial_.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->
