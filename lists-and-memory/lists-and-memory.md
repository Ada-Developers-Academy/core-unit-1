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

You can think of RAM as a series of blocks of memory, each with their own address, very much like the index in a list.

![Memory Addresses](../assets/lists-and-memory/ram-addresses.png)

Note that different types of data can take up more or less units of memory and the size of each unit of memory can depend on the type of computer system.

In the version of Python we are using CPython, you can see the memory address for any variable with the `id` function.

```python
>>> name = "Aubrey"
>>> id(name)
4305075184
```

## Variables & References

In python, if you make a variable like:

```python
sales_tax = 0.09
```

Python connects with the operating system (macOS in our case) and allocates an unused block of memory to store the information.  Then the variable is given a _reference_ to where that variable is stored in memory.

![Variable sales_tax referring to it's value in memory](../assets/lists-and-memory/lists-and-memory.png)

Further when you use the equal sign (`=`) assign another variable to `sales_tax` Python simply has the new variable use the same reference and it "refers" to the same value in memory.

```python
fees = sales_tax
```

![Multiple variables referring to the same value](../assets/lists-and-memory/multiple-references.png)

You can see the identify that both refer to the same value in memory using our friend the `id` function and see that both variables refer to the same memory address.

```python
>>> sales_tax = 0.09
>>> fees = sales_tax
>>> id(sales_tax)
4304253904
>>> id(fees)
4304253904 
```

Lists are no different except that instead of a variable containing a reference to the entire data, it contains a reference to an object which contains metadata (information about the object like it's length etc) and an _array of references_, where each element in the list refers to a different object in memory, just like a normal variable.

![Lists in memory](../assets/lists-and-memory/lists-in-memory.png)

Notice that the section of the List in memory with the small set of blocks next to each other.  Each of those represent a reference.  In Python, a List maintains metadata about the list (Type, length etc) and contiguous chunks of memory which contain _references_ to where the actual data is stored.  So you can think of the data as twice removed from the actual array variable.  A primitive variable like an `int` is like a friend who can show you where their things are, while a list is like a person who can show you to a collection of people, each of whom can direct you to their belongings. 

### Indexing

Notice the references in the `items` section of a list are contiguous.  Further each reference is the same size, so Python only needs to know where the collection of `items` begins and then it can use the following formula to quickly retrieve a specific list element.

`reference_address = start_of_items_collection + size_of_reference * index_number`

So if:

- The `items` collection started at the memory address 100
- Each reference is 8 Bytes in size

Long term storage like hard drives or SSDs which are persistent are another topic.

## Summary


## Check for Understanding