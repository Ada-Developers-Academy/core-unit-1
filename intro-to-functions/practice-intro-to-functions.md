2
What's the best function name
What's the best name for argument

You maintain a lot of plants. For any given plant, you need to check if it needs water, check if it needs sunlight, and a few other tasks. Which of these is the best name for this function?

`maintain_plant(plant)`
`maintainPlant(plant)`
`checkIfPlantNeedsWaterAndSunlight(plant)`
`check_if_plant_needs_water_and_sunlight(plant)`

You are writing a function named `needs_water`, which will return whether or not a plant needs water. What data type is this `needs_water` most likely going to return?

String
Dictionary
List
Boolean
None of the Above

You are writing a function named `relocate_plant`, which will take one plant and a proposed new spot for it, and move the plant there. Which one of these is the best set of parameters?

`relocate_plant(location)`
`relocate_plant(monstera, location)`
`relocate_plant(plant, location_on_shelf)`
`relocate_plant(plant, location)`

The question prompt names "take one plants and a proposed new spot for it," which implies having two parameters. Our best practice is to have short, accurate, generic names.

6
Syntax identification

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

Identify this piece of syntax: `def maintain_plant(plant)`
Iin specifically the line `def maintain_plant(plant)`, identify this piece of syntax: `plant`
Iin specifically the line `def maintain_plant(plant)`, identify this piece of syntax: `maintain_plant`
Identify this piece of syntax: `relocate(plant, new_location)`
Identify this piece of syntax: `"A Mellow Mood for Maidenhair"`
Describe what this code is doing: `new_location = find_available_sunny_spot(plant)`
Describe what this code is doing: `return plant`
Describe what this code is doing:
```python
if needs_water(plant):
    water(plant)
```

Using your own words, define what "passing something into a function" means.

Using your own words, define what "getting a return value" means.

2
Syntax reorder

Of the lines of code below, re-order them to its ideal order. Assume that each line would be indented correctly.

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

Technically, we could re-orer the assignments of `line_1`, `line_2`, `line_3`, and `line_4` to any combination we want. However, it's ideal to have them ordered because of readability and coherence to all programmers. :)


4
Read through this code. What does this function do?

```python
def get_daily_special(todays_date):
    special = ""

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

Determines what season and day of the week it is
* Determines the special based on today's season and day of the week
Sets all of the season and weekend specials
Concatenates today's date with the season and day of the week

4
Identify the cause of the error: Indentation
Identify the cause of the error: Missing colon
Identify the cause of the error: NameError
Identify the cause of the error: Mispelling a function call

* Logical Error
* Incorrect parameters
* Indentation
* Missing colon
* Missing parentheses
* Reads a variable that has no value
* Mispelling

2

Following the current pattern in the function, modify the function so that invoking `get_example_sentence("they/them"` returns `"They went to the park. I went with them. They brouth their frisbee.`, and doesn't modify the rest of the functionality.

```python
def get_example_sentence(pronouns):
    if pronouns == "she/her":
        return "She went to the park. I went with her. She brought her frisbee."
    if pronouns == "he/him":
        return "He went to the park. I went with him. He brought his frisbee."
    if pronouns == "ze/hir":
        return "Ze went to the park. I went with hir. Ze brought hir frisbee."
    else:
        return "I'm not quite sure how to use these pronouns, it's best to ask and confirm!"
```