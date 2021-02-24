# What is OOP?

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=f544a6b1-5cd7-4a63-96b3-acd9002f7a84&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

## Learning Goals

- Define what Object-Oriented Programming is as a programming paradigm

## Introduction

A paradigm is a set of ideas that support a specific perspective. Programming paradigms are large concepts that focus on particular approaches to problem solving.

_Imperative programming_ is a programming paradigm that says programmers should solve problems by defining instructions for a computer to follow. You've programmed in the imperative programming paradigm if you've ever thought, "In order to solve that problem, I need to write down what steps a computer needs to take first, then second, then third."

_Object-oriented programming_ is a programming paradigm that is a subset of imperative programming that focuses on how we arrange and operate on data.

We can classify entire programing languages according to the programming paradigms they emphasize.

## Vocabulary and Synonyms

| Vocab                       | Definition                                                                                                                       | Synonyms                | How to Use in a Sentence                                                                                                                                                                                      |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Object-oriented programming | A programming paradigm based on "objects," which contain state (attributes) and behavior (methods)                               | OOP                     | "OOP means we will define classes, and use classes to make objects"                                                                                                                                           |
| Object                      | A collection of structured data along with the operations that can be performed on that data. Often means one instance.          | Instance                | "In OOP, we'll be making a lot of objects," "We should invoke the `add_friend` method on the `User` object," "Each `User` object in the `User` list will have an ID"                                          |
| Class                       | A template or blueprint used to create objects of a specific data type. Defines what concrete objects will look like.            | Prototype               | "The `String` class defines all of the attributes and methods that `String` objects have."                                                                                                                    |
| Instance                    | One particular object of a certain data type/class. Follows the format defined by its class, and has specific, individual state. | Object                  | "That specific `User` instance has an ID of `25`," "We should instantiate a new `User` instance here, then save it to the database," "The method `add_friend` takes in one instance of `User` as a parameter" |
| State                       | A generic term for the data that an object "knows" at one point in time. Usually, state can change over time.                    | -                       | "When a `User` object sends a message, the program checks the state of `online_status`"                                                                                                                       |
| Attribute                   | A named property of a class. Attributes are usually used to keep track of state.                                                 | Property, field, "attr" | "The `User` class defines the attribute `online_status`," "The `online_status` attribute is a boolean," "We check the `online_status` property before we send a message"                                      |
| Behavior                    | A generic term for what an object can "do."                                                                                      | -                       | "The `User` class should have the behavior of adding a friend to the friend list"                                                                                                                             |
| Method                      | A function that is defined inside of a class. Methods are usually used to describe behavior.                                     | Function                | "We need to call the `add_friend` method on `User`," "`User`'s `send_message` method checks the state of `online_status` at the beginning"                                                                    |

## Object-Oriented Programming

Object-oriented programming (OOP) is a programming paradigm that encourages structuring data as **objects.**

Objects are _things_ that represent concepts as data, hold their own distinct state, and carry out behaviors related to the concept they represent.

Objects are the primary building blocks for problem solving in object-oriented programming languages like Python.

Python lets us create objects that represent concepts like numbers, text, lists, the idea of true and false, and more. Even concepts that we define ourselves! Each of these ideas is represented as a different data type.

For example, Python defines `int` and `float` data types to represent certain kinds of numbers. The `str` (string) data type represents text, which is a bunch of letters, strung together. When we need to work with conditions that can be true or false, the `bool` (Boolean) data type has us covered.

Each of these data types:

- represents a different, specific idea as data
- has particular behavior that is meaningful to its concept

For example...

- Integers
  - represent whole numbers
  - can be subtracted with another integer or float
- Strings
  - represent text
  - can be concatenated (joined) with other strings
- Booleans
  - represent true or false
  - can be negated—true becomes false, while false becomes true

### Defining Classes

Beyond using Python's built-in data types, we can define our own data types.

To define our own data type, we create a **class.** A **class** is code that defines a template for creating similar objects.

Each class definition will have:

- A class name
  - This name is used as the "data type" name
- Concept-related **attributes**
  - An attribute is a piece of data
  - A class definition holding an attribute means we expect this class to hold a specific piece of data
- Concept-related **methods**
  - A method is a function that describes behavior or action
- Logic to describe what happens every time the class is used to make an **instance.**

### !callout-info

## Examples: Idea to Class

Observe these examples of classes that already exist, or classes that could exist.

| Idea to represent                                                                                              | Class Name |
| -------------------------------------------------------------------------------------------------------------- | ---------- |
| A class that describes the idea of a sequence of text                                                          | str        |
| A class that describes an ordered list                                                                         | list       |
| A class that describes a vehicle driver enrolled in a ride-share service, who has a ride history and a vehicle | Driver     |
| A class that describes a music album sold in a digital music store, and all its data                           | Album      |

### !end-callout

### Creating Instances of Classes

An **instance** is a concrete, literal manifestation of a class.

A _class_ defines the plans for a data type, much like a template, blueprint, or recipe. It determines the initial—or base—state, and the behaviors of that data type. The class definition is used to build instances.

An _instance_ is a single example of a class. The class provides the recipe to bake a cookie and the instance is the actual cookie (in its physical and yummy form)! Class instances, like other pieces of data, allocate and use memory, and have concrete state and behavior.

In our code, after a class is defined, we can create one instance, 50 instances, or thousands of instances. All of these instances will be distinct from one another, because they can all hold different attributes, and each occupies a different place in memory.

### !callout-info

## Examples: Instances of Classes

Observe these examples of classes that already exist, or classes that could exist.

| Class  | One Instance of the Class                      | Another Instance of the Class                     |
| ------ | ---------------------------------------------- | ------------------------------------------------- |
| str    | `"Hello World! I am an instance of a String!"` | `"The quick brown fox jumped over the lazy dog."` |
| list   | `["red", "orange", "yellow"]`                  | `["June", "July", "August"]`                      |
| Driver | A driver with a driver ID of `DR0004`          | A driver with a driver ID of `DR0005`             |
| Album  | Dirty Computer (2018)                          | Purple Rain (1984)                                |

### !end-callout

#### Synonyms for Creating Instances

Creating instances is something we'll do a lot, almost as much as making variables or using loops. There are a lot of ways to say that we're creating an instance.

We might say...

- I'm making an instance of an `Album`. This instance represents one album, named "Purple Rain."
- I'm creating an instance of `Album`. This instance represents one album, "Purple Rain."
- I'm instantiating the `Album` class. Now I have an instance, which is "Purple Rain."
- I'm making an `Album` object. The `Album` object is the "Purple Rain" album.
- The "Purple Rain" instance of `Album` is very different from the "Dirty Computer" instance of `Album`.
- "Purple Rain" and "Dirty Computer" are both instances of `Album`.

### State and Behavior

When we start defining our own classes, we will specify their **state** and their generic **behavior.**

**State** describes any data or attributes that should be kept over its lifetime—from the moment we create an instance until we let the system reclaim its resources.

**Behavior** describes any actions that objects of this class should be able to do.

### !callout-info

## Examples: State and Behavior

Observe these examples of classes that already exist, or classes that could exist.

| Class  | Instances                                                                                                                 | Something Kept in State                                                           | Behavior it Can Do                                                             |
| ------ | ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| str    | `"Hello World! I am an instance of a String!"`                                                                            | These specific characters, in this specific order                                 | Become CAPITALIZED if it needs to                                              |
| list   | `["red", "orange", "yellow"]`                                                                                             | These specific items, in this specific order                                      | Reverse the order of its elements                                              |
| Driver | A driver with ID `DR0004`, 3 trips, who has earned $35, has an average rating of 4.67                                     | Their ID, number of trips, total amount of money earned, and total average rating | Calculate their own average rating, tell you the number of trips they've taken |
| Album  | Dirty Computer (2018), which has 14 tracks in a certain order, was released April 2018, has a total album length of 48:42 | Tracks (number and order), release date, total album length                       | Return the audio data for any specific track it has                            |

### !end-callout

## Summary

In OOP...

We represent an idea as a data type by defining a **class.** A class is a template, or blueprint of the idea. The class is where we define the idea's possible **state** and **behavior.**

After we define the idea by defining a **class**, we use this class to create examples, or **instances** of the class. These instances are also known as **objects.**

## Check for Understanding

<!-- Question 1 -->
<!--prettier-ignore-start -->
### !challenge
* type: checkbox
* id: 23cea37b-7937-4386-8f70-f3968d2e2b5c
* title: What is OOP?
##### !question
What is a **class**?
##### !end-question
##### !options
* A way to create our own data types
* A template to create an object
* A way to bundle data and its state and behavior
##### !end-options
##### !answer
* A way to create our own data types
* A template to create an object
* A way to bundle data and its state and behavior
##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Quesiton 2 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: 287bf162-ad2d-4ce0-9f2a-5d82d497f129
* title: What is OOP?
##### !question
Which option below describes an instance?
##### !end-question
##### !options
* Instances are clones of a class, have the same attributes, and occupy the same place in memory.
* Instances are distinct from each other, can hold different attributes, and occupy different places in memory.
* Instance is a synonym for class. Instances are templates and create objects.
##### !end-options
##### !answer
* Instances are distinct from each other, can hold different attributes, and occupy different places in memory.
##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 3 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: 868ae4c0-35ae-40eb-8d5f-fff31d1376ac
* title: What is OOP?
##### !question
What is the difference between state and behavior?
##### !end-question
##### !options
* State describes data or attributes that change the actions of the object, while behavior describes concrete actions of the object.
* Behavior describes the data or attributes that should be kept over its lifetime, while state describes the actions the class should be able to do.
* Behavior describes actions that objects should be able to do, while state describes the data or attributes of an object that should be kept over its lifetime.
##### !end-options
##### !answer
* Behavior describes actions that objects should be able to do, while state describes the data or attributes of an object that should be kept over its lifetime.
##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question Takeaway -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: nBwx6O
* title: What is OOP?
##### !question

What was your biggest takeaway from this lesson? Feel free to answer in 1-2 sentences, draw a picture and describe it, or write a poem, an analogy, or a story.

##### !end-question
##### !placeholder

My biggest takeaway from this lesson is...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->
