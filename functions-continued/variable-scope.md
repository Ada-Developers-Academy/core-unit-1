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

| Vocab                | Definition                                                                                                                                                     | Synonyms                                                 | How to Use in a Sentence                                                                                                                                                                                                          |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Variable             | A variable is a name that references a value, or piece of data, stored in computer memory. We can assign values to variables, and read values from variables.  | holder of a value, reference                             | "That variable is named `foo`," "We should use `foo` on this line," "I need to pass the value of `foo` to this function"                                                                                                          |
| Variable Declaration | The line of code where we first introduce a variable, usually the first place where we give a variable a name and a value                                      | Where the variable is defined, initializing the variable | "I declared the variable `bar` on line 3, and accessed it on line 4," "I defined the variable `bar` with the initial value `42`," "I got a `NameError` on line 50 because I never initialized the variable `bar` before line 50." |
| Scope                | The area of a program where a given variable can be accessed or used                                                                                           | Variable Scope                                           | "The variable `baz` is in scope in the function `qux`," "`baz` is out of scope on this line of code," "This variable is scoped to this function."                                                                                 |
| Local Variable       | A kind of variable that has the smallest scope: local scope. The most common kind of variable.                                                                 | Variable                                                 | "`foo` is a local variable," "Let's create a local variable called `foo`"                                                                                                                                                         |
| Function             | Lines of code (1 or more) that are related, grouped together, and named. Once defined, these lines of code are reusable and can be called over and over again. | Method                                                   | "I defined a function," "I used a function," "I wrote a function"                                                                                                                                                                 |
| Global Variable      | A kind of variable that has the largest scope: global scope.                                                                                                   | global                                                   | "It's dangerous to use the global variable `bar` inside of the function," "We can read the global variable `bar` anywhere in the file."                                                                                           |

## Variable Scope Is Where a Variable Can Be Read

**Variable scope** is the area of a program where a given variable can be accessed.

A variable **has** scope.

Practically, **scope** usually means the **lines of code** where a variable can be accessed.

When we can access a variable successfully, and it doesn't give a runtime error, we usually say that the variable is **in scope.**

```python
my_daily_fruit = "apple"

print(f"An {my_daily_fruit} a day keeps the doctor away?")
```

In this example, we access the variable `my_daily_fruit` on the line `print(f"An {my_daily_fruit} a day keeps the doctor away?")`, and it doesn't give us a runtime error. This means that the variable `my_daily_fruit` is **in scope** on that line.

### Debugging Variable Scope: `NameError`

When we try to access a variable that is **not** in scope, the Python interpreter raises a runtime error `NameError` for that variable.

Observe and run this code that attempts to access `my_undefined_fruit` even though `my_undefined_fruit` is not defined within this code.

```python
# No definition of my_undefined_fruit found here!
print(f"An {my_undefined_fruit} a day keeps the doctor away?")
```

Our error message gives us a clue that **the variable `my_undefined_fruit` isn't defined within this scope.** Therefore, we got an error for accessing a variable not in scope.

```bash
NameError: name 'my_undefined_fruit' is not defined
```

## Variable Scope Is Defined by Kind and Location

Now that we know what variable scope is, how does a variable's scope get determined? What are the rules that say what a variable's scope is?

Variable scope is determined by:

1. The kind of variable that's defined
2. The location (line of code) where the variable is defined

### Local Variables Are the Most Popular Kind

**Local variables** are a kind of variable. Everything we've learned about variables so far still applies to local variables.

Properties of local variables:

- named with the `lower_snake_case` naming convention we've been using so far already.
- the most common kind of variable (and account for 90% of the variables we will use).
- variables with the smallest scope. Details to be discovered over time.

### !callout-secondary

## Variables in Short Examples

Most of the variables in our short examples so far have actually been _global_ variables! Let's take a look at how we can create a new scope so we can continue our discussion of _local_ variables.

### !end-callout

### Functions Create New Local Variable Scope

Local variables defined inside of a function only have scope **within that function.**

If we try to access a variable that was scoped to a function, we will get our predicted `NameError`.

```python
def display_breakfast():
    breakfast_message = "My breakfast today is an apple"
    print(breakfast_message)

display_breakfast()
print("Let's try to access the value of breakfast_message outside of the display_breakfast function:")
print(f"The value of breakfast_message is {breakfast_message}")
```

In our example above, when we try to access `breakfast_message` outside of its scope (in the `display_breakfast` function), we get the error message `NameError: name 'breakfast_message' is not defined`.

A function completes when it encounters a `return` statement, or otherwise reaches the end of its code. The `display_breakfast` function has no return statement, so it completes after printing its message. After it finishes, the names of its local variables become unavailable. Those names existed only while the function was running, and cannot be accessed from outside the function.

The string `"My breakfast today is an apple"` was created within the function itself. This data is referred to by the name `breakfast_message`, a local variable that only exists inside the function. When the name becomes unavailable, there is no longer any way to access that data. The Python interpreter tracks this, and will eventually recover the memory, to be reused elsewhere. We can no longer access that data.

As a result, once `display_breakfast` has completed, neither the local variable `breakfast_message`, nor the string data to which it referred, can ever be accessed in the rest of the program.

If we run the function again, a new string message is created. It may be located in a different area of memory entirely! This time, the local variable `breakfast_message` will refer to _that_ location, rather than the previous location. Even though the function is the same, each time we run it we get a new local variable referring to different data.

#### Parameters Are Scoped to Its Function

Recall that parameters are names for the arguments we pass into a function.

**Parameters are scoped like local variables**. Their names are available only within the function's local variable scope.

```python
def display_breakfast(breakfast_fruit):
    print(f"My breakfast today is {breakfast_fruit}")

display_breakfast("an apple")
print("Let's try to access the value of breakfast_fruit outside of the display_breakfast function:")
print(f"The value of breakfast message is {breakfast_fruit}")
```

In our example above, when we try to access the parameter `breakfast_fruit` outside of its scope, we get the error message `NameError: name 'breakfast_fruit' is not defined`. Since `breakfast_fruit` is a parameter of the `display_breakfast` function, it is only available within the function body.

#### Return Values Are Important

Functions are great! They let us build reusable blocks of code that make designing large systems easier. But how useful can they be if all of the data they keep in their local variables "disappears" after the function completes? Fortunately, Python provides a way to share that local data with the outside world!

If we want a **value** to come _out_ of a function, we **must** use the function's `return` statement to return that value.

```python
def display_breakfast():
    breakfast_message = "My breakfast today is an apple"
    print(breakfast_message)
    return breakfast_message

resulting_message = display_breakfast()
print("Instead of trying to access breakfast_message, let's return breakfast_message, store it in resulting_message, and access resulting_message instead:")
print(f"The value of resulting_message is {resulting_message}")
```

In this example, the `display_breakfast` function creates a new string value stored in the `breakfast_message` local variable. After printing the value, it goes on to return that string back to the caller. While the local variable `breakfast_message` is not accessible outside the function, we _are_ able to return the _value_ to which it referred. We store that value in the `resulting_message` variable, outside the function.

In general, we can say this function performs some useful operation, then returns the result of that operation to the outer scope. **This is one of the main patterns that we use in programming.**

## There Are More Kinds of Variables

**Global variables** are a kind of variable with global variable scope. Global variables can be accessed inside **or** outside of any functions.

Typically, global variables are declared **outside of any functions.**

Properties of global variables:

- named with the `lower_snake_case` naming convention we've been using so far already.
- variables with the largest scope.
  - Can be accessed and modified outside any function
  - Can be accessed and modified inside any function

For the small example programs that are common at the beginning of our coding journey, global variable use is inevitable. We'll also use them during in-progress code development and while debugging. Over time, we'll learn more techniques that will help us either avoid using global variables entirely, or increase our code quality in cases where we do use them.

```python
def display_breakfast():
    print("Let's try to access the value of breakfast_message INSIDE of the display_breakfast function:")
    print(breakfast_message)


breakfast_message = "My breakfast today is an apple"
print("Let's try to access the value of breakfast_message OUTSIDE of the display_breakfast function:")
print(f"The value of breakfast message is {breakfast_message}")

display_breakfast()
```

In this example, `breakfast_message` is a global variable, because it was declared **outside** of any function in our code. We are able to access it outside of the `display_breakfast` function, AND inside the `display_breakfast` function. We did **not** get a `NameError` when running this code, because `breakfast_message` is in scope.

Because global variable scope is so large and so powerful, global variable scope gives programmers more opportunities to create bugs. Over time, observe what tools and strategies are introduced to help lower this risk!

### !callout-warning

## Using Global Variables

Python has one specific rule about global variables: we can **read** global variables anywhere. However, **declaring** global variables _inside of a function_ is a little trickier. In fact, declaring global variables inside of functions is discouraged! It's discouraged so much, that this curriculum won't even teach you how to do it!

On your own, feel free to look up more about this topic. A search engine term to use could be "Python use global variables."

### !end-callout

## Applying Variable Scope

We will apply our knowledge about variable scope to help us solve future programming problems.

In this example, follow these steps in order:

1. Read the code and comments. Trace the values of the local variable after each function call.
2. Predict what the code will print out.
3. Run the code.
4. Compare your predictions against what you actually see.
5. Write down your conclusions about how local variables get released at the end of each function call, and get re-initialized at the beginning of each function call.

```python
def display_breakfast(breakfast_of_champions):
    # The parameter breakfast_of_champions exists in this function!
    print(f"This function call has the parameter breakfast_of_champions with the value {breakfast_of_champions}")

    # The local variable breakfast_message exists in this function!
    breakfast_message = f"My breakfast today is {breakfast_of_champions}"
    print(breakfast_message)

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

On the bright side, it makes our code extremely consistent and predictable. The only way to set the value of the `breakfast_of_champions` parameter is to pass a value in to the `display_breakfast` function call. Then the only place we can read that value is within the function body.

### !callout-success

## Variables With Different Scopes and the Same Name 🎉

Even if there were another variable outside the function which shared the name `breakfast_of_champions` the value will **never** "leak" out from the function to affect the outer value. Variables declared in different scopes, **even if they share the same name**, are two separate variables with no inherent relationship. When using variables, knowing what values they **aren't** can be just as valuable as knowing what values they are.

### !end-callout

## Summary

Variable scope is the area of a program where a variable can be accessed.

When we access variables that are within scope, we can read them, manipulate them, re-assign them, and do all the good things that variables can do.

When we access variables out of scope, we get errors. We often get errors like `NameError`.

We often make **local variables** within functions. Those variables are locally scoped to the function in which they are created.

## Check for Understanding

<!-- Question 1 -->

<!-- prettier-ignore-start -->
### !challenge

* type: multiple-choice
* id: 45954838-a89d-4b65-a5db-e6e52aae3ed7
* title: Variable Scope

##### !question

Finish this sentence: Variable scope is...

##### !end-question

##### !options

* the area of a program where a variable can be defined for the first time
* the area of a program where a variable can be accessed
* the area of a program where a variable can be released from memory
* the area of a program where a variable can be renamed

##### !end-options

##### !answer

* the area of a program where a variable can be accessed

##### !end-answer

### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->

<!-- prettier-ignore-start -->
### !challenge

* type: multiple-choice
* id: e3584e35-5c7d-4e46-a210-a1a0b697e8c0
* title: Local Variables

##### !question

Read this code, and assume `cut`, `cook`, and `plate` are all valid, defined functions.

```python
def prepare_dinner(ingredients):
    chopped_food = cut(ingredients)
    cooked_food = cook(chopped_food)
    plated_food = plate(cooked_food)
    return plated_food

prepare_dinner(["Jackfruit", "Onion", "Mango", "Avocado", "Ginger", "Cucumber", "Lime", "Jalapeño"])
```
Variables that can be read inside of the `prepare_dinner` function are...
##### !end-question

##### !options

* `ingredients`
* `chopped_food`, `cooked_food`, `plated_food`
* `ingredients`, `chopped_food`, `cooked_food`, `plated_food`
* `ingredients`, `plated_food`


##### !end-options

##### !answer

* `ingredients`, `chopped_food`, `cooked_food`, `plated_food`

##### !end-answer

### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 3 -->

<!-- prettier-ignore-start -->
### !challenge

* type: multiple-choice
* id: e9704a8e-e835-44c3-8bf0-57433d7654e9
* title: Describe These Variables

##### !question

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

##### !end-question

##### !options

* `dinner_recipe`, `chopped_food`, `cooked_food`, and `plated_food` are all local variables. They can all be accessed inside of the function.
* `dinner_recipe`, `ingredients`, `chopped_food`, `cooked_food`, and `plated_food` are all local variables. They can all be accessed inside of the function.
* `dinner_recipe` is a global variable. `ingredients` is a parameter. `chopped_food`, `cooked_food`, and `plated_food` are local variables. Only the parameters and local variables can be accessed inside of the function.
* `dinner_recipe` is a global variable. `ingredients` is a parameter. `chopped_food`, `cooked_food`, and `plated_food` are local variables. They can all be accessed inside of the function.

##### !end-options

##### !answer

* `dinner_recipe` is a global variable. `ingredients` is a parameter. `chopped_food`, `cooked_food`, and `plated_food` are local variables. They can all be accessed inside of the function.

##### !end-answer

### !end-challenge
<!-- prettier-ignore-end -->
