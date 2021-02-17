# Instance Methods

## Learning Goals

- Define instance methods
- Practice building classes with instance methods

## Instance Methods Are Behaviors Instances Can Do

Class definitions can contain functions. When a function is inside of a class, we call those functions **methods.**

**Instance methods** are behaviors that _instances_ of classes can do.

| Class  | Instances                                                                                                                 | Behavior It Can Do                                                           | Method Name |
| ------ | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| String | `"Hello World! I am an instance of a String!"`                                                                            | Become CAPITALIZED if it needs to                                            | upper()   |
| List   | `["red", "orange", "yellow"]`                                                                                             | Reverse the order of its elements                                            | reverse() |
| Driver | A driver with ID `DR0004`, 3 trips, who has earned $35, has an average rating of 4.67                                     | Calculate its own average rating, tell you the number of trips they've taken | stats()  |
| Album  | Dirty Computer (2018), which has 14 tracks in a certain order, was released April 2018, has a total album length of 48:42 | Return the audio data for any specific track it has                          |  get_audio_data()

## Defining Instance Methods

Instance methods are defined with similar syntax to other functions. But to be an instance method, they must appear inside a class definition, and just like the `__init__` method, the first parameter listed **must** be `self`.

```python
class ExampleClassName:

    def example_instance_method(self):
        pass
```

- We can `return` a value
- We can add as many parameters we want after `self`
- Inside of this method, we can access attributes and _other_ methods of the instance, using `self`
- We can do any other typical Python logic in here, such as loops, conditionals, etc.

### !callout-info

## `self` Must Be The First Parameter

Just like the `__init__` method, the first parameter listed **must** be `self`.

### !end-callout

Observe these examples for an `Album` class. The examples increase in complexity.

```python
class Album:

    def get_audio_data(self):
        return "Prince - When Doves Cry (5:54) (Track 1) (Genre: Pop, rock, R&B, psychedelia)"
```

In the above example, every instance of `Album` has the instance method `get_audio_data`. Calling this method will always return `"Prince - When Doves Cry (5:54) (Track 1) (Genre: Pop, rock, R&B, psychedelia)"`.

```python
class Album:

    def __init__(self, title, release_date, tracks):
        self.title = title
        self.release_date = release_date
        self.track_list = tracks

    def get_audio_data(self):
        return self.track_list
```

In the above example, the instance method `get_audio_data` reads the attribute `track_list`. It reads and returns this attribute with `return self.track_list`. It will return whatever the value of `self.track_list` is, which was defined in the `__init__` method. It was assigned the value passed in as the `tracks` parameter.

```python
class Album:

    def __init__(self, title, release_date, tracks):
        self.title = title
        self.release_date = release_date
        self.track_list = tracks

    def get_audio_data(self, track_index):
        if 0 < track_index <= len(self.track_list):
            return self.track_list[track_index - 1]
        else:
            return "Invalid track"
```

In the above example, the instance method `get_audio_data` takes an additional parameter `track_index`. This means that whenever we call this method, we must pass in an argument for `track_list`. `track_list` represents the index track we want audio data from.

Inside the `get_audio_data` method, we use the attribute `self.track_list` _**and**_ the argument `track_index`. We assume `self.track_list` is a list, and we use it in a conditional statement. We use `track_index` in the line `return self.track_list[track_index - 1]`.

### !callout-info

## Instances of a Class do not share State but they do share Behavior

As we've been learning, the two building-blocks of a class are **state** (ie. its attributes) and **behavior** (ie. its methods). 

Like we saw in the [Creating Instances lesson](creating-instances.md), **each instance of a Class has its own state**. This means that one album object can have the title "When Doves Cry" and another album object have the title "Dirty Computer". 

We will see now that **all instances of a class have the same behavior**. This means that the method `get_audio_data` will be the same for all album objects. The only thing that will change from one instance to another is the value of the `track_list` attribute.

### !end-callout

<!-- Question 1 -->

<!-- prettier-ignore-start -->
### !challenge

* type: code-snippet
* language: python3.6
* id: UG0Oiq
* title: Defining Instance Methods

##### !question

Use this `Driver` class, and do not create a constructor. Create an instance method named `get_number_of_trips`. This method should not take any additional parameters besides the required ones, and it should always return `5`.

##### !end-question

##### !placeholder

```py
class Driver:
    pass
```

##### !end-placeholder

##### !tests

```py
import unittest
from main import *

class TestDriverClass(unittest.TestCase):
  def test_driver_has_five_trips(self):
    speed_racer = Driver()
    self.assertIs(speed_racer.get_number_of_trips(), 5)
```

##### !end-tests

##### !explanation

An implementation that works is this:

```python
class Driver:
    
    def get_number_of_trips(self):
        return 5
```

##### !end-explanation

### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->

<!-- prettier-ignore-start -->
### !challenge

* type: code-snippet
* language: python3.6
* id: ZPeS72
* title: Defining Instance Methods

##### !question

Create a `Driver` class that meets these specifications:

- The constructor should expect one parameter, which will be a record of trips
- The constructor should assign a value to an attribute that will hold the record of trips
    - We can assume that the attribute is a list
- There should be an instance method named `get_number_of_trips`
    - Return the length of the list of trips

##### !end-question

##### !placeholder

```py
class Driver:
    pass
```

##### !end-placeholder

##### !tests

```py
import unittest
from main import *

class TestDriverClass(unittest.TestCase):
  def test_driver_has_five_trips(self):
    speed_racer = Driver([])
    self.assertIs(speed_racer.get_number_of_trips(), 0)
    racer_x = Driver(["trip 1", "trip 2", "trip 3", "trip 4"])
    self.assertIs(racer_x.get_number_of_trips(), 4)
```

##### !end-tests

##### !explanation

An implementation that works is this:

```python
class Driver:
    
    def __init__(self, trips):
        self.trips = trips

    def get_number_of_trips(self):
        return len(self.trips)
```

##### !end-explanation

### !end-challenge
<!-- prettier-ignore-end -->

## Calling Instance Methods

To call an instance method, we **must** first have a reference to an instance of the class.

Then, we use the dot operator between the instance and the method call.

```python
name_of_instance.name_of_instance_method()
```

When we call an instance method, we never specify that the first parameter is `self`. Python recognizes that instance methods will always need to pass in the instance as `self` whenever we call an instance method... _Python only needs us to specify `self` when defining the method._

### Calling Instance Methods Inside a Class Definition

Inside of a class definition, our reference to an instance is usually through `self`.

In this example, `Album` has two instance methods: `get_genre` and `get_audio_data`. Observe that in `get_audio_data`, it calls the method `get_genre` through `self`.

```python
class Album:

    def __init__(self, tracks):
        self.tracks = tracks

    def get_genre(self):
        return "Pop, rock, R&B, psychedelia"

    def get_audio_data(self, track_index):
        genre = self.get_genre()
        audio_data = f"Prince - When Doves Cry (5:54) (Track 1) (Genre: {genre})"
        return audio_data
```

Notice that when we called the `get_genre` method, we didn't need to pass in any arguments. Even though the `get_genre` method requires `self` as the first argument, _Python does not need us to specify `self` when calling the method._

Inside of the `get_audio_data`, we leverage all of the other Python knowledge we have: we use return values, local variables, and string formatting.

<!-- Question 3 -->

<!-- prettier-ignore-start -->
### !challenge

* type: code-snippet
* language: python3.6
* id: JErqxs
* title: Calling Instance Methods Inside a Class Definition

##### !question

Modify the supplied `Driver` class:

- Modify the line `avg_rating = total_rating / 1` inside of `get_avg_rating`
- This line should make use of the method `get_number_of_trips` so that it properly calculates the average trip rating.

##### !end-question

##### !placeholder

```py
class Driver:
    
    def __init__(self, trips):
        self.trips = trips

    def get_number_of_trips(self):
        return len(self.trips)
    
    def get_avg_rating(self):
        total_rating = 0
        for trip_rating in self.trips:
            total_rating += trip_rating

        avg_rating = total_rating / 1
        return avg_rating
```

##### !end-placeholder

##### !tests

```py
import unittest
from main import *

class TestDriverClass(unittest.TestCase):
  def test_driver_get_avg_rating(self):
    speed_racer = Driver([4, 4, 4])
    self.assertAlmostEqual(speed_racer.get_avg_rating(), 4.0)
    racer_x = Driver([1, 2, 3, 4, 5])
    self.assertAlmostEqual(racer_x.get_avg_rating(), 3.0)
```

##### !end-tests

##### !explanation

An implementation that works is this:

```python
class Driver:
    
    def __init__(self, trips):
        self.trips = trips

    def get_number_of_trips(self):
        return len(self.trips)
    
    def get_avg_rating(self):
        total_rating = 0
        for trip_rating in self.trips:
            total_rating += trip_rating

        avg_rating = total_rating / self.get_number_of_trips()
        return avg_rating
```

##### !end-explanation

### !end-challenge
<!-- prettier-ignore-end -->

### Calling Instance Methods Outside a Class Definition

Outside of a class definition, our reference to an instance is often through a variable that was set after making the instance.

We'll also see the instance being passed into other functions, or being stored in other objects as well. In those cases, we access the instance through the relevant parameter, or an attribute on some other object. The way we call instance methods on the object is the same for all those cases.

This example creates two `Album` instances, storing each in their own variable. After storing the instances, we use the dot operator on each variable to call the method `get_genre` on each instance.

```python
purple_rain = Album()
purple_rain.get_genre()

dirty_computer = Album()
dirty_computer.get_genre()
```

In the above example, we assume that both the constructor and `get_genre` were defined with no parameters besides `self`.

This example creates two `Album` instances with their own track lists, storing each in their own variable. After storing the instances, we use the dot operator on each variable to call the method `get_audio_data` on each instance, passing in the track number for which to get the data.

```python
purple_rain = Album(["When Doves Cry"])
purple_rain.get_audio_data(1)

dirty_computer = Album(["Dirty Computer", "Take a Byte"])
dirty_computer.get_audio_data(2)
```

In the above example, we assume that the constructor accepts a list of track data, and `get_audio_data` accepts a track number, in addition to the required `self` parameter.

## Tracing Code Through Instance Methods

It's important to practice tracing code when working with OOP, just as it is with any other programming paradigm. When we trace code, we pick a line of code to start from, and assume some current program state. Then we execute each line ourselves as Python would, and follow the path to see what other code gets called.

Having somewhere to take notes about how the state changes can be very helpful!

If we come across code that looks like this, we ask "What is happening when this method gets called?"

```python
name_of_instance.name_of_instance_method()
```

To answer that question, we might follow certain steps to trace code:

- What do we know about _what_ calls the method?
  - What is to the left of the `.` (dot operator)?
  - Is it an instance of a class?
  - What class is it an instance of?
    - Where is this class defined?
- What do we know about the method being called?
  - What is to the right of the `.` (dot operator)?
  - Is it a method being invoked, with `()` at the end?
  - Where is this method defined? Is it inside the class definition?

Once we've determined where the method is defined, we can trace the code into that method definition.

For example, let's consider debugging this:

```python
purple_rain.get_audio_data(1)
```

We might think:

1. `purple_rain` is an instance of what class?
   - `Album`
1. Where is the definition for `Album`?
1. Inside the definition of album, is there a method named `get_audio_data`?
1. Where is the definition for `get_audio_data`?
   - What arguments does it take in?

These answers should lead us to the `get_audio_data` method inside of the `Album` class.

## Debugging OOP and Instance Methods

Recall that every instance keeps track of the values of their own attributes.

The debugger tool gives us great insight into the attributes of any instance. We can inspect each instance to see the current value of any object attribute. We can also use the debugger to step into instance methods, just as we can step into regular functions. This can help us understand the operation of a complex piece of code more quickly!

<!-- insert image and details relevant to the image ;_; -->
<!-- TODO: insert more text lol -->

<!-- No CFU; this lesson has several questions throughout the lesson -->
