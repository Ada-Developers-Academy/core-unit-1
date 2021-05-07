# Debugging With VS Code

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=af37992e-9059-48db-bb72-ace20062b52a&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

Python is widely used with VS Code and so VS Code's developers have put the time in to integrate the Python debugger into the standard VS Code plugin for Python.

In this lesson we will learn to connect VS Code and the Python debugger to help us fix errors in our code.

## Goal and Structure

In order to use a debugger in VS Code while working on Python projects, we need to set up our tools and then learn how to navigate and use them.

This lesson is broken up into the following sections:

1. Setting up VS Code to use and run the Python debugger
2. Using a small example Python program to learn how to and practice:
    - Adding and removing breakpoints
    - Running the debugger and watching the program pause
    - Observing variable state at a breakpoint
    - Creating and using a watch
    - Resuming, stepping over, stepping into, step out, restart, and stop

## Before Starting

Create a new project folder and Python file.

```bash
$ mkdir testing-example # make a testing-example folder
$ cd testing-example    # change into that folder
$ touch guess_number.py # create an empty python fole
$ code .                # Open the folder as a project in VS Code
```

Fill `guess_number.py` with the following python code.

```python
from random import randrange

number = randrange(10)

guess = -1
while number != guess:
  guess = int(input('Please enter a guess between 0-10  ==>'))
  if guess < number:
    print(f"{guess} is too low")
  elif number > guess:
    print(f"{guess} is too high")
  else:
    print("You guessed it!")

```

## Setting Up

To get started with the VS Code debugger, first find the debugger button on the left sidebar.

![Debugger Icon](../assets/vs-code-debugger/debugger-icon.png)

You may then need to create a `launch.json` file by clicking on `Run and Debug`.

![Run and debug button](../assets/vs-code-debugger/run-and-debug.png)

Then select `create a launch.json file` to make a configuration.  

![Debug Python File](../assets/vs-code-debugger/debug-configuration.png)

Save the resulting `launch.json` file.

You are set up!  You can close `launch.json` now.

## Debugging

### Adding and Removing Breakpoints

You can add a breakpoint by clicking to the **left** of the line number.  You will see a red dot appear to indicate the breakpoint.  You can click it again to make it dissapear.  

![Breakpoint](../assets/vs-code-debugger/number-breakpoint.png)  


Add a breakpoint to lines 5 and 11. See how you can toggle them on and off.


### Running the Debugger

You can then run the debugger at any time with the green triangle play button.

![Debugger play button](../assets/vs-code-debugger/debugger-play.png)
*Fig. The start debugging button*

Notice that the program will pause at the first breakpoint it encounters.

**What are the values of the variables?**  

### Watches

You can create a watch by clicking on the `+` icon and enter any expression.

![Entering a Watch](../assets/vs-code-debugger/watch-guess-before.png)  
*Fig. Creating a watch*

![Watches](../assets/vs-code-debugger/watch-guess-after.png)  
*Fig. A watch while the debugger is running*


**In the watch box, enter `number < guess`**.  What does it evaluate to?  Try a few more expressions.

![Watch example](../assets/vs-code-debugger/watch_example.png)  
*Fig. Watching an expression*

### Stepping Over & Stepping Into

Notice when the debugger is paused at a breakpoint you get the menu below.

![Debugger Menu](../assets/vs-code-debugger/debugger-menu.png)
*Fig. The debugger buttons*

This menu has the following buttons:

|  Button 	|  What it does 	| 
|---	|---	|
| **Resume**  	|  Continues the debugger executing until it gets to the next breakpoint, or the program exits. 	|
|  **Step Over** 	|  This button executes the current line and moves to the next line.  It will execute any function invoked on the current line, without pausing inside that function. 	|
|   **Step Into**	|  This button goes into any function invoked on the current line and pauses at the 1st line. 	|
| **Step Out**  | This button finishes the rest of the current function and pauses at the calling function. |
| **Restart** | This button restarts the debugger from the start.  |
| **Stop**  | This button stops the debugger.  |

These buttons let you deliberately navigate through the program's execution allowing you to examine the state of the application at any step in the process.

**Try using the buttons to navigate through the code.**  Do you see the values of the variables changing?

In the code try using the step over and step into buttons, do you notice a difference?  No, why not?

It's because we don't have any functions that we have written and used  The debugger is wisely deciding not to jump into the source code for the `input` function as that is part of the Python library.

## Check for Understanding
<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: paragraph
* id: 637ba598-f5db-4bb4-8730-a8595224a664
* title: Key Takeaway
* points: 1
* topics: Python, Debugging

##### !question

What is your key takeaway from this lesson?  

##### !end-question

##### !placeholder

##### !end-placeholder

<!-- other optional sections -->
<!-- !hint - !end-hint (markdown, hidden, students click to view) -->
<!-- !rubric - !end-rubric (markdown, instructors can see while scoring a checkpoint) -->
<!-- !explanation - !end-explanation (markdown, students can see after answering correctly) -->

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->
