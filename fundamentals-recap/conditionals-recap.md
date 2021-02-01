# Conditionals Recap

## Learning Goals

- Define truthiness and falsiness
- Use `and` and `or` conditional logic

## Introduction

Let's ensure we're on the same page about some programming fundamentals by reviewing conditional logic!

## Vocabulary and Synonyms

| Vocab                  | Definition                                                                                                                                                           | Synonyms    | How to Use in a Sentence                                                                                                                       |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Boolean                | A data type that has only two valid values, `True` and `False`, and represent true and false                                                                         | bool        | "The variable `is_wednesday` is a boolean, and it's `True` if it's Wednesday, and `False` if it's not."                                        |
| Conditional Expression | An expression that evaluates to either truthy or falsy, typically used in order to determine if a conditional requirement is met. Usually used with `if` statements. | conditional | "Our code asks `is_wednesday` is equal to `True` with `is_wednesday == True`. If that conditional is true, then we wear our Wednesday outfit." |
| Truthy                 | A value that is considered `True` inside a conditional expression, even if it is not literally `True`                                                                | -           | "The value of `is_wednesday` ended up being `"pink"` instead of `True`, but since `"pink"` is truthy, we wore our Wednesday outfit."           |
| Falsy                  | A value that is considered `False`, even if it is not literally `False`                                                                                              | -           | "The value of `is_wednesday` ended up being `0`, which is falsy. Therefore, it's not Wednesday."                                               |

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
a_different_expression_is_truthy = True

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
True and 100
1 and True
3 > 0 and 100 <= 999
```

For `or`, if at least one side is truthy, then the entire expression is `True`. Otherwise, it's `False`. The following examples evaluate as `True`:

```python
False or True
False or 1
0 or True
3 > 0 or 100 > 999
```

### `and` Truth Table

Use this table to remember what `and` statements do, where "Left" refers to what's on the left of the `and`, "Right" refers to what's on the right of `and`, and "Result" is what the expression evaluates to.

| Left  | Right | Result |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | False  |
| False | True  | False  |
| False | False | False  |

### `or` Truth Table

Expressions with an `or` evaluate to `True` when at least one side of the `or` is truthy.

| Left  | Right | Result |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

## Negation With `not`

The `not` operator goes before any expression and _negates_ that expression. When `not` is in front of a truthy expression, the entire expression becomes `False`. When `not` is in front of a falsy expression, the entire expression becomes `True`.

The following examples all evaluate to `True`:

```python
not False
not 0
True and not False
not False or False
not None
```

The following examples all evaluate to `False`:

```python
not True
not 1
True and not True
not True or False
```

## Order of Operations and Operator Precedence

Conditional expressions can grow in size and complexity. How do we determine that they are truthy or falsy?

Generally, conditional expressions are evaluated from left-to-right, and each expression with one operator resolves first before moving to the next operator.

Consider, which evalutes to `False`:

```python
10 < 2 > True
```

First, `10 < 2` is evaluated to `False`. Then, we consider `False` to be the left side of the next operator, and evaluate `False > True`. `False > True` evaluates to `False`. Therefore, the entire expression is `False`.

### Different Operators Have Priority

When there are multiple kinds of operators in a single conditional expression, operators with higher precedence get evaluated first.

This is an abbreviated list of operators in their "operator precedence" order, where 1 has the highest precedence and will be evaluated before the second. 2 has the second-highest precedence and is evaluated before 3, etc.

1. `or`
1. `and`
1. `not`
1. `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==`
1. `+`, `-`
1. `*`, `/`, `//`, `%`
1. `**`

Operators in the equal levels of precedence are evaluated left-to-right.

### Expressions in Parentheses Always Get Grouped Together

Expressions that are grouped together in parentheses `()` will always only get evaluated together.

Consider these examples that all evalute to `True`:

```python
( 100 > 3 ) == ( 5 < 6 )
not ( 3 > 100 )
( 5 * 5 ) > ( 20 + 4)
True != ( not True )
False or (not ( 3 > 100 ))
False or (( 3 > 100 ) or not False)
```

## Check for Understanding

<!-- Question 1 -->

<!-- prettier-ignore-start -->
### !challenge

* type: checkbox
* id: AP5ndq
* title: Conditionals Recap

##### !question

Assume we have the following variable declarations:

```python
var1 = None
var2 = 1
var3 = {}
var4 = [0, 0]
var5 = "None"
```

Select all options that will evaluate to true:

##### !end-question
##### !options

* `var1 or var2`
* `var3 or (var1 and var2)`
* `var5 and var2`
* `var4 or var3`
* `not var5 and var2`
* `var5 or var3`
* `var2 or not var5`
* `not (var3 or var1)`

##### !end-options
##### !answer

* `var1 or var2`
* `var5 and var2`
* `var4 or var3`
* `var5 or var3`
* `var2 or not var5`
* `not (var3 or var1)`

##### !end-answer
##### !hint

```python
var1 = None # will resolve to False
var2 = 1 # will resolve to True
var3 = {} # will resolve to False
var4 = [0, 0] # will resolve to True (note, only an empty list will resolve to False, even though all ov the values in this list would themselves resolve to False, the list is not empty)
var5 = "None" # will resolve to True (this is a string, not the keyword None)

var1 or var2 
# False or True evaluates to True
var3 or (var1 and var2) 
# False or (False and True) evaluates to False or False which evaluates to False
var5 and var2 
# True and True evaluates to True
var4 or var3 
# True or False evaluates to True
not var5 and var2 
# not True and True evaluates to False and True which evaluates to False
var5 or var3 
# True or False evaluates to True
var2 or not var5 
# True or not True evaluates to True or False which evaluates to True
not (var3 or var1) 
# not (False or False) evaluates to not False which evaluates to True
```

##### !end-hint
##### !explanation

```python
var1 = None # will resolve to False
var2 = 1 # will resolve to True
var3 = {} # will resolve to False
var4 = [0, 0] # will resolve to True (note, only an empty list will resolve to False, even though all ov the values in this list would themselves resolve to False, the list is not empty)
var5 = "None" # will resolve to True (this is a string, not the keyword None)

var1 or var2 
# False or True evaluates to True
var3 or (var1 and var2) 
# False or (False and True) evaluates to False or False which evaluates to False
var5 and var2 
# True and True evaluates to True
var4 or var3 
# True or False evaluates to True
not var5 and var2 
# not True and True evaluates to False and True which evaluates to False
var5 or var3 
# True or False evaluates to True
var2 or not var5 
# True or not True evaluates to True or False which evaluates to True
not (var3 or var1) 
# not (False or False) evaluates to not False which evaluates to True
```

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->
