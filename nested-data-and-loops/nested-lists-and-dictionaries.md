# Nested Lists and Dictionaries

## Learning Goals

- Practice accessing and modifying nested data structures

## Introduction



## Vocabulary and Synonyms

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---
Two-dimensional arrays

## Lists Containing Lists

Lists can contain lists.

```python
[ ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'] ]
```

In this example:
- The outer list has five elements
- The inner lists have three elements
    - Inner lists don't need to be the same length as each other

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

Lists of lists are also called **two-dimensional arrays.**

### Accessing One Element

In order to get the value of one element in a nested list, we must chain the syntax to index a list.

```python
example_list[ index_to_find_inner_list ][ index_to_find_element ]
```

Callout: One way to remember how to read this code is to read it left-to-right. The first expression that's evaluated is `example_list[ index__to_find_inner_list ]`. This value is the inner list! Then, we continue reading to the right, and we see we are indexing this inner list, with `index_to_find_element`.

Observe these examples:
```python
sarahs_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', 'l'],
    ['m', 'n', 'o']
]

c = sarahs_list[0][2]
e = sarahs_list[1][1]
g = sarahs_list[2][0]
j = sarahs_list[3][0]
n = sarahs_list[4][1]
```

### Modifying An Element

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

## Dictionaries Containing Lists

Dictionaries can contain lists.

```python
{
    'oranges' : ['a', 'b', 'c', 'd'],
    'apples' : ['e', 'f']
}
```

In this example:
- The outer dictionary has two key-value pairs: `'oranges'` and `'apples'`
- One inner list has four elements
- The other inner list has two elements

### Accessing One Element

To access one element, we chain the syntax to get a value from a dictionary, and then index a list.

```python
example_dict[ key_to_find_inner_list ][ index_to_find_element ]
```

Callout: Again, we practice reading this code from left-to-right. First, we evaluate the expression `example_dict[ key_to_find_inner_list ]`. Then, moving to the right, we index that list with `index_to_find_element`.

Observe these examples:
```python
sarahs_dict = {
    'oranges' : ['a', 'b', 'c', 'd'],
    'apples' : ['e', 'f']
}

b = sarahs_dict['oranges'][1]
d = sarahs_dict['oranges'][3]
e = sarahs_dict['apples'][0]
```

### Modifying An Element

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
- The second inner dictionary has two key-value pairs

### Accessing One Value

To access one value from a nested dictionary, we chain the syntax to get a value from a dictionary.

```python
example_list[ index_to_find_item ][ key_to_access_value ]
```

Callout: Again, we practice reading this code from left-to-right. First, we evaluate the expression `example_dict[ key_to_find_inner_list ]`. Then, moving to the right, we index that list with `index_to_find_element`.

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
```

### Modifying A Value

Modifying the contents of a nested dictionary follows the syntax rules we've seen before. We want to re-assign a value, so we use the assignment operator.

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
```

## Dictionaries Containing Dictionaries

Dictionaries containing dictionaries follows the patterns we've seen before.

### Accessing and Modifying Inner Values

We access a value from inner dictionary by chaining `[]`s with the appropriate key names.

Modifying a value in an inner dictionary needs re-assignment to the required key of the inner dictionary.

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