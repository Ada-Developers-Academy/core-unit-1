# Problem Set: Debugging Continued

Moira has been working on some code related to Conway's Game of Life, but has run into some bugs.  Today's task is to fork Moira's Replit and help Moira debug her code.

Before getting started, here is some important information about the project that Moira is working on:

Conway's Game of Life is a classic cellular automata simulation in computer science.  In Conway's Game of Life, there is a stage or grid, and each point in the stage is a cell.  Each generation, every cell on the stage lives or dies based on a few simple rules.

1. Any live cell with < 2 neighbors dies
1. Any live cell with 2-3 neighbors lives
1. Any live cell with > 3 neighbors dies
1. Any dead cell with 3 neighbors comes alive

A cell's neighbors are the 8 cells immediately around the cell.

Before going further, take a minute to play with this [Game of Life simulator](https://playgameoflife.com/).  Add a few points to the grid and press start to watch the simulation.

In today's project, Moira is testing her code using the Blinker pattern.  The Blinker is an oscillator that flips from 3 vertical cells to three horizontal cells each generation:

[Blinker](../assets/debugging-contd_ps-game-of-life-blinker.png)[source](https://commons.wikimedia.org/wiki/File:Game_of_life_blinker.gif)

Take a minute to make a Blinker in the simulator linked above and run it to verify it's behavior.

Moira's project is to compute one generation of the Game of Life.  She has been given functions that print the stage and calculate the number of neighbors of a cell.  These functions are:

```python
print_stage(stage)
count_neighbors(stage, x_pos, y_pos)
```

She has also been given the code that sets up the initial state of the stage with the 3 vertical cells of a Blinker (```init_stage(stage)```).  Her task is to write the function ```one_generation(stage)```.  If her function works, this sequence of function calls:

```python
init_stage(stage)
print("First Generation:")
print_stage(stage)
one_generation(stage)
print("Second Generation:")
print_stage(stage)
```

will result in this output:
[Target Output](../assets/debugging-contd_ps-output.png)

Before starting work, please fork Moira's Replit.  Follow the link: (https://replit.com/@JasmineLopez4/DebuggingContdProblemSet)[https://replit.com/@JasmineLopez4/DebuggingContdProblemSet] and click the Fork button to create a copy that you can edit.

<!--BEGIN CHALLENGE-->

### !challenge

* type: paragraph
* id: a7981c89-552e-4587-9133-341aaa4752f3
* title: First Error

##### !question

Answer the following questions:
What happens when you run Moira's code?  
What line is the error on?
What type of error is it?
Why is the line throwing an error?

##### !end-question

<!--optional-->
##### !explanation

Moira's code raises an exception.  The line that causes the error is line 16, inside the one_generation function.  The error is a TypeError.  The line is throwing an error because v_pos is an integer and the `len` function requires an iterable argument, like a list or a dictionary.

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

Moira now knows what is happening and why it's happening.  It's time to try to fix the error!  

Moira's goal with this nested for loop was to access each cell of the stage and then make the appropriate changes for this generation for each cell.

<!--BEGIN CHALLENGE-->

### !challenge

* type: paragraph
* id: 8c74e298-f8e7-4635-8990-b8cc5791be43
* title: What is `stage`?

##### !question

Before Moira can fix her nested loop, she needs to make sure that she understands the data structure that she's looping over.  Read through the provided functions and use debugging tools like print statements to investigate the `stage` variable that she is working with.  What is `stage`?

##### !end-question

<!--optional-->
##### !explanation

`stage` is a list of lists.  After calling `init_stage()`, `stage` contains: `[[False, True, False], [False, True, False], [False, True, False]]`.  The inner lists are lists of `True` and `False`, where `True` indicates that the cell is alive and `False` indicates that the cell is dead.  When `stage` is printed out using `print_stage`, each inner lists is displayed as one horizontal row.

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

Moira needs the inner for loop to loop over each of the elements in each of the inner loops.  She also needs the vertical position and horizontal position of each of the cells so that she can use those to call count_neighbors for each cell.

<!--BEGIN CHALLENGE-->

### !challenge

* type: short-answer
* id: 42cc6a3a-e111-4344-ba03-bc4b2730c0d3
* title: Fixing the for loop

##### !question

What is the change that Moira needs to make to line 16 to fix this bug?  Input the new line 16 below, omitting any tabs.

##### !end-question

##### !answer

for h_pos in range(len(stage[v_pos])):

##### !end-answer


<!--optional-->
##### !hint

Moira needs to loop over the list at position v_pos inside of stage.  She can access the list using the code `stage[v_pos]`.  In her for loop, she needs to h_pos to iterate over the length of the inner list.  She can get the correct range for her for loop with the code `range(len(stage[v_pos]))`.

##### !end-hint


<!--optional-->
##### !explanation

By changing the code to `for h_pos in range(len(stage[v_pos])):`, the for loop is now looping over each horizontal position in each inner list. 

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

Moira runs her code and discovers that the error is gone!  Unfortunately, the output does not match the expected output.

<!--BEGIN CHALLENGE-->

### !challenge

* type: paragraph
* id: 2404607e-9db0-48bd-9222-61a58913ffb4
* title: What's the bug?
<!--Other optional fields (checkpoints only) -->
<!--`points: 1`: the number of points for scoring as a checkpoint-->
<!--`topics: python, pandas`: the topics for analyzing points-->

##### !question

What is the bug that Moira sees now?  What is the expected output?  What is the code doing?

##### !end-question

<!--optional-->
##### !explanation

The first generation has three living vertical cells.  The second generation should have three living horizontal cells.  Moira's code produces a second generation where all of the cells are dead.

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

<!--BEGIN CHALLENGE-->

### !challenge

* type: paragraph
* id: f9f85ba0-3390-46c0-9244-38b1bffa6821
* title: Getting to the why

##### !question

Moira wants to get her code working, but before she can do that she needs to understand why her code is doing what it's doing. 

Take a few minutes and use some debugging techniques to find out why her code is behaving the way it is.

List a few of the things you tried and what you discovered.

##### !end-question

<!--optional-->
##### !explanation

Some examples of things to try:

Add print statements that print out `stage` at the beginning and the end of `one_generation`.

Add print statements inside of the for loops that print out `stage`.

Comment out sections of code and re-add it line by line.

Grab the code and run it inside of VSCode with the debugger.

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

<!--BEGIN CHALLENGE-->

### !challenge

* type: paragraph
* id: 882c916d-55ab-4c53-888b-8b8d68ea8021
* title: Why is the code doing what it's doing?

##### !question

Why doesn't Moira's 'one_generation' function work?  Why are all of the cells dead in the second generation in the test?

##### !end-question

<!--optional-->
##### !explanation

Conway's Game of Life calculates the alive or dead status of each cell based on the state of the previous generation.  Moira's code is *changing* the state of the cells before the code finishes the calculations for each cell.  That means that cells are being set to dead (`False`) in the first row, and when the neighbors for the second row are calculated, the `count_neighbors` function is not accurate.   The `stage` that `count_neighbors` is using to calculate thing is being changed as the for loop is running, which is causing the `count_neighbors` result to be incorrect!

##### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

<!--BEGIN CHALLENGE-->

### !challenge

* type: paragraph
* id: 4b1ba8ea-b9e5-4c37-b486-17fd865bc17b
* title: How to fix the code?

##### !question

Moira knows what's happening and why it's happening.  She's not quite sure yet how to fix her code, though!  What are some debugging steps she can take as she works on a solution?

##### !end-question

### !end-challenge

<!--END CHALLENGE-->

