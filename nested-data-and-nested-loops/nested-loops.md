# Nested Loops
<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=fc7b155f-874d-48b1-9ddd-acd101449356&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

## Learning Goals

- Apply knowledge about loops with nested loops

## Introduction

We can have loops inside of loops! We call the arrangement of a loop inside another loop a _**nested loop**_.

Nested loops are no different from non-nested loops! They can seem intimidating to read and understand at first. But by building on what we already know about other loops, we can expand our understanding and overcome that fear! We just need to practice reading, understanding, and writing nested loops until they feel just as familiar to us as any other loop!

### !callout-info

## Nested Loops != Nested Data Structures

Nested loops do not require nested data structures; the only thing that nested loops and nested data structures have in common is being nested.

### !end-callout

## Vocabulary and Synonyms

| Vocab       | Definition                              | Synonyms       | How to Use in a Sentence                                                                                                                                                                                           |
| ----------- | --------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Nested loop | A loop that runs inside of another loop | Loop in a loop | "The logic for checking whether the word has vowels is in the nested loop, " "While we're iterating through that list of strings, we should do a nested loop through each string and check whether it has vowels." |

## Observing Loops in Loops

Any kind of loop can be inside any other kind of loop; we can have for-loops inside of while-loops, while-loops inside of for-loops, and they can be nested to any depth. The logic of the loops can vary; they can iterate over the same data, iterate over different data, or do something completely different!

The key to nested loops is in understanding how many times each loop runs, and over what data.

Let's look at an example of a nested loop and step through what the code does.

### !callout-info

## We Can Iterate Over Strings

This example relies on knowing that strings are iterable; they are secretly sequences of characters!

### !end-callout

```python
def map_character_frequency(words):
    char_map = {}
    for word in words:
        for character in word:
            if character not in char_map:
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

Overall, the function `map_character_frequency` is responsible for making a dictionary that will contain every unique character and the number of times each occurs.

The function `map_character_frequency` takes in a list of words. In the function body, we create an empty dictionary `char_map` . Then, we use a for-loop to look at every word in our list of words. In this for-loop, the variable `word` will hold one word in `words`.

We then loop through every character in each `word`. Each character is represented with the variable `character`. For every character, we will run this set of instructions: we'll check whether it's in our `char_map` dictionary as a key already. If it is _not_ in the `char_map` dictionary already, then this is the first time we're seeing it, and it should be added to the dictionary as a key with a value of one. Otherwise, it's already in the dictionary, and we must increment the frequency count.

![Diagram illustrating nested loops: words is a list containing "red", "orange", "yellow", "green". word is a string with the characters "o", "r", "a", "n", "g", "e". character has the value "a". char_map has the key-value pairs "r": 2, "e": 1, "d": 1, "o": 1.](../assets/nested-data-and-nested-loops_nested-loops_counting-chars.png)  
*Fig. This diagram shows the state of the algorithm partway through. We see the __`words`__ list in the cyan table to the left. The __`word`__ loop control variable is referring to the __`"orange"`__ string, shown just to the right in orange. We see that strings are themselves iterable, and the __`character`__ loop control variable is referring to the __`"a"`__ in __`"orange"`__. The __`"a"`__ is just about to be added to the __`char_map`__ dictionary (on the right in fuchsia) with a value of __`1`__ since this is the first __`"a"`__ we've seen. Notice that __`"r"`__ has a value of __`2`__, since we have seen an __`"r"`__ in __`"red"`__ and an __`"r"`__ in __`"orange"`__.*

### !callout-info

## Let's Repeat That Explanation in Different Words

We can trace the logic going from "innermost code" to "outermost code". The innermost lines of code modify `char_map` within the `if...else` block. We perform this modification to `char_map` for every character of each word, for every word, from our original list of words.

Tracing the logic going from the outermost to the innermost code, we loop through every word in our word list, then every character of each word, then check whether each character is in `char_map`.

### !end-callout

The function ultimately returns `char_map` . Before we invoke the `map_character_frequency` function, we create a list of words in `colors`. We pass the `colors` list into the function. When we get the character frequency map back, we print it to the console.

### Practice

Read through this code and answer these questions.

```python
def map_character_frequency(words):
    char_map = {}
    for word in words:
        for character in word:
            if character not in char_map:
                char_map[character] = 1
            else:
                char_map[character] += 1
    return char_map

colors = ["red", "orange", "yellow", "green"]

colors_char_map = map_character_frequency(colors)
print(colors_char_map)
```

<!-- Question 1 -->

<!-- prettier-ignore-start -->
### !challenge

* type: multiple-choice
* id: sF6pz1
* title: Nested Loops

##### !question

How many loops are in the function `map_character_frequency()` ?

##### !end-question

##### !options

* 1 for-loop, 1 while-loop
* 2 for-loops, 0 while-loops
* 0 for-loops, 2 while-loops
* 2 for-loops, 0 while-loops, 1 if-else loop

##### !end-options

##### !answer

* 2 for-loops, 0 while-loops

##### !end-answer

### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->

<!-- prettier-ignore-start -->
### !challenge

* type: multiple-choice
* id: 9fw2wh
* title: Nested Loops

##### !question

Which line of code best describes iterating over the list `words` ?

##### !end-question

##### !options

* `for word in words:`
* `for character in word:`
* `if character in char_map:`
* `char_map[character] += 1`

##### !end-options

##### !answer

* `for word in words:`

##### !end-answer

### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 3 -->

<!-- prettier-ignore-start -->
### !challenge

* type: multiple-choice
* id: myW4kq
* title: Nested Loops

##### !question

What is the local variable for each item in `words` ?

##### !end-question

##### !options

* `char_map`
* `word`
* `words`
* `character`

##### !end-options

##### !answer

* `word`

##### !end-answer

### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 4 -->

<!-- prettier-ignore-start -->
### !challenge

* type: multiple-choice
* id: hAerR2
* title: Nested Loops

##### !question

Which line of code best describes iterating over each character in `word` ?

##### !end-question

##### !options

* `for word in words:`
* `for character in word:`
* `if character in char_map:`
* `char_map[character] += 1`

##### !end-options

##### !answer

* `for character in word:`

##### !end-answer

### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 5 -->

<!-- prettier-ignore-start -->
### !challenge

* type: multiple-choice
* id: 9ShXFW
* title: Nested Loops

##### !question

What is the local variable for each item in `word` ?

##### !end-question

##### !options

* `char_map`
* `word`
* `words`
* `character`

##### !end-options

##### !answer

* `character`

##### !end-answer

### !end-challenge
<!-- prettier-ignore-end -->

### Tips

- Use indentation to understand the nesting
- Take time to understand the local variables in each loop
- Use words, comments, and pseudocode, and use the phrase "for each ..., we do ..." and "while ... is true, we do ..."

## Visualizing Loops in Loops

Sometimes it can be challenging to visualize how a particular loop runs. A _**loop table**_ is a tool we can use to help us visualize the operation of loops, both nested and unnested. Let's use our now-familiar character counting code as an example.

```python
def map_character_frequency(words):
    char_map = {}
    for word in words:
        for character in word:
            if character not in char_map:
                char_map[character] = 1
            else:
                char_map[character] += 1
    return char_map

words = ["deer", "reads"]

char_map = map_character_frequency(words)
print(char_map)
```

| `word`  | `character` | `char_map`                                 |
| ------- | ----------- | ------------------------------------------ |
| `deer`  | `d`         | `{"d": 1}`                                 |
| `deer`  | `e`         | `{"d": 1, "e": 1}`                         |
| `deer`  | `e`         | `{"d": 1, "e": 2}`                         |
| `deer`  | `r`         | `{"d": 1, "e": 2, "r": 1}`                 |
| `reads` | `r`         | `{"d": 1, "e": 2, "r": 2}`                 |
| `reads` | `e`         | `{"d": 1, "e": 3, "r": 2}`                 |
| `reads` | `a`         | `{"d": 1, "e": 3, "r": 2, "a": 1}`         |
| `reads` | `d`         | `{"d": 2, "e": 3, "r": 2, "a": 1}`         |
| `reads` | `s`         | `{"d": 2, "e": 3, "r": 2, "a": 1, "s": 1}` |

At this point, there are no more characters and no more words to loop through.

## Writing Loops in Loops

Writing loops in loops has no special syntax. However, here are some tips and and steps to consider and follow.

Logical errors are the most common errors with nested loops. Attempt to have a clear goal in mind:

- What are you looping through?
- Why do you need to nest these loops? Could we solve this without nested loops?
- How can I prove to myself that my loops are working as intended?

### Debugging Loops in Loops

Debugging loops in loops is extremely challenging when we're unclear about how many loops are happening, and the state of the code at any given moment.

When debugging, prioritize the process of stepping through each loop and checking each variable. Check each variable in each loop using:

- a debugger tool
- paper and pencil, write down each variable
- a loop table
- `print` statements
