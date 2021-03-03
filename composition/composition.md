# Composition

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?pid=18e3de8f-d85b-42e5-9f9d-acdf017fdebb&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

## Learning Goals

- Use attributes to create composition between two classes
- Define one-to-one and one-to-many composition relationships
- Use instance methods on objects composed inside other objects

## Vocabulary and Synonyms

| Vocab <div style="width:100px;">| Definition |Synonym|How to Use in a Sentence |
| ----- | ---------- |----|------------------------ |
| One-to-one | One composite object is associated with one component object  | has-one |On an e-commerce site, each order has a *one-to-one* relationship with each shipment (destination address, tracking number, etc). <br/> In a gradebook application, each student *has one* final grade. <br/> On a social media platform, each user *has one* profile picture|
| One-to-many | One composite object is associated with a collection of component objects. | has-many | In a gradebook application, one class *has many* students and *has many* assignments. <br/> On a social media platform, one user has a *one-to-many* relationship with posts.|

## Initializing Components as Attributes in the Constructor

It's common to set the attributes of a composite class to component instances provided by other code that uses our class. Python lets us assign to attributes directly. We can let all the components in our class be passed into the constructor of the composite class, and assign the attributes in the constructor itself.

Consider this example of a one-to-one composition relationship:

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

This works similarly even with a _list_ of instances, which expresses a one-to-many composition relationship:

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

## One-to-One and One-to-Many Composition Relationships

We just saw examples of one-to-one and one-to-many composition relationships.

A one-to-one relationship is a relationship in which a composite class has an attribute representing a single instance of a component class as in this example:

```python
class ExampleComponent:

    def __init__(self, name):
        self.name = name

class ExampleComposite:

    def __init__(self, name, component):
        self.name = name
        self.component = component
```

A one-to-many relationship is a relationship in which a composite class has an attribute representing a _list_ of instances of a component class as in this example:

```python
class ExampleComposite:

    def __init__(self, name, components):
        self.name = name
        self.components = components
```

Note that `components` is a list of `component` objects. As usual, we use good naming, here the plural `components`, to help us remember what we expect an attribute to contain.

## A Longer Example: Product, ShippingAddress, and ShoppingCart

Let's look at one more example of one-to-one and one-to-many composition relationships.

```python
class Product:
 
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def calculate_cost(self):
        return self.price * self.quantity

class ShippingAddress:

    def __init__(self, name, street_address, city, state, zip_code):
        self.name = name
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip_code = zip_code

class ShoppingCart:

    def __init__(self, products, shipping_address):
        self.products = products
        self.shipping_address = shipping_address

    def calculate_total_cost(self):
        total_price = 0.0

        for product in self.products:
            #----Refer to this line for Check for Understanding Question 2----
            total_price += product.calculate_cost()

        return total_price

    def summary(self):
        return f"{len(self.products)} products will be shipped to {self.shipping_address.name}."
```

```python
p1 = Product(5.00, 5)
p2 = Product(2.50, 13)
p3 = Product(77.99, 2)
products = [p1, p2, p3]

ravis_address = ShippingAddress(
    name="Ravi", 
    street_address="123 John St", 
    city="Seattle",
    state="WA",
    zip_code="98112"
    )

sc = ShoppingCart(products, ravis_address)

total_cost = sc.calculate_total_cost()

print(f"The total cost of the products in the shopping cart is ${total_cost}")
print(sc.summary())
```

This code produces the console output:

```
The total cost of the products in the shopping cart is $213.48
3 products will be shipped to Ravi.
```

## Check for Understanding

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: multiple-choice
* id: bcd60833-bf2b-442d-b5b2-05afd630944f
* title: Composition
<!-- * points: [1] (optional, the number of points for scoring as a checkpoint) -->
<!-- * topics: [python, pandas] (optional the topics for analyzing points) -->

##### !question

In the example above, `Product` is the

##### !end-question

##### !options

* Component Class
* Composite Class
* Child Class
* Parent Class

##### !end-options

##### !answer

* Component Class

##### !end-answer

<!-- other optional sections -->
<!-- !hint - !end-hint (markdown, hidden, students click to view) -->
<!-- !rubric - !end-rubric (markdown, instructors can see while scoring a checkpoint) -->
<!-- !explanation - !end-explanation (markdown, students can see after answering correctly) -->
##### !explanation

An instance of a `ShoppingCart` has many `Product`s. Since instances of `Product` are contained in `ShoppingCart`, `Product` is the component class, while `ShoppingCart` is the composite class.

##### !end-explanation


### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: multiple-choice
* id: cd47699d-3533-4d5d-990c-470cd0b254c4
* title: Composition
<!-- * points: [1] (optional, the number of points for scoring as a checkpoint) -->
<!-- * topics: [python, pandas] (optional the topics for analyzing points) -->

##### !question

In the example above, refer to the line of code below `#----Refer to this line for Check for Understanding Question 2----`. <br/> `calculate_cost()` is 

##### !end-question

##### !options

* An attribute of the `Product` class
* An attribute of the `ShoppingCart` class
* An instance method invoked on an instance of the `Product` class
* An instance method invoked on an instance of the `ShoppingCart` class

##### !end-options

##### !answer

* An instance method invoked on an instance of the `Product` class

##### !end-answer

<!-- other optional sections -->
<!-- !hint - !end-hint (markdown, hidden, students click to view) -->
<!-- !rubric - !end-rubric (markdown, instructors can see while scoring a checkpoint) -->
<!-- !explanation - !end-explanation (markdown, students can see after answering correctly) -->

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->



<!-- Question Takeaway -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: oMV7Ny
* title: Composition
##### !question

What was your biggest takeaway from this lesson? Feel free to answer in 1-2 sentences, draw a picture and describe it, or write a poem, an analogy, or a story.

##### !end-question
##### !placeholder

My biggest takeaway from this lesson is...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->
