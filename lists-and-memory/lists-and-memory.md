# Lists and Memory

## Goal

- Explain how Python structures data into lists

## Introduction

For most of us Lists were our first _data structure_, that is, rather than a variable holding a single value, Lists hold an arbitrary set of data and provide a structure to organize, access and modify the information.  In this lesson we will examine how lists work behind the scences.  


## Vocabulary and Synonyms

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---
|  List | An ordered list of values. Items in the list are sometimes called elements. Can get the value of an item by using square brackets and the index of the item. | Array | I needed an ordered collection of student names, so I used a list. |
| Memory | Information and the medium on which it is stored for immediate use by a computing system.  Memory can also refer to the device which stores the information. | RAM (Random Access Memory) | There was too much data to load at once so we ran out of memory. |
| Reference | A value which enables a program to directly access a datum (a piece of data). | Handle | I passed a reference to the student records into the function |
| Contiguous | Things that are directly next to one another.  In many languages data in an array is stored in contiguous chunks. | adjacent | It's easier to write a collection of data to media when it is contiguous or adjacent to one another. |

## Memory

Every time your program stores a value in a variable, it is using _memory_.  Memory or RAM is a part of the computer which functions kind of like a series of post-it-notes on a fridge.  The information is quick to retrieve, and intended to be temporary.  When the program ends or the computer shuts down, information stored in RAM is erased.  Computer programs use memory to store information like variables they need while the program is executing.  

In python, if you make a variable like:

```
sales_tax = 0.09
```

Python connects with the operating system (macOS in our case) and allocates an unused block of memory to store the information.  Then the variable is given a _reference_ to where that variable is stored in memory.


Long term storage like hard drives or SSDs which are persistent are another topic.

## Summary


## Check for Understanding