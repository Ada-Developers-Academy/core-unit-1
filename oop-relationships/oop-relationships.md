# OOP Relationships

## Learning Goals

- Define Inheritance in OOP as an "is a" relationship: superclass, subclass
- Define Composition in OOP as a "has a" relationship

## Introduction

When multiple objects interact with each other, they form a relationship. Like any relationship, two classes having a relationship should spark many questions for us: What do the classes do together? How do they communicate with each other? What's the nature of their relationship? Is one class in charge? Are the two classes changing and modifying each other, or is it one-way? What happens if one class changes, and the other stays stagnant?

Because OOP is a paradigm that encourages forming relationships between these objects, OOP principles describe several types of these relationships. Two of these types of relationships are _inheritance_ and _composition_.

These relationships will affect _how_ we solve problems that involve more than one class. Eventually, these types of relationships get applied when following software design patterns.

## Vocabulary and Synonyms

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---

## Inheritance: Passing on Implementation

Sometimes, two classes are similar... but different. The two classes share the same attributes and the same methods... but one class has additional attributes, additional methods, and a different name. We could formalize a relationship between these two classes with inheritance.

Inheritance designates a **parent class** and a **child class**. Using inheritance, the _child class_ will "copy" the state and behavior defined in the _parent class_.

When a _child class_ tries to use an attribute or method that it doesn't define in its own class, it will look up to the _parent class_. If the parent class has that attribute or method defined, the child class will use that implementation.

Not only can child classes inherit state and behavior, they can also **override** them. A child class may need to have attributes or methods of the same name, but different implementation. When a child class re-defines an inherited property, the child class _overrides_ it. When overriding, the child class can optionally still look to the parent class's implementation.

### !callout-info

## Synonyms
We can refer to the parent class as a "super class." We can refer to the child class as a "sub class."

### !end-callout

### Example: Temmie, Karen, and Pizza

Let's roleplay a non-programming example!

Imagine a 10-year-old, Temmie, and her caregiver, Karen. It's Friday night, and the two of them have invited us over for dinner.

We can ask Karen to make a call and order pizza on the phone. When we do that, Karen will go to her room, find her phone on the desk, and then call Dino's Pizza Palace.

When we ask Temmie to make a call and order pizza on the phone, but Temmie doesn't know how to do that on her own. However, Temmie _inherits_ the properties and behaviors of her caregiver. Temmie has never bought her own phone, and she's never called a pizza place, but she can look up to how Karen does it. Temmie will go to her own room, look for her own phone on the desk, and then call Dino's Pizza Palace.

A week has passed, and we're back for more pizza dinner with Karen and Temmie. Temmie has learned about all of the different pizza places in the world. We can ask Temmie to call and order pizza on the phone. Temmie can _override_ the behavior she's inherited. This time, Temmie will go to her own room, look for her own phone on the desk, and then call _Pizza Planet_ instead. Karen's own behavior (and preference for Dino's) does not change.

Another week has passed, and it's time for pizza #3. This time, Temmie has learned so much more, and she can completely override how she orders pizza. Temmie might go to her room, look for her own phone on the desk, and then open up a food delivery app. Or, Temmie could completely forego this whole process, and go outside, walk to the nearby pizza joint, and get pizza that way. However, the important thing is that Temmie _knows_ that she even has an "order pizza" behavior. It's important that Temmie _knows_ that she _does_ own a phone.

### Example: Form Buttons

Let's consider a more realistic programming example.

Anders is developing a mobile app that lets him send money to the people around him. Anders found that the logic for making a button was complex. A button needs to be visible, it needs to be tappable. While the button is pressed, it should appear differently. After a button is tapped, it needs to kick off another event in the app. Anders took this behavior and created a `Button` class. He got to use this `Button` class to make dozens of buttons around his app.

However, when a user goes to send money, the button should only work if the user presses the button for longer than three seconds. Anders knows that this "send payment button" is a `Button`, but it operates just a _little_ differently than a regular `Button`. Anders doesn't want to make a `SendPaymentButton` class that duplicates the code from `Button`, because if `Button` changes, then he'd need to remember to update `SendPaymentButton`, too. Anders doesn't want to change the `Button` class for this very rare case.

Anders can create a `SendPaymentButton` class that _inherits_ `Button`. The `SendPaymentButton` class will inherit all of the state and behavior that a `Button` has, but it can _override_ the logic so that a user must hold the button.

### Inheritance is "Is-A" Relationship

We can often describe inheritance as an "is-a" relationship between two classes, where the child class "is a" parent class. This implies that inheritance affects how a class is defined.

### Everything Inherits From `object`

Python has a special class named `object`. `object` is a class that defines the methods `__init__`, `__str__`, and a dozen other things.

Python is designed so that every class and object eventually inherits from `object`. Following the rules of inheritance, we can see how every class has `__init__`, `__str__`, etc. defined-- these are _inherited methods_!

For more details on `object`, run `help(object)` in a Python repl!

## Composition: Expecting Instances to Hold onto Other Instances

Most of the time, a class has attributes, and those attributes are strings, numbers, lists, dictionaries, booleans, and so on. Sometimes, however, the value of an attribute is an instance of another class.

This relationship is called composition. Composition means that one class is expected to have objects of another class stored or referenced inside of it.

Composition between two classes describes a **composite** class and a **component** class. The _composite class_ contains at least one object of type _component class_.

Composition is interesting, because the _composite class_ is made that much more complex and interesting with the addition of a _component class_.

When a _composite class_ **has a** _component class_, the composite class can use that component class. The _composite class_ could possibly read attributes, modify attributes, and invoke methods from the _component class_.

Any time that one class knows about another class's attributes and methods, we programmers should recognize that the other class is being _exposed_. One class might carelessly read or modify attributes, or invoke methods, that aren't intended to be used. Every time a class exposes its properties, the programmer should consider the trust that is built between these two classes.

### Composition is a "Has-A" Relationship

We can describe composition as a **has-a** relationship, where the composite class "has a" component class. This implies that composition affects a class's state.

### Example: The Good Book Club and Bus Fares

Brooklyn is the organizer of a book club. The book club itself has many things, such as a name ("The Good Book Club") and location. The book club itself can do many things, too, such as schedule meetings. Also, the book club _has_ many members.

For The Good Book Club, Brooklyn sometimes needs to go through the members and send them emails about the next meeting, so it's good that she has a reference to all the members, and their names and email addresses.

However, one day, Brooklyn realized she left her wallet at home. A member of the book club, Cody, lent her money for the bus. That's when Brooklyn realized that Cody _has the ability to give money to her_. In fact, Brooklyn realized that _all members_ of the book club have the ability to lend money to her.

With this knowledge, Brooklyn could go up to each member and ask them to lend money to her.

Regardless if Brooklyn actually does that, the fact that Brooklyn knows that it's possible to do that through The Good Book Club is very telling. There is trust needed between The Good Book Club and the members it has.

### Example: Shopping Cart and Product

Angela is making an e-commerce web app that will allow users to shop for items and make orders.

Angela wants to mimic other e-commerce sites. Each user should be able to add products to a shopping cart. Then, when the user is finished, the user should checkout the shopping cart, which should charge the user the total amount of money owed.

Angela's made a `ShoppingCart` class. As she builds the `checkout` method, she needs to calculate the total cost. To do that, she wants to iterate through a list of products, and add their prices together.

However, `Product`s are complex objects, and they have their own class! Angela then wants to set up _composition_ between these two classes. The `ShoppingCart` is the _composite class_, and it will have an attribute named `products`. `products` will be a list of `Product` instances, and `Product` is the _component class_.

Now, inside the `checkout` method, `ShoppingCart` can iterate through `products` and access the `price` attribute of each `Product`.

## Relationships, Design Patterns, and Better Code

Inheritance and composition are just two types of relationships in OOP. There are many more ways that classes can interact with each other.

As classes interact with each other, code becomes more complex. By nature, inheritance and composition increase code complexity, and make once-separate parts of code depend on each other. On the flip side, inheritance and composition are also the basis of a few different design patterns, and can help solve problems in creative ways.

## Check for Understanding

<!-- Make up a scenario of inheritance, identify parent class, child class -->

<!-- A second one of those if we're creative enough -->

<!-- Make up a scenario of composition, identify composite class and component class -->

<!-- A second one of those if we're creative enough -->

<!-- Make up a scenario, MC on if it's inheritance, composition, or neither -->
