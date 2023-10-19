# Iterating Over Dictionaries

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=14dee6b2-a55c-41e8-a15b-ace100310334&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

## Learning Goals

- Practice using for loops to iterate through a dictionary

## Introduction

The overall concept for iterating over dictionaries is the same as iterating over lists. We use `for` loops to iterate over each dictionary item.

However, because dictionary items are key-value pairs, there are a few ways that we can iterate over them: **by key-value pair**, **by key alone**, or **by value alone**.

## `for` Loops for Keys and Values Need `.items()`

To iterate over the key-value pairs of a dictionary, we use the following syntax:

```python
for my_key, my_value in my_dict.items():
    print(my_key, my_value)
```

| <div style="min-width:250px;">Piece of Code</div>              | <div style="min-width:400px;">Notes</div>                                                                                                                                                                                                |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `for`                      | `for` is a reserved keyword in Python. Python recognizes `for` as the beginning of a `for` loop.                                                                                                     |
| `my_key`                   | **Replace this** part with a name that represents what each key is. This will be used as a variable name that will receive the _key_ in each key-value pair during the iteration, one key at a time. |
| `my_value`                 | **Replace this** part with a name that represents what each value is. It will be used as a variable, which during iteration will receive the _value_ in each key-value pair, one at a time.          |
| `in`                       | `in` is a reserved keyword in Python. It separates the name of the iteration variables (`my_key` and `my_value` in the example) and the dictionary we're iterating over.                             |
| `my_dict`                  | **Replace this** part with the desired dictionary to iterate over. This can be a dictionary literal, a variable that holds a dictionary, or any other expression that evaluates to a dictionary.     |
| `.items()`                 | `.items()` is a method that dictionaries have. It returns a view of the dictionary, or a version of the dictionary's key-value pairs that are iterable.                                              |
| `:`                        | This colon begins the `for` loop's body                                                                                                                                                              |
| ` print(my_key, my_value)` | **Replace this** with any code that should execute during each loop. This is the loop's body.                                                                                                        |

### About `.items()`

The most unique part about iterating over the keys & values of dictionaries is that we can call `.items()` on a dictionary to access the key/value pairs in a loop.

Python is unable to iterate over the key/value pairs in dictionaries by default; `.items()` lets us use the `for` loop with it. If we neglect to add `.items()`, we'll likely get something similar to this error:

```bash
ValueError: too many values to unpack (expected 2)
```

### About `my_key` and `my_value`

As dictionaries iterate over key-value pairs, the values of `my_key` and `my_value` change with each iteration.

1. In the first iteration, the value of `my_key` will be the key of a key-value pair, and the value of `my_value` will be the value of that same key-value pair.
2. In the second iteration, the value of `my_key` will be the key of a different key-value pair, and the value of `my_value` will be the value of that same key-value pair.
3. ... etc., until there are no more key-value pairs in the dictionary.

We should change `my_key` and `my_value` to have variable names appropriate to the context of the dictionary.

### About the Loop Body

Similar rules about the `for` loop that we stated for arrays also apply to looping over dictionaries:

1. Loop bodies must be indented.
1. All Python logic and syntax still apply inside the loop!

### Examples

Follow these steps for each example:

1. Read through the code and identify:
   - What is the dictionary?
   - What is each key and value?
   - What do we name each key and value?
   - How do we use each key and value in the loop?
2. Predict what will print
3. Run the code and check your prediction

```python
menu = {
    "appetizer": "Brussels Sprouts",
    "beverage": "Fancy Lemonade"
}

for dish, food in menu.items():
    print(f"The special {dish} for tonight is the {food}.")
```

```python
menu = {
  "Brussels Sprouts": 18.99,
  "Fancy Lemonade": 56.00
}

for food, price in menu.items():
    taxed_price = price * 1.101
    print(f"The cost of {food} is {taxed_price}")

print("That sure was a meal!")
```

## More Examples

Our loop logic can be more complex, and include conditionals, calculations, and function calls.

```python
menu = {
  "Brussels Sprouts": 18.99,
  "Fancy Lemonade": 56.00,
  "Summer Salad": 48.50,
  "Tomato Soup": 18.50
}

for food, price in menu.items():
    taxed_price = price * 1.101
    if taxed_price > 20:
        print(f"{food} costs more than $20.")
    else:
        print(f"{food} costs less than $20")

print("That sure was a meal!")
```

<details style="max-width: 700px; margin: auto;">
    <summary>
      Activity: Create a loop table to calculate the `taxed_price` for each food item in the `menu`. Click this sentence to see the final result.
    </summary>

| <div style="text-align:center;">food</div>         | price        | <div style="text-align: center;">taxed_price (rounded up)</div>   | <div style="text-align:center;">print statement |
| ------------- | ------------- | ------------- | ------------- |
| Brussel Sprouts     | 18.99   | <div style="text-align:center;">20.91</div> | "Brussel Sprouts costs more than $20."
| Fancy Lemonade       | 56.00  | <div style="text-align:center;">61.66</div> | "Fancy Lemonade costs more than $20."
| Summer Salad         | 48.50  | <div style="text-align:center;">53.40</div> | "Summer Salad costs more than $20."
| Tomato Soup          | 18.50  | <div style="text-align:center;">20.37</div> | "Tomato Soup costs more than $20."  


</details>

Loops will often live in functions. We can use a `for` loop on a dictionary that was passed into a function, too!

```python
def consider_specials(specials):
    for dish, special in specials.items():
        print(f"For the special {dish}, why not consider the {special} tonight?")

menu = {
    "appetizer": "Brussels Sprouts",
    "beverage": "Fancy Lemonade"
}

consider_specials(menu)
```

## `for` Loops With Only Keys Doesn't Need `.items()`

When we need to iterate over a dictionary and we **don't** need a reference to the value for each key-value pair, we can use this alternative syntax:

```python
for my_key in my_dict:
    print(my_key)
```

This syntax only names `my_key`, which will be each key, and does not require us to call `.items()` on our dictionary.

We can see in this example, our code does not raise a `ValueError` when we use this syntax!

Of course, even if we only have the key, we can access the value using dictionary syntax.

```python
menu = {
    "appetizer": "Brussels Sprouts",
    "beverage": "Fancy Lemonade"
}

for dish in menu:
    print(f"The special {dish} for tonight is the {menu[dish]}.")
```

### !callout-info

## Loop Styles

If this syntax accomplishes the same thing, which `for` loop style should we prefer? It is always up to the developer, but usually we'll prefer having keys and values available and iterating with `.items()`.

### !end-callout

## Iterating With `.keys()` or `.values()`

Similar to the `items` method, dictionaries also have a `keys` method to explicitly retrieve the dictionary keys, and a `values` method for retrieving the dictionary values.

While we have seen that we can iterate over the dictionary keys by leaving off the `.items()` method call from our `for` loop, we can accomplish the same thing by explicitly calling the `keys` method. This `keys` method is most commonly used for iteration, but we can also use it as a source of data for creating a list of the keys.

The syntax to use the `keys` method is similar to using `items` method. We use a `.` between the object and the method name, and follow the name with `()`, resulting in `.keys()`. We can then iterate as usual.

Consider this example:

```python
menu = {
    "appetizer": "Brussels Sprouts",
    "beverage": "Fancy Lemonade"
}

print("What are the categories on the menu tonight?")
categories = []

for category in menu.keys():
    categories.append(category)

print(categories)
```

### !callout-info

## Loop Patterns

Alternatively, we could have printed the categories inside the for loop. We thought it would be nice to see this pattern again, as it accomplishes something slightly different.

### !end-callout

Dictionaries also provide the `values` method, which gives us access to just the values of a dictionary. The `values` method is most commonly used for iteration, but we can also use it as a source of data for creating a list of the values.

Calling the `values` method, is performed as we have done for `items` and `keys`. We use a `.` between the object and the method name, and follow the name with `()`, resulting in `.values()`. We can then iterate as usual.

Consider this example:

```python
menu = {
    "appetizer": "Brussels Sprouts",
    "beverage": "Fancy Lemonade"
}

print("What are the special dishes on the menu tonight?")
special_dishes = []

for special_dish in menu.values():
    special_dishes.append(special_dish)

print(special_dishes)
```

## Check for Understanding

<!-- Question 1 -->

<!-- prettier-ignore-start -->
### !challenge
* type: checkbox
* id: 6c3bc24e-e25e-4d85-8e8e-868cb4baa41f
* title: Iteration Practice 1

##### !question

Which option will print the keys of this menu dictionary?

```python
drink_menu = {
    "hot": "coffee",
    "cold": "iced tea"
}
```

##### !end-question

##### !options

*
```python
for drink_type in drink_menu.keys():
  print(drink_type)
```

*
```python
for drink in drink_menu.values():
  print(drink)
```

*
```python
for drink_type, drink in drink_menu.items():
  print(drink)
```

##### !end-options

##### !answer

*
```python
for drink_type in drink_menu.keys():
  print(drink_type)
```
##### !end-answer

### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->

<!-- prettier-ignore-start -->
### !challenge

* type: checkbox
* id: c5a6748a-ad7e-4f50-93d4-f8d72e9f0f2a
* title: Iteration Practice 2

##### !question

Which option will print the values of this menu dictionary?

```python
dessert_menu = {
    "ice cream": "Vanilla Bean",
    "cake": "Chocolate Lava Cake",
    "pie": "Apple Pie"
}
```
##### !end-question

##### !options

*
```python
for dessert in dessert_menu.values():
  print(dessert)
```
*
```python
for category, dessert in dessert_menu.items():
  print(dessert)
```

##### !end-options

##### !answer

*
```python
for dessert in dessert_menu.values():
  print(dessert)
```
*
```python
for category, dessert in dessert_menu.items():
  print(dessert)
```

##### !end-answer

### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question Takeaway -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: O5fxwG
* title: Iterating Over Dictionaries
##### !question

What was your biggest takeaway from this lesson? Feel free to answer in 1-2 sentences, draw a picture and describe it, or write a poem, an analogy, or a story.

##### !end-question
##### !placeholder

My biggest takeaway from this lesson is...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->
