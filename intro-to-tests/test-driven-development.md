# Test Driven Development

## Learning Goals
- Define Test Driven Development (TDD)
- Explain how TDD augments our programming workflow

## Introduction

**Test-Driven Development (TDD)** is a programming workflow technique where we write unit tests **before** and **to drive** writing our source code (solution code/implementation code).

When we use this programming technique, programmers get to use _automated tests_ as a way to explore, build, and test our code as a repeated workflow loop.

### How to TDD

Test-Driven-Development follows this process and order. Note that writing the test comes before writing the implementation code. That's the "test-driven" part!

1. Write a test
1. Watch it fail
1. Make it pass
1. Refactor
1. Repeat!

A more complete workflow that includes steps that are already part of our development work flow is summarized with the following steps:

#### TDD is Summarized as "Red, Green, Refactor"

![Red Green Refactor](assets/tdd_flow.gif)

We'll often hear this cycle shorthanded as __Red, Green, Refactor__.

1. Write a test that describes a feature of the software. Included in this ste
1. Run the test, and watch it fail. Watching it fail is crucial! This helps us confirm that the test is working as expected: we **should** get a test failure (or reasonable error) before the implementation code is written. This is watching a test result in **red** (or not passing the test).
1. Write code that makes all the tests pass. This makes the test **green.**
1. Look for opportunities to improve our code. This is most appropriate time to **refactor**-- after we have a messy working solution. This step does not add functionality.

We should not forget to make sure that our tests are still passing after the refactor!

<!-- available callout types: info, success, warning, danger, secondary  -->
### !callout-info

## Development Workflow
The steps above augment our current workflow, which include reading feature requirements and making regular git commits. 

### !end-callout


### TDD Checks Our Code As We Go

We should run our **entire** automated unit test suite often. When our requirements change, we can feel secure in changing our code because we have some _tests_ to let us know if we've broken something.

__Tests are transient.__ As we work on a project, our understanding of the problems at hand will change. As they do, your tests will change.

Keep in mind the balance between evolving requirements, evolving tests, and tests that should stay the same. This balance will change with every task.

## Check for Understanding

<!-- Question Takeaway -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: d0f49285
* title: TDD
##### !question

Describe the Red-Green-Refactor cycle.

##### !end-question
##### !placeholder

The Red-Green-Refactor cycle...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: 7ec32957
* title: TDD
##### !question

What was your biggest takeaway from this lesson? Feel free to answer in 1-2 sentences, draw a picture and describe it, or write a poem, an analogy, or a story.

##### !end-question
##### !placeholder

My biggest takeaway from this lesson is...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->



