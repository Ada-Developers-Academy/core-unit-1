# Iterating Over Lists

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=bafff635-d7fc-4a1d-9f02-ace10031ff1b&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

## Learning Goals

- Practice using for loops to iterate through an array

## Introduction

`for` Loops are one of the most common ways to iterate. `for` loops can iterate over **each element in a list.**

## Vocabulary and Synonyms

| Vocab      | Definition                                                                              | Synonyms                          | How to Use in a Sentence                                                                                                               |
| ---------- | --------------------------------------------------------------------------------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `for` loop | A kind of loop that will loop over every element in something iterable, such as a list. | for loop, for-loop, for each loop | "I wrote a `for` loop so I can run my function for each element," "I should write a `for` loop here so I can iterate through the list" |

## Syntax for `for` Loops

To iterate over a list, we use the following syntax:

```python
for my_element in my_list:
    print(my_element)
```

| <div style="min-width:200px;">Piece of Code</div>       | <div style="min-width:450px;">Notes</div>                                                                                                                                                                                          |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `for`                | `for` is a reserved keyword in Python. Python recognizes `for` as the beginning of a `for` loop.                                                                                               |
| `my_element`         | **Replace this** part with a name that represents what each list element is. It will be used as a variable, which during iteration will take on the value of each list element, one at a time. |
| `in`                 | `in` is a reserved keyword in Python. It separates the name of the `my_element` variable and the list we're iterating over.                                                                    |
| `my_list`            | **Replace this** part with the desired list to iterate over. This can be a list literal, a variable that holds a list, or any other expression that evaluates to a list.                       |
| `:`                  | This colon begins the `for` loop's body                                                                                                                                                        |
| ` print(my_element)` | **Replace this** with any code that should execute during each loop. This is the loop's body.                                                                                                  |

### About `my_element`

The variable `my_element` gets assigned and re-assigned through a `for` loop.

When a `for` loop starts, `my_element` gets assigned the value of the first element in the list. The value of `my_element` changes with each following iteration.

1. In the first iteration, the value of `my_element` will be the first element in the list.
2. In the second iteration, the value of `my_element` will be the second element in the list.
3. In the third, it will be the third element...
4. ... etc., until there are no more elements in the list.

We should always change `my_element` to be a variable name appropriate to the context of the list. Think about what each element in the list represents. If we are iterating over a list of books, we might change `my_element` to `book`. For a list of rooms, the name `room` might be more appropriate.

The name we choose doesn't affect the underlying iteration value in any way, but it can help us remember what data we're processing in the loop body.

### About the Loop Body

1. The loop body **must be indented one level deeper than the** `for` **statement that begins the loop.**
   - The loop's body ends when the code indentation returns to the previous level.
1. All Python logic and syntax still applies inside the loop! For example, a loop might contain conditionals, calculations, or function calls.

### Examples

Follow these steps for each example:

1. Read through the code and identify:
   - What is the list?
   - What is each element?
   - What do we name each element?
   - How do we use each element in the loop?
2. Predict what will print
3. Run the code and check your prediction

#### Example: Dining Out

```python
options = ["the place I'm craving but is too far away",
           "the place we always go to",
           "that place that just opened but looks too fancy"
           ]

for option in options:
    print(f"What about getting food from {option} tonight?")
```

#### Example: Calculating Taxes

```python
prices = [18.99, 56.00, 48.50, 18.50]

for price in prices:
    taxed_price = price * 1.101
    print(f"The cost of one item is {taxed_price}")

print("That sure was a meal!")
```

## Visualizing `for` Loops

<!-- TODO: Add a diagram to visualize loops, and describe it. -->

One way we can visualize how the value of `my_element` changes over each iteration is to create a table in our notes, on a whiteboard, or with any other medium.

We set up our table by making a column for each piece of data we'd like to track. Then we add a row for each iteration through the loop.

| iteration # | index of `my_element` | value of `my_element` |
| ----------- | --------------------- | --------------------- |
| 1           | 0                     | ...                   |
| 2           | 1                     | ...                   |

For example, we can fill out tables for our examples like so:

#### Example: Dining Out Explained

```python
options = ["the place I'm craving but is too far away",
           "the place we always go to",
           "that place that just opened but looks too fancy"
           ]

for option in options:
    print(f"What about getting food from {option} tonight?")
```

| iteration # | <div style="width: 80px;">index of `option`</div> | <div style="width: 100px;">value of `option`</div>  | print output                                                                        |
| ----------- | ------------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------- |
| 1           | 0                                                 | `"the place I'm craving but is too far away"`       | `"What about getting food from the place I'm craving but is too far away tonight?"` |
| 2           | 1                                                 | `"the place we always go to"`                       | `"What about getting food from the place we always go to tonight?"`                         |
| 3           | 2                                                 | `"that place that just opened but looks too fancy"` | `"What about getting food from that place that just opened but looks too fancy tonight?"`   |

#### Example: Calculating Taxes Explained

```python
prices = [18.99, 56.00, 48.50, 18.50]

for price in prices:
    taxed_price = price * 1.101
    print(f"The cost of one item is {taxed_price}")

print("That sure was a meal!")
```

| iteration # | index of `price` | value of `price` | value of `taxed_price` at the end of the loop |
| ----------- | ---------------- | ---------------- | --------------------------------------------- |
| 1           | 0                | `18.99`          | `20.907989999999998`                          |
| 2           | 1                | `56.00`          | `61.656`                                      |
| 3           | 2                | `48.50`          | `53.3985`                                     |
| 4           | 3                | `18.50`          | `20.3685`                                     |

## Building up a List of Results

In our iteration examples so far, all we've really done is print out the values. A more common coding pattern is to process each list value and store the result in a _new_ list that we can use somewhere else.

To achieve this, we create a new, empty list before our loop. Then as we process each value, we append the result to the new list. At the end of the loop, our new list contains a processed version of the original list, with the processed values matching the ordering of the original list.

Take a moment to think about why this must be true. Then answer the following questions.

Is `taxed_prices`:

- initialized as an empty array inside the `for` loop? Why or why not?
- accessed or modified inside the `for` loop? How?
- accessed or modified after the `for` loop? How?

```python
prices = [18.99, 56.00, 48.50, 18.50]
taxed_prices = []

for price in prices:
    taxed_price = price * 1.101
    taxed_prices.append(taxed_price)

print(taxed_prices)
```

## Increasing Complexity

As mentioned earlier in this lesson, our loop logic can be more complex, and include conditionals, calculations, and function calls.

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

When we use a `for` loop in a function, we can iterate over any lists passed in as a parameter, too!

Note that this isn't a special case. It follows from one of the properties of `for` loops we learned about earlier. The `my_list` value used in the `for` loop can be any variable, including a function parameter, that refers to a list.

```python
def consider_options(options):
    for option in options:
        print(f"What about getting food from {option} tonight?")

pizza_places = ["your favorite pizza place", "my favorite pizza place"]
consider_options(pizza_places)
```

We can even put loops inside of loops! We will explore this in a future lesson.

## Check for Understanding

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: e45acb1f-5be4-4f87-b6d2-60831f03d620
* title: Loop Review

##### !question

Consider this code:

```python
def display_most_spoken_languages():
    languages = ["Chinese", "Hindi", "English", "Spanish", "Arabic"]

    for language in languages:
        print(f"{language} is one of the top 5 most spoken languages in the world.")

    return languages
```

What does the variable `language` represent?

##### !end-question

##### !options
* A list of the most spoken language. The elements are strings.
* A single element in the `languages` list. The value changes during iteration.
* The return value of the function `display_most_spoken_languages()`
##### !end-options

##### !answer
* A single element in the `languages` list. The value changes during iteration.
##### !end-answer

### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question Takeaway -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: JPDZnt
* title: Iterating Over Lists
##### !question

What was your biggest takeaway from this lesson? Feel free to answer in 1-2 sentences, draw a picture and describe it, or write a poem, an analogy, or a story.

##### !end-question
##### !placeholder

My biggest takeaway from this lesson is...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->
