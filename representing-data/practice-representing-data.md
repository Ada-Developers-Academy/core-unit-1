# Practice: Representing Data

```python
materials = ["Wood", "Paper", "Cardboard"]
```

What is the data type of `materials`?

- String
- None
- Boolean
- List

Consider the list `["Wood", "Paper", "Cardboard"]`. Which of these is the most readable variable name?

- `material`
- `materials`
- `list`
- `l`

Which of these is the best representation of a grocery list in Python?

- `"Spinach, Broccoli, Eggplant, Potatoes"`
- `[Spinach, Broccoli, Eggplant, Potatoes]`
- `["Spinach", "Broccoli", "Eggplant", "Potatoes"]`
- `[["Spinach"], ["Broccoli"], ["Eggplant"], ["Potatoes"]]`

Describe some ways you can recognize that a problem's solution might use a list.

| Date (YYYY-MM-DD format) | Number of Crows Spotted in the Parking Lot |
| ------------------------ | ------------------------------------------ |
| 2020-09-01               | 3                                          |
| 2020-09-02               | 5                                          |
| 2020-09-03               | 5                                          |
| 2020-09-04               | 6                                          |
| 2020-09-05               | 2                                          |
| 2020-09-06               | 2                                          |
| 2020-09-07               | 1                                          |
| 2020-09-08               | 0                                          |

Imagine this data is from an organization called "The Fellowship of Simon's Neighbors" that collects data on Simon's neighbors. Look through the data and make a prediction about what this data means and represents, and how you would explain it to a 10 year old.

Type the most important data out as one list, and store it in a variable. Choose your variable name wisely.

Create a variable named `hobbies` and assign it to a list that contains your own hobbies. Run this code to make sure you don't have any syntax errors or runtime errors.

```python

# Make a variable named hobbies in the line above this comment

print(f"My hobbies include {hobbies}")
```

Create a variable named `groceries` and assign it to a list that contains your own grocery list. Run this code to make sure you don't have any syntax errors or runtime errors.

```python

# Make a variable named groceries in the line above this comment

print(f"My grocery list includes {groceries}")
```

Here is a function named `add_grocery(grocery_list, new_item)`. Inside of the function body `add_grocery`, add code that will append the `new_item` to `grocery_list`.

```python
def add_grocery(grocery_list, new_item):
    pass
    # Replace pass with a new function body
    # that appends new_item to grocery_list

groceries = ["Spinach", "Broccoli", "Eggplants", "Potatoes"]
add_grocery(groceries, "Carrots")
```

Here is a function named `steal_top_food(my_groceries, their_groceries)`. This function takes in two grocery lists, `my_groceries` and `their_groceries`.This function should:

1. Read the first element from the list `their_groceries`, and store it into a local variable.
2. Replace (re-assign) the first element in `my_groceries` with the stored value (the local variable) from step 1.
3. Return the list `my_groceries`

Implement the function `steal_top_food`

```python
def steal_top_food(my_groceries, their_groceries):
    pass
    # Replace pass with a new function body
    # that fulfills the requirements

simons_groceries = ["Spinach", "Broccoli", "Eggplants", "Potatoes"]
devins_groceries = ["Avocados", "Oat Milk", "Mangoes"]
steal_top_food(simons_groceries, devins_groceries)
```
