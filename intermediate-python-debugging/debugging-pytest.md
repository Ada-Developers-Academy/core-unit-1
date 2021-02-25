# Debugging Tests With Pytest


All the previous lessons on debugging apply to running tests, but VS Code has the ability to run individual tests from the editor and it allows you to run tests in the debugger.  This can help you get tests to pass and identify why they fail.

## Learning Goals

By the end of this lesson, we will be able to...

- Run the debugger on individual tests

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
