# Problem Set: Using the Debugger

## Directions

In this problem set we will use the debugger to identify two errors.  To run the activity clone the code at [AdaGold/python-debugging](https://github.com/AdaGold/python-debugging).  Then follow the directions in the README to set up the repo.

The code contains two bugs, one runtime error crashes the program on execution and the other is a logic error which calculates the incorrect sum for an Order.  

After following the setup instructions on the python-debugging repo, follow the instructions below.

## Practice

### First Bug: Debugging with Breakpoints

When you execute the program with:

`$ python3 app.py`

The program crashes with the following stack trace:

```
Traceback (most recent call last):
  File "/Users/username/ada/python/python-debugging/app.py", line 16, in <module>
    f"{calculate_total(kamala_order)}")
  File "/Users/username/ada/python/python-debugging/grocery_store/order.py", line 16, in calculate_total
    total += order["products"][i]["price"]
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
```

Hmmmm... The program is crashing at line 16 of `grocery_store/order.py`.

Lets put a breakpoint at line 16 of `grocery_store/order.py`.

![Visual of a breakpoint in order.py at line 16](../assets/vs-code-debugger/order-py-breakpoint.png)
*Fig. A breakpoint*

Then go to the debugger icon.

![Debugger Icon](../assets/vs-code-debugger/debugger-icon.png)
*Fig. The VS Code debugging icon*

You **may** need to click on the select list, select `Add Configuration` and choose select `Python: Current File`.

![select debug current python file](../assets/vs-code-debugger/debug-current-python-file.png)
*Fig. Select debug configuration*

Otherwise you can simpily select "Python: Current File" from the drop down list.  

### Running Debugger

Then you can run the debugger by opening `app.py` and pressing the green triangle "Play" button.

![Debugger Play Button](../assets/vs-code-debugger/start-debugger.png)
*Fig. Start debugging button*

You will notice that the application stops in `order.py`.

![Running Debugger](../assets/vs-code-debugger/running-debugger.png)
*Fig. Pausing at a breakpoint.*

### Finding the Bug with Watches

Notice that the loop attempts to add up all the product prices.  In Watch add a watch for `order["products"][i]`

![Adding a watch on a product](../assets/vs-code-debugger/watch-price.png)
*Fig. A watch*

<details style="max-width: 700px; margin: auto;">
  <summary>
    Try to identify the cause of the problem.  Open this to see our answer.
  </summary>

The bug is in `product.py`, and it relates to the price of products.

Hypothesize a cause for the error, make changes to fix it, and then re-run the debugger.

Repeat this process until the program stops crashing, and the bug is fixed. During this debugger process, practice:

- Adding another breakpoint to `product.py` inside the `create_product` function
- Stepping through the program when re-running the debugger
</details>

  

### Second Bug: Debugging a Failing Test

One of the tests is failing, find the failing test in `tests/test_order.py`.  

![Failing test](../assets/vs-code-debugger/exercise-failing-test.png)
*Fig. An example of a failing test in VS Code*

Create a breakpoint in the failing test `test_calculate_total_with_multiple_products` and use the step-into and step over commands to trace through the code and see why the test is failing.  You can click on the `Debug Test` link above the test function to run that one test in the debugger.
