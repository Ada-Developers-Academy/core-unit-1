# Tuples

## Learning Goals

- Practice representing ordered data as a tuple

## Introduction

A "tuple" is an ordered, **immutable** collection similar to lists. Tuples can be used to return multiple values from a function and for occasions where we would like to store data that's not intended to change.

## Vocabulary and Synonyms

| Vocab     | Definition                                           | Synonyms            | How to Use in a Sentence          |
| --------- | ---------------------------------------------------- | ------------------- | --------------------------------- |
| Tuple     | An immutable data type that can store ordered values |                     | I stored the id values in a tuple |
| Immutable | Unchanging over time or unable to be changed         | unchangeable, fixed | Python dictionary keys must be immutable data types.                                  |
| Mutable   | Able to change                                     | changeable          | Appending a value to a list modifies the list directly because it is mutable. Tuples don't have an append method because they are immutable!                                  |

## What Is a Tuple?

A tuple is an ordered, immutable collection of elements. The length and data type of each element in a tuple never changes. This means that elements cannot be added, replaced, or removed.

### !callout-info

## You Say Tuple, I Say Tuple

There are two main pronunciations of tuple. One sounds like "to pull," and the other rhymes with "supple." It's said both ways, so we should get used to hearing it both ways!

<br/>

Where did this weird word come from? Originally it's a mathematical term related to groups of things. Think single, double, triple, quadruple, quin<u>tuple</u>. Rather than remembering all the different names for these groups, mathematicians settled on the general term _n-tuple_, where _n_ is the number of things in the group!

### !end-callout

## Tuple Syntax

### Create a New Tuple

There are three ways we can create a tuple:

1. Use Python's built-in `tuple` function to create an empty tuple or build a new tuple from an existing data structure.
1. Initialize with parentheses.
1. Omit the parentheses and have Python implicitly interpret the values as a tuple.

```python
#1
example_tuple_1 = tuple([1, 2, 3, 3])

#2
example_tuple_2 = (1, 2, 3, 3)

#3
example_tuple_3 = 1, 2, 3, 3
```

### Create a Tuple With One Element

Single-element tuples are initialized using a trailing comma before the closing parentheses. It is this one character that tells Python to treat a single parenthesized value as a tuple. For example:

```python
cartoon = ("Daria")
anime = ("Sailor Moon",)

print(type(cartoon))
print(type(anime))
```

Notice how `("Daria")` is surrounded by parentheses but evaluates to a string data type. Because there is no trailing comma, Python interprets `("Daria")` as an expression that evaluates to a string data type. It views the parentheses as grouping an expression, not as the start of a tuple. For `("Sailor Moon",)`, the trailing comma is what signals Python to interpret `("Sailor Moon",)` as a single-element tuple. It is really easy to forget this trailing comma, so beware!

### Accessing Values in a Tuple

Tuple indices, like lists, are both ordered and zero-based. This means that the first index in a tuple is 0. In the example below, we can access an element within a tuple like we would a list:

```python
example_list = [1, 2, 3, 4, 5, 6]
example_tuple = (1, 2, 3, 4, 5, 6)

print(example_list[0])
print(example_list[-1])
print(example_list[1:4])

print(example_tuple[0])
print(example_tuple[-1])
print(example_tuple[1:4])
```

Loops can also be used to iterate through all the elements in tuples.

```python
destinys_child = ("Beyonce", "Kelly", "Michelle")
for singer in destinys_child:
    print(singer)
```

## Element Data Types

Tuples can store any data type including mutable data types like lists and dictionaries.

```python
food_tuple = (["apples", "pears", "bananas"], "carrot", "noodles")

instructor_tuple = (
    {
        "name": "Claire",
        "favorite_dessert": "cake",
        "dislikes": "ice cream",
        "is great": True,
        "bad traits": None
    },
    10,
    "algorithms"
)
```

Once the tuple is initialized, the mutable elements cannot be replaced. Attempts at replacing the element will cause a TypeError. For example, changing the list inside of `food_tuple` from a list to an integer will return `TypeError: 'tuple' object does not support item assignment`.

```python
food_tuple = (["apples", "pears", "bananas"], "carrot", "noodles")
food_tuple[0] = 5
```

But be careful! Although we cannot replace the elements in a tuple, it's still possible to update, add, and remove the values inside of the mutable elements.

In general, we tend _not_ to store mutable types in tuples. One of the main reasons to use a tuple is to communicate our intent that some collection of data should _not_ change. So we should be suspicious of code that modifies mutable values within a tuple.

So why does Python allow mutable values in tuples at all? We'll see an example of this related to function return values in a moment!

## Tuple Operations

### Concatenation

We can combine tuples to form a new tuple using the `+` operator. However, if we try to combine a tuple with a different data type we will receive a `TypeError`. After concatenation, the original tuples remain unchanged.

```python
sweet_menu = ("ice cream", "cake", "cupcake")
savory_menu = ("pasta", "ramen", "pizza")

all_menu_items = savory_menu + sweet_menu
print(all_menu_items)
# prints ("ice cream", "cake", "cupcake", "pasta", "ramen", "pizza")

print(savory_menu)
# prints ("pasta", "ramen", "pizza")
print(sweet_menu)
# prints ("ice cream", "cake", "cupcake")

all_menu_items = "New" + sweet_menu
# receive TypeError: can only concatenate str (not "tuple") to str
```

### Repetition

If we need elements to repeat within a tuple, we can use the `*` operator, just like we can with lists and strings.

```python
nums = (1, 2, 3)
new_nums = nums * 3
print(new_nums)
# (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

## Problem Solving Strategies With Tuples

### Returning Multiple Values From a Function

In Python, functions can return multiple values using tuples. Let's write a function that looks for an item in a list. If it finds the item it will return `True` along with where the item was found. If the item is _not_ found, it will return `False` and `None`. 

```Python
def find_with_pos(items, item):

    if item in items:
        return True, items.index(item)

    return False, None

found, pos = find_with_pos([1, 2, 3], 3)
print(f"found: {found}, pos: {pos}")
```

Here, we used the implicit tuple syntax (without parentheses) to package up and return two pieces of data. When we assign the result to `found, pos`, Python assigns the returned values in order, so `found` receives the value that was at position 0 in the returned tuple, and `pos` gets the value that was at position 1.

Parentheses could also be used, but when using tuples to return multiple values, this implicit style is more common.

This example also shows the most common reason that a tuple might contain a mutable value. Functions can return mutable types. This function happens to only return immutable values (a boolean and a number), but Python functions can just as easily return mutable values like lists or dictionaries. Python handles multiple return values by returning them in a tuple. So if one of the return values is mutable, then the tuple will contain a mutable value!

## Creating Constants

Constants are values that are designed to never change and are often used across multiple parts of a program. Because tuples are immutable, they are a great candidate for storing several pieces of data that are intended to be read only, never changed.

## Dictionary Keys

Dictionary keys are required to be immutable, making tuples a great way to have multiple pieces of data refer to a single value. This can be useful for storing location data using coordinates.

```python
destinations = {
    (-122.349358, 47.620422): {
        "building_name": "Space Needle",
        "city": "Seattle, Washington, United States"
    },
    (35.658581, 139.745438): {
        "building_name": "Tokyo Tower",
        "city": "Tokyo, Japan"
    }
}

print(destinations[(35.658581, 139.745438)])

```

### !callout-warning

## Tuples Used as Dictionary Keys May Not Contain Mutable Data

When we use tuples as dictionary keys, they must contain immutable data only. If the tuple contains any mutable data, directly or indirectly, it will result in a `TypeError`.

```python
my_dict = {}
my_tuple = (0,)
my_tuple_with_mutable_data = ([],)
my_dict[my_tuple] = 1  # OK
my_dict[my_tuple_with_mutable_data] = 1
# TypeError: unhashable type: 'list'
```
### !end-callout

# Check for Understanding

<!--prettier-ignore-start-->
### !challenge

* type: checkbox
* id: 78138480-78d5-44d4-ac41-323b4c6c39de
* title: Tuples

##### !question

How do we create a new tuple? 

##### !end-question

##### !options

* soups = tuple()
* soups = ("ramen", "congee", "stew")
* soups = ()
* soups = "ramen", "congee", "stew"

##### !end-options

##### !answer

* soups = tuple()
* soups = ("ramen", "congee", "stew")
* soups = ()
* soups = "ramen", "congee", "stew"

##### !end-answer

### !end-challenge
<!--prettier-ignore-end-->

<!--prettier-ignore-start-->
### !challenge

* type: checkbox
* id: f5cea13b-ce38-4c3a-bb6f-c03fd01e9205
* title: Tuples

##### !question

How are tuples different from lists?

##### !end-question

##### !options

* lists are mutable 
* tuples cannot contain duplicates
* tuples are immutable 

##### !end-options

##### !answer

* lists are mutable 
* tuples are immutable 

##### !end-answer

### !end-challenge
<!--prettier-ignore-end-->


<!--prettier-ignore-start-->

### !challenge

* type: paragraph
* id: 8e31a545-1c3c-4104-a715-bd76ef0125b8
* title: Biggest Takeaway

##### !question

What was your biggest takeaway from this lesson? Feel free to answer in 1-2 sentences, draw a picture and describe it, or write a poem, an analogy, or a story.

##### !end-question

##### !placeholder

My biggest takeaway from this lesson is...

##### !end-placeholder

### !end-challenge

<!--prettier-ignore-end-->

