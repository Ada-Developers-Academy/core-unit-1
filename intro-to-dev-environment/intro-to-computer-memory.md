# Intro to Computer Memory

## Goal

The goal of this lesson is to introduce computer memory. We believe that having an introduction to the stack and heap will allow us to better understand and debug memory allocation, variables, and references vs. values moving forward.

## Introduction

Computers are programmable machines that carry out sequences of instructions and operations. All of the modern computing devices that will run our code will have a memory component. When our code runs, our computers use this memory component to hold onto information like values and variables.

What does it mean when our Activity Monitor says a program takes 100% CPU utilization? What do we mean when we say "memory"? Learning a few things about computer memory can help us be more comfortable debugging.

## Vocabulary and Synonyms

- CPU
- RAM
- Stack
- Heap

## CPU

Computers have a CPU, or a Central Processing Unit. The CPU is a physical bunch of electronic circuitry located in a small place on a motherboard. The CPU's responsibility is to do something very important: execute instructions from software.

We can compare the CPU to a human brain. They're both a physical object specialized in taking input data and _processing_ it.

The CPU is amazing! The CPU itself performs basic math, logic, control, and reading and outputting data. However, with good software (including an operating system), and the help of other computer components, the CPU runs even the most complex programs.

## Physical Memory

The CPU will process many instructions that require data to be stored.

Physical memory devices can hold this data. The CPU will use physical memory by storing data on it and reading data from it.

Memory devices organize the data it stores by having and using **memory addresses**.

Each piece of data on memory will occupy a memory location, which has a memory address.

### Metaphor: Storage Units With Addresses

We can compare a memory device to a [Self-Storage Unit Center](https://en.wikipedia.org/wiki/Self_storage), where each self-storage unit has an address like 100, 101, 102, etc. We can put the data from a `taxes` program into the storage units with the addresses 301, 302, and 303. We can put the data from a `weather` program into the storage units 304, 305, and 306.

When I want to get my data and possessions from my `taxes` program, I'll go to units 301, 302, and 303, and grab whatever is in there. To get data from my `weather` program, I'll go to units 304, 305, and 306, and get what's in those units.

If I need to change my `weather` program data, I'll go to units 304, 305, and 306, and add in my rain data and my rain boots. The next time I _get_ data from 304, 305, and 306, I'll end up grabbing my rain data and rain boots too!

## RAM

RAM, or Random-access memory, is a form of computer memory. RAM sticks are physical memory devices that attach to a motherboard. RAM has two unique traits compared to other forms of computer memory:

1. RAM is fast
1. RAM holds data temporarily

Ram is fast! The phrase "random-access memory" refers to how RAM is fast; we can say it takes the same amount of time to "randomly access" anything in memory, no matter where it's physically located on the RAM stick.

Ram holds data temporarily. When a computer turns off, and no more power is supplied to the RAM sticks, RAM stops holding memory. RAM holds data temporarily, and can't be used for long-term data storage.

If RAM is fast, but temporary, what do we use RAM for?

### How the CPU Uses RAM

Since the CPU is responsible for running computer programs, the CPU will use RAM to hold temporary data while an application is running.

The CPU can directly access RAM, so the CPU can rely on it a lot!

## The Stack and Heap

RAM has two special regions: the stack and the heap.

The stack and the heap are both used to store temporary data within RAM.

However, these two regions manage, optimize, organize, and store temporary data using different strategies.

### !callout-info

## Stacks and Heaps Self-Storage Metaphor

We could call the stack and heap two different neighborhoods in our Self-Storage Unit Center, where the different neighborhoods follow different rules for filling up self-storage units.

### !end-callout

### Stack

The stack is a region of memory that is strong at being _really_ fast at managing the most recently stored data. The more recently pushed or stored the data is, the faster it is to manage the data.

### !callout-info

## Stacks Self-Storage Metaphor

We could say that storage units are aligned in a row (mimicking a "stack" structure). If we want to hold more rainboots, we'll add the new storage unit 307 to our storage unit stack, and put the rainboots in there. When we want to grab our rainboots, we'll go directly to the top storage unit, 307, and grab whatever is in there. We didn't have to navigate with too much difficulty, as long as we knew the rainboots were recently added.

### !end-callout

### Heap

The heap is a region of memory that is strong at holding a lot of data, or an unknown amount of data. The heap doesn't manage memory allocation in a special shape like the stack. This form more organically and dynamically allocate memory for any data.

When we don't know how big data is, the heap is more reliable. Data stored on the heap can be accessed by a lot of different functions in a program.

### !callout-info

## Heaps Self-Storage Metaphor

We could say that in this region, self-storage units are assigned whenever someone comes in and asks for a certain number of storage units. The self-storage unit manager will do their best to give the customer a row of storage units all next to each other. When a renter is finished with their storage unit and is done with it, the manager could consider re-renting that unit again. However, navigating the storage units here may be trickier, or just take a little longer.

### !end-callout

### Stack and Heap Summary

| Region | How it stores data                                                                                                                                                       | Strength                                                 |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------- |
| Stack  | Like a stack of dishes. New data gets placed "on top" of the stack of dishes. The data that is the last to come into the stack is the data that's the first to come out. | _Very_ fast for occasions where data is _very_ temporary |
| Heap   | Determines how much and where memory is allocated as data of varying sizes comes in.                                                                                     | Stores data of unknown sizes well                        |

## Applied to Variables

Consider variable assignment:

```python
apples = "Hello, World!"
```

When this program runs, our CPU begins to process it.

Every time our CPU runs into variable assignment, our CPU wants to put that data in memory. However, the CPU doesn't want to store the full idea "the variable `apples` has the value `"Hello, World!"`. Instead, the CPU thinks of **_two things_** that should be held in memory:

1. On the heap, store the value of the variable at a specific memory address
2. On the stack, store the variable and the specific memory address that it _points to_

### Example

When running the line `apples = "Hello, World!"`, the CPU wants to store these two things in memory:

1. The value `"Hello, World!"`
2. The variable `apples`

The CPU decides to process `apples = "Hello, World!"` by allocating memory like this:

1. On the heap, the string value `"Hello, World!"` gets stored with a memory address of `5555`
2. On the stack, the variable named `apples` gets stored. Along with the variable name, it stores the information "the value that this variable points to is in the memory address `5555`."

## Summary

This primer on computer memory should help us think more like a computer, and empathize with how a computer stores data just a little bit more.

We can also feel a closer relationship between the physical computer hardware, the data in memory, and the variables we work with in Python code.

## Check for Understanding

<!-- Question Takeaway -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: iqa4s7
* title: Intro to Computer Memory
##### !question

What was your biggest takeaway from this lesson? Feel free to answer in 1-2 sentences, draw a picture and describe it, or write a poem, an analogy, or a story.

##### !end-question
##### !placeholder

My biggest takeaway from this lesson is...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->
