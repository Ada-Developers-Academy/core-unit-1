# Intro to Computer Memory

## Goal

The goal of this lesson is to introduce computer memory. We believe this introductory content will help us better understand the machines we work on.

## Introduction

Computers are machines that carry out sequences of operations. We call these sequences of operations programs. Programs tell a computer what operations to perform, in what order, and on what data. The instructions of a program, its operations and data, are loaded into a part of the computer called memory.

What does it mean when our Activity Monitor says a program takes 100% CPU utilization? What do we mean when we say "memory"? Knowing a bit more about what's going on inside a computer can help us be more comfortable when we sit down to write programs.

## Vocabulary and Synonyms

- CPU
- RAM
- Volatile memory

## CPU

At the heart of a computer is the CPU, or Central Processing Unit. We sometimes simply call it the processor. Modern computers have _many_ kinds of processors, but the CPU is the main one that generally does the most work.

The CPU is a physical bunch of electronic circuitry located in a small package on the main board, or **motherboard**, of the computer. We can think of it as many tiny gates that let specific patterns of electricity flow along very precisely defined paths (that are etched with light!). By controlling the gates, and altering the flow of the electricity, the CPU does something very important: it executes instructions from software.

The CPU is amazing! Even though all it does is direct the flow of electricity through its circuitry, this lets it perform basic math, logic, control, and data read and write operations. By combining these simple operations with well-designed software (that _we_ are going to write!), the CPU can carry out even the most complex tasks!

## Physical Memory

The CPU will process many instructions that require data to be stored.

Physical memory devices hold this data. Like the CPU, physical memory is itself a package of electrical circuits. It holds the patterns of electricity that the CPU interprets as data. The CPU uses physical memory by writing data to it and reading data from it.

## RAM

RAM, or Random-access memory, is a form of computer memory. RAM sticks are physical memory devices that attach to a motherboard. RAM has two unique traits compared to other forms of computer memory:

1. RAM is fast
1. RAM holds data temporarily

RAM is fast! For one, it's directly connected to the CPU. And no matter the address, the CPU can access any location in RAM in the same amount of time. Imagine being able to access a storage unit on the top floor just as quickly as a unit near the front door! This property is what the "random-access" part of RAM describes.

### !callout-info

## Sequential Access Memory

In contrast to RAM, there is another memory configuration called SAM, or sequential access memory. It is less common these days, and is most typically used as long-term storage, often in the form of magnetic tape. It's referred to as "sequential" because if we need to access some data stored in the middle of the tape, we must inspect the tape sequentially, from the beginning, until we reach the data of interest. Compared to RAM, it's relatively inexpensive, high capacity, and _very_ slow.

### !end-callout

RAM holds data temporarily. When a computer turns off, and no more power is supplied to the RAM sticks, RAM stops holding memory. RAM holds data temporarily, and can't be used for long-term data storage. We refer to this data impermanence as being "volatile."

If RAM is fast, but volatile, what do we use RAM for?

### How the CPU Uses RAM

The CPU is responsible for running computer programs. When we start a program, first it gets copied into RAM. Then the CPU starts fetching instructions from the RAM containing the program code. As it carries out those instructions, it will also use RAM to read and write the temporary data the application needs while it's running.

Modern CPUs are very fast, and need a lot of data to stay busy. As a result, the CPU will end up accessing RAM billions of times every second! Fortunately, the connection between the CPU and RAM is direct and dependable, allowing this incredible system to operate reliably.

### Metaphor Pt 1: RAM As the Countertop

We've discussed that memory and RAM that is responsible for storing instructions. There are other parts of a computer that are responsible for long-term storage (such as a hard disk drive).

To illustrate the difference between these memory and storage, we can compare a computer to a kitchen.

The CPU is the chef. _RAM_ is countertop space. Long-term storage is a pantry or fridge.

The chef is limited in how much they can do at once by their countertop space, which is for putting things temporarily while doing something with them.

## Memory Addresses

Memory devices organize the data it stores by having and using **memory addresses**.

Each piece of data in memory occupies a memory location, which has an assigned memory address that the CPU can use to locate it.

### Metaphor Pt 2: The Countertop With Numbered Bins

To illustrate how the CPU uses memory addresses to temporarily put and locate instructions and data, let's continue to compare a computer to a kitchen.

Again, the CPU is the chef and RAM is countertop space. The CPU chef organizes their countertop space (memory) into labeled and numbered bins.

Each bin has a label like 100, 101, 102, etc. The CPU chef can put data from a `taxes` program into the bins with the labels 301, 302, and 303. We can put the data from a `weather` program into the bins 754, 755, and 756.

When the chef wants to get data and supplies from their `taxes` program, they go to bins 301, 302, and 303, and grab whatever is in there. To get data from their `weather` program, the chef goes to bins 754, 755, and 756, and gets what's in those bins.

If they need to change our `weather` program data, the CPU chef goes back to units 754, 755, and 756, and adds their onions and potatoes. The next time they get data from bins 754, 755, and 756, they'll end up grabbing their updated onions and potatoes, too!

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