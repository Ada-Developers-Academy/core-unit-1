# What is OOP?

## Learning Goals

- Define what Object-Oriented Programming as a programming paradigm is

## Introduction

A paradigm is a set of ideas that support a specific perspective. Programming paradigms influence how we solve problems. Programming paradigms are large ideas; sometimes, we even classify entire programming languages to fit into a programming paradigm.

_Imperative programming_ is a programming paradigm that says programmers should solve problems by defining instructions for a computer to follow. You've programmed in the imperative programming paradigm if you've ever thought, "In order to solve that problem, I need to write down what steps a computer needs to take first, then second, then third."

_Object-oriented programming_ is a programming paradigm that is a subset of imperative programming, and it will influence how we think about data.

## Vocabulary and Synonyms

| Vocab                       | Definition                                                                                                                                                | Synonyms                | How to Use in a Sentence                                                                                                                                                                                      |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Object-oriented programming | A programming paradigm based on "objects," which contain state (attributes) and behavior (methods)                                                        | OOP                     | "OOP means we will define classes, and use classes to make objects"                                                                                                                                           |
| Object                      | A data structure that can be its own specific data types, hold unique data, and can do unique behavior. Can often mean one instance.                      | Instance                | "In OOP, we'll be making a lot of objects," "We should invoke the `add_friend` method on the `User` object," "Each `User` object in the `User` list will have an ID"                                          |
| Class                       | A template or blueprint used to create objects of a specific data type. A class is generic and bastract; it defines what concrete objects will look like. | Template, blueprint     | "The `String` class defines all of the attributes and methods that `String` objects have," "                                                                                                                  |
| Instance                    | One particular object of a certain data type/class. Follows the format defined by its class, and has specific, individual state.                          | Object                  | "That specific `User` instance has an ID of `25`," "We should instantiate a new `User` instance here, then save it to the database," "The method `add_friend` takes in one instance of `User` as a parameter" |
| State                       | A generic term for the data that an object "knows" at one point in time. Usually, state can change over time.                                             | -                       | "The `User` object keeps `online_status` on state," "When a `User` object sends a message, the program checks the state of `online_status`"                                                                   |
| Attribute                   | A named property of a class. Attributes are usually used to keep track of state.                                                                          | Property, field, "attr" | "The `User` class defines the attribute `online_status`," "The `online_status` attribute is a boolean," "We check the `online_status` property before we send a message"                                      |
| Behavior                    | A generic term for what an object can "do."                                                                                                               | -                       | "The `User` class should have the behavior of adding a friend to the friend list"                                                                                                                             |
| Method                      | A function that is defined inside of a class. Methods are usually used to describe behavior.                                                              | Function                | "We need to call the `add_friend` method on `User`," "`User`'s `send_message` method checks the state of `online_status` at the beginning"                                                                    |

## Object-Oriented Programming

Object-oriented programming (OOP) is a programming paradigm that encourages structuring data as **objects.**

Objects are _things_ that can be their own specific data types, hold unique data, and can do unique behavior.

For example, Python, the programming language, demonstrates using OOP to solve problems.

Numbers, text, sequences, maps, sets, and the idea of true and false can be used to solve problems. Python captures each of these ideas into different data types. Python has defined the data types `int`, `float`, `str`, `dict`, `set`, `bool`, and more.

Each of these data types:

- represent a different, unique idea as data
- have unique behavior that is meaningful to itself

For example...

- Integers
  - represent whole numbers
  - can be subtracted with another integer or float
- Strings
  - represent text
  - can be concatenated with other strings
- Booleans
  - represent true or false
  - can be negated

### Defining Classes

Beyond using Python's built-in data types, we can define our own data types.

To define our own data type, we create a **class.** A **class** is code that defines a template for creating similar objects.

Each class definition will have:

- A class name
  - This name is used as the "data type" name
- Generic **attributes**
  - An attribute is a piece of data
  - A class definition holding an attribute means we expect this class to hold a specific piece of data
- Generic **methods**
  - A method is a function that describes behavior or action
- Logic to describe what happens every time the class is used to make an **instance.**

### !callout-info

## Examples: Idea to Class

Observe these examples of classes that already exist, or classes that could exist.

| Idea to represent                                                                                         | Class Name |
| --------------------------------------------------------------------------------------------------------- | ---------- |
| A class that describes the idea of a sequence of text                                                     | String     |
| A class that describes an ordered list                                                                    | List       |
| A class that describes a vehicle driver working at a ride-share app, who has a ride history and a vehicle | Driver     |
| A class that describes a music album sold in a digital music store, and all its data                      | Album      |

### !end-callout

### Creating Instances of Classes

An **instance** is a concrete, literal manifestation of a class.

A _class_ defines a data type _generically_, much like a template, or blueprint. It determines what that data type _can potentially_ hold as state or behavior.

On the other hand, an _instance_ of a class is a _concrete thing_ of that data type, with concrete state and behavior. One instance is one specific thing that has literal state and literal behavior. Each instance allocates and uses memory, just like other pieces of data.

In our code, after a class is defined, we can create one instance, 50 instances, or thousands of instances. All of these instances will be unique from each other, because they can all hold different attributes, and occupy different places in memory.

### !callout-info

## Examples: Instances of Classes

Observe these examples of classes that already exist, or classes that could exist.

| Class  | One Instance of the Class                      | Another Instance of the Class                     |
| ------ | ---------------------------------------------- | ------------------------------------------------- |
| String | `"Hello World! I am an instance of a String!"` | `"The quick brown fox jumped over the lazy dog."` |
| List   | `["red", "orange", "yellow"]`                  | `["June", "July", "August"]`                      |
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

When we start defining our own classes, we will define their generic **state** and their generic **behavior.**

**State** describes any data or attributes that should be kept over its lifetime.

**Behavior** describes any actions that objects of this class should be able to do.

### !callout-info

## Examples: State and Behavior

Observe these examples of classes that already exist, or classes that could exist.

| Class  | Instances                                                                                                                 | Something Kept in State                                                         | Behavior it Can Do                                                           |
| ------ | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| String | `"Hello World! I am an instance of a String!"`                                                                            | These specific characters, in this specific order                               | Become CAPITALIZED if it needs to                                            |
| List   | `["red", "orange", "yellow"]`                                                                                             | These specific items, in this specific order                                    | Reverse the order of its elements                                            |
| Driver | A driver with ID `DR0004`, 3 trips, who has earned $35, has an average rating of 4.67                                     | Its ID, number of trips, total amount of money earned, and total average rating | Calculate its own average rating, tell you the number of trips they've taken |
| Album  | Dirty Computer (2018), which has 14 tracks in a certain order, was released April 2018, has a total album length of 48:42 | Tracks (number and order), release date, total album length                     | Return the audio data for any specific track it has                          |

### !end-callout

## Summary

In OOP...

We will represent an idea as a data type by defining a **class.** A class is a template, or blueprint of the idea. The class is where we define the idea's generic **state** and **behavior.**

After we've defined the idea by defining a **class**, we will use this template/blueprint to create manifestations, or **instances** of this class. These instances are also known as **objects.**

## Check for Understanding

<!-- Definition question about classes being templates/blueprints -->

<!-- Definition question about instance -->

<!-- Definition question about state and behavior -->
