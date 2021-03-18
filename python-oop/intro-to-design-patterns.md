# Intro to Design Patterns

## Learning Goals

- Define software design pattern

## Introduction

![Grey's Anatomy star Meredith Gray standing in front of Seattle Skyline](../assets/python-oop_intro-to-design-patterns_skyline.jpg)  
[(source)](https://www.popsugar.com/smart-living/Grey-Anatomy-Seattle-Tour-45105070)

Tatiana is moving to Seattle! As part of her move, she has one goal: get her possessions to her new apartment. Even though her goal is clear, she actually has a lot of decisions as to _how_:

- How is knowledge about her moving spread?
  - Will she tell everyone that she's moving by sending an email? Or over the phone?
  - Do her friends need to proactively ask her if she's moving?
  - Will Tatiana tell everyone the details of her new address? Or just the city?
- How is she packing her possessions?
  - Are they in big boxes? Small boxes?
  - Are they organized by type? Use? Color? Shape?
  - Are the boxes labeled on top? What do the labels look like? Are they unlabeled?
- What will she use to transport her possessions?
  - A moving truck?
  - Her friend's car?
  - An airplane?
  - Cargo ship?
- Will she get help with moving? If yes, then how?
  - Will she hire movers who specialize in moving efficiently?
  - Will she hire drivers who specialize in driving?
- When unloading, who knows about the layout of her new place?
  - Does Tatiana have to stay by the door, and direct each person where to go?
  - Will each mover have a map of her new place?
  - Will each box indicate what room they should be in?

All of these questions are details about _how_ Tatiana moves:

- Who has information? Who _doesn't_ have information?
- How are things organized and structured?
- How do things move from place to place?
- How many specialized workers are involved? How many generalists are involved?
- What kind of responsibilities are there? Who fulfills those responsibilities?

Even though Tatiana will eventually move, some of these answers can make her life much more difficult. Depending on her situation, moving by airplane might be extremely costly.

However, Tatiana could copy patterns of how other people move. Tatiana can copy her friend who just moved, and rely on a specialized driver instead of learning how to drive herself. How Tatiana delegates responsibilities to her friends can help them be more or less independent. How Tatiana packs and labels boxes can make packing or unpacking easier.

These considerations are similar to how we solve problems in programming.

## Vocabulary and Synonyms

| Vocab                   | Definition                                                                                                                                                        | Synonyms       | How to Use in a Sentence                                                                                                                                    |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Software design pattern | Reusable patterns commonly used to solve problems. Usually describes how classes and functions are structured and used. Usually conceptual and language-agnostic. | design pattern | "Janice has come across a similar problem before in a different project. To solve it, her team used the adapter design pattern, and made an adapter class." |

## What are Design Patterns?

**Software design patterns** are reusable patterns that usually guide how class and functions are structured and used.

When we build programs, we ask questions like:

- For each class,
  - What is it responsible for?
  - What does it know? What does it _not_ know?
  - What does it do? What does it _not_ do?
  - What other classes and functions does it depend on in order to work?
- For each function or method,
  - What is it responsible for?
  - When does it get called? How does it get called?
  - What does it depend on?

Different design patterns give different answers to these questions.

Additionally, when many programmers have learned the same design patterns, design patterns can be a shared language and make problem-solving smoother.

## Example Design Patterns

Because design patterns are conceptual, many of them are language-agnostic. It's not very important to memorize design patterns. It's more useful to recognize that these patterns simply exist. These patterns are additional creative tools in our software toolbox.

Here are a few common design patterns:

| Design Pattern | Description                                                                                                          | Benefits                                                                                                                                                                                                                                                                   |
| -------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Iterator       | A class whose responsibility is to know how to iterate through an object.                                            | Imagine an object that is complex, not-iterable, and is iterated over in other classes often. All relevant classes can use the Iterator to iterate over the object, rather than re-implement the logic. If the iterated object changes, only the iterator needs to change. |
| Factory        | A class or method whose responsibility is to create instances of some class.                                         | If a constructor is updated, only the factory needs to change, rather than each line that calls the constructor. The factory can hold logic that is more suited to making instances than directly calling the constructor.                                                 |
| Adapter        | A class whose responsibility is to help two other classes communicate with each other.                               | Imagine two classes that must communicate with each other, but are very different. An adapter can hold the logic that translates the communication between them, rather than change the two original classes.                                                              |
| Observer       | A class whose responsibility is to watch for changes over many objects, and notify many objects when changes happen. | Instead of many objects needing to refer to each other to announce changes, many objects can depend on one observer.                                                                                                                                                       |
| Decorator      | A class or method whose responsibility is to dynamically alter and extend the behavior of a function or class.       | If many objects must be extended in the same way, one decorator can decorate all of them without changing their implementation.                                                                                                                                            |
| Strategy       | A class whose responsibility is to represent an algorithm.                                                           | All relevant classes can use the strategy class instead of implementing the algorithm. If an algorithm needs to be updated, only the strategy class needs to change.                                                                                                       |

## Overdesign or Wrong Design Leads to Unmaintainable Code

Every design pattern has its pros and cons.

### !callout-info

## Back to Tatiana's Moving Example

When the boxes are unloaded, Tatiana wishes that each box went directly to the correct room. Tatiana might accomplish this by having really good and clear labels on her boxes. However, that requires Tatiana to know what rooms exist and decide what room each box belongs to while she's packing. How Tatiana labels her boxes can make unloading easier (pro), but means she's responsible for knowing and doing more while packing (con).

### !end-callout

There is such a thing as "overdesigning," or using a design pattern that increases complexity way more than necessary.

It's often best to implement a solution without a design pattern, make a git commit, and then refactor.

## Moving Forward: How Do We Use These?

Design patterns are applied when it makes problem-solving easier. It takes time, experience, research, context, and experimentation to apply design patterns effectively.

When considering a design pattern, the team should consider:

- Does this make the code more or less maintainable over time?
- What is the cost of implementing this design pattern?
- What are the benefits of implementing this design pattern?
- What are the alternatives?

### !callout-info

## Hungry for Examples?

As mentioned, applying design patterns takes time, experience, research, context, and experimentation. If you're hungry to see examples of design patterns in Python, feel free to do extra research. One external resource to begin your research may be [python-patterns.guide](https://python-patterns.guide/).

### !end-callout

## Check for Understanding

<!-- Something like matching between design pattern and definition. x3 times. Test Iterator, Decorator, and Factory, as these are the most common patterns for a junior dev (IMHO) -->

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge
* type: checkbox
* id: be55b24a-8a6e-4bcc-9661-f5354cdd59b6
* title: Intro to Design Patterns
##### !question
Which of these options are design patterns?
##### !end-question
##### !options
* Iterator
* Function
* Decorator
* Factory
* Adapter
##### !end-options
##### !answer
* Iterator
* Decorator
* Factory
* Adapter
##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->
<!-- prettier-ignore-start -->
### !challenge
* type: checkbox
* id: fae4bb8a-4879-44bc-83cb-3a3efb031908
* title: Intro to Design Patterns
##### !question

Which options describes the design pattern of an Iterator?

##### !end-question
##### !options

* A class that can iterate through an object. Available to other classes to use, however, if the object changes, the iterator will need to change.
* A while or for loop.
* A class whose responsibility is to know how to iterate through an object.

##### !end-options
##### !answer

* A class that can iterate through an object. Available to other classes to use, however, if the object changes, the iterator will need to change.
* A class whose responsibility is to know how to iterate through an object.

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 3 -->
<!-- prettier-ignore-start -->
### !challenge
* type: checkbox
* id: 0prltj
* title: Intro to Design Patterns
##### !question

Which options describes the design pattern of a Factory?

##### !end-question
##### !options

* A class that can iterate through an object. Available to other classes to use, however, if the object changes, the iterator will need to change.
* A class or method whose responsibility is to create instances of some class.
* A class that holds logic to create instances, which requires close attention to a constructor. If a constructor is updated, only the factory needs to change, rather than each line that calls the constructor.

##### !end-options
##### !answer

* A class or method whose responsibility is to create instances of some class.
* A class that holds logic to create instances, which requires close attention to a constructor. If a constructor is updated, only the factory needs to change, rather than each line that calls the constructor.

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 4 -->
<!-- prettier-ignore-start -->
### !challenge
* type: checkbox
* id: b64da97d-08cb-48d9-9165-2010c70bdcca
* title: Intro to Design Patterns
##### !question

Which options describes the design pattern of a Decorator?

##### !end-question
##### !options

* A class or method whose responsibility is to create instances of some class.
* A class or method whose responsibility is to dynamically alter and extend the behavior of a function or class.
* A class or method that can extend multiple objects without changing their implementation.

##### !end-options
##### !answer

* A class or method whose responsibility is to dynamically alter and extend the behavior of a function or class.
* A class or method that can extend multiple objects without changing their implementation.

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->
