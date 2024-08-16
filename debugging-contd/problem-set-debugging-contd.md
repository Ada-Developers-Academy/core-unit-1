# Problem Set: Debugging Continued

## Overview

Dahlia is a geneticist and programmer who is stuck while debugging her program. Dahlia has been tasked with analyzing genetic sequences which are provided as strings of characters. 

Our objective is to fork [Dahlia's Replit](https://replit.com/@adacore/EncodeAndDecodeGeneticSequencesStarter) and help Dahlia debug her code.

She needs to determine if each sequence is DNA or RNA, and compress the sequence for storage. Dahlia will compress them by replacing repeating characters in the string with a single character followed by a number representing how many times the character was repeated. 

Dahlia's code can either be ran in test mode or production mode. When you run the project on Replit, the console will prompt you to enter `t` to test the project, or `r` to run the code in production mode.

Before jumping into debugging, please take a few minutes to read through the `PROBLEM_SET_README.md` file in the Replit for further information on how Dahlia is trying to achieve her goals and what the files in her project should be doing. 

When you're ready, come back to this page to answer the questions below about the debugging process and the bugs you found.

Before starting work, please fork Dahlia's Replit. Follow the link: [https://replit.com/@adacore/EncodeAndDecodeGeneticSequencesStarter](https://replit.com/@adacore/EncodeAndDecodeGeneticSequencesStarter) and click the Fork button to create a copy that you can edit. 

## Part 1 Questions

<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: a7981c89-552e-4587-9133-341aaa4752f3
* title: Debugging Continued
##### !question

Answer the following questions:

1. What happens when you use the `t` option to test Dahlia's code without making any changes?  
1. In which file, and on what line of code is the error on?
1. What type of error is it?
1. Why is the line throwing an error?

##### !end-question
##### !explanation

1. Dahlia's code raises an exception.  

2. The line that causes the error is line 73 of `part_one.py`, inside the `encode_strand` function: `new_entry = strand[index - 1] + count`.  

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

1. What happens when you use the `r` option to run Dahlia's code without making any changes?  
1. In which file, and on what line of code is the error on?
1. What type of error is it?
1. Why is the line throwing an error?

##### !end-question
##### !explanation

1. Dahlia's code raises an exception. 

2. The line that causes the error is line 20 of `part_one.py`, inside the `driver` function. 

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

1. How can we convert and integer to a string? What function can we use to cast a variable of one type to another type?
2. What keys were declared when the dictionary's lists for categories were created? What values does the `categorize_strand` function return? How can we make them match?

##### !end-hint
##### !explanation

1. Dahlia changes line 73 of `part_one.py` to
    ```py
    new_entry = strand[index - 1] + str(count)
    ```  
    - By wrapping `count` in the `str()` function, we convert `count` into a string that can be concatenated to another string like `strand[index - 1]`.
2. There are other ways she could fix it, but Dahlia decides to change lines 14-16 of `part_one.py` to update the keys in `categorized_sequences` so that they match the integer values returned by the function `categorize_strand`.
    ```py
    categorized_sequences[-1] = [] # strands that can't be determined
    categorized_sequences[0] = [] # dna strands
    categorized_sequences[1] = [] # rna strands
    ```

##### !end-explanation

### !end-challenge

<!-- prettier-ignore-end -->
<!--END CHALLENGE-->

Dahlia uses the `r` option to run her code and discovers that the error is gone!  Unfortunately, the actual output does not match the expected output. When she runs the code using the `t` option she sees a new crash.

<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: 2404607e-9db0-48bd-9222-61a58913ffb4
* title: Debugging Continued
##### !question

Dahlia's code produces this output when ran in test mode:

```py
Please enter r to run or t to test => t
Traceback (most recent call last):
  File "/home/runner/EncodeAndDecodeGeneticSequencesStarter/main.py", line 17, in <module>
    tests()
  File "/home/runner/EncodeAndDecodeGeneticSequencesStarter/sequence_tests.py", line 16, in tests
    part_one_tests()
  File "/home/runner/EncodeAndDecodeGeneticSequencesStarter/sequence_tests.py", line 21, in part_one_tests
    dna_tests()
  File "/home/runner/EncodeAndDecodeGeneticSequencesStarter/sequence_tests.py", line 27, in dna_tests
    assert result == DNA_ENCODED
AssertionError
```

Answer the following question:
1. What is the bug that Dahlia sees now?  
2. What is the expected output?  
3. What is the code doing?

##### !end-question
##### !explanation

1. Dahlia is seeing a mismatch between the string that `encode_strand` is returning and the expected string for the test `DNA_ENCODED`.

2. The expected output should include all bases listed in the genetic sequence we're compressing.

3. If we use the debugger or print statements to look at the values of `result` and `dna_encoded1`, we'll see that the last base in a sequence and its count is not being added to the compressed sequence stored in `result`. 

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

- Add print statements that print out `stage` at the beginning and the end of `one_generation`.

- Add print statements inside of the for loops that print out `stage`.

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

When our loop ends, the variable `count` points to the correct number of characters for the last base in the sequence, but we still need to do some work to create a new entry for that character and append it to our `encoding` list before we call join in our `return` statement.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: 4b1ba8ea-b9e5-4c37-b486-17fd865bc17b
* title: Debugging Continued
##### !question

Dahlia knows what's happening and why it's happening. What code does she need to add or change to ensure the last base and its count gets added to the `encoding` list before we call join in our `return` statement?

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

Before you answer these questions, ensure you have followed all instructions in the `PROBLEM_SET_README.md` file for Part 2 to change the imports in `main.py`, as well as uncommented the Part 2 tests in the `sequence_tests.py` file.

<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: f9f85ba0-3390-46c0-9244-38b1bffa6824
* title: Debugging Continued
##### !question

When Dahlia runs her code with the `r` option, no errors are raised, but she gets a test failure when running with the `t` option.

Take a few minutes and use some debugging techniques to find out why the Part 2 code is behaving the way it is.

List a few of the things you tried and what you discovered.

##### !end-question
##### !explanation

Some examples of things to try:

- Add print statements that print out `stage` at the beginning and the end of `one_generation`.

- Add print statements inside of the for loops that print out `stage`.

- Comment out sections of code and re-add it line by line.

- Grab the code and run it inside of VSCode with the debugger.

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: 4b1ba8ea-b9e5-4c37-b486-17fd865bc17f
* title: Debugging Continued
##### !question

Now Dahlia knows the issue is in `part_two.py`'s `categorize_strand` function. Ready with info on what's happening and why it's happening from her debugging techniques, what code does Dahlia need to change to fix the issue with the loop?

##### !end-question
##### !explanation

The step value of the `range` function call was 4, which means some bases were getting skipped during categorization. To fix this issue, Dahlia updated the step argument of the `range` function in the loop to 2. 

```py
for index in range(0, len(strand) - 1, 2):
```

Take some time to try to debug Dahlia's code. When you are ready, take a look at [Dahlia's solution here](https://replit.com/@adacore/EncodeAndDecodeGeneticSequencesSolution).

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->