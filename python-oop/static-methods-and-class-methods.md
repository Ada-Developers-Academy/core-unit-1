# Static Methods and Class Methods

## Learning Goals

- Define static methods
- Recognize the syntax to build static methods
- Define class methods
- Recognize the syntax to build class methods

## Introduction

The most common kind of method defined in OOP is instance methods. These methods can only be called from an instance. Instance methods typically are used to describe behaviors that instances can do, and to update the state associated with one instance.

There are other kinds of methods that we can define within a class. These methods will not be called from an instance, and won't be responsible for maintaining an instance.

### !callout-info

## Class Variables? Instance Variables?

This lesson talks about instance variables and class variables. Instance variables are variables associated with an instance. In Python terms, they are variables stored on a `self` instance. We can also call them attributes. Class variables are variables that are defined inside the class definition, outside any instance method. We can access them with dot notation off the class: `ExampleClass.example_class_var`

```python
class ExampleClass:
    example_class_var = "This is an example class variable!"


print(ExampleClass.example_class_var)

ExampleClass.example_class_var = "I've successfully re-assigned the example class var!"

print(ExampleClass.example_class_var)
```

Class variables hold _class state_. Every individual class variable gets shared and applied among all instances of the class.

### !end-callout

## Vocabulary and Synonyms

| Vocab         | Definition                                                                                                                                      | Synonyms | How to Use in a Sentence                                                                                                                                    |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Static method | A method that does not depend on an instance, and does not access instance or class variables.                                                  | -        | "The method `meets_age_requirement(age)` will always do the same behavior, regardless of instance or class state, so we can make it a static method."       |
| Class method  | A method that has a reference to the class itself. This method does not depend on an instance, and cannot access instance variables or methods. | -        | "All `MovieTheater`s share the class state `is_open`. Our method `reopen_all_theaters` can be a class method that depends on the `is_open` class variable." |

## Static Methods are Stateless Methods from a Class

Static methods are methods that are typically called from a class, not an instance.

Additionally, static methods don't have access to instance variables (attributes) or class variables.

Because static methods don't have access to those variables, they tend to be unchanging in nature.

### !callout-info

## Programming Vocab!

The word "static" means "unchanging" and "fixed." The term "static" gets applied to many concepts where the programmer expects it to never change.

### !end-callout

## Static Methods: Syntax

To define a static method, we:

- use the `@staticmethod` decorator that the Python library provides
- do not pass in `self` as a parameter

```python
class ExampleClass:

    @staticmethod
    def example_method():
        print("I'm inside the static method, example_method!")
```

Once a static method is defined, we can invoke it using dot notation, typically from the class itself.

```python
ExampleClass.example_method()
```

This code produces the console output:

```
I'm inside the static method, example_method!
```

Any code that can reference the class can call a static method. This means that we can call a static method from another static method, class method, instance method, or even inside another class.

### Static Methods: Syntax Details

In Python, we actually _can_ call static methods from an object instance, not just a class. However, because we don't pass in `self`, we don't have a reference to `self`. Static methods do not depend on an instance.

Observe this code, which shows that we _can_ call static methods from an object instance, but we can't access `self`.

```python
class ExampleClass:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def example_method():
        print("I'm inside the static method, example_method!")
        print(f"I'm accessing an instance variable, {self.name}")
```

```python
example_instance = ExampleClass("Hello, World!")

example_instance.example_method()
```

This code produces the console output:

```
I'm inside the static method, example_method!
Traceback (most recent call last):
  File "main.py", line 13, in <module>
    example_instance.example_method()
  File "main.py", line 9, in example_method
    print(f"I'm accessing an instance variable, {self.name}")
NameError: name 'self' is not defined
```

We should observe from the output that:

- The code _did_ successfully begin the static method, and it _did_ print `I'm inside the static method, example_method!`
- The code threw a runtime error `NameError`, because we are unable to access `self`

## Static Methods: Application

Static methods are often utility functions. "Utility functions" is an informal term to describe a function responsible for doing common, routine tasks.

Static methods are great for:

- returning fixed values not associated with an instance
- doing operations that aren't associated with an instance

## Class Methods are Methods with Class State

Class methods are methods that are only called from a class, not an instance.

Class methods have access to class variables. However, they do _not_ have access to any instance variables.

## Class Methods: Syntax

To define a class method, we:

- use the `@classmethod` decorator that the Python library provides
- do not pass in `self` as a parameter
- pass in `cls` as a parameter

Instead of passing in `self`, the variable that represents an instance itself, in class methods, we pass in `cls`, a variable that represents the class itself.

`cls` is the conventional name for this parameter.

```python
class ExampleClass:

    @classmethod
    def example_method(cls):
        print("I'm inside the class method, example_method!")
        print("In a class method, cls will be the class itself", cls)
```

Once a static method is defined, we can invoke it using dot notation, typically from the class itself.

```python
ExampleClass.example_method()
```

This code produces the console output:

```
I'm inside the class method, example_method!
In a class method, cls will be the class itself <class '__main__.ExampleClass'>
```

Any code that can reference the class can call a class method. Similar to static methods, we can call a class method from other static, class, or instance methods, or even inside another class.

### Class Methods: Syntax Details

We actually _can_ call class methods from an object instance, too. However, the `@classmethod` decorator will specify that the first parameter, `cls`, will _always_ have the value of the class itself.

Even if we call a class method from an instance, we will not have access to the instance it`self`.

Observe this code, which shows that `cls` is still the value of the class, no matter what invokes the class method.

```python
class ExampleClass:

    @classmethod
    def example_method(cls):
        print("I'm inside the class method, example_method!")
        print("In a class method, cls will be the class itself", cls)
```

```python
example_instance = ExampleClass()
example_instance.example_method()
```

Output:

```
I'm inside the class method, example_method!
In a class method, cls will be the class itself <class '__main__.ExampleClass'>
```

We should observe from the output that:

- The code successfully ran the class method, even though it was invoked with `example_instance.example_method()`
- When we printed `cls`, it continued to be `<class '__main__.ExampleClass'>`

### Using `cls` to Access Class Variables

As mentioned above, class methods can access any class variables that are defined, using the `cls` variable:

```python
class ExampleClass:
    example_class_var = "This is an example class variable!"

    @classmethod
    def example_method(cls):
        print("I'm inside the class method, example_method!")
        print("I can access class variables using the cls parameter:", cls.example_class_var)
```

```
ExampleClass.example_method()
```

This code produces the console output:

```
I'm inside the class method, example_method!
I can access class variables using the cls parameter: This is an example class variable!
```

Of course, class variables can be accessed without the `cls` parameter, as long as there's access to the class itself. The following version of `ExampleClass` produces the same output as the previous version:

```python
class ExampleClass:
    example_class_var = "This is an example class variable!"

    @classmethod
    def example_method(cls):
        print("I'm inside the class method, example_method!")
        print("I can access class variables using the cls parameter:", ExampleClass.example_class_var)
```

The difference is that `cls` will _always_ represent the current class itself; specifying `ExampleClass` could have consequences if class definitions change.

## Class Methods: Application

Class methods are special because they have access to class variables, and class state.

Class methods are great for:

- modifying class state that applies across all instances of the class
- doing operations that aren't associated with an instance
- doing operations that rely on the class itself, such as making instances of that class

## Check for Understanding

<!-- Use the static method decorator to create a static method that... -->
<!-- Use the class method decorator to create a static method that... -->
