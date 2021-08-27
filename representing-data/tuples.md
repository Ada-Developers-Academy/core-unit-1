# Tuples

## Introduction

A "tuple" is an ordered, **immutable** collection similar to lists. Tuples can be used to return multiple values from a function and for occasions where we would like to store data that's not intended to chage.

## Vocabulary and Synonyms

| Vocab     | Definition | Synonyms | How to Use in a Sentence |
| --------- | ---------- | -------- | ------------------------ |
| Tuple     | conte      | conte    | conte                    |
| Immutable | conte      | conte    | conte                    |
| Mutable   | conte      | conte    | conte                    |

## Tuple Fundamentals

A tuple is an ordered, immutable collection of elements. The length and data type of each element in a tuple never changes. This means that elements cannot be added, replaced, or removed.

## Tuple Syntax

### Create a new tuple

There are three ways we can create a tuple:

1. Using Python's built-in `tuple` function to create an empty tuple or convert a data structure into a tuple.
2. Initialize with parentheses
3. Omitting the parentheses and have Python implicitly interpet the values as a tuple.

```Python
#1
example_tuple_1 = tuple([1, 2, 3, 3])

#2
example_tuple_2 = (1, 2, 3, 3)

#3
example_tuple_3 = 1, 2, 3, 3
```

### Create a Tuple with One Element

Single-element tuple are initiliazed using a trailing comma before the closing parentheses. It is this one character that distinguishes the tuple from being evaluated as an expression. For example,

```Python
cartoon = ("Daria")
anime = ("Sailor Moon",)

print(type(cartoon))
print(type(anime))
```

Notice how `"Daria"` is surrounded by parentheses but evalutes to a string data type. Because there is no trailing comma, Python interprets `cartoon = ("Daria")` as an expression that evaluates to a string data type. For `anime`, the trailing comma is what signals Python to interpret `"Sailor Moon"` as a single-element tuple. It is really easy to forget this trailing comma, so beware!

### Accessing values in a tuple

Tuple indices, like lists, are both ordered and zero-based. This means that the first index in a tuple is 0. In the example below, we can access an element within a tuple like we would a list:

```Python
example_list = [1, 2, 3]
example_tuple = (1,2,3)

print(example_list[0])
print(example_list[-1])

print(example_tuple[0])
print(example_tuple[-1])
```

Loops can also be used to access the elements within tuples.

```Python
destinys_child = ("Beyonce", "Kelly", "Michelle")
for singer in destinys_child:
    print(singer)
```

## Element Data Types

Tuples can store any data type including mutable data types like lists and dictionaries.

```Python
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

Once the tuple is initialized, the mutable elements cannot replaced. Attempts at replacing the element will cause a TypeError. For example, if we try to change the list inside of `food_tuple` from a list to an integer, we will receive: `TypeError: 'tuple' object does not support item assignment`.

```Python
food_tuple = (["apples", "pears", "bananas"], "carrot", "noodles")
food_tuple[0] = 5
```

Although we cannot replace the elements in a tuple, we can update, add, and remove the values inside of mutable elements.

**Update List in Tuple**

```Python
food_tuple = (["apples", "pears", "bananas"], "carrot", "noodles")
food_tuple[0][0] = "grapes"
print(food_tuple)
# prints (["grapes", "pears", "bananas"], "carrot", "noodles")
```

**Add element to list in tuple**

```Python
food_tuple[0].append("persimmon")
print(food_tuple)
# prints (["grapes", "pears", "bananas", "persimmon"], "carrot", "noodles")
```

**Remove element to list in tuple**

```Python
food_tuple[0].remove("pears")
print(food_tuple)
# prints (["grapes", "bananas", "persimmon"], "carrot", "noodles")
```

**Update dictionary value in tuple**

```Python
instructor_tuple = (
    {
        "name": "Claire",
        "favorite_dessert": "cake"
    },
)
instructor_tuple[0].favorite_dessert = "chocolate"
print(instructor_tuple[0])
# prints {
#         "name": "Claire",
#         "favorite_dessert": "chocolate"
#     }
```

**Add dictionary key-value in tuple**

```Python
instructor_tuple = (
    {
        "name": "Claire",
        "favorite_dessert": "cake"
    },
)
instructor_tuple[0]["favorite_meal"] = "pork katsu"
print(instructor_tuple[0])
# prints {
#         "name": "Claire",
#         "favorite_dessert": "chocolate",
#         "favorite_meal": "pork katsu"
#     }
```
