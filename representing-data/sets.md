# Sets 

## Introduction 

Sets are a unique data structure in Python.  Sets can be used to store data like lists and dictionaries, but sets also have a wide array of built in functionality based on the concept of sets in mathematics, and this is where sets really shine!  In this lesson we will explore the basics of sets and look at the ways we can take advantage of the features of sets in algorithms and problem solving.

## Vocabulary and Synonyms 

| Vocab | Definition | Synonyms | How to Use in a Sentence |
| ----------------- | ----------------------------------------------------------------------------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Set | An abstract data type that can store unique values, without any particular order |  | I added this project to my set of demos.
| Union | The union of a collection of sets is a new set consisting of all the elements in the input sets. | Juncture | I took the set of movies Mark and Hiba have seen and calculated the union resulting in a set of all the movies they've seen.
| Intersection | The intersection of two sets, A and B is a set containing all the elements of A which also belong to set B | Overlap | I took the set of movies starring Iron man and Black Panther and calculated the intersection resulting in the set of movies they both appeared in.
| Difference | The difference of two sets A and B consists of a set consisting of all the elements in set A excluding any element also found in set B. |  | I wanted to get a list of all the Hong Kong action movies which do not include Jackie Chan, so I took the difference of the set of HK movies and the set of Jackie Chan movies.
| Disjoint | Two sets A and B are disjoint when the intersection of set A and set B is empty. |  | Apparently the set of movies staring Uma Thurmond and Jackie chan is disjoint.  They've never worked together.

## Set Fundamentals

A "set" is an unordered collection of unique elements.  Similar to a list, a set can store several values, but unlike a list, a set does not maintain any particular order and cannot contain duplicates.  Like lists and dictionaries, we can add things to a set, remove things from a set, and dump everything out.  In addition, we can do many interesting things around comparing the contents of one set to another and combining the contents of sets in specific ways.

 There are a few rules that govern sets:

1. Each element of a set is unique.
1. Each element of a set must be immutable.
1. Elements in a set are unordered.

What does it mean that each element is unique?  If you add an element to a set, for example `5` and then try to add another `5` to the set, the number of items in the collection does not increase.

What does it mean that each element of a set must be immutable?  This means that we can only add unchangable elements to a set.  We can add `5` or `3` or `"pizza"` to the set because the values of 5, 3, or "pizza" cannot be modified.  However we cannot add a list or dictionary to a set because we can modify a list by appending new elements, overwriting existing elements and we can add and remove new key-value pairs to a dictionary.  If you do attempt to add a mutable value to a set you will get a `TypeError` with the message `unhashable type`.

What is meant by the statement that, "Elements in a set are unordered."?  A set does not maintain it's elements in any order.  

For example the following code.

```python
example_set = set()
example_set.add(5)
example_set.add(6)
example_set.add('pizza')
print(example_set)
```

Will print `{'pizza', 5, 6}`.  The set does not maintain order by insertion.

### Set Operations and Syntax

**Create a new set:**

```python
new_set = set() 
set_with_contents = {1, 2, 3, 'a', 'b'} 
```

Notice that creating a new, empty, set instance can be accomplished with `set()` and you can create a new set with values using the curly braces (`{}`).  The syntax for creating a new set with values differs from creating a dictionary in that there are no key-value pairs, only a list of values separated by commas.

**Add an element to a set:**

```python
set_a = {1, 2, 3}
set_a.add(4) 
```

The `add` method can be used to add a value to a set.

**Remove an element from a set:**

```python
set_a = {1, 2, 3}
set_a.remove(1) # set_a now equals {2, 3}
set_a.remove(4) # Raises a KeyError

set_a.discard(2) # set_a now equals {3}
set_a.discard(4) # does nothing
```

There are two ways to remove an element, `remove()` which raises a `KeyError` if the element is not present, and `discard()` which does not.


**Remove and return a random element from a set:**
```python
set_a = {1, 2, 3}
random_element = set_a.pop()

set_b = set()
random_element = set_b.pop() # Throws a KeyError
```

The `pop` method removes and returns one element from a set.  If the set is empty, `pop()` will throw a `KeyError`.


**Remove all elements from a set:**

```python
set_a = {1, 2, 3}
set_a.clear() # set_a is now an empty set
```

The `clear()` method removes all elements from a set leaving the set empty.

### Set Interactions

Now that we are familiar with the basic set operations, we can get into the exciting world of set to set interactions!  Let's start with two basic sets:

![Set A and Set B](../assets/new-lesson_sets_sets.png)  
*Fig. Set A {1, 2, 3, 4} and Set B {4, 5, 6, 7}.*

#### Union

The union of two sets combines the sets into a new set that includes all of the elements of the original sets.  Any overlapping elements are included only once in the result set.

![Union of Set A and Set B](../assets/new-lesson_sets_set-union.png)  
*Fig. Result Set {1, 2, 3, 4, 5, 6, 7}.*

```python
set_a = {1, 2, 3, 4}
set_b = {4, 5, 6, 7}

# Two syntax methods to create a set union:
# union() function:
result_set1 = set_a.union(set_b) # {1, 2, 3, 4, 5, 6, 7}

# | operator:
result_set2 = set_a | set_b # {1, 2, 3, 4, 5, 6, 7}
```

In the code above the union of `set_a` and `set_b` results in `{1, 2, 3, 4, 5, 6, 7}` consisting of all the elements in both sets.  However values, like `4` are included only once.  Overlapping elements are included once in the resulting set.

We can perform Union operations either by using the `union()` method, or the `|` operator.  Both the method and operator result in a new set consisting of the union of the given sets.

#### Intersection

The intersection of two sets is a new set composed of all of the elements that were present in both sets.  The overlapping elements are included only once in the result set.

![Intersection of Set A and Set B](../assets/new-lesson_sets_set-intersection.png)  
*Fig. Result Set {4}.*

```python

set_a = {1, 2, 3, 4}
set_b = {4, 5, 6, 7}

# Two syntax methods to create a set intersection:
# intersection() function:
result_set1 = set_a.intersection(set_b) # {4}

# & operator:
result_set2 = set_a & set_b # {4}
```

Much like with union, we can perform set intersection using either the `intersection` method or the `&` operator.  When we perform the intersection of two sets a new set is returned consisting of *only* the values contained in both of the given sets.

#### Difference

The difference of two sets is a new set composed of all of the elements of the first set _except_ for any elements that overlap with the second set.  

![Difference of Set A and Set B](../assets/new-lesson_sets_set-difference.png)  
*Fig. Result Set {1, 2, 3}.*

```python

set_a = {1, 2, 3, 4}
set_b = {4, 5, 6, 7}

# Two syntax methods to create a set difference:
# difference() function:
result_set1 = set_a.difference(set_b) # {1, 2, 3}

# - operator:
result_set2 = set_a - set_b # {1, 2, 3}
```

#### And More!


<!-- available callout types: info, success, warning, danger, secondary, star  -->
### !callout-info

## There is more!

There are more set interactions in Python that we will not cover in this curriculum.  [Follow your curiosity!](https://www.programiz.com/python-programming/set)

### !end-callout

### Set Comparisons

In addition to the previous set operations, Python has built-in ways to compare sets.  This can be quite practical for us.  For example, we might want to know if a set of users who are "Editors" and verify if all the editors are also "Publishers" in our web application.

#### Subset

Imagine two sets, `authors` and `editors`.  The `editors` set would be a subset of `authors` if every element of `editors` was also contained in `authors`.  

```python

editors = {"Lorraine", "Colin", "Aedan"}
authors = {"Lorraine", "Colin", "Aedan", "Ajwa", "Ciara"}

editors.issubset(authors) # evaluates to True

editors <= authors # evaluates to True
```

We can use the `issubset()` method or the `<=` operator to determine if one set is a subset of another.  Because all the elements of `editors` are contained in the set `authors`, the `editors` set is a subset of `authors` and both the `issubset()` and `<=` operator returns `True`.  We can also observe that two equal sets like `users` and `authors` are also subsets of each other.

#### Proper Subset

Two equal sets are also subsets of each other.

```python
authors = {"Lorraine", "Colin", "Aedan", "Ajwa", "Ciara"}
users = {"Lorraine", "Colin", "Aedan", "Ajwa", "Ciara"}

authors <= users # evaluates to True
users <= authors # evaluates to True
```

However a set is a proper subset if the other set contains all of the elements from the first set.  A set is not a proper subset of another set if the two sets are equal.

```python
editors = {"Lorraine", "Colin", "Aedan"}
authors = {"Lorraine", "Colin", "Aedan", "Ajwa", "Ciara"}


editors < authors # evaluates to True

users = {"Lorraine", "Colin", "Aedan"}

users < editors # evaluates to False
```

We use the `<` operator to determine if one set is a proper subset.  In the above example `editors` is a proper subset of `authors` because every element in `editors` is contained in `authors`, but the two sets are not equal (`authors` contain more).  `users < editors` evaluates to `False` because the two sets are equal.

#### Disjoint

Two sets are disjoint if they have no overlapping elements.

```python

set_a = {1, 2, 3}
set_b = {4, 5, 6}
set_c = {3, 4, 5}

# Only one syntax method to test if a set is disjoint with another set
# disjoint() function
set_a.disjoint(set_b) # evaluates to True
set_a.disjoint(set_c) # evaluates to False
```

## Problem Solving With Sets

We have now been introduced to the fundamentals of sets, next we can apply our knowledge of sets to solve programming problems.

Lets say we are working on an algorithm to compare two lists and find the elements that are common to both.  For example common favorite movies between two friends.

Here's the code for this type of approach:

```python
bethan_movies  = ["Candyman", "Free Guy", "Old", "Luck by Chance", "Billu"]
hussain_movies = ["Old", "Billu", "Gulaal", "Blue", "Fruit & Nut", "Wonder Woman"] 

result_list = []
for movie in bethan_movies:
    if movie in hussain_movies:
        result_list.append(movie)

return result_list
```

This solution will get the job done, but it's not very efficient.  The line `for movie in bethan_movies:` iterates through the first list and the line `if movie in hussain_movies:` iterates through the entire `hussain_movies` list with each iteration.

We can use sets to simplify this code by converting our lists into sets and then using set functionality to solve the problem.

### Creating Sets From Other Data Structures

First we need to turn our lists into sets.  The syntax for this is:

```python
bethan_movies  = ["Candyman", "Free Guy", "Old", "Luck by Chance", "Billu"]
hussain_movies = ["Old", "Billu", "Gulaal", "Blue", "Fruit & Nut", "Wonder Woman"] 

bethan_set = set(bethan_movies) 
hussain_set = set(hussain_movies) 
```

Next, we can use set intersection to generate a set of all of the elements that are contained in both sets:

```python
result_set = set_a & set b
```

If we want the results in a list we can convert a set into a list in a similar way to how we converted the list into a set:

```python
result_list = list(result_set)
```

We can turn this into a method with the following:

```python
def common_favorite_movies(movie_list_a, movie_list_b):
    movie_set_a = set(movie_list_a) 
    movie_set_b = set(movie_list_b) 

    result_set = movie_set_a & movie_set_b

    return result_set
```

### Eliminating Duplicates

Let's say we have a string of letters and we want to find all of the unique characters in the string.  Here's a brute force solution that we could use:

```python
phrase = "Fuzzy Wuzzy was a bear"
result = []

for char in phrase:  # loop over each character in the string
    if char not in result: # if the character is not in the result set:
        result.append(char) # add the character to the result set

for char in result: # print out the results
    print(char)
```

Just like our other brute force solution, this will get the job done, but we can use sets to come up with a more streamlined solution!

```python
phrase = "Fuzzy Wuzzy was a bear"
result_set = set(phrase) 
```

If we want to print out the set, we can use a for loop just like the for loop we used for the list above:

```python
for char in result_set:
    print(char)
```

Here's our final solution:

```python
phrase = "Fuzzy Wuzzy was a bear"
result_set = set(phrase)
for char in result_set:
    print(char)
```

## Check for Understanding

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: checkbox
* id: b21888b8-b27e-4d9d-b0fb-55f6de5e93f4
* title: How to create a set?
* topics: python, sets

##### !question

How can you create a new set?

##### !end-question

##### !options

* `names = set()`
* `names = {"Peter", "Lai"}`
* `names = {}`
* `names = {"name": "Peter"}`

##### !end-options

##### !answer

* `names = set()`
* `names = {"Peter", "Lai"}`

##### !end-answer

<!-- other optional sections -->
<!-- !hint - !end-hint (markdown, hidden, students click to view) -->
<!-- !rubric - !end-rubric (markdown, instructors can see while scoring a checkpoint) -->
##### !explanation

The line `names = set()` creates a new empty set.  The line `names = {"Peter", "Lai"}` creates a new set containing the two given strings.

The lines `names = {}` and `names = {"name": "Peter"}` create dictionaries instead.

##### !end-explanation

### !end-challenge

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: multiple-choice
* id: 3dc99142-2dc3-4831-afd9-b9089bcdca59
* title: How are sets different from lists
* topics: python, sets

##### !question

How are sets different from lists?

##### !end-question

##### !options

* A set maintains a specific order
* A set **cannot** contain duplicates
* A set cannot hold integers
* A list contains key-value pairs

##### !end-options

##### !answer

* A set **cannot** contain duplicates

##### !end-answer

<!-- other optional sections -->
<!-- !hint - !end-hint (markdown, hidden, students click to view) -->
<!-- !rubric - !end-rubric (markdown, instructors can see while scoring a checkpoint) -->
<!-- !explanation - !end-explanation (markdown, students can see after answering correctly) -->

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->

<!-- ======================= END CHALLENGE ======================= -->

<!-- Question Takeaway -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: aa450824-d399-45ff-8d38-be98a44072d5
* title: Biggest Takeaway
##### !question

What was your biggest takeaway from this lesson? Feel free to answer in 1-2 sentences, draw a picture and describe it, or write a poem, an analogy, or a story.

##### !end-question
##### !placeholder

My biggest takeaway from this lesson is...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->