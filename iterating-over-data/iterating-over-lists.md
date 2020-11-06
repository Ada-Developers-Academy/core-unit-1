# Iterating Over Lists

## Introduction

`for` Loops are one of the most common ways to iterate. `for` loops can iterate over **each element in a list.**

## Learning Goals

- Practice using for loops to iterate through an array

## Vocabulary and Synonyms

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---
`for` loop | A kind of loop that will loop over every element in something iterable, such as a list. | for loop, for-loop, for each loop | "I wrote a `for` loop so I can run my function for each element," "I should write a `for` loop here so I can iterate through the list"

## Syntax for `for` Loops

To iterate over a list, we use the following syntax:

```python
for my_element in my_list:
    print(my_element)
```

| Piece of Code | Notes
| --- | ---
`for` | `for` is a reserved keyword in Python. Python recognizes `for` as the beginning of a `for` loop.
`my_element` | **Replace this** part with a name that represents what each element is. This is the name of the local variable we can use in this `for` loop to represent each element, one at a time.
`in` | `in` is a reserved keyword in Python. It separates the name of the `my_element` variable and the list we're iterating on.
`my_list` | **Replace this** part with the desired list to iterate over. This can be a variable that holds a list, a list literal, or any expression that becomes a list
`:` | This colon begins the `for` loop's body
`    print(my_element)` | **Replace this** with any code that should execute during each loop. This is the loop's body.

### About `my_element`

The variable `my_element` gets assigned and re-assigned through a `for` loop.

When a `for` loop starts, `my_element` gets assigned the value of the first element in the list. Then value of `my_element` changes with each following iteration.

1. In the first iteration, the value of `my_element` will be the first element in the list.
2. In the second iteration, the value of `my_element` will be the second element in the list.
3. In the third, it will be the third element...
4. ... etc., until there are no more elements in the list.

We should always change `my_element` to be a variable name appropriate to the context of the list. What does each element in the list represent?

### About the Loop Body

1. All lines of code inside a for loop **must start at one deeper indentation level compared to the beginning of the loop.**
    - The loop's body ends when the indentation level returns back.
1. All Python logic and syntax still applies inside the loop!

### Examples

Follow these steps for each example:
1. Read through the code. What is the list? What is each element? What do we name each element? How do we use each element in the loop?
2. Predict what will print
3. Run the code and check your prediction

```python
options = ["the place I'm craving but is too far away", "the place we always go to", "that place that just opened but looks too fancy"]

for option in options:
    print(f"What about getting food from {option} tonight?")
```

**Another Example:**

```python
prices = [18.99, 56.00, 48.50, 18.50]

for price in prices:
    taxed_price = price * 1.101
    print(f"The cost of one item is {taxed_price}")

print("That sure was a meal!")
```

## Visualizing `for` Loops

<!-- TODO: Add a diagram to visualize loops, and describe it. -->

One way we can visualize how the value of `my_element` changes over each iteration with a table.

Each column can be some data we want to track, and every row can be one iteration.

| iteration # | index of `my_element` | value of `my_element`
| --- | --- | ---
| 1 | 0 | ...
| 2 | 1 | ...

For example, we can fill out tables for our examples like so:

```python
options = ["the place I'm craving but is too far away", "the place we always go to", "that place that just opened but looks too fancy"]

for option in options:
    print(f"What about getting food from {option} tonight?")
```

| iteration # | index of `option` | value of `option`
| --- | --- | ---
| 1 | 0 | `"the place I'm craving but is too far away"`
| 2 | 1 | `"the place we always go to"`
| 3 | 2 | `"that place that just opened but looks too fancy"`

**Another Example:**

```python
prices = [18.99, 56.00, 48.50, 18.50]

for price in prices:
    taxed_price = price * 1.101
    print(f"The cost of one item is {taxed_price}")

print("That sure was a meal!")
```

| iteration # | index of `price` | value of `price` | value of `taxed_price` at the end of the loop
| --- | --- | --- | ---
1 | 0 | `18.99` | `20.907989999999998`
2 | 1 | `56.00` | `61.656`
3 | 2 | `48.50` | `53.3985`
4 | 3 | `18.50` | `20.3685`

## Variable Scope

Inside `for` loops, we still can access and use any variables that are within scope.

A common pattern we'll use is to initialize a variable before a `for` loop, and modify it within a `for` loop.

Read through this code, and answer these questions:

Is `taxed_prices`
- ... initialized as an empty array inside the `for` loop?
- ... accessed or modified inside the `for` loop? How?
- ... accessed or modified after the `for` loop? How?

```python
prices = [18.99, 56.00, 48.50, 18.50]
taxed_prices = []

for price in prices:
    taxed_price = price * 1.101
    taxed_prices.append(taxed_price)

print(taxed_prices)
```

## Increasing Complexity

Our loop logic can be more complex, and include conditionals, calculations, and function calls.

```python
prices = [18.99, 56.00, 48.50, 18.50]

for price in prices:
    taxed_price = price * 1.101
    if taxed_price > 20:
        print(f"This item costs more than $20.")
    else:
        print(f"We found something under $20!")

print("That sure was a meal!")
```

Loops will often live in functions. We can use a `for` loop on a list that was passed into a function, too!

```python
def consider_options(options):
    for option in options:
        print(f"What about getting food from {option} tonight?")

pizza_places = ["your favorite pizza place", "my favorite pizza place"]
consider_options(pizza_places)
```

We can also put loops inside of loops! We will explore that in a future lesson.

## Check for Understanding


