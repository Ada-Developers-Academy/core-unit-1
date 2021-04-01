# Problem Set: Intro to OOP

## Directions

Complete all questions below.

## Defining Small Classes

<!-- Two questions -->

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge
* type: checkbox
* id: 8b51d66f-7eb6-49fb-b396-7f1787511dfa
* title: Intro to OOP
##### !question
Which option contains the correct syntax to define a class?
##### !end-question
##### !options
* 
```python
class Dog
    pass
```
* 
```python
class Dog:
    pass
```
##### !end-options
##### !answer
* 
```python
class Dog:
    pass
```
##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: cb8a0a95-23c9-40ec-a7aa-c6d5d7c2f3f2
* title: Intro to OOP
##### !question
Define a class named "Member". In the class body, use `pass` to create an "empty" class.
##### !end-question
##### !tests
```py
import unittest
from main import *

class TestMemberClass(unittest.TestCase):
  def test_member_is_defined(self):
    self.assertTrue(Member())
```
##### !end-tests
##### !explanation
An example of a working implementation:

```python
class Member:
    pass
```
##### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

## Defining Constructors and Attributes

<!-- Two questions: one constructor takes one param, another constructor takes three params -->

<!-- Question 3 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: cjA1gx
* title: Intro to OOP
### !question

Define a class named `Pizza`. It takes in one parameter that represents a size, such as `"MEDIUM"` or `"EXTRA LARGE"`. In the constructor, it should define an attribute named `size`. The value of `size` is the size passed in.

### !end-question
### !tests
```python
import unittest
from main import *

class TestPython1(unittest.TestCase):
    def test_pizza_has_size(self):
        pizza = Pizza("MEDIUM")
        self.assertEqual(pizza.size, "MEDIUM")
```
### !end-tests
### !explanation

An example of a working implementation:

```python
class Pizza:
    def __init__(self, size):
        self.size = size
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 4 -->
<!-- prettier-ignore-start -->
### !challenge
* type: ordering
* id: 1HambX
* title: Intro to OOP
##### !question

Read the following prompts. Then, arrange the code snippets below so they match the order of the prompts.

1. Creates an instance of the `Pizza` class
1. Reads the instance of the `Pizza` class
1. Reads the attribute `size` from the instance of `Pizza`
1. Sets the instance's `size` to a new value
1. Produces an error

##### !end-question
##### !answer

1. `medium_pizza = Pizza("MEDIUM")`
1. `medium_pizza`
1. `medium_pizza.size`
1. `medium_pizza.size = "EXTRA LARGE"`
1. `medium_pizza(size)`

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 5 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: spGIAF
* title: Intro to OOP
### !question

Define a class named `Pokemon`.

- At initialization, `Pokemon` takes in three arguments: a name, a "primary type," and a "secondary type."
    - For example, this creates an instance of `Pokemon`: `Pokemon("Gengar", "ghost", "poison")`
- There are three attributes on each `Pokemon` that should be set to the correct values:
    - `name`
    - `primary_type`
    - `secondary_type`

### !end-question
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
    def test_pokemon(self):
        gengar = Pokemon("Gengar", "ghost", "poison")
        self.assertEqual(gengar.name, "Gengar")
        self.assertEqual(gengar.primary_type, "ghost")
        self.assertEqual(gengar.secondary_type, "poison")
```
### !end-tests
### !explanation

An example of a working implementation:

```python
class Pokemon:

    def __init__(self, name, primary_type, secondary_type):
        self.name = name
        self.primary_type = primary_type
        self.secondary_type = secondary_type
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 6 -->
<!-- prettier-ignore-start -->
### !challenge
* type: ordering
* id: HYSC7n
* title: Intro to OOP
##### !question

Read the following prompts. Then, arrange the code snippets below so they match the order of the prompts.

1. Creates an instance of the `Pokemon` class
1. Reads the instance of the `Pokemon` class
1. Accesses the attribute `name` from the instance of `Pokemon`
1. Accesses the attribute `primary_type` from the instance of `Pokemon`
1. Accesses the attribute `secondary_type` from the instance of `Pokemon`
1. Prints the attribute `name` from the instance of `Pokemon`

##### !end-question
##### !answer

1. `tangusaur = Pokemon("Tangusaur", "poison", "grass")`
1. `tangusaur`
1. `tangusaur.name`
1. `tangusaur.primary_type`
1. `tangusaur.secondary_type`
1. `print(tangusaur.name)`

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

### !callout-secondary

## Tangusaur?

The fictional Pokemon in this problem set were [randomly generated](https://pokemon.alexonsager.net/).

### !end-callout

<!-- Question 7 -->
<!-- prettier-ignore-start -->
### !challenge
* type: ordering
* id: betEim
* title: Intro to OOP
##### !question

Assume this definition of the `Pokemon` class. Note that it uses keyword argument syntax.

```python
class Pokemon:

    def __init__(self, name, primary_type="normal", secondary_type=None):
        self.name = name
        self.primary_type = primary_type
        self.secondary_type = secondary_type
```

Read the following code snippets. Then, arrange the options below so they match the order of the code snippets.

1. `abchan = Pokemon("Abchan", primary_type="psychic", secondary_type="fighting")`
1. `magibat = Pokemon("Magibat", primary_type="water", secondary_type="flying")`
1. `"Abchan"`
1. The instance of the Pokemon with a `name` of `"Abchan"`
1. `"flying"`
1. `"water"`
1. `"psychic"`
1. `"fighting"`

##### !end-question
##### !answer

1. Creates an instance of `Pokemon` where the `primary_type` has a value of `psychic` and the `secondary_type` has a value of `fighting`
1. Creates an instance of `Pokemon` where the `primary_type` has a value of `water` and the `secondary_type` has a value of `flying`
1. `abchan.name`
1. `abchan`
1. `magibat.secondary_type`
1. `magibat.primary_type`
1. `abchan.primary_type`
1. `abchan.secondary_type`

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

## Defining Instance Methods

<!-- Two questions -->

<!-- Question 8 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: jA2V9q
* title: Intro to OOP
### !question

Create a class named `BasketballTeam`, which fulfills the following requirements:

- Has one attribute, `members`, which starts as an empty list in the constructor
- Has an instance method named `add_member`
    - Has one parameter, which is a new member's name
    - Adds the new member's name to the `members` attribute
    - Returns `True`

The following code should be able to work successfully with the `BasketballTeam` class.

```python
green_team = BasketballTeam()
print("Initially, the green_team has no members:", green_team.members)

yellow_team = BasketballTeam()
print("Initially, the yellow_team has no members:", yellow_team.members)

green_team.add_member("Charly")
yellow_team.add_member("Martina")
green_team.add_member("Rahma")
yellow_team.add_member("Lilly-Ann")
green_team.add_member("Gillian")

print("The green_team has the members Charly, Rahma, and Gillian", green_team.members)
print("The yellow_team has the members Martina and Lilly-Ann", yellow_team.members)
```

### !end-question
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
    def test_basketballteam_add_member(self):
        green_team = BasketballTeam()
        self.assertEqual(green_team.members, [])

        charly_result = green_team.add_member("Charly")
        rahma_result = green_team.add_member("Rahma")
        gillian_result = green_team.add_member("Gillian")

        self.assertIn("Charly", green_team.members)
        self.assertIn("Rahma", green_team.members)
        self.assertIn("Gillian", green_team.members)
        self.assertTrue(charly_result)
        self.assertTrue(rahma_result)
        self.assertTrue(gillian_result)
```
### !end-tests
### !explanation

An example of a working implementation:

```python
class BasketballTeam:

    def __init__(self):
        self.members = []

    def add_member(self, new_member):
        self.members.append(new_member)
        return True
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 9 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: Uus859
* title: Intro to OOP
### !question

Create a class named `Automobile`, which fulfills the following requirements:

- Takes in one parameter in its constructor for the initial speed, which is an integer
- Has one attribute, `speed`
    - The attribute `speed` should have the value of the initial speed passed in
- Has an instance method `accelerate`
    - Has one parameter, which is an integer that is the amount to change speed by
    - Increases the `speed` attribute by the argument
    - Returns `speed`

The following code should be able to work successfully with the `Automobile` class.

```python
bus = Automobile(45)

bus.accelerate(5)

print("The speed of the bus is 50:", bus.speed)

bus.accelerate(-2)

print("The speed of the bus is 48:", bus.speed)
```

### !end-question
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
    def test_automobile_accelerate(self):
        vroom = Automobile(45)

        new_speed = vroom.accelerate(5)

        self.assertEqual(new_speed, 50)
        self.assertEqual(vroom.speed, 50)
```
### !end-tests
### !explanation

An example of a working implementation:

```python
class Automobile:

    def __init__(self, initial_speed):
        self.speed = initial_speed

    def accelerate(self, speed_delta):
        self.speed += speed_delta
        return self.speed
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

## Using Instance Methods

<!-- Two questions about having two instance methods, and one instance method calls another -->

<!-- Question 10 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: yHAKor
* title: Intro to OOP
### !question

Use the following definition of `BasketballTeam`. Each `BasketballTeam` has:

- An attribute `score_dict`, which maps a member's name to the number of points they've scored
- An instance method `get_total_score`, which goes through the values of `score_dict` and sums and returns the total number of points

Read through this example code to see what usage of `score_dict` could look like:

```python
original_scores = {
    "Charly": 12,
    "Rahma": 12,
    "Gillian": 12
}
green_team = BasketballTeam(original_scores)

print("I can get Charly's score:", green_team.score_dict["Charly"])

print("I can get the team's total score, which is 36:", green_team.get_total_score())
```

Create an instance method named `requires_overtime`.

This method should:

- Take in one argument, which is a number of points from an opposing basketball team
- Compare this team's total score against the opposing score:
    - if the two scores are equal, return `True`
    - if the two scores aren't equal, return `False`
- **Required**: Use the `get_total_score` instance method
    - Invoke it with `self.get_total_score()` inside `requires_overtime`

### !end-question
### !placeholder

```python
class BasketballTeam:

    def __init__(self, initial_score_dict):
        self.score_dict = initial_score_dict

    def get_total_score(self):
        return sum(self.score_dict.values())
```
### !end-placeholder
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):

    def test_basketballteam_get_total_score(self):
        original_scores = {
            "Charly": 12,
            "Rahma": 12,
            "Gillian": 12
        }

        green_team = BasketballTeam(original_scores)

        self.assertEqual(green_team.get_total_score(), 36)

    def test_basketballteam_requires_overtime(self):
        original_scores = {
            "Charly": 12,
            "Rahma": 12,
            "Gillian": 12
        }
        green_team = BasketballTeam(original_scores)

        green_team_score = green_team.get_total_score()

        self.assertEqual(
            green_team.requires_overtime(green_team_score), True)
        self.assertEqual(
            green_team.requires_overtime(green_team_score + 1), False)
        self.assertEqual(
            green_team.requires_overtime(green_team_score - 1), False)
```
### !end-tests
### !explanation

An example of a working implementation:

```python
class BasketballTeam:

    def __init__(self, initial_score_dict):
        self.score_dict = initial_score_dict

    def get_total_score(self):
        return sum(self.score_dict.values())

    def requires_overtime(self, opposing_score):
        return self.get_total_score() == opposing_score
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 11 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: h1a8o1
* title: Intro to OOP
### !question

Use the following definition of `Automobile`. Each `Automobile` has:

- An attribute `speed`, which is an integer
- An instance method `accelerate`, which adjusts the `speed` based on the given speed delta

Read through this example code to understand `Automobile` better:

```python
bus = Automobile()
bus.speed = 45

bus.accelerate(5)

print("The speed of the bus is 50:", bus.speed)

bus.accelerate(-2)

print("The speed of the bus is 48:", bus.speed)
```

Create an instance method named `adjust_to_speed_limit`.

This method should:

- Take in one argument, which is a speed limit
- **Required**: Use the `accelerate` instance method
    - Invoke it with `self.accelerate()` inside `adjust_to_speed_limit`
- Follow the rules of this table:

| If ...                                        | Then...                               |
| --------------------------------------------- | ------------------------------------- |
| Current `speed` is under `speed_limit` by 5+  | accelerate with a speed delta of `2`  |
| Current `speed` is under `speed_limit` by 1-4 | accelerate with a speed delta of `1`  |
| Current `speed` is equal to `speed_limit`     | Don't change speed                    |
| Current `speed` is over `speed_limit`         | accelerate with a speed delta of `-1` |

Read through this example code to see what useage of `adjust_to_speed_limit` could look like:

```python
bus = Automobile()

bus.speed = 45
bus.adjust_to_speed_limit(50)
print(bus.speed) # output: 47

bus.speed = 45
bus.adjust_to_speed_limit(46)
print(bus.speed) # output: 46

bus.speed = 45
bus.adjust_to_speed_limit(44)
print(bus.speed) # output: 44

bus.speed = 45
bus.adjust_to_speed_limit(45)
print(bus.speed) # output: 45
```

### !end-question
### !placeholder

```python
class Automobile:
    def __init__(self):
        self.speed = 0

    def accelerate(self, speed_delta):
        self.speed += speed_delta
        return self.speed
```
### !end-placeholder
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
    def test_automobile_accelerate(self):
        bus = Automobile()
        bus.speed = 45

        new_speed = bus.accelerate(5)

        self.assertEqual(new_speed, 50)
        self.assertEqual(bus.speed, 50)

    def test_automobile_adjust_to_speed_limit(self):
        bus = Automobile()

        bus.speed = 45
        bus.adjust_to_speed_limit(50)
        self.assertEqual(bus.speed, 47)
        bus.speed = 45
        bus.adjust_to_speed_limit(46)
        self.assertEqual(bus.speed, 46)
        bus.speed = 45
        bus.adjust_to_speed_limit(44)
        self.assertEqual(bus.speed, 44)
        bus.speed = 45
        bus.adjust_to_speed_limit(45)
        self.assertEqual(bus.speed, 45)
```
### !end-tests
### !explanation

An example of a working implementation:

```python
class Automobile:
    def __init__(self):
        self.speed = 0

    def accelerate(self, speed_increase):
        self.speed += speed_increase
        return self.speed

    def adjust_to_speed_limit(self, speed_limit):
        difference = self.speed - speed_limit

        if difference <= -5:
            self.accelerate(2)
        elif -5 < difference < 0:
            self.accelerate(1)
        elif difference > 0:
            self.accelerate(-1)
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 12 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: FOhorV
* title: Intro to OOP
### !question

Given this definition of `BasketballTeam`, implement the `get_leading_team` function.

This function must:

- Take in two arguments: an instance of `BasketballTeam` as `home_team`, and another instance of `BasketballTeam` as `away_team`
- If the score of `home_team` is greater than or equal to `away_team`, return `home_team`
- Otherwise, return `away_team`
- **Required**: Use the instance method `get_total_score` on `home_team` and `away_team`

The following code should be able to work successfully with the `get_leading_team` function.

```python
green_team = BasketballTeam("Green Team", {
    "Charly": 12,
    "Rahma": 12,
    "Gillian": 12
})
yellow_team = BasketballTeam("Yellow Team", {
    "Martina": 12,
    "Lilly-Ann": 100
})

leading_team = get_leading_team(green_team, yellow_team)

print("Leading team is the yellow team:", yellow_team.team_name)
```

Note that `get_leading_team` is _not_ inside of the `BasketballTeam` class. To solve this problem, you do not need to alter the code in `BasketballTeam`.

### !end-question
### !placeholder

```python
def get_leading_team(home_team, away_team):
    pass

class BasketballTeam:

    def __init__(self, team_name, initial_score_dict):
        self.team_name = team_name
        self.score_dict = initial_score_dict

    def get_total_score(self):
        return sum(self.score_dict.values())
```
### !end-placeholder
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
    def test_get_leading_team_is_home(self):
        home_team = BasketballTeam("Home Team", {
            "Charly": 12,
            "Rahma": 12,
            "Gillian": 12
        })
        away_team = BasketballTeam("Away Team", {
            "Martina": 12,
            "Lilly-Ann": 12
        })

        leading_team = get_leading_team(home_team, away_team)

        self.assertIs(leading_team, home_team)

    def test_get_leading_team_is_away(self):
        home_team = BasketballTeam("Home Team", {
            "Charly": 12,
            "Rahma": 12,
            "Gillian": 12
        })
        away_team = BasketballTeam("Away Team", {
            "Martina": 12,
            "Lilly-Ann": 100
        })

        leading_team = get_leading_team(home_team, away_team)

        self.assertIs(leading_team, away_team)

    def test_get_leading_team_ties_prefer_home(self):
        home_team = BasketballTeam("Home Team", {
            "Charly": 12,
            "Rahma": 12
        })
        away_team = BasketballTeam("Away Team", {
            "Martina": 12,
            "Lilly-Ann": 12
        })

        leading_team = get_leading_team(home_team, away_team)

        self.assertIs(leading_team, home_team)
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def get_leading_team(home_team, away_team):
    if home_team.get_total_score() >= away_team.get_total_score():
        return home_team
    else:
        return away_team


class BasketballTeam:

    def __init__(self, team_name, initial_score_dict):
        self.team_name = team_name
        self.score_dict = initial_score_dict

    def get_total_score(self):
        return sum(self.score_dict.values())
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 13 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: aCjYBj
* title: Intro to OOP
### !question

Given this definition of `Automobile`, implement the `set_traffic_speed` function.

This function must:

- Take in 2 arguments: a list of instances of `Automobile`s, named `vehicles`, and a `target_speed`
- Loop through each vehicle in `vehicles` and set their speed to `target_speed`
- **Required**: Use the instance method `set_speed` on each vehicle in `vehicles`

To solve this problem, you do not need to alter the code in `Automobile`.

### !end-question
### !placeholder

```python
def set_traffic_speed(vehicles, target_speed):
    pass


class Automobile:
    def __init__(self):
        self.speed = 0

    def set_speed(self, new_speed):
        self.speed = new_speed
```
### !end-placeholder
### !tests
```python
import unittest
from main import *

class TestChallenge(unittest.TestCase):
    def test_automobile_set_speed(self):
        bus = Automobile()
        bus.set_speed(30)

        self.assertEqual(bus.speed, 30)

    def test_set_traffic_speed(self):
        bus = Automobile()
        bus.set_speed(30)
        bike = Automobile()
        bike.set_speed(15)
        trolley = Automobile()
        trolley.set_speed(20)

        set_traffic_speed([bus, bike, trolley], 5)

        self.assertEqual(bus.speed, 5)
        self.assertEqual(bike.speed, 5)
        self.assertEqual(trolley.speed, 5)
```
### !end-tests
### !explanation

An example of a working implementation:

```python
def set_traffic_speed(vehicles, target_speed):
    for vehicle in vehicles:
        vehicle.set_speed(target_speed)


class Automobile:
    def __init__(self):
        self.speed = 0

    def set_speed(self, new_speed):
        self.speed = new_speed
```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->
