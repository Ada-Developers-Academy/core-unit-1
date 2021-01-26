# Practice: Fundamentals Vocabulary

## Directions

Complete these questions. Retry questions until you have the correct answer on each. Use any resource to answer these questions (including notes, other code, the Internet, assistance from others).

When you finish, write down any remaining questions you have in your notes, and bring them to class.

# Practice!

<!-- Question 1 -->

<!-- prettier-ignore-start -->
### !challenge

* type: multiple-choice
* id: 82df3237-9f64-4ddc-b5a2-843f53430b15
* title: Fundamentals Vocabulary Review I

##### !question

What is a statement?

##### !end-question

##### !options
* a unit of code that can be evaluated into one value
* a unit of code that performs an action
* a value

##### !end-options

##### !answer
* a unit of code that performs an action
##### !end-answer

### !end-challenge
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
### !challenge

* type: multiple-choice
* id: 3a91ff89-ad35-4f18-bb44-fccd104677dc
* title: Fundamentals Vocabulary Review II

##### !question

What is the expression in this code snippet?

```python
if score > 150000:
   print(“New High Score!”)
```
##### !end-question

##### !options

* `if score > 150000:`
* `print("New High Score!")`
* `score > 150000`

##### !end-options

##### !answer

* `score > 150000`

##### !end-answer

### !end-challenge
<!-- prettier-ignore-end -->


<!-- prettier-ignore-start -->
### !challenge

* type: multiple-choice
* id: 5a5b2aa8-08ef-4a98-bf3c-e1a61461ceaa
* title: Data Types review

##### !question

The code snippet below returns a `TypeError: can't multiply sequence by non-int of type 'str’` which means we cannot multiply strings. Let's check the data type of the inputs, starting with `n1`. Which option holds the syntax we use to check `n1`'s data type in a print statement?

```python
1 n1 = input("enter a number: ")
2 n2 = input("enter another number: ")
3
4 def multiply(n1, n2):
5  	return n1*n2
6
7 multiply(n1,n2)
```

##### !end-question

##### !options

* `type = n1`
* `type(n1)`
* `type.n1()`
* `n1 = type()`

##### !end-options

##### !answer

* `type(n1)`

##### !end-answer

### !end-challenge
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
### !challenge

* type: checkbox
* id: 8174678f-cf23-4605-a033-91c957a2cf81
* title: Casting Review

##### !question

In this code, we need to cast some value into an integer with `int()`. Pick all lines of code where _it's possible_ to cast a value into an int with `int()`.

```python
1 n1 = input("enter a number: ")
2 n2 = input("enter another number: ")
3
4 def multiply(n1, n2):
5  	return n1*n2
6
7 multiply(n1,n2)
```
##### !end-question

##### !options
* line 1
* line 2
* line 5
* line 7
##### !end-options

##### !answer
* line 1
* line 2
* line 5
* line 7
##### !end-answer

##### !explanation
The int() function could be used anywhere to convert a piece of data into an integer.
##### !end-explanation

### !end-challenge
<!-- prettier-ignore-end -->


<!-- prettier-ignore-start -->
### !challenge

* type: checkbox
* id: b2c12540-3562-4fe1-aedc-54332282b9aa
* title: Literal Review

##### !question

Which of the following options is a dictionary literal?

##### !end-question

##### !options

*
```python
fruits = {
    "apple": "gala apple",
    "orange": "sumo orange",
    "pear": "anjou pear",
}
```
* `fruits`
* `"orange": "sumo orange"`

##### !end-options

##### !answer

*
```python
fruits = {
    "apple": "gala apple",
    "orange": "sumo orange",
    "pear": "anjou pear",
}
```

##### !end-answer

### !end-challenge
<!-- prettier-ignore-end -->
