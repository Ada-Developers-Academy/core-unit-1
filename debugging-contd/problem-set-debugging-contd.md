# Problem Set: Debugging Continued

## Overview

Dahlia is a geneticist and programmer who is stuck while debugging her program. Dahlia has been tasked with analyzing genetic sequences which are provided as strings of characters. 

Our objective is to fork and clone [Dahlia's repository](https://github.com/Ada-Activities/Encode-Decode-Genetic-Sequences) and help Dahlia debug her code.

She needs to determine if each sequence is DNA or RNA, and compress the sequence for storage. Dahlia will compress them by replacing repeating characters in the string with a single character followed by a number representing how many times the character was repeated. 

To run the project: 
- execute `python3 main.py` in the console

To run the tests: 
- execute `pytest tests/test_part_one.py` in the console to run just the part 1 tests
- execute `pytest tests/test_part_two.py` in the console to run just the part 2 tests

Or
- Use the "Testing" tab (beaker icon) in VS Code and configure the set up for `Pytest`, then run the tests from the Testing panel.

Before jumping into debugging, please take a few minutes to read through the `PROBLEM_SET_README.md` file in the repository for further information on how Dahlia is trying to achieve her goals and what the files in her project should be doing. 

The focus of this exercise is to practice identifying bugs. We will continue to practice this skill during our time together at Ada and we should feel comfortable doing so without the use of AI tools like ChatGPT. Later, we'll practice debugging code with the assistance of prompting. For now, we'll stick to tools like rubber ducking or performing web searches to fix these bugs.

When you're ready, come back to this page to answer the questions below about the debugging process and the bugs you found.

Before starting work, please fork and clone Dahlia's repository. Follow the link: [https://github.com/Ada-Activities/Encode-Decode-Genetic-Sequences](https://github.com/Ada-Activities/Encode-Decode-Genetic-Sequences), click the Fork button to create a copy in your own account, and then clone it down to your local machine to edit it. 

## Part 1 Questions

<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: a7981c89-552e-4587-9133-341aaa4752f3
* title: Debugging Continued
##### !question

Answer the following questions:

1. What happens when you run the tests in `tests/test_part_one.py` without making any changes?  
2. In which file, and on what line of code is the error on?
3. What type of error is it?
4. Why is the line throwing an error?

##### !end-question
##### !explanation

1. Dahlia's code raises an exception.  

2. The line that causes the error is line 73 of `source/part_one.py`, inside the `encode_strand` function: `new_entry = strand[index - 1] + count`.  

3. The error is a `TypeError`.  

4. The line is throwing an error because `strand[index - 1]` evaluates to a string type and we are trying to concatenate the integer `count` to it. We cannot concatenate a string and an integer. We need both values to be string types if we want to use the `+` operator to add a value onto the end of an existing string.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: 8c74e298-f8e7-4635-8990-b8cc5791be43
* title: Debugging Continued
##### !question

Answer the following questions:

1. What happens when you run `main.py` without making any changes?  
2. In which file, and on what line of code is the error on?
3. What type of error is it?
4. Why is the line throwing an error?

##### !end-question
##### !explanation

1. Dahlia's code raises an exception. 

2. The line that causes the error is line 20 of `source/part_one.py`, inside the `driver` function. 

3. The error is a `KeyError`. 

4. The line is throwing an error because `categorized_sequences[category].append(sequence)` tries to access a key in the dictionary that does not exist. That means that the variable `category` must not point to a value that exists as a key in the dictionary `categorized_sequences`.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

Dahlia now knows what is happening and why it's happening. 
- For the first bug, we need a way to convert an `integer` to a string so that we can concatenate a number to the string that `strand[index - 1]` evaluates to.
- For the second bug we need to ensure that the keys in the dictionary `categorized_sequences` matches the values returned by the `categorize_strand` function.

It's time to try to fix these errors!  

<!-- prettier-ignore-start -->
### !challenge

* type: paragraph
* id: 42cc6a3a-e111-4344-ba03-bc4b2730c0d3
* title: Debugging Continued

##### !question

How can Dahlia change her code to fix the two bugs above? Check out our prior lessons or search online if necessary!

##### !end-question
##### !hint

1. How can we convert an integer to a string? What function can we use to cast a variable of one type to another type?
2. What keys were declared when the dictionary's lists for categories were created? What values does the `categorize_strand` function return? How can we make them match?

##### !end-hint
##### !explanation

1. Dahlia changes line 73 of `source/part_one.py` to
    ```py
    new_entry = strand[index - 1] + str(count)
    ```  
    - By wrapping `count` in the `str()` function, we convert `count` into a string that can be concatenated to another string like `strand[index - 1]`.
2. There are other ways she could fix it, but Dahlia decides to change lines 14-16 of `source/part_one.py` to update the keys in `categorized_sequences` so that they match the integer values returned by the function `categorize_strand`.
    ```py
    categorized_sequences[-1] = [] # strands that can't be determined
    categorized_sequences[0] = [] # dna strands
    categorized_sequences[1] = [] # rna strands
    ```

##### !end-explanation

### !end-challenge

<!-- prettier-ignore-end -->
<!--END CHALLENGE-->

Dahlia runs her code in `main.py` and discovers that the error is gone! Unfortunately, when she runs the tests in `tests/test_part_one.py` the actual output does not match the expected output. When looking at the test results, she sees a new crash.

<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: 2404607e-9db0-48bd-9222-61a58913ffb4
* title: Debugging Continued
##### !question

Dahlia's code produces this output when the tests for part one are ran:

```py
(venv) Encode-Decode-Genetic-Sequences % pytest tests/test_part_one.py
================================================== test session starts ==================================================
platform darwin -- Python 3.13.1, pytest-8.3.5, pluggy-1.6.0
rootdir: /Users/Ada_Student/Documents/Learn/debugging-cont/Encode-Decode-Genetic-Sequences
collected 8 items                                                                                                       

tests/test_part_one.py F..F....                                                                                   [100%]

======================================================= FAILURES ========================================================
________________________________________________ test_encode_DNA_strand _________________________________________________

    def test_encode_DNA_strand():
        # Arrange
        expected = DNA_ENCODED
    
        # Act
        result = encode_strand(DNA)
    
        # Assert
>       assert result == expected, f"Expected {expected}, but got {result}"
E       AssertionError: Expected G5A3G2C4T3A4C4T5A4C5G3A4T4A3, but got G5A3G2C4T3A4C4T5A4C5G3A4T4
E       assert 'G5A3G2C4T3A4C4T5A4C5G3A4T4' == 'G5A3G2C4T3A4C4T5A4C5G3A4T4A3'
E         
E         - G5A3G2C4T3A4C4T5A4C5G3A4T4A3
E         ?                           --
E         + G5A3G2C4T3A4C4T5A4C5G3A4T4

tests/test_part_one.py:14: AssertionError
________________________________________________ test_encode_RNA_strand _________________________________________________

    def test_encode_RNA_strand():
        # Arrange
        expected = RNA_ENCODED
    
        # Act
        result = encode_strand(RNA)
    
        # Assert
>       assert result == expected, f"Expected {expected}, but got {result}"
E       AssertionError: Expected C3A5U4C4G3U2A4U5G5A3C3G4A4C5, but got C3A5U4C4G3U2A4U5G5A3C3G4A4
E       assert 'C3A5U4C4G3U2A4U5G5A3C3G4A4' == 'C3A5U4C4G3U2A4U5G5A3C3G4A4C5'
E         
E         - C3A5U4C4G3U2A4U5G5A3C3G4A4C5
E         ?                           --
E         + C3A5U4C4G3U2A4U5G5A3C3G4A4

tests/test_part_one.py:46: AssertionError
================================================ short test summary info ================================================
FAILED tests/test_part_one.py::test_encode_DNA_strand - AssertionError: Expected G5A3G2C4T3A4C4T5A4C5G3A4T4A3, but got G5A3G2C4T3A4C4T5A4C5G3A4T4
FAILED tests/test_part_one.py::test_encode_RNA_strand - AssertionError: Expected C3A5U4C4G3U2A4U5G5A3C3G4A4C5, but got C3A5U4C4G3U2A4U5G5A3C3G4A4
============================================== 2 failed, 6 passed in 0.03s ==============================================
```

Answer the following questions:
1. What is the bug that Dahlia sees now?  
2. What is the expected output?  
3. What is the code doing?

##### !end-question
##### !explanation

1. Dahlia is seeing a mismatch between the string that `encode_strand` is returning and the expected string for the test `DNA_ENCODED`.

2. The expected output should include all bases listed in the genetic sequence we're compressing.

3. If we use the debugger or print statements to look at the values of `result` and `DNA_ENCODED`, we'll see that the last base in a sequence and its count are not being added to the compressed sequence stored in `result`. 

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: f9f85ba0-3390-46c0-9244-38b1bffa6821
* title: Debugging Continued
##### !question

Dahlia wants to get her code working, but before she can do that she needs to understand why her function `encode_strand` is behaving unexpectedly. 

Take a few minutes and use some debugging techniques to find out why her code is behaving the way it is.

List a few of the things you tried and what you discovered.

##### !end-question
##### !explanation

Some examples of things to try:

- Add print statements to `encode_strand` inside the for-loop to see what is getting appended to the list called `encoding` with each iteration.

- Add a print statement to the test just before the assert statement to see the value of result.

- Comment out sections of code and re-add it line by line.

- Grab the code and run it inside of VSCode with the debugger.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: 882c916d-55ab-4c53-888b-8b8d68ea8021
* title: Debugging Continued
##### !question

Why doesn't Dahlia's `encode_strand` function work? What is happening that means the last base of the genetic sequence never gets added?

##### !end-question
##### !explanation

The function `encode_strand` that is compressing the sequence is not accounting for adding the last base to the compressed string. 

<br>

When our loop ends, the variable `count` points to the correct number of characters for the last base in the sequence, but we still need to do some work to create a new entry for that character and append it to our `encoding` list before we call `join` in our `return` statement.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: 4b1ba8ea-b9e5-4c37-b486-17fd865bc17b
* title: Debugging Continued
##### !question

Dahlia knows what's happening and why it's happening. What code does she need to add or change to ensure the last base and its count gets added to the `encoding` list before we call `join` in our `return` statement?

##### !end-question
##### !explanation

There are other ways Dahlia could solve this issue, but she chose to add 2 lines of code to the function `encode_strand`. After the loop ends, Dahlia has added the following lines before the `return` statement:

```py
new_entry = strand[-1] + str(count)
encoding.append(new_entry)
```

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

## Part 2 Questions

In Part 2, Dahlia has refactored her code to first compress the strings, then categorize them. 

### !callout-info

## Set Up for Part 2

Before you answer these questions, ensure you have followed all instructions in the `PROBLEM_SET_README.md` file for Part 2 to change the imports in `main.py`.

### !end-callout

<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: f9f85ba0-3390-46c0-9244-38b1bffa6824
* title: Debugging Continued
##### !question

When Dahlia runs her code in `main.py`, no errors are raised, but she gets a test failure when running the tests in `tests/test_part_two.py`.

Take a few minutes and use some debugging techniques to find out why the Part 2 code is behaving the way it is.

List a few of the things you tried and what you discovered.

##### !end-question
##### !explanation

Some examples of things to try:

- Add print statements to `encode_strand` inside the for-loop to see what is getting appended to the list called `encoding` with each iteration.

- Add a print statement to the test just before the assert statement to see the value of result.

- Comment out sections of code and re-add it line by line.

- Run the code or tests using the debugger in VS Code.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: 4b1ba8ea-b9e5-4c37-b486-17fd865bc17f
* title: Debugging Continued
##### !question

Now Dahlia knows the issue is in `source/part_two.py`'s `categorize_strand` function. Ready with info on what's happening and why it's happening from her debugging techniques, what code does Dahlia need to change to fix the issue with the loop?

##### !end-question
##### !explanation

The step value of the `range` function call was 4, which means some bases were getting skipped during categorization. To fix this issue, Dahlia updated the step argument of the `range` function in the loop to 2. 

```py
for index in range(0, len(strand) - 1, 2):
```

Take some time to try to debug Dahlia's code. When you are ready, take a look at [Dahlia's solution](https://github.com/Ada-Activities/Encode-Decode-Genetic-Sequences/tree/solution) in the solution branch. You will need to select the files you are interested in reviewing from the Github UI. 

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->
