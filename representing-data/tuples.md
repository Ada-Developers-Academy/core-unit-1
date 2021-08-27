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

Once the tuple is initialized, the mutable elements cannot be replaced. Attempts at replacing the element will cause a TypeError. For example, changing the list inside of `food_tuple` from a list to an integer will return `TypeError: 'tuple' object does not support item assignment`.

```Python
food_tuple = (["apples", "pears", "bananas"], "carrot", "noodles")
food_tuple[0] = 5
```

Although we cannot replace the elements in a tuple, we can update, add, and remove the values inside of the mutable elements.

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

## Tuple Operations

### Addition

We can combine tuples to form a new tuple using the `+` operator. However, if we try to combine at tuple with a different data type we will receive a `TypeError`.

```Python
sweet_menu = ("ice cream", "cake", "cupcake")
savory_menu = ("pasta", "ramen", "pizza")

all_menu_items = savory_menu + sweet_menu
print(all_menu_items)
# prints ("ice cream", "cake", "cupcake", "pasta", "ramen", "pizza")

all_menu_itmes = "New" + sweet_menu
# receive TypeError: can only concatenate str (not "tuple") to str
```

### Multiplication

If we need elements to repeat within a tuple, we can use the `*` operator.

```Python
nums = (1, 2, 3)
new_nums = nums*3
print(new_nums)
# (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

### Problem Solving Strategies with Tuples

## Returning multiple values from a function

In Python, functions can return multiple values using tuples. Lets say we are provided a dictionary and need to return two values from the dictionary:

```Python
def display_student_info(id):

    student_dict = {
        "345": {
            "name" : "June",
            "grade": 8
        },
        "346": {
            "name": "Mariah",
            "grade": 8
        }
    }

    for student_id, student_data in student_dict.items():
        print(student_id)
        if id == student_id:
            return student_data["name"], student_data["grade"]

(name, grade) = display_student_info("346")
print(f"Student name: {name}, grade: {grade}")
```

## Creating constants

Constants are values that are designed to never change and are often used across different parts of a program. Because tuples are immutable, they are a great candidate in storing data multiple pieces of data that are intended to never change and only accessed.

## Dictionary Keys

Dictionary keys are required to be immutable, making tuples a great way to have multiple pieces of data refer to a single value. This can be useful for storing location data using coordinates.

```Python
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
* soups = {"ramen", "congee", "stew"}
* soups = ()
* soups = ramen, congee, stew

##### !end-options

##### !answer

* soups = tuple()
* soups = {"ramen", "congee", "stew"}
* soups = ()
* soups = ramen, congee, stew

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

* tuples are immutable 

##### !end-answer

### !end-challenge
<!--prettier-ignore-end-->

<!--BEGIN CHALLENGE-->

### !challenge

- type: paragraph
- id: 8e31a545-1c3c-4104-a715-bd76ef0125b8
- title: Biggest Takeaway

##### !question

What was your biggest takeaway from this lesson? Feel free to answer in 1-2 sentences, draw a picture and describe it, or write a poem, an analogy, or a story.

##### !end-question

##### !placeholder

My biggest takeaway from this lesson is...

##### !end-placeholder

### !end-challenge

<!--END CHALLENGE-->
