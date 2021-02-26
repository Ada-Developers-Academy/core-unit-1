# Problem Set: Static Methods and Class Methods

## Directions

Complete all questions below.

## Practice

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge
* type: checkbox
* id: 606307f5-71f6-4101-9043-bd1559673c0c
* title: Static Methods and Class Methods
##### !question

How are decorators useful?

##### !end-question
##### !options

* Decorators extend the behavior of functions using wrapped functions which can be thought of as reusable building blocks
* Static and class methods use decorators
* Decorators always modify the behavior of functions, which is necessary for implementing design patterns like Iterators

##### !end-options
##### !answer

* Decorators extend the behavior of functions using wrapped functions which can be thought of as reusable building blocks
* Static and class methods use decorators

##### !end-answer

##### !explanation
When using decorators, the wrapped function shouldn't need to be modified. Think of a wrapped function as a _permanent_ behavior tied to the decorator. If a function does not need the behavior the decorator would provide, then do not use that particular decorator or (if necessary) create another wrapped function that contains that desired behavior. In the end, it really depends on the _needs_ of your program. Design patterns like decorators are used to help optimize, they're not always _required_ to be used.
##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->
<!-- prettier-ignore-start -->
### !challenge
* type: short-answer
* id: f8c590a2-10be-4a93-b11d-b3586eb23feb
* title: Static Methods and Class Methods

##### !question
Complete the sentence:

> A _____ method does not have access to the instance (`self`) but has access to the class via (`cls`).
##### !end-question

##### !answer
class
##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 3 -->
<!-- prettier-ignore-start -->
### !challenge
* type: checkbox
* id: 717f8180-5d0c-41e6-aa7b-d9ec104fcc80
* title: Static Methods and Class Methods
##### !question

Icey's Ice Cream Shop is building a mobile app for customer orders. Select the option that would display the following output:

```
Welcome to Icey's Ice Cream Shop!
What would you like to order today?
You ordered a vanilla fudge sundae!
```
##### !end-question
##### !options
* 
```python
class Order:
    greeting = "Welcome to Icey's Ice Cream Shop! \nWhat would you like to order today?"

    def __init__(self, flavor, topping, dessert_type):
        self.flavor = flavor
        self.topping = topping
        self.dessert_type = dessert_type

    def display_order(self):
        print(f"You ordered a {self.flavor} {self.topping} {self.dessert_type}!")

    @classmethod
    def greet(cls):
        print(cls.greeting)

customer_order = Order("vanilla", "fudge", "sundae")
customer_order.greet()
customer_order.display_order()
```

* 
```python
class Order:
    greeting = "Welcome to Icey's Ice Cream Shop! \nWhat would you like to order today?"

    def __init__(self, flavor, topping, dessert_type):
        self.flavor = flavor
        self.topping = topping
        self.dessert_type = dessert_type

    def display_order(self):
        print(f"You ordered a {self.flavor} {self.topping} {self.dessert_type}!")

    @classmethod
    def greet(cls,self):
        print(self.greeting)

customer_order = Order("vanilla", "fudge", "sundae")
customer_order.greet()
customer_order.display_order()
```
* 
```python
class Order:
    greeting = "Welcome to Icey's Ice Cream Shop! \nWhat would you like to order today?"

    def __init__(self, flavor, topping, dessert_type):
        self.flavor = flavor
        self.topping = topping
        self.dessert_type = dessert_type

    def display_order(self):
        print(f"You ordered a {self.flavor} {self.topping} {self.dessert_type}!")

    @classmethod
    def greet(cls,self):
        print(self.greeting)

customer_order = Order("vanilla", "fudge", "sundae")
print(customer_order.greet)
customer_order.display_order()
```
##### !end-options

##### !answer
* 
```python
class Order:
    greeting = "Welcome to Icey's Ice Cream Shop! \nWhat would you like to order today?"

    def __init__(self, flavor, topping, dessert_type):
        self.flavor = flavor
        self.topping = topping
        self.dessert_type = dessert_type

    def display_order(self):
        print(f"You ordered a {self.flavor} {self.topping} {self.dessert_type}!")

    @classmethod
    def greet(cls):
        print(cls.greeting)

customer_order = Order("vanilla", "fudge", "sundae")
customer_order.greet()
customer_order.display_order()
```
##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 4 -->
<!-- prettier-ignore-start -->
### !challenge
* type: checkbox
* id: 8cbb9181-0d99-434d-bec4-b269ca33a3f6
* title: Static Methods and Class Methods

##### !question
Icey wants to add a compliment after customera makes an order. Select the option that would generate the following output:

```
Welcome to Icey's Ice Cream Shop!
What would you like to order today?
You ordered a vanilla fudge sundae!
That's a delicious Icey order!
```
##### !end-question

##### !options
* 
```python
class Order:
    greeting = "Welcome to Icey's Ice Cream Shop! \nWhat would you like to order today?"

    def __init__(self, flavor, topping, dessert_type):
        self.flavor = flavor
        self.topping = topping
        self.dessert_type = dessert_type

    def display_order(self):
        print(f"You ordered a {self.flavor} {self.topping} {self.dessert_type}!")

    @classmethod
    def greet(cls):
        print(f"{cls.greeting}")

customer_order = Order("vanilla", "fudge", "sundae")
customer_order.greet()
customer_order.display_order()
```

* 
```python
class Order:
    greeting = "Welcome to Icey's Ice Cream Shop! \nWhat would you like to order today?"

    def __init__(self, flavor, topping, dessert_type):
        self.flavor = flavor
        self.topping = topping
        self.dessert_type = dessert_type

    def display_order(self):
        print(f"You ordered a {self.flavor} {self.topping} {self.dessert_type}!")

    @staticmethod 
    def greet(cls):
        print(f"{cls.greeting}")

customer_order = Order("vanilla", "fudge", "sundae")
customer_order.greet()
customer_order.display_order()
```
* 
```python
class Order:
    greeting = "Welcome to Icey's Ice Cream Shop! \nWhat would you like to order today?"

    def __init__(self, flavor, topping, dessert_type):
        self.flavor = flavor
        self.topping = topping
        self.dessert_type = dessert_type

    def display_order(self):
        print(f"You ordered a {self.flavor} {self.topping} {self.dessert_type}!")

    @classmethod
    def greet(cls):
        print(f"{cls.greeting}")

    @staticmethod
    def compliment():
        print("That's a delicious Icey order!")

customer_order = Order("vanilla", "fudge", "sundae")
customer_order.greet()
customer_order.display_order()
customer_order.compliment()
```
##### !end-options

##### !answer
* 
```python
class Order:
    greeting = "Welcome to Icey's Ice Cream Shop! \nWhat would you like to order today?"

    def __init__(self, flavor, topping, dessert_type):
        self.flavor = flavor
        self.topping = topping
        self.dessert_type = dessert_type

    def display_order(self):
        print(f"You ordered a {self.flavor} {self.topping} {self.dessert_type}!")

    @classmethod
    def greet(cls):
        print(f"{cls.greeting}")

    @staticmethod
    def compliment():
        print("That's a delicious Icey order!")

customer_order = Order("vanilla", "fudge", "sundae")
customer_order.greet()
customer_order.display_order()
customer_order.compliment()
```
##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->
