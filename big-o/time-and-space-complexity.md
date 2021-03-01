# Time and Space Complexity

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=245174e4-436c-4a6a-bbb8-acd301432229&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

## Learning Goals

- Define time and space complexity

## Introduction

Computers run our programs pretty quickly. For our projects, when we run the code or run the tests, it takes a fraction of a second, sometimes maybe one or two seconds. Our computers use a tiny bit of memory while running the program.

However, those fractions of seconds add up. And what would happen if a computer did not have enough memory to hold everything in your code? Recall every app you've used that was slow; it might have been slow because of slow Internet, and it might have been slow because retrieving and processing data takes noticeable time and resources.

In programming, a way to create safe code is to consider different, extreme, possible situations. A great software situation to constantly think about is, "What would happen if our data set was millions of items?"

With a data set that is millions of items large, does our program slow down dramatically? Or slowly? Does our program take a very large amount of memory space?

Ultimately, every machine that runs programs has limits, whether it's time or memory. Machines have limited processing power and memory. Considering how much computing time and memory a program running our code consumes leads us to writing better code. Code that is fast or doesn't take a lot of memory is considered to be efficient.

## Vocabulary and Synonyms

| Vocab            | Definition                                                                                         | Synonyms | How to Use in a Sentence                                                                                                 |
| ---------------- | -------------------------------------------------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| Algorithm        | A specific process, set of rules, or solution to be followed when problem-solving                  | -        | "Sorting items in a list can be implemented a lot of different ways; there are different algorithms for sorting."        |
| Efficient        | A quality of code that means it is fast, and/or it does not take up much memory                    | -        | "My code is so slow, it takes a minute to finish running with this data set! I should refactor it to be more efficient." |
| Time Complexity  | A measurement of how the amount of time an algorithm takes to run as the size of the input changes |
| Space Complexity | A measurement of how much memory an algorithm uses as the size of the input changes                   |

## Considering the Algorithm

We consider time and space complexity with regards to _algorithms._ Algorithms are a set of instructions to follow, given some input. As programmers, that input is usually a data set.

## Time Complexity is How Long It Takes

Whenever we run an algorithm, our computer runs a series of **operations,** or set of instructions.

Given an algorithm with some input, how many operations does it do?

When the size of the input data set grows by one, how many more operations does our algorithm do?

When the size of the input data grows by a million, how many more operations does our algorithm do?

Time complexity is the measurement of how the amount of time an algorithm takes to run as the size of the input changes. Time complexity is usually measured in number of operations.

### Example: Quickly Finding Taylor in an Address Book

Different algorithms take different amounts of operations. Let's consider different "algorithms" for solving this problem:

Finding your friend Taylor's phone number in an address book. (A physical one, with bound pages.)

Read through these different ways that we could find Taylor's phone number in an address book. These different ways are different algorithms. As you read them, consider how much work you have to do (or how many operations it takes).

- Start at the first page of the address book. Read through each page. If you see Taylor's name, you have found their phone number.
- Re-organize your address book so the contacts are in alphabetical order. Then, flip to the half-way point of the address book, then determine which half of the address book "Taylor" is in. Then look through that half of the address book, split that in half, and determine which half to look through. Do this until we find "Taylor"
- Use a bookmark you inserted before that is labeled "Taylor", that leads straight to Taylor's phone number.

Re-read the examples again. If you had a million contacts, which of these would methods would be suddenly more burdensome? Which methods would only be a little more difficult?

When we compare how many operations these algorithms take, we are considering their **_time complexity._**

## Space Complexity is How Much Memory is Required

Whenever we run an algorithm, our computer uses memory. Every variable, literal, reference, and object in our program takes up a small (or large) block of memory.

Given an algorithm with some input, how many variables do we put in memory?

When our data set grows by one or a million, how many more variables are stored in memory?

Space complexity is the measurement of how the amount of memory an algorithm uses changes as the size of the input increases.

### !callout-info

## It Uses Memory? But I Didn't Save Anything

We say our computer uses memory, but there are no extra files. Wouldn't our computer run out of memory if we ran any program millions of times? Unless your program installs, downloads, saves, or writes something specifically to the computer, running programs use different kind of computer memory. Ideally, after a program finishes running, all the temporary memory from the program is released, deleted, and freed up, for more programs to run.

This is why people say to close your programs if your computer is running slowly!

### !end-callout

### Example: Finding Taylor in an Address Book With Little Resources

Different algorithms use different amounts of memory. Let's return to our address book problem as an example:

Finding your friend Taylor's phone number in an address book. (A physical one, with bound pages.)

Read through the algorithms that have slightly different details. Consider how much **_space_** each algorithm takes-- how many pages are used? How many other tools are used?

- Each contact gets their own page in the address book. Start at the first page of the address book. Read through each page. If you see Taylor's name, you have found their phone number.
- Re-organize your address book so the contacts are in alphabetical order. Then, open to the half-way point of the address book, then determine which half of the address book "Taylor" is in. Then open that half of the address book, split that in half, and determine which half to look through. Do this until we find "Taylor."
- Use a bookmark you inserted before that is labeled "Taylor", that leads straight to Taylor's phone number.

Re-read the examples again, imagining having a million contacts. Did any of these algorithms require us to create and hold something that wasn't an address book?

***Space complexity*** is considering how much space an algorithm takes.

## Best, Worst, and Average Cases

We could consider performance of an algorithm in three different scenarios: best case, worst case and average case scenarios.

- The best case scenario means a scenario where the algorithm finishes the most efficiently it could ever, truly, mathematically be
- The worst case scenario is the specific scenario where the algorithm would perform the most inefficiently in one or both aspects:
  - The algorithm takes the maximum amount of time
  - The algorithm consumes the maximum amount of memory to solve the problem
- The average case scenario would be the more common scenario that is neither the best nor worst case

### Example: The Address Book's Best, Worse, and Average Case

Let's consider our example, finding our friend "Taylor" in our address book.

Let's pick a specific algorithm: Start at the first page of the address book. Read through each page. If you see Taylor's name, you have found their phone number.

- The best case scenario is that Taylor's the very first contact we see. That didn't take any time at all!
- The worst case scenario is that Taylor is the very last contact, on the very last page, in the address book. With this algorithm, you would need to read the entire address book to find one phone number
- The average case scenario is that Taylor is somewhere in the middle.

If Taylor is the second contact or the second-to-last contact, is that kind of a best case scenario? Kind of a worst case scenario? It isn't; as programmers we can consider those cases to be average cases.

## We Compare Efficiency Between Algorithms

Given two algorithms, we can consider which algorithm is more efficient by comparing the time and space complexity.

We can consider time and space complexity by worst and average case, too. Considering the worst case scenario allows us to know how the program will do in the most critical positions. If an algorithm is to be used many times on many different instances, it may be more important to know the average execution time.

An efficient algorithm is one that runs as fast as possible and requires as little computer memory as possible. We often have to make a trade-off between these two goals. For any given algorithm, do we choose to use more memory to make our program faster, or settle for a slower program that uses less memory?

The answer will ultimately on the context of the algorithm! That being said, we can and will use formal measurements to inform our decisions more confidently.

## Check for Understanding

<!-- Question Takeaway -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: VW43GM
* title: Time and Space Complexity
##### !question

What was your biggest takeaway from this lesson? Feel free to answer in 1-2 sentences, draw a picture and describe it, or write a poem, an analogy, or a story.

##### !end-question
##### !placeholder

My biggest takeaway from this lesson is...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->
