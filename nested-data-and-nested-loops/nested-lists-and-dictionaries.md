# Nested Lists and Dictionaries

## Learning Goals

- Practice accessing and modifying nested data structures

## Introduction

As we know, lists can contain any type of data, including other lists and dictionaries. Similarly, dictionary keys can hold any type of data, including lists and other dictionaries.

Even if we can understand this theoretically, nested lists and dictionaries are truly tricky to get a hold of. Nested lists and dictionaries introduce and mix a lot of different syntaxes together, which can easily become time-consuming headaches. Even the most experienced programmers need to slow down to read through nested lists and dictionaries.

Nested lists and dictionaries can become the backbone of structuring data. If we take the time now to practice our skills, we'll be in much better shape later.

We recommend working through this lesson in the following way:

- Read through each section slowly
  - Ensure that in each section, you recognize how to read an element, and how to modify an element
- When you come across a block of code, practice reading through the code line-by-line
- Take notes, either as you go, or at the end of each section to summarize
- Notice when you think something was surprising or unexpected, and write it down
- If time allows, for each block of code, come up with one sentence to describe it

## Vocabulary and Synonyms

| Vocab                  | Definition                                                                                                                                                                                                                           | Synonyms                              | How to Use in a Sentence                                                                                                              |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Two-dimensional arrays | A list where each element is a list. This often implies that all inner lists have the same length. When all inner lists have the same length, a two-dimensional array can resemble a grid, as the structure mimics rows and columns. | 2d array, nested lists, nested arrays | "To implement the game Tic-Tac-Toe, we used a 2d array to represent the spots in the grid, where the center spot was in `grid[0][0]`" |

## Lists Containing Lists

Lists can contain lists.

```python
[ ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'] ]
```

In this example:

- The outer list has five elements
- The inner lists each have three elements

It may help to add white-space to read this data structure more clearly. This is the same list of lists.

```python
[
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', 'l'],
    ['m', 'n', 'o']
]
```

It's helpful to note that inner lists don't need to be the same length as each other. The following is a valid list of lists:

```python
[ ['a', 'b', 'c'], ['d'], ['e', 'f']]
```

Lists of lists are also called **two-dimensional arrays**.

### Accessing One Element

To get the value of one element in a nested list, we chain the syntax for indexing into a list.

```python
example_list[ index_to_find_inner_list ][ index_to_find_element ]
```

One way to understand this code is to read it carefully from left-to-right. The first expression that's evaluated is `example_list[ index_to_find_inner_list ]`. The value of this expression is the inner list at the position stored in `index_to_find_inner_list`!

We continue reading to the right, where we index this resulting list with `[ index_to_find_element ]`, which retrieves the value from the inner list at the position stored in `index_to_find_element`.

### !callout-info

## Reading Longer Chains Left-to-Right

Depending on the structure of our data, additional chaining can be done. We must remain aware of what each partial expression evaluates to as we read the whole expression from left-to-right.

### !end-callout

Observe these examples:

```python
sarahs_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', 'l'],
    ['m', 'n', 'o']
]

the_letter_c = sarahs_list[0][2]
the_letter_e = sarahs_list[1][1]
the_letter_g = sarahs_list[2][0]
the_letter_j = sarahs_list[3][0]
the_letter_n = sarahs_list[4][1]

print(the_letter_c, the_letter_e, the_letter_g, the_letter_j, the_letter_n)
```

In this example, the variable `the_letter_c` will have the value `'c'`, the variable `the_letter_e` will have the value `'e'`, and so on. We can prove that with the `print` statement, which produces the following console output:

```
c e g j n
```

### !callout-secondary

## A Variable Named `the_letter_c`? Really?

Please note that we intentionally have kind of goofy variable names in this lesson. 😇

### !end-callout

### Modifying an Element

This is example syntax for modifying one element in a nested list.

```python
example_list[ index_to_find_inner_list ][ index_to_find_element ] = 'This is my new value!'
```

Observe these examples:

```python
sarahs_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', 'l'],
    ['m', 'n', 'o']
]

sarahs_list[0][1] = '🤠'
sarahs_list[1][0] = '🤠'
sarahs_list[2][1] = '🤠'
sarahs_list[3][2] = '🤠'
sarahs_list[4][1] = '🤠'

print(sarahs_list)
```

This code produces the console output:

```
[['a', '🤠', 'c'], ['🤠', 'e', 'f'], ['g', '🤠', 'i'], ['j', 'k', '🤠'], ['m', '🤠', 'o']]
```

## Dictionaries Containing Lists

Dictionary values can contain lists too. However, lists _cannot_ be used as dictionary keys.

```python
{
    'oranges' : ['a', 'b', 'c', 'd'],
    'apples' : ['e', 'f']
}
```

In this example:

- The outer dictionary has two key-value pairs: `'oranges'` and `'apples'`
- The list stored at the `'oranges'` key has four elements
- The list stored at the `'apples'` key has four elements

### Accessing One Element

Similarly to how we accessed one element in a nested list, we chain the syntax for getting a value from a dictionary, and then index the resulting list to access one element.

```python
example_dict[ key_to_find_inner_list ][ index_to_find_element ]
```

### !callout-info

## Reading Code From Left-to-Right

Again, we practice reading this code from left-to-right. First, we evaluate the expression `example_dict[ key_to_find_inner_list ]`. Then, moving to the right, we index that list with `index_to_find_element`.

### !end-callout

Observe these examples:

```python
sarahs_dict = {
    'oranges' : ['a', 'b', 'c', 'd'],
    'apples' : ['e', 'f']
}

the_letter_b = sarahs_dict['oranges'][1]
the_letter_d = sarahs_dict['oranges'][3]
the_letter_e = sarahs_dict['apples'][0]

print(the_letter_b, the_letter_d, the_letter_e)
```

This code produces the console output:

```
b d e
```

### Modifying an Element

This is example syntax for modifying one element in a nested list.

```python
example_list[ index_to_find_inner_list ][ index_to_find_element ] = 'This is my new value!'
```

Observe these examples:

```python
sarahs_dict = {
    'oranges': ['a', 'b', 'c', 'd'],
    'apples': ['e', 'f']
}

sarahs_dict['oranges'][1] = '🍊'
sarahs_dict['oranges'][3] = '🍊'
sarahs_dict['apples'][0] = '🍎'

print(sarahs_dict)
```

The above code produces this console output:

```
{'oranges': ['a', '🍊', 'c', '🍊'], 'apples': ['🍎', 'f']}
```

## Lists Containing Dictionaries

Lists can contain dictionaries.

```python
[
    {
        'orange': '🍊',
        'apple': '🍎'
    },
    {
        'bird': '🐦',
        'dog': '🐶'
    }
]
```

In this example:

- The outer list has two items
- The first inner dictionary has two key-value pairs
- The second inner dictionary also has two key-value pairs

### Accessing One Value

Accessing one value from a dictionary nested within a list continues the themes we've already seen. We need to use the syntax for getting an index from a list, followed by the syntax for retrieving the value from a dictionary.

```python
example_list[ index_to_find_item ][ key_to_access_value ]
```

Again, let's practice reading this code from left-to-right. First, we evaluate the expression `example_list[ index_to_find_item ]`, which evaluates to an inner dictionary. Then, continuing to the right, we use `[ key_to_access_value ]` to lookup the value of a key in that inner dictionary.

Observe these examples:

```python
sarahs_list = [
    {
        'orange': '🍊',
        'apple': '🍎'
    }
]

orange_emoji = sarahs_list[0]['orange']
apple_emoji = sarahs_list[0]['apple']

print(orange_emoji, apple_emoji)
```

The above code produces this console output:

```
🍊 🍎
```

### Modifying A Value

Modifying the contents of a nested dictionary follows the syntax rules we've seen before. To re-assign a value, we use the assignment operator.

Observe these examples:

```python
sarahs_list = [
    {
        'orange': '🍊',
        'apple': '🍎'
    }
]

sarahs_list[0]['orange'] = 'A fruit that is round and orange'
sarahs_list[0]['apple'] = 'A fruit with a lot of varieties'

print(sarahs_list)
```

The above code produces this console output:

```
[{'orange': 'A fruit that is round and orange', 'apple': 'A fruit with a lot of varieties'}]
```

## Dictionaries Containing Dictionaries

We have one final combination to consider!

Dictionaries can also have dictionaries as values, but dictionaries _cannot_ be used as keys.

Using nested dictionaries follows the patterns we've already seen, so this section will focus more on the code than the explanations.

### Accessing and Modifying Inner Values

Accessing one value from nested dictionaries uses the expected key lookup syntax. We chain each lookup using `[]`s with the appropriate key names.

Likewise, modifying a value in a nested dictionary requires re-assignment to the desired key of the inner dictionary.

```python
sarahs_dict = {
    'fruit_emoji': {
        'orange': '🍊',
        'apple': '🍎'
    },
    'animal_emoji': {
        'bird': '🐦',
        'dog': '🐶'
    }
}

bird_emoji = sarahs_dict['animal_emoji']['bird']
sarahs_dict['animal_emoji']['dog'] = '🐕'

print(bird_emoji)
print(sarahs_dict)
```

The above code produces this console output:

```
🐦
{'fruit_emoji': {'orange': '🍊', 'apple': '🍎'}, 'animal_emoji': {'bird': '🐦', 'dog': '🐕'}}
```

## Check for Understanding

<!-- Use 1-4 sentences to describe this data structure. Describe each layer of the data structure, starting with the outer data structure. -->

<!-- A second time: Use 1-4 sentences to describe this data structure. Describe each layer of the data structure, starting with the outer data structure. -->

<!-- Modify this function so it returns the value `25` -->

<!-- Modify this function so it returns the value `"Electric"` -->

<!-- MC:

Nested data structures can go three layers deep! Extend your knowledge. Which of these is the syntax to get the value `"Pikachu"`?

game_data = {
    "pokedex": [
        {
            "id": 25,
            "name_en": "Pikachu",
            "type": "Electric"
        }
    ]
}

pokedex["name_en"]
pokedex{"name_en"}
game_data["pokedex"]["name_en"]
game_data{"pokedex"}["name_en"]

 -->

<!-- More questions will be in the huge worksheet -->
