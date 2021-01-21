# Practice: Intro to Functions

## Directions

Complete all questions below.

## Practice

### Problem Statements and Functions

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: 7eaadcae-9001-4d2f-a6e6-3242e28ac4f1
* title: Intro to Functions
##### !question

Imagine that you maintain a lot of plants. For any given plant, you need to check if it needs water, check if it needs sunlight, and a few other tasks. You're creating one function to describe all of those tasks. Which of these is the best name for this function?

##### !end-question
##### !options

* `check_if_plant_needs_water_and_sunlight(plant)`
* `checkIfPlantNeedsWaterAndSunlight(plant)`
* `maintain_plant(plant)`
* `maintainPlant(plant)`

##### !end-options
##### !answer

* `maintain_plant(plant)`

##### !end-answer
##### !explanation

The question prompt says that the function is responsible for many tasks, beyond checking if the plant needs water and sunlight. Python best coding style practices recommends using `snake_case` style for naming functions.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: ooI7dJ
* title: Intro to Functions
##### !question

You are writing a function named `needs_water`, which will return whether or not a plant needs water. What data type is this `needs_water` most likely going to return?

##### !end-question
##### !options

* String
* Dictionary
* List
* Boolean
* None of the Above

##### !end-options
##### !answer

* Boolean

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 3 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: EPPL9w
* title: Intro to Functions
##### !question

You are writing a function named `relocate_plant`, which will take one plant and a proposed new spot for it, and move the plant there. Which one of these is the best set of parameters?

##### !end-question
##### !options

* `relocate_plant(location)`
* `relocate_plant(monstera, location)`
* `relocate_plant(plant, location_on_shelf)`
* `relocate_plant(plant, location)`

##### !end-options
##### !answer

* `relocate_plant(plant, location)`

##### !end-answer
##### !explanation

The question prompt names "take one plants and a proposed new spot for it," which implies having two parameters. Our best practice is to have short, accurate, generic names.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

### Syntax

<!-- Question 4 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: v6k6kC
* title: Intro to Functions
##### !question

Given this code...

```python
def maintain_plant(plant):
    if needs_water(plant):
        water(plant)
    if needs_sunlight(plant):
        new_location = find_available_sunny_spot(plant)
        relocate(plant, new_location)
    sing_to_plant(plant, "A Mellow Mood for Maidenhair")
    return plant
```

Identify this piece of syntax: `def maintain_plant(plant):`

##### !end-question
##### !options

* Function signature
* Function call
* Function name and parameters
* Function name and arguments

##### !end-options
##### !answer

* Function signature

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 5 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: 8TrnuR
* title: Intro to Functions
##### !question

Given this code (duplicated from above)...

```python
def maintain_plant(plant):
    if needs_water(plant):
        water(plant)
    if needs_sunlight(plant):
        new_location = find_available_sunny_spot(plant)
        relocate(plant, new_location)
    sing_to_plant(plant, "A Mellow Mood for Maidenhair")
    return plant
```

Specifically in the line `def maintain_plant(plant):`, identify this piece of syntax: `plant`

##### !end-question
##### !options

* Keyword
* Function name
* Argument
* Parameter

##### !end-options
##### !answer

* Parameter

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 6 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: owr3gL
* title: Intro to Functions
##### !question

Given this code (duplicated from above)...

```python
def maintain_plant(plant):
    if needs_water(plant):
        water(plant)
    if needs_sunlight(plant):
        new_location = find_available_sunny_spot(plant)
        relocate(plant, new_location)
    sing_to_plant(plant, "A Mellow Mood for Maidenhair")
    return plant
```

Specifically in the line `def maintain_plant(plant):`, identify this piece of syntax: `maintain_plant`

##### !end-question
##### !options

* Keyword
* Function name
* Argument
* Parameter

##### !end-options
##### !answer

* Function name

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 7 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: 9cU7Dg
* title: Intro to Functions
##### !question

Given this code (duplicated from above)...

```python
def maintain_plant(plant):
    if needs_water(plant):
        water(plant)
    if needs_sunlight(plant):
        new_location = find_available_sunny_spot(plant)
        relocate(plant, new_location)
    sing_to_plant(plant, "A Mellow Mood for Maidenhair")
    return plant
```

Identify this piece of syntax: `relocate(plant, new_location)`

##### !end-question
##### !options

* Function signature
* Function call
* Function name and parameters
* Function name and arguments

##### !end-options
##### !answer

* Function call

##### !end-answer
##### !explanation

Although a "function name and arguments" is in this line of code, this is the syntax to call the function `relocate()`.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 8 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: o27lpu
* title: Intro to Functions
##### !question

Given this code (duplicated from above)...

```python
def maintain_plant(plant):
    if needs_water(plant):
        water(plant)
    if needs_sunlight(plant):
        new_location = find_available_sunny_spot(plant)
        relocate(plant, new_location)
    sing_to_plant(plant, "A Mellow Mood for Maidenhair")
    return plant
```

Identify this piece of syntax: `"A Mellow Mood for Maidenhair"`

##### !end-question
##### !options

* Keyword
* Function name
* Argument
* Parameter

##### !end-options
##### !answer

* Argument

##### !end-answer
##### !explanation

`"A Mellow Mood for Maidenhair"` is a string literal. We are passing it into the function call `sing_to_plant()`. When we pass a value into a function call, it is an _argument_.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 9 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: 43ENx4
* title: Intro to Functions
##### !question

Given this code (duplicated from above)...

```python
def maintain_plant(plant):
    if needs_water(plant):
        water(plant)
    if needs_sunlight(plant):
        new_location = find_available_sunny_spot(plant)
        relocate(plant, new_location)
    sing_to_plant(plant, "A Mellow Mood for Maidenhair")
    return plant
```

Pick the best description for what this code is doing: `new_location = find_available_sunny_spot(plant)`

##### !end-question
##### !options

* Invokes the function `find_available_sunny_spot(plant)`
* Checks if `needs_sunlight(plant)` is `True`. If it is, invoke the function `find_available_sunny_spot(plant)`
* `new_location` is the name of the return value for the function `find_available_sunny_spot()`
* `new_location` is set to the value that `find_available_sunny_spot(plant)` evaluates to

##### !end-options
##### !answer

* `new_location` is set to the value that `find_available_sunny_spot(plant)` evaluates to

##### !end-answer
##### !explanation

`new_location = ` begins assignment to the variable `new_location`. `new_location` is assigned the returned value from the function call `find_available_sunny_spot(plant)`.

This line does _not_ check whether `plant` needs sunlight. This line does not _only_ invoke the function. `new_location` is _not_ part of the function definition for `find_available_sunny_spot()`.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 10 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: y2O2w2
* title: Intro to Functions
##### !question

Given this code (duplicated from above)...

```python
def maintain_plant(plant):
    if needs_water(plant):
        water(plant)
    if needs_sunlight(plant):
        new_location = find_available_sunny_spot(plant)
        relocate(plant, new_location)
    sing_to_plant(plant, "A Mellow Mood for Maidenhair")
    return plant
```

Pick the best description for what this code is doing: `return plant`

##### !end-question
##### !options

* Immediately exits the function
* If `needs_water` and `needs_sunlight` are `True`, immediately exit the function and return `plant`
* Returns the result of everything that happened in the function `maintain_plant()`
* Returns the value assigned to the variable `plant`

##### !end-options
##### !answer

* Returns the value assigned to the variable `plant`

##### !end-answer
##### !explanation

This line returns the value in the variable `plant`.

`return` statements _do_ immediately exit the function, but it is important to describe the return value, too. This single line of code does _not_ imply dependency on `needs_water` or `needs_sunlight`, or anything that has happened in the function.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 11 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: 3uGMMF
* title: Intro to Functions
##### !question

Given this code (duplicated from above)...

```python
def maintain_plant(plant):
    if needs_water(plant):
        water(plant)
    if needs_sunlight(plant):
        new_location = find_available_sunny_spot(plant)
        relocate(plant, new_location)
    sing_to_plant(plant, "A Mellow Mood for Maidenhair")
    return plant
```

Pick the best description for what this code is doing:

```python
if needs_water(plant):
    water(plant)
```

##### !end-question
##### !options

* If the function call `needs_water(plant)` returns, then call the function `water()` with the parameter `plant`
* If the function call `needs_water(plant)` succeeds, then call the function `water()` with the parameter `plant`
* If the function call `needs_water(plant)` is `True`, then call the function `water()` with the argument `plant`
* If the function call `needs_water(plant)` is `True`, then modify `plant` with the `water()` function

##### !end-options
##### !answer

* If the function call `needs_water(plant)` is `True`, then call the function `water()` with the argument `plant`

##### !end-answer
##### !explanation

When we call the function `water()`, the variable `plant` is called the _argument_. We should describe the conditional expression as "if it is `True`". Describing it as "returns" or "succeeds" is ambiguous. The code does not have any syntax that implies that `plant` will be modified in the `water()` function, as we don't see the implementation of `water()`.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

### In Your Own Words

<!-- Question 12 -->
<!-- prettier-ignore-start -->
### !challenge

* type: short-answer
* id: 0b46033a-b21c-442a-9238-5c03ca365bb0
* title: Intro to Functions

##### !question

Using your own words, define what "passing something into a function" means.

##### !end-question
##### !placeholder

Passing a function means...

##### !end-placeholder
##### !answer

/.*/

##### !end-answer
##### !explanation

An example description: Passing something into a function means that we are calling a function and supplying an argument to it. We pass in values as arguments. We can also say that the values we expect to be passed into a function are the parameters. We can say that "passing something into a function" is giving "input" to the function.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 13 -->
<!-- prettier-ignore-start -->
### !challenge

* type: short-answer
* id: BrEpeA
* title: Intro to Functions

##### !question

Using your own words, define what "getting a return value from a function" means.

##### !end-question
##### !placeholder

Getting a return value from a function means...

##### !end-placeholder
##### !answer

/.*/

##### !end-answer
##### !explanation

An example description: Getting a return value from a function means receiving whatever that function returns. After we get a return value from a function call, we usually assign it to a variable. When we invoke a function, and it evaluates into one value, using that one value is "getting its return value." We can say that "getting a return value" is getting "output" from the function.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

### Syntax Reordering

<!-- Question 14 -->
<!-- prettier-ignore-start -->
### !challenge
* type: ordering
* id: nFr02Z
* title: Intro to Functions
##### !question

Reorder the lines of code below to create a function that assembles the lyrics of the song "I'm a Little Teapot." If multiple arrangements would generate the same result, be sure to pick the _least surprising_ arrangement. Assume that each line would be indented correctly.

The song lyrics are, "I'm a little teapot, Short and stout. Here is my handle, Here is my spout!"

##### !end-question
##### !answer

1. `def sing_im_a_little_teapot():`
1. `line_1 = "I'm a little teapot"`
1. `line_2 = "Short and stout"`
1. `line_3 = "Here is my handle"`
1. `line_4 = "Here is my spout"`
1. `entire_song = f"{line_1}, {line_2}. {line_3}, {line_4}!"`
1. `return entire_song`

##### !end-answer
##### !explanation

This is the ideal construction of this function:

```python
def sing_im_a_little_teapot():
    line_1 = "I'm a little teapot"
    line_2 = "Short and stout"
    line_3 = "Here is my handle"
    line_4 = "Here is my spout"
    entire_song = f"{line_1}, {line_2}. {line_3}, {line_4}!"
    return entire_song
```

Technically, we could order the assignments of `line_1`, `line_2`, `line_3`, and `line_4` any way we want. However, we should prefer putting them into an order that minimizes potential confusion for other programmers who read it.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

### Reading Code

<!-- Question 15 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: 2rhUAe
* title: Intro to Functions
##### !question

Read through this code. Assume that `get_season()` and `get_day_of_week()` are valid functions. What does this function do?

```python
def get_daily_special(todays_date):
    current_season = get_season(todays_date)

    if current_season == "Spring":
        special = "Eggplants"
    elif current_season == "Summer":
        special = "Blueberries"
    elif current_season == "Fall":
        special = "Sweet Potatoes"
    else:
        special = "Oranges"

    day_of_week = get_day_of_week(todays_date)

    if day_of_week == "Saturday" or day_of_week == "Sunday":
        special = f"Weekend {special}"

    return special
```

##### !end-question
##### !options

* Sets all of the season and weekend specials
* Determines what season and day of the week it is
* Determines the special based on today's season and day of the week
* Concatenates today's date with the season and day of the week

##### !end-options
##### !answer

* Determines the special based on today's season and day of the week

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

### Debugging Functions

<!-- Question 16 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: Rxvbnm
* title: Intro to Functions
##### !question

Assuming that `get_season()` and `get_day_of_week()` are valid functions, given this code...

```python
def get_daily_special(todays_date):
current_season = get_season(todays_date)

    if current_season == "Spring":
        special = "Eggplants"
    elif current_season == "Summer":
        special = "Blueberres"
    elif current_season == "Fall":
        special = "Sweet Potatoes"
    else:
        special = "Oranges"

    day_of_week = get_day_of_week(todays_date)

    if day_of_week == "Saturday" or day_of_week == "Sunday":
        special = f"Weekend {special}"

    return special
```

There is a syntax or runtime error in this code. What is the cause of this error?

##### !end-question
##### !options

* Logical Error
* Incorrect parameters
* Incorrect Indentation
* Missing colon
* Missing parentheses
* Reads a variable that has no value
* Misspelling

##### !end-options
##### !answer

* Incorrect Indentation

##### !end-answer
##### !hint

If there are typos within a string literal, the spelling may be wrong, but it will not cause a syntax or runtime error.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 17 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: uS0vJj
* title: Intro to Functions
##### !question

Assuming that `get_season()` and `get_day_of_week()` are valid functions, given this code...

```python
def get_daily_special(todays_date):
    current_season = get_season(todays_date)

    if current_season == "Spring":
        special = "Egplants"
    elif current_season == "Summer":
        special = "Blueberries"
    elif current_season == "Fall":
        special = "Sweet Potatoes"
    else
        special = "Oranges"

    day_of_week = get_day_of_week(todays_date)

    if day_of_week == "Saturday" or day_of_week == "Sunday":
        special = f"Weekend {special}"

    return special
```

There is a syntax or runtime error in this code. What is the cause of this error?

##### !end-question
##### !options

* Logical Error
* Incorrect parameters
* Incorrect Indentation
* Missing colon
* Missing parentheses
* Reads a variable that has no value
* Misspelling

##### !end-options
##### !answer

* Missing colon

##### !end-answer
##### !hint

If there are typos within a string literal, it may be wrong spelling, but it will not cause a syntax or runtime error.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 18 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: T2IbR3
* title: Intro to Functions
##### !question

Assuming that `get_season()` and `get_day_of_week()` are valid functions, given this code...

```python
def get_daily_special(todays_date):
    current_season = get_season(todays_date)

    if current_season == "Spring":
        special = "Eggplants"
    elif current_season == "Summer":
        special = "Blueberries"
    elif current_season == "Fall":
        special = "Sweet Potatos"
    else:
        special = "Oranges"

    get_day_of_week(todays_date)

    if day_of_week == "Saturay" or day_of_week == "Sunday":
        special = f"Weekend {special}"

    return special
```

There is a syntax or runtime error in this code. What is the cause of this error?

##### !end-question
##### !options

* Logical Error
* Incorrect parameters
* Incorrect Indentation
* Missing colon
* Missing parentheses
* Reads a variable that has no value
* Misspelling

##### !end-options
##### !answer

* Reads a variable that has no value

##### !end-answer
##### !hint

If there are typos within a string literal, it may be wrong spelling, but it will not cause a syntax or runtime error.

##### !end-hint
##### !explanation

Though we might consider calling this error a logical error, in general, the logic is correct. Ultimately, the error comes from reading the variable `day_of_week`, which has no value assigned to it. We should have set it to the return value from the call to `get_day_of_week`.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 19 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: XpTwkZ
* title: Intro to Functions
##### !question

Assuming that `get_season()` and `get_day_of_week()` are valid functions, given this code...

```python
def get_daily_special(todays_date):
    current_season = get_season(todays_date)

    if current_season == "Spring":
        special = "Eggplants"
    elif current_season == "Summer":
        special = "Blueberries"
    elif current_season == "Fall":
        special = "Sweet Potatoes"
    else:
        specail = "Oranges"

    day_of_week = get_day_of_week(todays_date)

    if day_of_week == "Saturday" or day_of_week == "Sunday":
        specail = f"Weekend {special}"

    return special
```

There is a syntax or runtime error in this code. What is the cause of this error?

##### !end-question
##### !options

* Logical Error
* Incorrect parameters
* Incorrect Indentation
* Missing colon
* Missing parentheses
* Reads a variable that has no value
* Misspelling

##### !end-options
##### !answer

* Misspelling

##### !end-answer
##### !hint

If there are typos within a string literal, it may be wrong spelling, but it will not cause a syntax or runtime error.

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->

### Adding to Existing Functions

<!-- Question 20 -->

<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: CUhJy2
* title: Intro to Functions
### !question

Following the current pattern in the code below, modify the function so that invoking `get_example_sentence("they/them")` returns `"They went to the park. I went with them. They brought their frisbee."`, and doesn't alter the rest of the functionality.

### !end-question
### !placeholder

```python
def get_example_sentence(pronouns):
    if pronouns == "she/her":
        return "She went to the park. I went with her. She brought her frisbee."
    elif pronouns == "he/him":
        return "He went to the park. I went with him. He brought his frisbee."
    elif pronouns == "ze/hir":
        return "Ze went to the park. I went with hir. Ze brought hir frisbee."
    else:
        return "I'm not quite sure how to use these pronouns, it's best to ask and confirm!"
```

### !end-placeholder
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
    def test_returns_expected_sentences(self):
        self.assertEqual(get_example_sentence("she/her"),
                         "She went to the park. I went with her. She brought her frisbee.")
        self.assertEqual(get_example_sentence("he/him"),
                         "He went to the park. I went with him. He brought his frisbee.")
        self.assertEqual(get_example_sentence("ze/hir"),
                         "Ze went to the park. I went with hir. Ze brought hir frisbee.")
        self.assertEqual(get_example_sentence("other"),
                         "I'm not quite sure how to use these pronouns, it's best to ask and confirm!")
        self.assertEqual(get_example_sentence("they/them"),
                         "They went to the park. I went with them. They brought their frisbee.")
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def get_example_sentence(pronouns):
    if pronouns == "she/her":
        return "She went to the park. I went with her. She brought her frisbee."
    elif pronouns == "he/him":
        return "He went to the park. I went with him. He brought his frisbee."
    elif pronouns == "ze/hir":
        return "Ze went to the park. I went with hir. Ze brought hir frisbee."
    elif pronouns == "they/them":
        return "They went to the park. I went with them. They brought their frisbee."
    else:
        return "I'm not quite sure how to use these pronouns, it's best to ask and confirm!"
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->
