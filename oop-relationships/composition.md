# Composition

## Learning Goals

- Use attributes to create composition between two classes
- Use instance methods to access instances of objects composed inside another object

## Introduction


## Vocabulary and Synonyms

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---

## Composition Affects Our Attributes

This can manifest in code in a number of ways.

We could pass in an instance of the component class into the composite class's constructor, and assign it to an attribute:

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

<!-- Three reading code comp questions for this example, that's it -->
