# Iterating and Special Cases

## Learning Goals

- Define the `break` keyword as a way to exit a loop
- Define the `continue` keyword as a way to advance an iteration in a loop
- Use the `range()` syntax combined with a for loop

## Introduction

There are more things we can do with loops!

Are we able to stop a loop before it gets to the last element? Are we able to use `for` loops on other data structures?

By learning these different pieces of syntax, we can learn to wield them wisely whenever it becomes relevant.

## Vocabulary and Synonyms

| Vocab      | Definition                                                       | Synonyms | How to Use in a Sentence                                                                     |
| ---------- | ---------------------------------------------------------------- | -------- | -------------------------------------------------------------------------------------------- |
| `break`    | A keyword that will exit an entire loop                          | -        | "We can break out of the loop using `break`," "The loop exited early because it saw `break`" |
| `continue` | A keyword that will immediately advance one interation in a loop | -        | "The loop moved on because it saw `continue`"                                                |
| `range()`  | A Python function that creates a sequence                        | -        | "We used a `for` loop and `range()` in order to iterate through a series of numbers.         |

## `break` Exits a Loop

`break` is a keyword that can be used in a `for` loop. When the Python interpreter encounters a `break`, it will immediately exit the current loop, skipping any instructions from after the `break` until the end of the loop. We also say that it _breaks out_ of the loop.

```python
for fruit in ["apples", "oranges", "bananas"]:
    print("I'm in the for loop! The value of fruit is:", fruit)
    break
    print("This message will never print, because the for loop saw break before it saw me...")
```

We can pair this with conditionals (and other logic)!

```python
print("I'm looking for a four leaf clover in the field...")

for field_item in ["grass", "grass", "more grass", "four-leaf clover", "rocks", "rocks", "more rocks"]:
    print("...")
    if field_item == "four-leaf clover":
        print("I found a four-leaf clover!")
        print("My hunt is over! I can leave now")
        break
    print(f"I found {field_item} in the field...")
    print("Better keep looking.")
```

### !callout-info

## for-else

It turns out we can pair a `for` loop with an `else` clause! The `else` clause will run after a `for` loop finishes **if** it did **not** encounter a `break`. The `else` keyword must be at the same level of indentation as the `for`, and be followed by a `:`. The `else` body begins indented one level on the following line.

### !end-callout

```python
for field_item in ["grass", "grass", "more grass", "rocks", "rocks", "more rocks"]:
    print("...")
    if field_item == "four-leaf clover":
        print("I found a four-leaf clover!")
        print("My hunt is over! I can leave now")
        break
    print(f"I found {field_item} in the field...")
    print("Better keep looking.")
else:
    print("I didn't find a four-leaf clover today.")
```

## `continue` Advances One Loop

`continue` is another keyword that can be used in a `for` loop. When the Python interpreter encounters a `continue`, it will immediately jump to the beginning of the current loop, skipping any instructions from after the `continue` until the end of the loop. The loop will resume execution with the next item in the iteration, if one exists. Otherwise, the loop will terminate.

```python
lucky_charms_quantities = {
    "horseshoe": 4,
    "four-leaf clover": 0,
    "lucky coin": 10
}

for charm, quantity in lucky_charms_quantities.items():
    if quantity == 0:
        continue
    print(f"I found one more {charm}!")
    lucky_charms_quantities[charm] = quantity + 1
```

## `range()` Creates a Sequence

Python allows us to create a sequence of numbers using the `range()` function, much like:

- 1, 2, 3
- 499, 500, 501, 502
- 3, 6, 9, 12, 15
- 0, -1, -2, -3.

The function signature of `range` is:

```
range(start, stop, step)
```

Where `start` is the number at which the range should start, and `stop` is the number at which the range should stop. `stop` is exclusive, which means the `stop` number itself will _not_ be included in the range. `step` is the amount by which the range should increment. `step` is an **optional** argument, and its default value is `1`.

### Ranges in `for` Loops

We can pair ranges with `for` loops so that we iterate over a sequence of numbers. To do this, instead of a list or dictionary, we put in a range.

**Look at this example:**

```python
for number in range(0, 6):
    print(number)
```

Note that it printed up to `5`, and it didn't print `6`. Recall that the `stop` parameter, is _exclusive_. It goes **up** to, but excludes, the end value.

Another example:

```python
print("Blast off in:")

for count in range(10, 0, -1):
    print(count, "...")

print("Blast off!")
```

## Check for Understanding
