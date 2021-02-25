# Problem Set: Using the Debugger

In this exercise we will use the debugger to identify two errors.

The code here has two bugs, one runtime error crashes the program on execution and the other is a logic error which calculates the incorrect sum for an Order instance.  

## Activity

### 1st Bug

The program crashes with the following stack trace:

```
Traceback (most recent call last):
  File "/Users/username/ada/python/python-debugging/app.py", line 16, in <module>
    f"{kamala_order.calculate_total()}")
  File "/Users/username/ada/python/python-debugging/grocery_store/order.py", line 14, in calculate_total
    total += self.products[i].price
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
```

Hmmmm... It seems that it crashes at line 14 of `grocery_store/order.py`.

Lets put a breakpoint at line 14 of `grocery_store/order.py`.

![Visual of a breakpoint in order.py at line 14](assets/order-py-breakpoint.png)

Then go to the debugger icon.

![Debugger Icon](assets/debugger-icon.png)

You **may** need to click on the select list, select `Add Configuration` and choose select `Python: Current File`.

![select debug current python file](assets/debug-current-python-file.png)

Otherwise you can simpily select "Python: Current File" from the drop down list.  

### Running Debugger

Then you can run the debugger by opening `app.py` and pressing the green triangle "Play" button.

[Debugger Play Button](assets/debugger-play.png)

You will notice that the application stops in `order.py`.

![Running Debugger](assets/running-debugger.png)

### Finding the bug...

Notice that the loop attempts to add up all the product prices.  In Watch add a watch for `self.products[i].price`

![Adding a watch on price](assets/watch-price.png)

Do you see the problem?  The price for the products gets set in `product.py`, see if you can find the error, and then re-run the debugger.  Does it crash now?  If you need add another breakpoint to `product.py` in the `__init__` function and step through the program.


### The 2nd Bug

One of the tests is failing, find the failing test in `tests/test_order.py`.  

![Failing test](../assets/vs-code-debugger/exercise-failing-test.png)

Create a breakpoint and use the step-into and step over commands to trace through the code and see why the test is failing.
