# super()

## Learning Goals
- Use super() in inheritance

## Inheritance and constructors
Zelda is making an app for Ada's Candy Shop. Zelda is especially focused on designing chocolates at the moment. To keep track of all the chocolates in the store, Zelda creates a `Chocolate` class that derives from the `Candy` class. Just as there are several types of Candy, there are also several different types of chocolates that deserve their own distinction. 

With that in mind, Zelda will need create several instances of the `Chocolate` class. Because each instance of a chocolate varies in flavors and ingredients, __instance variables__ will need to be utilized.

Recall that every time we need a class to have instance variables, that class will need to create a constructor!

```Python
class Candy:
    def __init__(self, name, price, grams_of_sugar):
        self.name = name
        self.price = price
        self.grams_of_sugar = grams_of_sugar

    def display_candy_cat(self):
        print(" = ^____^ = ")

class Chocolate(Candy):
    def __init__(self, name, price, grams_of_sugar, ingredients):
        self.ingredients = ingredients

    def display_ingredients(self):
        for ingredient in self.ingredients:
            print(ingredient)
```

## Inheritiance

At the moment we can access all of Candy's members (constructor, instance variables and instance methods). However, if we extend our code in the future to allow for multiple inheritance, we'll need to refactor.

Good code keeps forward compatability in mind. In the future, you may want Chocolate to inherit from multiple classes. A general good practice in Python, is to use the `super` method. The `super` method ensures that child classes will call the correct parent class function via the Method Resolution order (MRO).

## Access the Superclass with `super()`

Super()` returns a temporary object of the parent class (also known as the superclass!). `super` provides access to the superclass's methods.

### When Would We Use `super()`?

We will call `super()` any time we define a child class that needs to inherit behaviors from it parent. 

## Examples
Imagine these two classes, where `Texter` is the child class, and `Adult` is the parent class.

```python
class Candy:
    def __init__(self, name, price, grams_of_sugar):
        self.name = name
        self.price = price
        self.grams_of_sugar = grams_of_sugar

    def display_candy_cat(self):
        print(" = ^____^ = ")

class Chocolate(Candy):
    def __init__(self, name, price, grams_of_sugar, ingredients):
        super.__init__(name, price, grams_of_sugar)
        self.ingredients = ingredients
        

    def display_ingredients(self):
        for ingredient in self.ingredients:
            print(ingredient)
```


## Not Covered: Multiple Inheritance

Many programming languages decree that each class shall inherit implementation from only one other class; each class only has one parent class. Python supports multiple inheritance, or the ability for a class to inherit from more than one parent class. This concept has many possible uses, but learning to apply it effectively is not a task to be undertaken lightly. As a result, we will not be spending time with multiple inheritance in this curriculum. But it can be a fascinating topic for further self-directed study.

As always, follow your curiosity!

## Check for Understanding
<!-- Question Takeaway -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: 2IraCr
* title: Inheritance
##### !question
What was your biggest takeaway from this lesson? Feel free to answer in 1-2 sentences, draw a picture and describe it, or write a poem, an analogy, or a story.
##### !end-question
##### !placeholder
My biggest takeaway from this lesson is...
##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->