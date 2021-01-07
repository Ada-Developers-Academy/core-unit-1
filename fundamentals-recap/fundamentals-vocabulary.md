# Fundamentals Vocabulary

## Learning Goals

- Define expression
- Define statement
- List all data types in Python
- Define literal

## Introduction

Let's ensure we're on the same page about some programming fundamentals by reviewing vocabulary!

## Vocabulary and Synonyms

| Vocab      | Definition                                                                                                                             | Synonyms | How to Use in a Sentence                                                                                                                                                                                                                                                                                   |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Expression | A unit of code that can be evaluated into one value                                                                                    | -        | "The expression `999 > 0` is `True`!" "We use the expression `999 > 0` to determine if our code prints `"Hello!"`," "While I'm debugging, I need to keep checking what the expression `total_price * 1.1` evaluates into"                                                                                  |
| Statement  | A unit of code that is used to execute a change                                                                                        | -        | "Variable assignment is a statement that changes what a variable refers to," "I put some print statements on lines 14-17 to help me figure out what's going on," "Don't forget to check the syntax on your if statement!"                                                                                  |
| Variable   | A name that is a reference to a specific place in memory, and the value stored there. Variables can be assigned and reassigned values. | var      | "I assigned the list `["red", "green", "blue]` to my variable named `my_rainbow`," "I can read my variable `my_rainbow` and get back the value it holds"                                                                                                                                                   |
| Literal    | A value that is the value itself.                                                                                                      | -        | "Variables are not literals, because they don't look like their value," "I can index a list literal like this: `["red", "blue", "yellow"][0]`. I didn't use a variable that holds a list, but a list value itself," "Literals help me experiment with code, because I'm looking at the values themselves." |

## Expressions: Everything Becomes a Value

In programming, an **expression** is a unit of code that can be evaluated into one value.

We use expressions mainly to get a _value_.

The following are examples of expressions, because when our code runs, these turn into one value.

| Expression        | Value                                   |
| ----------------- | --------------------------------------- |
| `42`              | `42`                                    |
| `800 + 900`       | `1700`                                  |
| `"Hello, World!"` | `"Hello, World!"`                       |
| `True`            | `True`                                  |
| `999 > 0`         | `True`                                  |
| `999 <= 0`        | `False`                                 |
| `999 == 0`        | `False`                                 |
| `my_list[0]`      | The first element of the list `my_list` |

### !callout-info

## Function Calls are Expressions

For functions, we can interpret a function call used as an evaluated value as an _expression_.

### !end-callout

## Statements

In programming, a **statement** is a unit of code that contains an action to execute.

We use statements mainly to _perform an action with side effects_.

The following are examples of statements.

| Statement                 | Side Effect                                                         |
| ------------------------- | ------------------------------------------------------------------- |
| `foo = "A value for foo"` | Assigns the variable `foo` to a value                               |
| `return foo`              | Exits a function, and optionally returns a value                    |
| `if` statements           | Begins a conditional clause                                         |
| `pass`                    | Statement to say "there is nothing to execute on this line of code" |

Many of these statements use syntax that will be covered more in-depth with deeper knowledge.

### !callout-info

## Statement

For functions, we can interpret a function call used to execute a change as a _statement_.

### !end-callout

## Values Have Data Types

Every value in Python has a data type.

### Built-in Data Types

This is a list of all data types available in the Python programming language.

| Data Type        | Description                                                                                                                                                  |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Integer          | Represents an integer! A whole number that is positive, negative, or zero.                                                                                   |
| Float            | Represents a number that isn't whole; it is fractional, or has a decimal place.                                                                              |
| String           | Represents text, specifically with an ordered sequence of characters.                                                                                        |
| Boolean          | Represents true or false.                                                                                                                                    |
| None             | Represents the concept of no value, or the absence of a value.                                                                                               |
| List             | An ordered list of values. Items in the list are sometimes called elements. Can get the value of an item by using square brackets and the index of the item. |
| Dictionary       | An unordered collection of key-value pairs. Can access values in the dictionary by using square brackets and the name of the key.                            |
| Range            | A sequence of numbers between a start, stop, and incrementing by a step.                                                                                     |
| Tuple            | An ordered, unchangeable collection of items.                                                                                                                |
| Set, frozenset   | An unordered collection. Cannot access values with index or key; must use a loop.                                                                            |
| bytes, bytearray | A collection of binary digits (bits).                                                                                                                        |

### !callout-info

## Explore Data Types

We will not go into depth with tuples or sets in this curriculum, but they are interesting and useful data types. You are free to learn more and apply them; follow your curiosity!

### !end-callout

### Get the Data Type with `type()`

If we're ever unsure about what the data type of a value is, we can use Python's built-in method `type()` to read the data type.

We use the method like this:

```python
type( expression_to_get_the_type_of )
```

Examples:

```python
print(type("This is a string!"))
print(type(6789 * 100))
print(type(3.3))
print(type(["do", "re", "mi"]))

my_bicycle_details = {
    "frame_color": "red",
    "num_of_wheels": 2,
    "grip_tape_color": "turquoise"
}
print(type(my_bicycle_details))
print(type(my_bicycle_details["num_of_wheels"]))
```

### Casting

We can convert a value to a different data type.

We can use these methods to convert a value into another data type

- `int()`
- `float()`
- `str()`
- `bool()`

```python
my_lucky_number = 7
my_num_as_float = float(my_lucky_number)
my_num_as_str = str(my_lucky_number)
my_num_as_bool = bool(my_lucky_number)

print(my_num_as_float)
print(my_num_as_str)
print(my_num_as_bool)

my_lucky_fraction = 3.33
my_fraction_as_int = int(my_lucky_fraction)

print(my_fraction_as_int)
```

### !callout-info

## Experiment with Casting

Often times, the behavior of converting isn't very predictable. What happens when we cast an empty list into a string? Or an integer into a boolean? It is best to experiment with converting in a REPL before using it in code.

### !end-callout

## Literals Are The Thing Itself

In programming, a **literal** is a way to write a value that is the value itself. If the value _looks_ the same as its value, then it is a literal.

```python
"This string is a string literal, because this string is literally a string."
```

This is in contrast to variables, which have a value, but are not the value itself, nor are they written as the value itself.

```python
my_string = "Hello, world!"
```

The string `"Hello, world!"` and the variable `my_string` both have the same value. However, they differ in how the value is written. `"Hello, world!"` is a string literal because what we see is literally what the value is. `my_string` does not _look_ like what its value is. `my_string` is not _literally_ the string `"Hello, world!"`.

```python
my_dict = {
    "bananas": 1,
    "mangos": 2
}
```

The dictionary `{"bananas": 1, "mangos": 2}` is a dictionary literal because it looks like its value. The variable `my_dict` refers to a dictionary as its value, but isn't a dictionary literal.

## Printing and Formatting Strings

Often times, we want to combine strings and non-string expressions.

Python allows us to combine these by making **f-strings.** These strings have a prefix of `f` at the beginning, and evaluate any expression that is contained in `{}` curly braces.

```python
f"The string to format and include Python syntax, where expressions inside curly braces turn into a value!: {2 + 3}"
```

We can observe these examples:

```python
print(f"The sum of 2 + 3 is {2 + 3}")

pineapples = "mY pInEaPpLe mEsSaGe"

print(f"Here is {pineapples}!")
```

There are many other ways to combine strings and non-string values. Some methods include concatenation, or the `format()` method. Feel free to research these and use them; follow your curiosity!

## Check for Understanding

<!-- Question 1 -->

<!-- prettier-ignore-start -->
### !challenge

* type: short-answer
* id: e255bf2d-f703-4a22-ba13-f142584bba93
* title: Expressions and Statements

##### !question

Using the code snippet below, on line 2, what is the expression?

```python

1   test_num = 5
2   if test_num > 10:
3       print "Bigger than ten!"

```
##### !end-question
##### !answer

test_num > 10

##### !end-answer
##### !hint

An expression is a piece of code that evaluates to a value.  In the conditional `if` statement, what is the portion that evaluates to True or False?

##### !end-hint
##### !explanation

In the `if` statement, `test_num > 10` will evaluate to False.  It is the expression that is being evaluated in the statement.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->

<!-- prettier-ignore-start -->
### !challenge

* type: short-answer
* id: f07c693b-b2f2-4e16-a114-74cf6fcfe43a
* title: Literals

##### !question

Using the code snippet below, identify at least 1 literal:

```python

1   test_num = 5
2   if test_num > 10:
3       print "Bigger than ten!"

```

##### !end-question
##### !answer

/5|10|"Bigger than ten!"/

##### !end-answer
##### !hint

There are three literals in the code snippet.  Remember, the literal is the value written as itself.

##### !end-hint
##### !explanation

There are three literals in the code snippet, `5`, `10` and `"Bigger than ten!"`.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->
