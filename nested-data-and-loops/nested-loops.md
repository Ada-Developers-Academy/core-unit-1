# Nested Loops

## Learning Goals

* Apply knowledge about loops with nested loops

## Introduction

We can have loops inside of loops! We call the arrangement of a loop inside another loop a _**nested loop**_.

Nested loops are no different from non-nested loops! They can seem intimidating to read and understand at first. But by building on what we already know about other loops, we can expand our understanding and overcome that fear! We just need to practice reading, understanding, and writing nested loops until they feel just as familiar to us as any other loop!

Callout: Nested loops do not require nested data structures; the only thing that nested loops and nested data structures have in common are being nested.

## Vocabulary and Synonyms

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---
Nested loop | A loop that runs inside of another loop | Loop in a loop | "The logic for checking whether the word has vowels is in the nested loop, " "While we're iterating through that list of strings, we should do a nested loop through each string and check whether it has vowels."

## Observing Loops in Loops

Any kind of loop can be inside any other kind of loop; we can have for-loops inside of while-loops, while-loops inside of for-loops, and they can be nested to any depth. The logic of the loops can vary; they can iterate over the same data, iterate over different data, or do something completely different!

The key to understanding nested loops is seeing how many times each loop runs. We should confirm that an entire nested loop finishes before moving on to the next iteration.

Let's look at an example of a nested loop and step through what the code does.

Callout: This example relies on knowing that strings are iterable; they are secretly sequences of characters!

``` python
def map_character_frequency(words):
    char_map = {}
    for word in words:
        for character in word:
            if character not in char_map.keys():
                char_map[character] = 1
            else:
                char_map[character] += 1
    return char_map

colors = ["red", "orange", "yellow", "green"]

colors_char_map = map_character_frequency(colors)
print(colors_char_map)
```

<!-- Teaching note: These explanation paragraphs have a lot of repetition. This is generally on purpose; reading through this code will be a big jump for many students, as they might have only just learned iteration. -->

What does this example do?

The function `map_character_frequency` takes in a list of words. In the function body, it creates an empty dictionary `char_map` . We'll look at every word in our list of words. For every word, we'll run a whole separate for-loop.

We then loop through every character in each word. For every character, we will run this set of instructions: we'll check if the character is in our `char_map` dictionary as a key already. If it is _not_ in the `char_map` dictionary already, then this is the first time we're seeing it, and it should go in the dictionary with a count of one. Otherwise, it's already in the dictionary, and we can increment the frequency count.

Callout: Let's reword this logic!

We can trace the logic going from "most inner code" to "most outer": We are touching `char_map` in only one place in the code: the `if...else` block. However, `char_map` gets modified for every character, in every word from our original list of words.

Tracing the logic going from the outermost to the innermost code, we loop through every word in our word list, then every character of each word, then check whether each character is in `char_map`.

<!-- end callout -->

The function ultimately returns `char_map` . The code outside of the function definition create an array of words in `colors` , and then passes it into the function. When we get the character frequency map back, we print it to the console.

### Practice

Read through this code and answer these questions.

``` python
def map_character_frequency(words):
    char_map = {}
    for word in words:
        for character in word:
            if character not in char_map.keys():
                char_map[character] = 1
            else:
                char_map[character] += 1
    return char_map

colors = ["red", "orange", "yellow", "green"]

colors_char_map = map_character_frequency(colors)
print(colors_char_map)
```

How many loops are in the function `map_character_frequency()` ?

* 1 for-loop, 1 while-loop
* 2 for-loops, 0 while-loops
* 0 for-loops, 2 while-loops
* 2 for-loops, 0 while-loops, 1 if-else loop

Which line of code best describes iterating over the list `words` ?

* `for word in words:`
* `for character in word:`
* `if character in char_map.keys():`
* `char_map[character] += 1`

What is the local variable for each item in `words` ?

* `char_map`
* `word`
* `words`
* `character`

Which line of code best describes iterating over each character in `word` ?

* `for word in words:`
* `for character in word:`
* `if character in char_map.keys():`
* `char_map[character] += 1`

What is the local variable for each item in `word` ?

* `char_map`
* `word`
* `words`
* `character`

### Tips

* Use indentation to understand the nesting
* Take time to understand the local variables in each loop
* Use words, comments, and pseudocode, and use the phrase "for each ..., we do ..." and "while ... is true, we do ..."

## Visualizing Loops in Loops

Sometimes it can be challenging to visualize how a particular loop runs. A _**loop table**_ is a tool we can use to help us visualize the operation of loops, both nested and unnested. Let's use our now-familiar character counting code as an example.

``` python
def map_character_frequency(words):
    char_map = {}
    for word in words:
        for character in word:
            if character not in char_map.keys():
                char_map[character] = 1
            else:
                char_map[character] += 1
    return char_map

words = ["deer", "reads"]

char_map = map_character_frequency(words)
print(char_map)
```

| `word` | `character` | `char_map` |
|--------|-------------|------------|
| `deer` | `d` | `{"d": 1}` |
| `deer` | `e` | `{"d": 1, "e": 1}` |
| `deer` | `e` | `{"d": 1, "e": 2}` |
| `deer` | `r` | `{"d": 1, "e": 2, "r": 1}` |
| `reads` | `r` | `{"d": 1, "e": 2, "r": 2}` |
| `reads` | `e` | `{"d": 1, "e": 2, "r": 2}` |
| `reads` | `a` | `{"d": 1, "e": 2, "r": 2, "a": 1}` |
| `reads` | `d` | `{"d": 2, "e": 2, "r": 2, "a": 1}` |
| `reads` | `s` | `{"d": 2, "e": 2, "r": 2, "a": 1, "s": 1}` |

<!-- | Outer loop # | Inner loop # | `word` | `character` | `char_map` |
|--------------|--------------|--------|-------------|------------|
| ---          | ---          | ---    | ---         | ---        |
| 1            | 1            | `deer` | `d` | `{"d": 1}` |

1 | 2 | `deer` | `e` | `{"d": 1, "e": 1}`

1 | 3 | `deer` | `e` | `{"d": 1, "e": 2}`

1 | 4 | `deer` | `r` | `{"d": 1, "e": 2, "r": 1}`

2 | 1 | `reads` | `r` | `{"d": 1, "e": 2, "r": 2}`

2 | 2 | `reads` | `e` | `{"d": 1, "e": 2, "r": 2}`

2 | 3 | `reads` | `a` | `{"d": 1, "e": 2, "r": 2, "a": 1}`

2 | 4 | `reads` | `d` | `{"d": 2, "e": 2, "r": 2, "a": 1}`

2 | 5 | `reads` | `s` | `{"d": 2, "e": 2, "r": 2, "a": 1, "s": 1}` -->

At this point, there are no more characters and no more words to loop through.

## Writing Loops in Loops

Writing loops in loops has no special syntax. However, here are some tips and and steps to consider and follow.

Logical errors are the most common errors with nested loops. Attempt to have a clear goal in mind:

* What are you looping through?
* Why do you need to nest these loops? Could we solve this without nested loops?
* How can I prove to myself that my loops are working as intended?

### Debugging Loops in Loops

Debugging loops in loops is extremely challenging when we're unclear about how many loops are happening, and the state of the code at any given moment.

When debugging, prioritize the process of stepping through each loop and checking each variable. Check each variable in each loop using:

* a debugger tool
* paper and pencil, write down each variable
* a loop table
* `print` statements
