# `super()`

## Learning Goals
- Use super() in inheritance

## Access the Superclass with `super()`
Python defines a function called `super()`!
Calling `super()` returns a temporary object of the parent class (also known as the superclass!). With this superclass, we can call all of the superclass's methods.

### When Would We Use `super()`
We will call `super()` any time that the superclass has an implementation of a method we want to use.
These situations are all contextual. Some example situations could be:

1. The parent class has already implemented a behavior, and the child class wants to do that and more
1. The relationship between the child class and parent class is such that the child should _always_ copy a behavior from the parent

## Examples
Imagine these two classes, where `Texter` is the child class, and `Adult` is the parent class.

```python
class Adult:
    def make_phone_call(self):
        print("I'm picking up the phone and dialing a number and using my voice!")

class Texter(Adult):
    def make_phone_call(self):
        print("I'm waiting four days")
        print("Now I'll forget to call them back")
        print("Now I'm just texting them instead")
    def make_emergency_phone_call(self):
        super().make_phone_call()
```

Imagine Terry, who is an avid texter. Whenever they are asked to call their friend, they instead wait a few days, forget to call them, and then eventually just send a text.

```python
terry = Texter()
terry.make_phone_call()
```
But what if Terry has an emergency? Terry probably shouldn't rely on their own way of making a phone call. Terry should probably _use a method defined in the superclass_, and call someone.

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