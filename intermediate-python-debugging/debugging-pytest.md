# Debugging Tests With Pytest


All the previous lessons on debugging apply to running tests, but VS Code has the ability to run individual tests from the editor and it allows you to run tests in the debugger.  This can help you get tests to pass and identify why they fail.

## Goals

We have practiced using a debugger tool while running Python programs. Our goal is to apply those same debugger skills when we are running unit tests.

This lesson is structured like a follow-along exercise to illustrate:

- Setting up Pytest for the VS Code debugger
- Running tests using the VS Code debugger

Besides setup, overall we should observe that our familiar tools of setting breakpoints, running, pausing, and debugging, are overall similar between tests and programs.

## Setting Up Pytest for VS Code Debugger

You can set up VS Code to run the tests in the editor with `command-shift-p` and enter `Python: Configure Tests`.  

![configure tests](../assets/vs-code-debugger/python-configure-tests.png)

VS Code will ask you which test framework you want to use.  Select Pytest.  VS Code might ask you to install Pytest, which you can do so.

![Select Test framework to use](../assets/vs-code-debugger/select-pytest.png)

Then select the folder containing your tests.

![Select the tests folder](../assets/vs-code-debugger/select-tests-dir.png)

Then VS code will provide feedback on your tests allowing you to run them in the editor individually or run a test in the debugger with a click.

## Running Tests In The Debugger

Once configured VS Code can run tests in the debugger using links above each test.

The image below is an example of a test in VS code which is failing.

![Failing test](../assets/vs-code-debugger/failing-test-vs-code.png)

While the image below shows another test which passes.  Notice the checkmarks next to `Run Test` and `Debug Test`.

![Passing test](../assets/vs-code-debugger/passing-test-vs-code.png)

You can then add breakpoints and use watches to examine why the test is not passing.

Find the problem and fix it so the test now passes.  Once you have finished, remove the breakpoints and run the test to verify the problem is solved.

## Summary

In this activity we used VS Code & the Python debugger to trace through our code and identify two bugs.  To do so we used breakpoints, watches and the step over and step into buttons.  These tools allow us to pause the program and see the values of our variables as the application is executing.
