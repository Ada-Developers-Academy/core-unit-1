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

<!-- Question 2 -->
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

<!-- Question 3 -->
<!-- prettier-ignore-start -->
### !challenge

* type: multiple-choice
* id: 5a5b2aa8-08ef-4a98-bf3c-e1a61461ceaa
* title: Data Types review

##### !question

Consider this code. Running this code produces the error `TypeError: can't multiply sequence by non-int of type 'str'`. Which of these options most accurately describes the cause of this error?

```python
n1 = input("enter a number: ")
n2 = input("enter another number: ")
def multiply(n1, n2):
 	return n1*n2
multiply(n1,n2)
```

##### !end-question

##### !options

* The function `input()` could give back an integer, string, or float. The type of `n1` and `n2` is unknown. Multiplication of unknown data types isn't possible.
* The function `input()` always gives back a string. The values of `n1` and `n2` are strings. Multiplication in the line `n1*n2` gives an error, because mulitplying strings isn't possible.
* The function `multiply()` calls `n1*n2`. The values of `n1` and `n2` are unknown when running the line `n1*n2`. Multiplication of unknown data types isn't possible.
* The function `mulitply()` requires `n1` and `n2` to be integers. `"enter a number: "` and `"enter another number: "` are strings, and multiplying strings isn't possible.

##### !end-options

##### !answer

* The function `input()` always gives back a string. The values of `n1` and `n2` are strings. Multiplication in the line `n1*n2` gives an error, because mulitplying strings isn't possible.

##### !end-answer

### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 4 -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: FsVllh
* title: Fundamentals Vocabulary
##### !question

What is the value of the expression `int("100")`?

If there is a string, use double-quotes where needed.

##### !end-question
##### !answer

100

##### !end-answer
##### !hint

Open up the Python interpreter with the command `python3` in the command line.

Use the Python interpreter to experiment with code. We can evaluate any expression in the interpreter. For example, try typing in the expression `int("100")` and pressing enter, and see what output comes out.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->


<!-- Question 5 -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: PLQcV3
* title: Fundamentals Vocabulary
##### !question

What is the value of the expression `int("-99")`?

If there is a string, use double-quotes where needed.

##### !end-question
##### !answer

-99

##### !end-answer
##### !hint

Open up the Python interpreter with the command `python3` in the command line.

Use the Python interpreter to experiment with code. We can evaluate any expression in the interpreter. For example, try typing in the expression `int("100")` and pressing enter, and see what output comes out.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: unzxTM
* title: Fundamentals Vocabulary
##### !question

What is the value of the expression `int(True)`?

If there is a string, use double-quotes where needed.

##### !end-question
##### !answer

1

##### !end-answer
##### !hint

Open up the Python interpreter with the command `python3` in the command line.

Use the Python interpreter to experiment with code. We can evaluate any expression in the interpreter. For example, try typing in the expression `int("100")` and pressing enter, and see what output comes out.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->


<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: JT1AQl
* title: Fundamentals Vocabulary
##### !question

What is the value of the expression `int(False)`?

If there is a string, use double-quotes where needed.

##### !end-question
##### !answer

0

##### !end-answer
##### !hint

Open up the Python interpreter with the command `python3` in the command line.

Use the Python interpreter to experiment with code. We can evaluate any expression in the interpreter. For example, try typing in the expression `int("100")` and pressing enter, and see what output comes out.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->



<!-- Question 4 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: v5J2Qt
* title: Fundamentals Vocabulary
##### !question

What is the value of the expression `int("Hello, casting!")`?

##### !end-question
##### !options

* `0`
* Error
* `SyntaxError: invalid syntax`
* `ValueError: invalid literal for int() with base 10: 'Hello, casting!'`

##### !end-options
##### !answer

* `ValueError: invalid literal for int() with base 10: 'Hello, casting!'`

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->


<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: fsmTXv
* title: Fundamentals Vocabulary
##### !question

What is the value of the expression `float("100")`?

If there is a string, use double-quotes where needed.

##### !end-question
##### !answer

100.0

##### !end-answer
##### !hint

Open up the Python interpreter with the command `python3` in the command line.

Use the Python interpreter to experiment with code. We can evaluate any expression in the interpreter. For example, try typing in the expression `int("100")` and pressing enter, and see what output comes out.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->


<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: 3uz8do
* title: Fundamentals Vocabulary
##### !question

What is the value of the expression `float(10 / 2)`?

If there is a string, use double-quotes where needed.

##### !end-question
##### !answer

5.0

##### !end-answer
##### !hint

Open up the Python interpreter with the command `python3` in the command line.

Use the Python interpreter to experiment with code. We can evaluate any expression in the interpreter. For example, try typing in the expression `int("100")` and pressing enter, and see what output comes out.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->


<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: Sb9SHJ
* title: Fundamentals Vocabulary
##### !question

What is the value of the expression `float(True)`?

If there is a string, use double-quotes where needed.

##### !end-question
##### !answer

1.0

##### !end-answer
##### !hint

Open up the Python interpreter with the command `python3` in the command line.

Use the Python interpreter to experiment with code. We can evaluate any expression in the interpreter. For example, try typing in the expression `int("100")` and pressing enter, and see what output comes out.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: LcXazs
* title: Fundamentals Vocabulary
##### !question

What is the value of the expression `float("Hello, casting!")`?

##### !end-question
##### !options

* `0.0`
* Error
* `SyntaxError: invalid syntax`
* `ValueError: could not convert string to float: 'Hello, casting!'`

##### !end-options
##### !answer

* `ValueError: could not convert string to float: 'Hello, casting!'`

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->


<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: GfI4jM
* title: Fundamentals Vocabulary
##### !question

What is the value of the expression `str(100)`?

If there is a string, use double-quotes where needed.

##### !end-question
##### !answer

"100"

##### !end-answer
##### !hint

Open up the Python interpreter with the command `python3` in the command line.

Use the Python interpreter to experiment with code. We can evaluate any expression in the interpreter. For example, try typing in the expression `int("100")` and pressing enter, and see what output comes out.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->


<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: yzgREY
* title: Fundamentals Vocabulary
##### !question

What is the value of the expression `str(True)`?

If there is a string, use double-quotes where needed.

##### !end-question
##### !answer

"True"

##### !end-answer
##### !hint

Open up the Python interpreter with the command `python3` in the command line.

Use the Python interpreter to experiment with code. We can evaluate any expression in the interpreter. For example, try typing in the expression `int("100")` and pressing enter, and see what output comes out.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->


<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: pw72Cy
* title: Fundamentals Vocabulary
##### !question

What is the value of the expression `str([True, 0, 55.55])`?

If there is a string, use double-quotes where needed.

##### !end-question
##### !answer

"[True, 0, 55.55]"

##### !end-answer
##### !hint

Open up the Python interpreter with the command `python3` in the command line.

Use the Python interpreter to experiment with code. We can evaluate any expression in the interpreter. For example, try typing in the expression `int("100")` and pressing enter, and see what output comes out.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->


<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: qgPojl
* title: Fundamentals Vocabulary
##### !question

What is the value of the expression `bool(100)`?

If there is a string, use double-quotes where needed.

##### !end-question
##### !answer

True

##### !end-answer
##### !hint

Open up the Python interpreter with the command `python3` in the command line.

Use the Python interpreter to experiment with code. We can evaluate any expression in the interpreter. For example, try typing in the expression `int("100")` and pressing enter, and see what output comes out.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->


<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: TnVLkK
* title: Fundamentals Vocabulary
##### !question

What is the value of the expression `bool(-99)`?

If there is a string, use double-quotes where needed.

##### !end-question
##### !answer

True

##### !end-answer
##### !hint

Open up the Python interpreter with the command `python3` in the command line.

Use the Python interpreter to experiment with code. We can evaluate any expression in the interpreter. For example, try typing in the expression `int("100")` and pressing enter, and see what output comes out.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->


<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: gmV017
* title: Fundamentals Vocabulary
##### !question

What is the value of the expression `bool("Hello, string!")`?

If there is a string, use double-quotes where needed.

##### !end-question
##### !answer

True

##### !end-answer
##### !hint

Open up the Python interpreter with the command `python3` in the command line.

Use the Python interpreter to experiment with code. We can evaluate any expression in the interpreter. For example, try typing in the expression `int("100")` and pressing enter, and see what output comes out.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->


<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: TOBAFq
* title: Fundamentals Vocabulary
##### !question

What is the value of the expression `bool(["Hello, string!"])`?

If there is a string, use double-quotes where needed.

##### !end-question
##### !answer

True

##### !end-answer
##### !hint

Open up the Python interpreter with the command `python3` in the command line.

Use the Python interpreter to experiment with code. We can evaluate any expression in the interpreter. For example, try typing in the expression `int("100")` and pressing enter, and see what output comes out.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->


<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: uMYUNK
* title: Fundamentals Vocabulary
##### !question

What is the value of the expression `bool([])`?

If there is a string, use double-quotes where needed.

##### !end-question
##### !answer

False

##### !end-answer
##### !hint

Open up the Python interpreter with the command `python3` in the command line.

Use the Python interpreter to experiment with code. We can evaluate any expression in the interpreter. For example, try typing in the expression `int("100")` and pressing enter, and see what output comes out.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->


<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: 50Wo1z
* title: Fundamentals Vocabulary
##### !question

What is the value of the expression `bool(None)`?

If there is a string, use double-quotes where needed.

##### !end-question
##### !answer

False

##### !end-answer
##### !hint

Open up the Python interpreter with the command `python3` in the command line.

Use the Python interpreter to experiment with code. We can evaluate any expression in the interpreter. For example, try typing in the expression `int("100")` and pressing enter, and see what output comes out.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->


<!-- prettier-ignore-start -->
### !challenge

* type: checkbox
* id: b2c12540-3562-4fe1-aedc-54332282b9aa
* title: Fundamentals Vocabulary

##### !question

Which of the following options is a dictionary literal?

##### !end-question

##### !options

*
```python
{
    "apple": "gala apple",
    "orange": "sumo orange",
    "pear": "anjou pear",
}
```
* `{"apple": "gala apple"}`
* `"orange": "sumo orange"`

##### !end-options

##### !answer

*
```python
{
    "apple": "gala apple",
    "orange": "sumo orange",
    "pear": "anjou pear",
}
```
* `{"apple": "gala apple"}`

##### !end-answer

### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 4 -->
<!-- prettier-ignore-start -->
### !challenge
* type: checkbox
* id: A1c1Qx
* title: Fundamentals Vocabulary
##### !question

Which of the following are literals?

##### !end-question
##### !options

* `"Welcome! Make yourselves comfortable!"`
* `app_name = "Ada's Super Ultra Amazing S-Rank App"`
* `["magenta", "purple", "blue"]`
* `None`
* `count`
* `count = 100`

##### !end-options
##### !answer

* `"Welcome! Make yourselves comfortable!"`
* `["magenta", "purple", "blue"]`
* `None`

##### !end-answer
##### !explanation



##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: checkbox
* id: 5uhdzz
* title: Fundamentals Vocabulary
##### !question

Which of the following are literals?

##### !end-question
##### !options

* `87`
* `"87"`
* `print()`
* `2 + 3`
* `True`
* `[]`

##### !end-options
##### !answer

* `87`
* `"87"`
* `True`
* `[]`

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: checkbox
* id: S9Y41l
* title: Fundamentals Vocabulary
##### !question

Which of the following are expressions?

Assume that all variables are properly defined.

##### !end-question
##### !options

* `sum = 5`
* `total = 10`
* `sum > total`
* `5 - 10`
* `is_eligible and not is_expired`
* `False or (is_eligible and not is_expired)`

##### !end-options
##### !answer

* `sum > total`
* `5 - 10`
* `is_eligible and not is_expired`
* `False or (is_eligible and not is_expired)`

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: yrmRlI
* title: Fundamentals Vocabulary
##### !question

Define what the value `None` means in your own words.

##### !end-question
##### !placeholder

In programming, None means...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: 7kQfOC
* title: Fundamentals Vocabulary
##### !question

What does this line of code print to the console?

```python
print(type("I'm programming!"))
```

Exclude any surrounding quotes. (For example, `print("Hello, World!")` prints `Hello, World!`.)

##### !end-question
##### !answer

/<class 'str'>/

##### !end-answer
##### !hint

Open up the Python interpreter with the command `python3` in the command line.

Use the Python interpreter to experiment with code. We can evaluate any expression in the interpreter. For example, try typing in the expression `int("100")` and pressing enter, and see what output comes out.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: LyP1Nn
* title: Fundamentals Vocabulary
##### !question

What does this code print to the console?

```python
age = 99
print(f"Tomorrow, I will be {age + 1} years old!")
```

Exclude any surrounding quotes. (For example, `print("Hello, World!")` prints `Hello, World!`.)

##### !end-question
##### !answer

Tomorrow, I will be 100 years old!

##### !end-answer
##### !hint

Open up the Python interpreter with the command `python3` in the command line.

Use the Python interpreter to experiment with code. We can evaluate any expression in the interpreter. For example, try typing in the expression `int("100")` and pressing enter, and see what output comes out.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: adQHxI
* title: Fundamentals Vocabulary
##### !question

What does this code print to the console?

```python
age = 99
print("Tomorrow, I will be {age + 1} years old!")
```

Exclude any surrounding quotes. (For example, `print("Hello, World!")` prints `Hello, World!`.)

##### !end-question
##### !answer

Tomorrow, I will be {age + 1} years old!

##### !end-answer
##### !hint

Open up the Python interpreter with the command `python3` in the command line.

Use the Python interpreter to experiment with code. We can evaluate any expression in the interpreter. For example, try typing in the expression `int("100")` and pressing enter, and see what output comes out.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->


<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: SBSiYv
* title: Fundamentals Vocabulary
##### !question

What does this code print to the console?

```python
age = 99
print("Tomorrow, I will be", age + 1, "years old!")
```

Exclude any surrounding quotes. (For example, `print("Hello, World!")` prints `Hello, World!`.)

##### !end-question
##### !answer

Tomorrow, I will be 100 years old!

##### !end-answer
##### !hint

Open up the Python interpreter with the command `python3` in the command line.

Use the Python interpreter to experiment with code. We can evaluate any expression in the interpreter. For example, try typing in the expression `int("100")` and pressing enter, and see what output comes out.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: VNJdEq
* title: Fundamentals Vocabulary
##### !question

What does this code print to the console?

```python
age = 99
print("The current value of age is:", age)
```

Exclude any surrounding quotes. (For example, `print("Hello, World!")` prints `Hello, World!`.)

##### !end-question
##### !answer

The current value of age is: 99

##### !end-answer
##### !hint

Open up the Python interpreter with the command `python3` in the command line.

Use the Python interpreter to experiment with code. We can evaluate any expression in the interpreter. For example, try typing in the expression `int("100")` and pressing enter, and see what output comes out.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: 4jUlbM
* title: Fundamentals Vocabulary
##### !question

What is the command line command to open the Python 3 interpreter?

##### !end-question
##### !answer

python3

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question  -->
<!-- prettier-ignore-start -->
### !challenge
* type: checkbox
* id: NU7rOw
* title: Fundamentals Vocabulary
##### !question

Imagine that we are running the Python 3 interpreter in a Terminal. What are all of the valid commands or key combinations to exit the interpreter, and return to the command line?

##### !end-question
##### !options

* `exit()`
* `close()`
* `quit()`
* `ctrl D`
* `ctrl C`

##### !end-options
##### !answer

* `exit()`
* `quit()`
* `ctrl D`

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

