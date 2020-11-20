# Pseudocode and Logic

## Learning Goals

By the end of this lesson, we will be able to...

- Define pseudocode 
- Explain how pseudocode can describe logic before implementation 
- Use pseudocode to describe logic before implementation

## Introduction

Our problem-solving process includes:

1. Read the problem
2. Clarify the problem with questions
3. Break down the problem into smaller sub-problems
4. Think through the solution with ideas, notes, pseudocode, comments, explanations, and tasks left to do more research on
5. Write parts of the solution in Python code
6. Repeat steps 4-6

As our programs become more complicated, it becomes harder to know where to get started, break down the steps that need to be done, and write clean code.

Breaking down a problem allows us to focus on what needs to be done and create steps to arrive at the minimum of what is needed to solve a problem. 

Today we will focus on a strategy that can help us accomplish these steps: starting with pseudocode.

## Vocabulary and Synonyms

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---
Pseudocode | an informal code style intended to give explanation and meaning | - | "Before I approach writing my Python code, I'll start with pseudocode," "I deleted my pseudocode line by line as I translated it into Python"

## What is Pseudocode?

**[Pseudocode](https://en.wikipedia.org/wiki/Pseudocode)** is a term that describes **informal, non-working, non-functioning lines of code intended to give explanation and meaning to developers.** It is code that is not intended to be part of the final solution/program.

Pseudocode...
- Catches logical errors and bugs more quickly
- Can possibly express thoughts more clearly than code
- Makes changes easier
- Documents our work
- Supports iterative refinement

Pseudocode allows us to think through the logic of solving a problem before implementing functioning code. It can help dramatically with our creative flow because what we write on the screen can match exactly what is in our brain.

By integrating pseudocode into the coding process, we'll be able to plan, communicate, and debug code better and more quickly.

### Examples

Observe the following examples. Try to figure out the goal of each block of code. Which block of code is easier to read and understand the goal?

1.
```python
fruits = ['apples', 'oranges', 'bananas', 'canned o-shaped spaghetti noodles']
grocery_list = []
loop through each fruit in fruits
  if the fruit is not 'canned o-shaped spaghetti noodles'
    then add the fruit to grocery_list
  end the conditional if
end the loop
```

2.
```python
fruits = ['kiwis', 'mangos', 'bananas']
fruit_basket = []

for fruit in fruits:
    fruit_basket.append(fruit)


if len(fruits) == len(fruit_basket):
    print("Successful!")
```

Which block of code is easier to read and understand the goal?

Overall, it should be easier to read Example 1 and understand its goal because it has pseudocode, or understandable descriptions of code.

Example 2 is full of working, functional code. Sometimes, Example 2 is easier to read, because it has less information to parse through. However, this requires developers to know the precise syntax at the time of writing it.

### Pseudocode Can Be Any Style

There are no rules about pseudocode and what it should look like! Therefore, all of these are valid examples of pseudocode.

The only rule is that **pseudocode should be deleted from the final solution, to ensure that the final solution runs correctly.**

It's more important to integrate the pseudocode _process_ rather than worry about pseudocode style.

### More Examples

Given the following problem, look at these different and valid examples of pseudocode.

Calculate the average of the numbers 3, 5, 6, 15, and 27 using a loop.

1.
```python
make a numbers variable, and it is an array
make a sum variable, and it starts with a value of 0

loop through each number in numbers array
  add number to sum
end the loop

the average is sum / number
```

2.
```python
# numbers is numbers from prompt
numbers = [3, 5, 6, 15, 27]
sum = 0

loop each number in numbers
  increment sum by number amount with sum += number
end

average = sum / number
```

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->

### !challenge

* type: short-answer
* id: fc11b33d-33b0-47c2-9d01-f6dc33ae88d8
* title: Pseudocode Style

##### !question

How do you describe the difference between these two styles of pseudocode? Which one is more "your style"? Why?

##### !end-question

##### !placeholder

Your answer here

##### !end-placeholder

##### !answer

/.+/

##### !end-answer

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->


## Applying the Process

In our problem-solving steps, we can use pseudocode to think through the solution with ideas, notes, and comments. We apply the process of writing pseudocode before we write implementation code.

In the two examples below, we should witness these things:

1. Break down the problem into sub-problems
1. Write pseudocode first
1. Then Python code
1. Repeat

### Applying the Process: Example 1

Calculate the average of the numbers 3, 5, 6, 15, and 27 using a loop.

1.
```python
make a numbers variable, and it is an array
make a sum variable, and it starts with a value of 0

add each number in numbers to sum using a loop

the average is sum / the total number of numbers
```

2.
```python
make a numbers variable, and it is an array
make a sum variable, and it starts with a value of 0

loop through each number in numbers array
  add number to sum
end the loop

the average is sum / the length of the numbers array
```

3.
```python
# numbers is numbers from prompt
numbers = [3, 5, 6, 15, 27]
sum = 0

loop through each number in numbers array
  increment sum by number amount with sum += number
end

average = sum / len(numbers)
```

4.
```python
numbers = [3, 5, 6, 15, 27]
sum = 0

for number in numbers:
    sum += number

average = sum / len(numbers)
```

### Applying the Process: Example 2

Count the number of even numbers from the numbers 3, 5, 6, 15, and 27 using a loop

1.
```python
make numbers variable: array, 3, 5, 6, 15, and 27 from prompt
make number of even numbers variable: start at 0

loop through each number in numbers
  if the number is even
    then add 1 to number of even numbers
  else
    then the number is odd
    dont do anything
  end else
end loop
```

2.
```python
numbers = array, 3, 5, 6, 15, and 27
num_of_even_nums = start at 0

for each number in numbers
  if the number is even
    then add 1 to number of even numbers
  else
    then the number is odd
    dont do anything
  end else
end
```

3.
```python
numbers = [3, 5, 6, 15, 27]
num_of_even_nums = 0

for number in numbers
  if number % 2 == 0
    then add 1 to number of even numbers
  else
    then the number is odd
    dont do anything
  end
end
```

4.
```python
numbers = [3, 5, 6, 15, 27]
num_of_even_nums = 0

for number in numbers:
    if number % 2 == 0:
        num_of_even_nums += 1

print("The number of even numbers is #{num_of_even_nums}")
```

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->

### !challenge

* type: multiple-choice
* id: b3bea8fe-e0c4-47f2-b017-2afa83e62681
* title: Pseudocode: Process

##### !question

Which of the following is an accurate description of the process in Examples 1 and 2?

##### !end-question

##### !options

* The developer started with equal parts of readable pseudocode and working Python code

* The developer started with a lot of readable pseudocode, and replaced the pseudocode with Python code step-by-step, starting with the "outermost" (non-indented) pseudocode

* The developer started with a lot of readable pseudocode, and replaced the pseudocode with Python code step-by-step, starting with the "innermost" (indented) pseudocode

* The developer started with a working Python solution, and then replaced the Python code with pseudocode

##### !end-options

##### !answer

* The developer started with a lot of readable pseudocode, and replaced the pseudocode with Python code step-by-step, starting with the "outermost" (non-indented) pseudocode

##### !end-answer

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->

## Check for Understanding

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->

### !challenge

* type: multiple-choice
* id: b3e5ad91-21e4-4553-a2a5-5173c0a902b4
* title: Pseudocode: Definition

##### !question

Which of these is the best definition of pseudocode?

##### !end-question

##### !options

* Pseudocode is a set of comments in code intended to give explanation to non-programmers

* Pseudocode is a formal and rigid system of writing code intended to help a developer work through a problem

* Pseudocode is an informal, non-working, non-functioning system of writing code intended to help a developer work through a problem

* Pseudocode is the code in a programming solution that can be understood by developers

##### !end-options

##### !answer

* Pseudocode is an informal, non-working, non-functioning system of writing code intended to help a developer work through a problem

##### !end-answer

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->
<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->


### !challenge

* type: multiple-choice
* id: 16111178-b617-4ec4-8e36-8b70de666b9b
* title: Pseudocode: Benefits

##### !question

Which of these is not a benefit of writing pseudocode?

##### !end-question

##### !options

* Makes Changes Easier
* Catch bugs and incorrect logic sooner and faster
* Supports iterative refinement
* Automatically verifies that your code works and is complete

##### !end-options

##### !answer

* Automatically verifies that your code works and is complete

##### !end-answer

### !end-challenge

### !challenge

* type: multiple-choice
* id: 5679488f-b26e-4655-bd3b-10269ac08e61
* title: Pseudocode: Process

##### !question

Which of these describes a general process of incorporating pseudocode into solving a problem

##### !end-question

##### !options


* Read the problem, clarify the problem, write pseudocode, write Python code, repeat
* Read the problem, clarify the problem, break it into smaller sub-problems, write pseudocode, write Python code, repeat
* Write pseudocode, write Python code, repeat
* Write Python code, write pseudocode, rewrite Python code, repeat

##### !end-options

##### !answer

* Read the problem, clarify the problem, break it into smaller sub-problems, write pseudocode, write Python code, repeat

##### !end-answer

### !end-challenge
