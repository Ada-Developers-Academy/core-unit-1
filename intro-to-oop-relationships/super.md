# super()

## Learning Goals

- Use super() in inheritance

## Inheritance

Zelda is making an app for Ada's Candy Shop. Zelda is especially focused on designing [chocolate truffles](https://en.wikipedia.org/wiki/Chocolate_truffle) at the moment.

Truffles are a kind of candy, so they should have all the attributes and behaviors of any other kind of candy. In addition, truffles have their own particular characteristics. They have an outer coating that could be one of a variety of chocolate types. They have a filling, such as a ganache, or fruit mousse. They may have additional toppings as well.

To keep track of all the truffle variations in the store, Zelda creates a `Truffle` class that derives from the `Candy` class. She would like her `Truffle` class to inherit all the properties and behaviors of the `Candy` class. She would also like to be able to store information about the coating, the filling, and the topping.

To store the information that is specific to a `Truffle` instance, Zelda will add **instance variables** to her `Truffle` class definition. And since we generally initialize our instance variables in the constructor, this means that she will need to add a constructor to her `Truffle` class.

Zelda starts with the following class definitions.

```python
class Candy:
    def __init__(self, name, price, grams_of_sugar):
        self.name = name
        self.price = price
        self.grams_of_sugar = grams_of_sugar

    def build_description(self):
        return f"{self.name}: ${self.price} ({self.grams_of_sugar}g)"

    def eat(self):
        print("Yum!")

class Truffle(Candy):
    def __init__(self, name, price, grams_of_sugar, coating, filling, topping):
        self.coating = coating
        self.filling = filling
        self.topping = topping

    def build_description(self):
        return f"{self.coating}-coated {self.filling}, topped with {self.topping}"
```

Zelda tests out the `Candy` class.

```python
c = Candy("taffy", .05, 20)
print(c.build_description())  # prints 'taffy: $0.05 (20g)'
c.eat()  # prints 'Yum!'
```

Looks great!

She moves on to the `Truffle` class.

```python
t = Truffle("truffle", 5, 100, "dark chocolate", "raspberry mousse", "chocolate drizzle")
print(t.build_description())  # prints 'dark chocolate-coated raspberry mousse, topped with chocolate drizzle'
t.eat()  # prints 'Yum!'
```

She's mostly pleased with this, but she'd like the `Candy` description to be included in the `Truffle` description. But worse, when she tries:

```python
print(t.name)
```

she gets `AttributeError: 'Truffle' object has no attribute 'name'`. But how can this be? She derived `Truffle` from `Candy`. Shouldn't it have picked up the attributes from `Candy` the same way it picked up the `eat` method? And how can she access `Candy`'s version of `build_description` from `Truffle`?

## Inheritance and Constructors

If we derive a class like `Truffle` from a parent class like `Candy`, as long as `Truffle` has no explicit constructor, then when we create a new instance of `Truffle` Python looks for a `__init__` in the parent class. It runs the parent class (`Candy`) constructor, which adds any attributes defined in that constructor into our `self` class instance.

But if `Truffle` defines its own constructor, as it does here, Python finds the `Truffle` constructor and stops looking for any others. So only the `Truffle` constructor is called. It adds the `Truffle` attributes to the `self` class instance, but since the `Candy` constructor hasn't been called, those attributes are missing. That's why trying to access the `name` attribute on our `Truffle` instance caused an `AttributeError`.

Somehow, we need to tell Python to call the `Candy` constructor from the `Truffle` constructor. This sounds very similar to needing to call the `Candy` version of `build_description` from the `Truffle` version.

In fact, the solution to both situations is the same!

## Access the Superclass With `super()`

We can call `super()` to get a temporary object that can be used to lookup methods in the parent class inheritance chain (the parent class is also called a superclass). Python starts this lookup process one level higher than the current class definition.

So if Zelda modifies her `Truffle` constructor as follows:

```python
class Truffle(Candy):
    def __init__(self, name, price, grams_of_sugar, coating, filling, topping):
        super().__init__(name, price, grams_of_sugar)  # new addition
        self.coating = coating
        self.filling = filling
        self.topping = topping
```

This tells Python to look for a `__init__` method (a constructor) in the superclass inheritance hierarchy. It will find the constructor in `Candy`, to which we can pass the subset of parameters that `Truffle`'s constructor received that `Candy` needs for its constructor.

We need to explicitly pass those parameters ourselves. Python won't automatically "forward" the constructor parameters for us.

Zelda makes this change and is happy to see that:

```python
t = Truffle("truffle", 5, 100, "dark chocolate", "raspberry mousse", "chocolate drizzle")
print(t.name)  # prints 'truffle'
```

no longer causes an `AttributeError`.

Zelda would still like to use the string that `Candy`'s `build_description` method builds inside `Truffle`'s logic. Seeing how Zelda used `super()` in the constructor, how might she modify `build_description` in `Truffle`?

<br/>

<details>
  <summary>
    Try modifying <code>Truffle</code>'s <code>build_description</code> yourself, then review Zelda's approach.
  </summary>

Zelda wants to have the description for a `Truffle` use the `Candy` logic for its first line, then the truffle-specific description on the second line. She knows that she can use `super()` to get at the version of `build_description` in `Truffle`'s superclass, `Candy`. She modifies the method as follows:

```python
    # in Truffle's class definition
    def build_description(self):
        first_line = super().build_description()
        second_line = f"{self.coating}-coated {self.filling}, topped with {self.topping}"
        return f"{first_line}\n{second_line}"
```

</details>

After modifying `Truffle`'s `build_description` and running the following code:

```python
t = Truffle("truffle", 5, 100, "dark chocolate", "raspberry mousse", "chocolate drizzle")
print(t.build_description())
```

Zelda is happy to see this output:

```
truffle: $5 (100g)
dark chocolate-coated raspberry mousse, topped with chocolate drizzle
```

### When Do We Use `super()`?

We call `super()` any time we need to use behavior defined in a superclass from a child class, but the child class has a method with the same name. The most common situation this occurs for is the constructor, since all classes name their constructor `__init__`. But this can happen for other methods too, as we saw for `build_description`.

We _don't_ need to call `super()` if the superclass method we want to call isn't hidden by a method having the same name in the child class. For instance, we did _not_ need to add an `eat` method to `Truffle` and then call the superclass version with `super()`. `Truffle` made no changes to `eat`, so didn't provide an **overridden** version of `eat`, and so the first version of `eat` that Python would find is the one defined in the `Candy` class.

## Check for Understanding

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- prettier-ignore-start -->

### !challenge

* type: multiple-choice
* id: 43ff8d17-0d07-4581-8ba5-3b0fa5381b0c
* title: super()

##### !question

Given the following classes:

```python
class A:
    def __init__(self, apples):
        self.apples = apples

class B(A):
    def __init__(self, apples, oranges):
        # mystery line
        self.oranges = oranges

b = B(1, 2)
print(b.apples)  # prints 1
```

What choice best replaces `# mystery line`?

##### !end-question

##### !options

* `super.__init__(apples)`
* `super().__init__(apples, oranges)`
* `self.__init__(apples)`
* `super().__init__(apples)`
* `super().__init__()`
* `self.apples = apples`

##### !end-options

##### !answer

* `super().__init__(apples)`

##### !end-answer

##### !explanation

* `super.__init__(apples)`: `super` is a function so we need to call it with `()`.
* `super().__init__(apples, oranges)`: The constructor in class `A` takes a single parameter, but this passes two.
* `self.__init__(apples)`: This would attempt to call class `B`'s constructor, which would lead to an endless loop. But first, the call would fail, because `B`'s constructor needs two parameters.
* `super().__init__(apples)`: This correctly calls `A`'s constructor passing the one parameter it needs.
* `super().__init__()`: The constructor in class `A` takes a single parameter, but none are passed.
* `self.apples = apples`: This _would_ create an attribute called `apples` in the `B` instance, but if `A`'s constructor performed any other operations or was modified, we would need to update `B`'s constructor to keep it in synch. Calling `A`'s constructor directly will help maintain the expected parent-child relationship between these classes.

##### !end-explanation

### !end-challenge

<!-- prettier-ignore-end -->

<!-- ======================= END CHALLENGE ======================= -->

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- prettier-ignore-start -->

### !challenge

* type: multiple-choice
* id: c30d6a91-8a53-44d9-b513-44b84a388c1c
* title: super()

##### !question

Given the following classes:

```python
class A:
    def wait(self):
        print("waiting...")

class B(A):
    def run(self):
        # mystery line
        print("running...")

b = B()
b.run()
# prints
# waiting...
# running...
```

What choice best replaces `# mystery line`?

##### !end-question

##### !options

* `super().wait()`
* `self.wait()`
* `self.run()`
* `super().run()`

##### !end-options

##### !answer

* `self.wait()`

##### !end-answer

##### !explanation

* `super().wait()`: This works, but using `super()` here is unnecessary.
* `self.wait()`: Since `wait` isn't defined in class `B`, Python will look for it in the superclass hierarchy. It will find the version in class `A` and use that. `super()` isn't needed here.
* `self.run()`: This calls `B`'s `run` method endlessly, until Python terminates with an error.
* `super().run()`: `run` isn't defined in class `A`, so this will terminate with an error.

##### !end-explanation

### !end-challenge

<!-- prettier-ignore-end -->

<!-- ======================= END CHALLENGE ======================= -->

<!-- Question Takeaway -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: 2IraCr
* title: super()
##### !question
What was your biggest takeaway from this lesson? Feel free to answer in 1-2 sentences, draw a picture and describe it, or write a poem, an analogy, or a story.
##### !end-question
##### !placeholder
My biggest takeaway from this lesson is...
##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->
