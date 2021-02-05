# Composition

## Learning Goals

- Use attributes to create composition between two classes
- Use instance methods to access instances of objects composed inside another object

## Initializing Components as Attributes in the Constructor

It's common to set the attributes of a composite class to component instances provided by other code that uses our class. Python lets us assign to attributes directly. We can let all the components in our class be passed into the constructor of the composite class, and assign the attributes in the constructor itself.

Consider this example:

```python
class ExampleComponent:

    def __init__(self, name):
        self.name = name

class ExampleComposite:

    def __init__(self, name, component):
        self.name = name
        self.my_favorite_component = component
```

```python
apple = ExampleComponent("apple")

orange = ExampleComposite("orange", apple)

print("Orange has an attr named my_favorite_component:", orange.my_favorite_component)
print("We can read the name from Orange's fav component using dot notation:", orange.my_favorite_component.name)
```

This code produces this console output:

```
Orange has an attr named my_favorite_component: <__main__.ExampleComponent object at 0x10ee8b8e0>
We can read the name from Orange's fav component using dot notation: apple
```

This works similarly even with a list of instances:

```python
class ExampleComponent:

    def __init__(self, name):
        self.name = name


class ExampleComposite:

    def __init__(self, name, components):
        self.name = name
        self.components = components
```

```python
apple = ExampleComponent("apple")
banana = ExampleComponent("banana")
mango = ExampleComponent("mango")

orange = ExampleComposite("orange", [apple, banana, mango])

print("Orange has an attr named components:", orange.components)
print("We can read the name from Orange's components:")

for fruit in orange.components:
    print(fruit.name)
```

This code produces this output:

```
Orange has an attr named components: [<__main__.ExampleComponent object at 0x10ecf08e0>, <__main__.ExampleComponent object at 0x10ecb10d0>, <__main__.ExampleComponent object at 0x10ec20820>]
We can read the name from Orange's components:
apple
banana
mango
```

## Composition Lets Us Read Component Properties

Outside of the constructor, we can read those instances at any point in the composite class, such as instance methods. We can read attributes and invoke methods from the component class, too.

```python
import random

class ExampleComponent:

    def __init__(self, name):
        self.name = name

    def get_random_num(self):
        print("***************************************************")
        print("I'm inside Component's instance method get_random_num")
        random_num = random.randint(0, 999)
        print("Now, I'm going to leave Component's instance method")
        print("***************************************************")
        return random_num

class ExampleComposite:

    def __init__(self, name, component):
        self.name = name
        self.component = component

    def read_fruits(self):
        print("I'm inside Composite's instance method read_fruits")
        print("I can read self.component here:", self.component)
        print("Now, I'm going to call self.component's instance method")

        result_from_component = self.component.get_random_num()

        print("This is what Component's method returned:", result_from_component)
```

```python
mango = ExampleComponent("mango")
orange = ExampleComposite("orange", mango)

orange.read_fruits()
```

We should observe:

- `ExampleComposite`...

  - has an attribute `component`
  - has an instance method `read_fruits`. Inside `read_fruits`:
    - we print that we're inside it, and we read the `component` attr
    - we call the `component` attr's instance method, `get_random_num` **with the line `self.component.get_random_num()`**
    - we print the return value from that instance method

- `ExampleComponent`...
  - has an instance method `get_random_num`. Inside `get_random_num`:
    - we print that we're inside it
    - we produce and return a random number

This code can produce the console output:

```
I'm inside Composite's instance method read_fruits
I can read self.component here: <__main__.ExampleComponent object at 0x10b7c8ac0>
Now, I'm going to call self.component's instance method
***************************************************
I'm inside Component's instance method get_random_num
Now, I'm going to leave Component's instance method
***************************************************
This is what Component's method returned: 473
```

## A Longer Example: Product and ShoppingCart

```python
class Product:

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def calculate_cost(self):
        return self.price * self.quantity

class ShoppingCart:

    def __init__(self, products):
        self.products = products

    def calculate_total_cost(self):
        total_price = 0.0

        for product in self.products:
            total_price += product.calculate_cost()

        return total_price
```

```python
p1 = Product(5.00, 5)
p2 = Product(2.50, 13)
p3 = Product(77.99, 2)
products = [p1, p2, p3]

sc = ShoppingCart(products)

total_cost = sc.calculate_total_cost()

print(f"The total cost of the products in the shopping cart is ${total_cost}")
```

This code produces the console output:

```
The total cost of the products in the shopping cart is $213.48
```

## Check for Understanding

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: acd9c2f0-3dfb-4c76-a5b1-fcf8af7522cc
* title: Composition
##### !question
Moana just moved to Europe and is having trouble converting to the metric system. To cope, she is creating an Alexa skill to convert metric measurements to imperial measurements.

Provided is her code so far. Select the option that best describes the relationship between `Temperature` and `MetricConverter`.

```python
class Temperature:
  def __init__(self, celsius):
    self.celsius = celsius
    self.metric_converter = Metric_Converter(self.celsius)

  def display_temperature(self):
    return "It is " + str(self.metric_converter.convert_to_fahrenheit()) + " degrees Fahrenheit today."

class MetricConverter:
    def __init__(self, celsius):
      self.celsius = celsius

    def convert_to_fahrenheit(self):
      return (int(self.celsius * (9/5) + 32))

today = Temperature(37)
print(today.display_temperature())
```
##### !end-question
##### !options
* `Temperature` is the component class. `MetricConverter` is the composite.
* `Temperature` is the composite class.`MetricConverter` is the component.
##### !end-options
##### !answer
* `Temperature` is the composite class.`MetricConverter` is the component.
##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: 00c359fc-58a7-4c95-94ac-3c718ed43e0a
* title: Composition

##### !question
Composition can be initiated by a single line of code. In this code snippet, which line is responsible for starting the relationship between `Bedroom` and `Area`?

```python
1   class Room:
2
3       def __init__(self, width, length):
4           self.width = width
5           self.length = length
6           self.area = Area(self.width, self.length)
7
8       def display_room_details(self):
9           return "This room is " + str(self.area.calculate_area()) + " sq.ft."
10
11
12  class Area:
13
14      def __init__(self, width, length):
15          self.width = width
16          self.length = length
17
18      def calculate_area(self):
19          return self.width * self.length
20
21
22  bedroom = Room(20, 20)
23  print(bedroom.display_room_details())
```
##### !end-question

##### !options
* 6
* 12
* 22
##### !end-options

##### !answer
* 6
##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->
