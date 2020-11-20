# Representing Data in Lists and Dictionaries

## Learning Goals

- Practice representing ordered data as a list
- Practice representing related data as a list

## Introduction

As we see more and more problems in programming, we'll be faced with a lot of ambiguous direction. Exciting computer science problems will often have no obvious place to start. Should you make a function? How many variables? Do we need iteration?

As part of _breaking down a problem_, one step we should consider, take, and practice, is representing data we see as data structures. To give ourselves a starting point in problem-solving, we can practice:
- Observing the problem and data given to us
- Turn these observations into data structures like strings, lists, dictionaries, and more

## Recognizing Lists When Reading Problem Statements

To practice representing data as lists, we will...

1. Consider the strengths of lists
1. Read an example problem statement
1. Write our own observations
1. Make conclusions

### The Strengths of Lists

Lists are great at...

| Strength                                  | Notes                                                                                                                               | How it's represented in code                                                                                         |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Lists contain 0+ elements                 | Lists contain multiple elements in a specific order. The elements don't need to be of the same type.                                | The syntax of a list literal is comma-separated elements. Lists could possibly be indicated by plural variable name. |
| Lists contain elements in an order        | Elements in a list are always in an order. This order could have zero significance, or it could have meaning based on how it's used | -                                                                                                                    |
| Lists have a property of length/size      | A frequently used property for lists is its length. An empty list has a length of zero.                                             | We can use the `len` function and pass in a list to get its length.                                                  |
| We can access elements in a list by index | If we know the index of an element in a list, we can get the element                                                                | We index with square brackets, `my_list[0]`                                                                          |
| We can add things to lists                | We can add elements to lists                                                                                                        | `my_list.append(new_element)` will add this element to the end of the list                                           |
| We can remove things to lists             | We can remove elements from lists                                                                                                   | `my_list.remove(value_to_remove)` will find the first instance of this value and remove it                           |

### An Example Problem Statement

Compare these two sequences of DNA, which contain many pieces of DNA. They are similar, but not the same, based on the order and value of each piece. These two sequences are the same length.

| No. | Sequence          |
| --- | ----------------- |
| 1   | GAGCCTACTAACGGGAT |
| 2   | CATCGTAATGACGGCCT |

We can visualize the differences between the two sequences like so:

```bash
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
^ ^ ^  ^ ^    ^^
```

Create a function. In this function:

- Make a list that contains all the differences between the two sequences.
- Find the differences between the two sequences.
  - Add each difference to the list of differences.

### Make Your Own Conclusions About Lists in Problem Statements

The ideal solution for the problem statement above uses lists.

Did you come to that conclusion? If so, how? Share your notes about what you observed in the above problem statement. **What pieces of the problem statement** directly helped you make those conclusions?

Learn Short Answer

### Our Conclusions About Lists in Problem Statements

| Observation                                                    | When it's related to lists                                                                                                                                                                                                           | Examples                                                                                                                                                               |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Using the word "list" or "array"                               | Literally using the word "list" is a good indicator that a list could be involved                                                                                                                                                    |
| Mentions of multiple "things" that are similar                 | A list usually groups similar things. Except for order (or depending on context), lists don't really have a way to represent one element being "more special" than another. Lists are great for lists of things of equal importance. | A list of groceries with no specific order, a list of letters in the alphabet, a list of books that are unavailable at the library                                     |
| Mentions of an order, sequence, or sorting to multiple things  | A list keeps its elements in an order, so any mention of "order," "sequence," or "sorting." being important might be a sign of a list.                                                                                               | A priority list of groceries, where the highest priority is first. The alphabet song, in order. A list of unavailable books sorted by their due date.                  |
| Mentions getting, using, comparing "one" element out of "many" | A problem that focuses comparing "one" (or a few) item to many others is a problem that lists can solve well.                                                                                                                        | Finding the highest priority grocery item. Counting how many letters in the alphabet are vowels. Finding all books with a due date of Sunday.                          |
| Mentions referencing an element by position                    | A problem that mentions an element by its position (index) is a clue that a list is a good idea.                                                                                                                                     | "The second item to buy is always coffee." "The alphabet should be replaced with `*` every fifth letter." "The `checkin` function should always grab the first book"   |
| Mentions adding or removing an element to a list               | Lists are really great at growing and shrinking.                                                                                                                                                                                     | "The user should be able to add or remove any number of shopping items" "Remove any letter that isn't uppercase." "Add a book every time someone checks out a book."   |
| Mentions the length of a list                                  | Lists can easily calculate its own length, and clues around constraints or freedoms around a list's length is a clue to use a list.                                                                                                  | "The grocery list should never be over 15 items." "An alphabet can have an infinite number of characters," "Check the number of books every time we check out a book." |

## Recognizing Dictionaries When Reading Problem Statements

To practice representing data as lists, we will...

1. Consider the strengths of lists
1. Read an example problem statement
1. Write our own observations
1. Make conclusions

### The Strengths of Dictionaries

Dictionaries are great at...

| Strength                                  | Notes                                                                                                                                                                                               | How it's represented in code |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| Data must be organized in key-value pairs | All data in dictionaries _must_ be in key-value pairs; there is no way to add a value without specifying a key                                                                                      | -                            |
| Data is unordered                         | Dictionaries may sometimes appear to have an order, but there is no consistent ordering of key-value pairs. This is helpful to express that there isn't necessarily priority or importance to order | -                            |
| Accessing values by using keys            | All values can be accessed by a key; this might have more meaning than accessing values by index, especially when keys are named intentionally                                                      | -                            |

### An Example Problem Statement

Imagine we are working on a research study that studies what color t-shirts people wear on Tuesdays. We've collected data on people passing by through the market, and the t-shirts we see per hour.

Given this data, create two data structures.

The first data structure should represent the data in the table below. The second data structure should represent the frequency of the color t-shirts at the end of Tuesday.

| Time Of Day | T-shirts colors seen          |
| ----------- | ----------------------------- |
| 08:00       | red, orange, green            |
| 09:00       | red, orange                   |
| 10:00       | blue                          |
| 11:00       | blue, green                   |
| 12:00       | blue, gray                    |
| 13:00       | red, blue                     |
| 14:00       | white                         |
| 15:00       | green, white                  |
| 16:00       | white, black                  |
| 17:00       | yellow, black                 |
| 18:00       | white, green, gray, red, blue |

### Make Your Own Conclusions About Dictionaries in Problem Statements

For this problem statement, the ideal solution is to create two dictionaries.

The first dictionary should have the time as the key, and the t-shirt colors seen in a list as the value.

The second dictionary should have a t-shirt color as the key, and the frequency of that t-shirt color as the value.

### !challenge
* type: short-answer
* id: 9523c54f-fd25-4dcf-be14-4d5a9ff33d43
* title: What were your conclusions about dictionaries?

##### !question
Did you come to the same conclusion? If so, how? Share your notes about what you observed in the above problem statement. **What pieces of the problem statement** directly helped you make those conclusions?
##### !end-question

##### !placeholder
Enter notes here
##### !end-placeholder

##### !answer
/.*/
##### !end-answer
### !end-challenge

### Our Conclusions About Dictionaries in Problem Statements

| Observation                                                      | When it's related to dictionaries                                                                                                                                                                                                                                    | Examples |
| ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| A close relationship between an idea and details about that idea | Using dictionary's key-value pairs, contextually, if the problem associates one idea very closely with details about that idea, we can make the idea the key, and the details the value.                                                                             | -        |
| Using the word "table"                                           | Dictionaries are great at representing tabular data, especially if there is one column that can represent a key, and one column that represents its corresponding value                                                                                              | -        |
| Using the word "map" or "translate"                              | Dictionaries can represent a mapping relationship. If there is some data that should be "mapped" or "translated" to another value, we can use a dictionary to represent that                                                                                         | -        |
| Mentions of frequency                                            | Dictionaries are great structures to map some data to its frequency. In this situation, the data would be the key, and its frequency (as an integer that starts at `0`) is the value                                                                                 | -        |
| Accessing values by key                                          | Dictionaries allow us to use keys as the primary way of accessing data. If two pieces of data have a close relationship, and contextually we may have more exposure to the key, we might want to use a dictionary. (Accessing data by value is a trickier operation) | -        |
| Modifying values                                                 | Dictionaries allow us to modify the values to key-value pairs easily. If two pieces of data have a close relationship, and contextually we are modifying the value often, we might want to use a dictionary.                                                         | -        |
