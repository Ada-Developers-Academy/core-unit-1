# Variable Scope

## Learning Goals

- Define variable scope
- Explain that variable scope affects how variables are defined and accessed
- Use variable scope to determine when to make variables

## Introduction

Recall what variables are. In programming, we store values in memory. When we create variables, we create _names_ that references those stored values in memory.

We can access the values of those variables, manipulate them, or re-assign those variables.

The rules in programming about how we can access those variables in code is called **variable scope.**

## Vocabulary and Synonyms

| Vocab                | Definition                                                                                                                                                                    | Synonyms                                                 | How to Use in a Sentence                                                                                                                                                                                                          |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Variable             | A variable is a name that references a value/piece of data stored in computer memory. We can assign variables, read variables, manipulate variables, and re-assign variables. | holder of a value, reference                             | "That variable is named `foo`," "We should use `foo` on this line," "I need to pass the value of `foo` to this function"                                                                                                          |
| Variable Declaration | The line of code where we first introduce a variable, usually the first place where we give a variable a name and a value                                                     | Where the variable is defined, initializing the variable | "I declared the variable `bar` on line 3, and accessed it on line 4," "I defined the variable `bar` with the initial value `42`," "I got a `NameError` on line 50 because I never initialized the variable `bar` before line 50." |
| Scope                | The area of a program where a given variable can be accessed or used                                                                                                          | Variable Scope                                           | "The variable `baz` is in scope in the function `qux`," "`baz` is out of scope on this line of code," "This variable is scoped to this function."                                                                                 |
| Local Variable       | A kind of variable that has the smallest scope: local scope. The most common kind of variable.                                                                                | Variable                                                 | "`foo` is a local variable," "Let's create a local variable called `foo`"                                                                                                                                                         |
| Function             | Lines of code (1 or more) that are related, grouped together, and named. Once defined, these lines of code are reusable and can be called over and over again.                | Method                                                   | "I defined a function," "I used a function," "I wrote a function"                                                                                                                                                                 |
| Global Variable      | A kind of variable that has the largest scope: global scope.                                                                                                                  | Global variable                                          | "It's dangerous to use the global variable `bar` inside of the function," "We can read the global variable `bar` anywhere in the file."                                                                                           |

## Variable Scope Is Where A Variable Can Be Read

**Variable scope** is the area of a program where a given variable can be accessed.

A variable **has** scope.

Practically, **scope** usually means the **lines of code** that a variable can be accessed.

When we can access a variable successfully, and it doesn't give a runtime error, we usually say that the variable is **in scope.**

```python
my_daily_fruit = "apple"

print(f"An {my_daily_fruit} a day keeps the doctor away?")
```

In this example, we access the variable `my_daily_fruit` on the line `print(f"An {my_daily_fruit} a day keeps the doctor away?")`, and it doesn't give us a runtime error. This means that the variable `my_daily_fruit` is **in scope** of that line.

### Debugging Variable Scope: `NameError`

When programmers try to access a variable that is **not** in scope, programmers will often get a runtime error `NameError` for that variable.

Observe and run this code that attempts to access `my_daily_fruit` even though `my_daily_fruit` is not defined within this code.

```python
print(f"An {my_daily_fruit} a day keeps the doctor away?")
```

Our error message gives us a clue that **the variable `my_daily_fruit` isn't defined within this scope.** Therefore, we got an error for accessing a variable not in scope.

```bash
NameError: name 'my_daily_fruit' is not defined
```

## Variable Scope Is Defined By Kind and Location

Now that we know what variable scope is, how does a variable's scope get determined? What are the rules that say what a variable's scope is?

Variable scope is determined by:

1. The kind of variable that's defined
2. The location (line of code) where the variable is defined

### Local Variables are the Most Popular Kind

**Local variables** are a kind of variable. Everything we've learned about variables so far still apply to local variables.

Properties of local variables:

- named with the `lower_snake_case` naming convention we've been using so far already.
- the most common kind of variable (and account for 90% of the variables we will use).
- variables with the smallest scope. Details to be discovered over time.

```python
my_daily_fruit = "apple"
print(f"The variable {my_daily_fruit} is a local variable.")
```

### Functions Create New Local Variable Scope

Local variables defined inside of a function only have scope **within that function.**

If we try to access a variable that was scoped to a function, we will get our predicted `NameError`.

```python
def display_breakfast():
    breakfast_message = "My breakfast today is an apple"
    print(f"{breakfast_message}")

display_breakfast()
print("Let's try to access the value of breakfast_message outside of the display_breakfast function:")
print(f"The value of breakfast_message is {breakfast_message}")
```

In our example above, when we try to access `breakfast_message` outside of its scope (in the `display_breakfast` function), we get the error message `NameError: name 'breakfast_message' is not defined`.

After a function "finishes" (the function `return`s or it exits/finishes running), the local variables "leave" and are "released." The local variables will simply not reference any values anymore (and the computer memory that held those values gets recovered), and we'll never be able to access those local variables again.

The local variables "restart" when the function gets called again; when a function gets called again, and all relevant local variables get re-initialized.

#### Parameters are Scoped to its Function

Recall that parameters are names to arguments we pass into a function.

**Parameters are like local variables,** with variable scope to that function.

```python
def display_breakfast(breakfast_fruit):
    print(f"My breakfast today is {breakfast_fruit}")

display_breakfast("an apple")
print("Let's try to access the value of breakfast_fruit outside of the display_breakfast function:")
print(f"The value of breakfast message is {breakfast_fruit}")
```

In our example above, when we try to access the parameter `breakfast_fruit` outside of its scope (in the `display_breakfast` function), we get the error message `NameError: name 'breakfast_fruit' is not defined`.

#### Return Values Are Important

Because local variables "disappear" after each function, let's revisit functions.

If we want a **value** to come _out_ of a function, we **must** use the function's `return` statement to return that value.

```python
def display_breakfast():
    breakfast_message = "My breakfast today is an apple"
    print(f"{breakfast_message}")
    return breakfast_message

resulting_message = display_breakfast()
print("Instead of trying to access breakfast_message, let's return breakfast_message, store it in resulting_message, and access resulting_message instead:")
print(f"The value of resulting_message is {resulting_message}")
```

**This will be one of the main patterns that we use in programming.**

### Recognizing Variable Scope

Beyond functions, other kinds of **blocks of code** in Python also create variable scope. We will learn about those in detail in the future.

For now, here is **one tip**: there is **a pattern** between **local variable scope** and **its level of indentation** in code.

## There Are More Kinds of Variables

**Global variables** are a kind of variable with global variable scope. Global variables can be accessed inside **or** outside of any functions.

Typically, global variables are declared **outside of any functions.**

Properties of global variables:

- named with the `lower_snake_case` naming convention we've been using so far already.
- variables with the largest scope.
  - Can be accessed and modified outside any function
  - Can be accessed and modified inside any function
- a kind of variable that we will use commonly at the beginning of our coding journey, and will use often while debugging or during in-progress code.
  - Using global variables right now is inevitable
  - Over time, we'll learn more tools that will help us avoid using global variables, or increase our code quality even when we do use global variables.

```python
def display_breakfast():
    print("Let's try to access the value of breakfast_message INSIDE of the display_breakfast function:")
    print(f"{breakfast_message}")


breakfast_message = "My breakfast today is an apple"
print("Let's try to access the value of breakfast_message OUTSIDE of the display_breakfast function:")
print(f"The value of breakfast message is {breakfast_message}")

display_breakfast()
```

In this example, `breakfast_message` is a global variable, because it was declared **outside** of any function in our code. We are able to access it outside of the `display_breakfast` function, AND inside the `display_breakfast` function. We did **not** get a `NameError` when running this code, because `breakfast_message` is in scope.

Because global variable scope is so large and so powerful, global variable scope gives programmers more opportunities to create bugs. Over time, observe what tools and strategies are introduced to help lower this risk!

### !callout-info

## Variables Best Practices

Technically, Python has one specific rule about global variables: we can **read** global variables anywhere. However, **declaring** global variables inside of a function is a little trickier. We discourage declaring global variables inside of functions! Programmers discourage it so much, that this curriculum won't even teach you how to do it! Feel free to look this up. A search engine term to use could be "Python use global variables".

### !end-callout

## We Use Variable Scope To Solve Problems

We will apply our knowledge about variable scope to help us solve future programming problems.

### It's Extremely Helpful That Local Variables "Leave"

Recall: Inside of functions, what happens to every local variable after a function finishes (returns or exits)? After a function finishes, every local variable "gets released," or becomes unusuable. The local variable only "comes back" if we call the function again, when it will be re-initialized with a new value and a new place in memory.

When we want to reliably call a function multiple times, knowing that local variables "leave" after each function call, and "restart" in each function call, creates more reliable code.

In this example, follow these steps in order:

1. Read the code and comments, and trace the values of the local variable after each function call
2. Predict what the code will print out
3. Run the code
4. Compare your predictions against what you actually see
5. Write down your conclusions about how local variables "leave" at the end of each function call, and get re-initialized at the beginning of each function call.

```python
def display_breakfast(breakfast_of_champions):
    # The parameter breakfast_of_champions exists in this function!
    print(f"This function call has the parameter breakfast_of_champions with the value {breakfast_of_champions}")

    # The local variable breakfast_message exists in this function!
    breakfast_message = f"My breakfast today is {breakfast_of_champions}"
    print(f"{breakfast_message}")

    # After the return statement, the function will end, and breakfast_of_champions AND breakfast_message will no longer exist...
    return breakfast_message

display_breakfast("waffles and syrup")
# print(f"Uncommenting this line and trying to access breakfast_of_champions will create a NameError: {breakfast_of_champions}")
# print(f"Uncommenting this line and trying to access breakfast_message will create a NameError: {breakfast_message}")
display_breakfast("rice and soup")
display_breakfast("coffee and toast")
# print(f"Uncommenting this line and trying to access breakfast_of_champions will create a NameError: {breakfast_of_champions}")
# print(f"Uncommenting this line and trying to access breakfast_message will create a NameError: {breakfast_message}")
```

At first, it may be frustrating that we can't access `breakfast_of_champions` or `breakfast_message` outside of the function.

On the bright side, it makes our code extremely consistent and predictable: Python will **never** think `breakfast_of_champions` has any value, except when we pass a value into the `display_breakfast` function call. Programming and using variables to know what values they **aren't** is just as valuable as knowing what values they are.

### Our Strategies Will Evolve!

As we learn about more concepts, such as _iteration_ and _classes_, we'll see that local variables have special scope within those kinds of blocks.

It will be crucial to understand the local variable scope for those cases, too, and to rely on them.

Looking ahead: When we learn about _iteration_ in programming, most syntaxes for iteration create their own variable scope.

In this example, follow these steps in order:

1. Read this code and make a prediction about what it does and what will happen when you run it
2. Run it
3. Make predictions about where the local variables are, and what rules about scope they may follow
4. Write down your predictions

```python
def announce_lunch_menu(lunch_items):
    print("It is now time to declare each lunch item, slowly, and dramatically.")
    for lunch_item in lunch_items:
        print("Today we will eat......")
        print("a.....")
        print(lunch_item)
    print("I hope you're hungry!")

packed_lunchbox_contents = ["sandwich", "salad", "chips", "appy juice"]
announce_lunch_menu(packed_lunchbox_contents)
```

## Summary

Variable scope is the area of a program where a variable can be accessed.

When we access variables that are within scope, we can read them, manipulate them, re-assign them, and do all the good things that variables can do.

When we access variables out of scope, we get errors. We often get errors like `NameError`.

We will often make **local variables** within functions, that are scoped to that function.

## Check for Understanding

Finish this sentence: Variable scope is...

- the area of a program where a variable can be defined for the first time
- the area of a program where a variable can be accessed
- the area of a program where a variable can be released from memory
- the area of a program where a variable can be renamed

Read this code, and assume `cut`, `cook`, and `plate` are all valid, defined functions.

```python
def prepare_dinner(ingredients):
    chopped_food = cut(ingredients)
    cooked_food = cook(chopped_food)
    plated_food = plate(cooked_food)
    return plated_food

prepare_dinner(["Jackfruit", "Onion", "Mango", "Avocado", "Ginger", "Cucumber", "Lime", "Jalapeño"])
```

Variables that have can be read inside of the function are...

- `ingredients`
- `chopped_food`, `cooked_food`, `plated_food`
- `ingredients`, `chopped_food`, `cooked_food`, `plated_food`
- `ingredients`, `plated_food`

Read this code, and assume `cut`, `cook`, and `plate` are all valid, defined functions.

```python
def prepare_dinner(ingredients):
    chopped_food = cut(ingredients)
    cooked_food = cook(chopped_food)
    plated_food = plate(cooked_food)
    return plated_food

dinner_recipe = ["Jackfruit", "Onion", "Mango", "Avocado", "Ginger", "Cucumber", "Lime", "Jalapeño"]
prepare_dinner(dinner_recipe)
```

Which of these describe the variables (and their scope) inside of this code?

- `dinner_recipe`, `chopped_food`, `cooked_food`, and `plated_food` are all local variables. They can all be accessed inside of the function.
- `dinner_recipe`, `ingredients`, `chopped_food`, `cooked_food`, and `plated_food` are all local variables. They can all be accessed inside of the function.
- `dinner_recipe` is a global variable. `ingredients` is a parameter. `chopped_food`, `cooked_food`, and `plated_food` are local variables. Only the parameters and local variables can be accessed inside of the function.
- `dinner_recipe` is a global variable. `ingredients` is a parameter. `chopped_food`, `cooked_food`, and `plated_food` are local variables. They can all be accessed inside of the function.

Rewrite this code so it **only** uses local variables and parameters in the `prepare_dinner` function, and does not create a `NameError` at runtime.

```python
def cut(foods):
    print("We're cuttin' up some food!")
    return foods

def cook(foods):
    print("We're adding some tastiness to some food!")
    return foods

def plate(foods):
    print("We're putting the food on the plates and bowls!")
    return foods

def prepare_dinner():
    chopped_food = cut(dinner_recipe)
    cooked_food = cook(chopped_food)
    plated_food = plate(cooked_food)
    return plated_food

dinner_recipe = ["Jackfruit", "Onion", "Mango", "Avocado", "Ginger", "Cucumber", "Lime", "Jalapeño"]
prepared_dinner = prepare_dinner(dinner_recipe)
print("Ah, what a delicious looking prepared dinner.")
```
