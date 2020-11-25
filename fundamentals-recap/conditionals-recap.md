# Conditionals Recap

## Learning Goals

- Define truthiness and falsiness
- Use `and` and `or` conditional logic

## Introduction

Let's ensure we're on the same page about some programming fundamentals by reviewing conditional logic!

## Vocabulary and Synonyms

Boolean
Conditional
Truthy
Falsy

## Truthiness vs. Falsiness

There are two boolean values: `True` and `False`, and they represent the concept of true and false.

When faced with the question of "is this value true or false?," values that are not booleans become truthy or falsey. A truthy value is something that would be considered `True`, even if it is not literally the value `True`. A falsey value is considered `False`, even if it's not literally `False`.

In Python, _all values are truthy_... with some exceptions.

The following values are falsey, and will resolve to `False` in a conditional statement:
- `None`
- `0` and `0.0`
- `""` (empty string)
- `[]` (empty list)
- `{}` (empty dictionary)
- There are a few more values; look them up!

## `if`, `elif`, `else` Control Statements

Using truthiness and falsiness, we can create control statements in Python. These statements allow for conditional logic: in _some_ contexts, one set of code should run, in contrast to _other_ contexts. What those contexts are depends on the control statement!

```python
this_expression_is_truthy = True
a_different_experssion_is_truthy = True

if this_expression_is_truthy:
    print("The expression is truthy!")
    print("We will run all code in the if clause.")
elif a_different_expression_is_truthy:
    print("The above if clause did NOT run...")
    print("AND this different expression IS truthy")
    print("So now we run the code is in this clause.")
else:
    print("The expression is falsey!")
    print("We will run all code in the else clause.")
```

## `and` vs. `or` Boolean Operations

We can combine two comparisons with a boolean operation. These expressions also eventually evaluate to `True` or `False`.

The boolean operations are:
- `and`
- `or`
- `not`

For the operations `and` and `or`, both of these have two sides: a left side and a right side. The operations use these two sides.

```python
apples and oranges
apples or oranges
```

For `and`, if and only if both sides are truthy, then the entire expression is `True`. Otherwise, it's `False`. The following examples use `and` and evaluate as `True`:

```python
True and True
3 and 100
3 > 0 and 100 <= 999
```

For `or`, if at least one side is truthy, then the entire experssion is `True`. Otherwise, it's `False`. The following examples evaluate as `True`:

```python
False or True
0 or 100
3 > 0 or 100 > 999
```

### `and` Truth Table

Use this table to remember what `and` statements do, by using the first column as the value of the left side, and the first row as the value of the right side.

| | True | False
| --- | --- | ---
| **True** | True | False
| **False** | False | False

### `or` Truth Table

Expressions with an `or` evaluate to `True` when at least one side of the `or` is truthy.

| | True | False
| --- | --- | ---
| **True** | True | True
| **False** | True | False

