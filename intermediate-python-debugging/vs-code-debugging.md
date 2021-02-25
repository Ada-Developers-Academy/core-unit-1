# Debugging With VS Code

Python is widely used with VS Code and so VS Code's developers have put the time in to integrate the Python debugger into the standard VS Code plugin for Python.

In this lesson we will learn to connect VS Code and the Python debugger to help us fix errors in our code.

## Learning Goals

By the end of this lesson we should be able to...

- Set up VS Code to run the Python debugger
- Run the Python debugger in VS Code to step through a program
- Use breakpoints, and watches to identify errors in code


## Setting Up

To get started with the VS Code debugger, first find the debugger button on the left sidebar.

![Debugger Icon](../assets/vs-code-debugger/debugger-icon.png)

You may then need to create a `launch.json` file by clicking on `Run and Debug`.

![Run and debug button](../assets/vs-code-debugger/run-and-debug.png)

Then Select `create a launch.json file` To make a configuration.  

![Debug Python File](../assets/vs-code-debugger/debug-configuration.png)

Save the resulting `launch.json` file.

That's it!  You are set up!  You can close `launch.json` now.

## Debugging

### Adding Breakpoints

You can add a breakpoint by clicking to the **left** of the line number.  You will see a red dot appear to indicate the breakpoint.  You can click again to make it dissapear.  

![Breakpoint](../assets/vscode-debugger/../vs-code-debugger/breakpoint.png)


### Running the Debugger

You can then run the debugger at any time with the green triangle play button.

![Debugger play button](../assets/vscode-debugger/debugger-play.png)

Notice that the program will pause at the 1st breakpoint it encounters.
### Watches

You can create a watch by clicking on the `+` icon and enter any expression.

![Entering a Watch](../assets/vs-code-debugger/watch-price.png)

![Watches](../assets/vs-code-debugger/watch.png)

### Stepping Over & Stepping Into

## Summary