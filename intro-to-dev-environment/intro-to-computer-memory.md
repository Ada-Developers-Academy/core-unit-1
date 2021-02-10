# Intro to Computer Memory

## Goal

The goal of this lesson is to introduce computer memory. We believe this introductory content will help us better understand the machines we work on.

## Introduction

Computers are machines that carry out sequences of operations. We call these sequences of operations programs. Programs tell a computer what operations to perform, in what order, and on what data. The instructions of a program, its operations and data, are loaded into a part of the computer called memory.

What does it mean when our Activity Monitor says a program takes 100% CPU utilization? What do we mean when we say "memory"? Knowing a bit more about what's going on inside a computer can help us be more comfortable when we sit down to write programs.

## Vocabulary and Synonyms

- CPU
- RAM

## CPU

At the heart of a computer is the CPU, or Central Processing Unit. We sometimes simply call it the processor. Modern computers have _many_ kinds of processors, but the CPU is the main one that generally does the most work.

The CPU is a physical bunch of electronic circuitry located in a small package on the main board, or **motherboard**, of the computer. We can think of it as many tiny gates that let specific patterns of electricity flow along very precisely defined paths (that are etched with light!). By controlling the gates, and altering the flow of the electricity, the CPU does something very important: it executes instructions from software.

The CPU is amazing! Even though all it does is direct the flow of electricity through its circuitry, this lets it perform basic math, logic, control, and data read and write operations. By combining these simple operations with well-designed software (that _we_ are going to write!), the CPU can carry out even the most complex tasks!

## Physical Memory

The CPU will process many instructions that require data to be stored.

Physical memory devices hold this data. Like the CPU, physical memory is itself a package of electrical circuits. It holds the patterns of electricity that the CPU interprets as data. The CPU uses physical memory by writing data to it and reading data from it.

Memory devices organize the data it stores by having and using **memory addresses**.

Each piece of data in memory occupies a memory location, which has an assigned memory address that the CPU can use to locate it.

### Metaphor: Storage Units With Addresses

We can compare a memory device to a [Self-Storage Unit Center](https://en.wikipedia.org/wiki/Self_storage), where each self-storage unit has an address like 100, 101, 102, etc. We can put the data from a `taxes` program into the storage units with the addresses 301, 302, and 303. We can put the data from a `weather` program into the storage units 304, 305, and 306.

When we want to get our data and possessions from our `taxes` program, we go to units 301, 302, and 303, and grab whatever is in there. To get data from our `weather` program, we go to units 304, 305, and 306, and get what's in those units.

If we need to change our `weather` program data, we go back to units 304, 305, and 306, and add our rain data and rain boots. The next time we _get_ data from 304, 305, and 306, we'll end up grabbing our updated rain data and rain boots too!

## RAM

RAM, or Random-access memory, is a form of computer memory. RAM sticks are physical memory devices that attach to a motherboard. RAM has two unique traits compared to other forms of computer memory:

1. RAM is fast
1. RAM holds data temporarily

RAM is fast! For one, it's directly connected to the CPU. And no matter the address, the CPU can access any location in RAM in the same amount of time. Imagine being able to access a storage unit on the top floor just as quickly as a unit near the front door! This property is what the "random-access" part of RAM describes.

Ram holds data temporarily. When a computer turns off, and no more power is supplied to the RAM sticks, RAM stops holding memory. RAM holds data temporarily, and can't be used for long-term data storage.

If RAM is fast, but temporary, what do we use RAM for?

### How the CPU Uses RAM

Since the CPU is responsible for running computer programs, the CPU will use RAM to hold temporary data while an application is running.

The CPU can directly access RAM, so the CPU can rely on it a lot!

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
