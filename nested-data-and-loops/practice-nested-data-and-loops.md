# Practice: Exception Handling

## Directions

Complete all questions below.

## Practice

The next 3 questions will be using the following data:

``` python

data = [
  {
    "name": "Jane Addams",
    "born": ["September 6, 1860", "Cedarville, IL"],
    "accomplishments": [
      "Nobel Peace Prize winner", 
      "mother of social work legislation"
      ]
  },
  {
    "name": "Marsha P. Johnson",
    "born": ["August 17, 1936", "Elizabeth, NJ"],
    "accomplishments": [
      "LGBTQ activist", 
      "a major catlyst in the Stonewall Uprising"
      ]
  },
  {
    "name": "Margaret Hamilton",
    "born": ["August 24, 1945", "Paoli, IN"],
    "accomplishments": [
      "coined the term software engineer", 
      "lead dev team for NASA's Apollo 11 on-board flight software", 
      "had to do it all on paper!!!"
      ]
  }
]

```

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge

* type: short-answer
* id: NJagehHAt
* title: Travserse Nested Data, pt. 1

##### !question

Using the data above, how would you print out the following: `"Jane Addams was born on September 6, 1860 in Cedarville, IL."`

Example, `print(f"Hi, I'm {data[0]["name"]}.")` would output 
`"Hi, I'm Jane Addams."`.

##### !end-question

##### !answer

/.+/

##### !end-answer

##### !placeholder

Your print statement here...

##### !end-placeholder


##### !hint

##### !end-hint

##### !explanation

`print(f"{data[0]["name"]} was born on {data[0]["born"][0]} in {data[0]["born"][1].")`

##### !end-explanation

### !end-challenge

<!-- prettier-ignore-end -->

<!-- Question 2 -->
<!-- prettier-ignore-start -->
### !challenge

* type: short-answer
* id: 4JQS16HRK
* title: Travserse Nested Data, pt. 2

##### !question

Using the data above, how would you print out the following: `"Margaret Hamilton had to do it all on paper!!!"`

##### !end-question

##### !answer

/.+/

##### !end-answer

##### !placeholder

Your print statement here...

##### !end-placeholder


##### !hint

##### !end-hint

##### !explanation

`print(f"{data[2]["name"]} {data[2]["accomplishments"][2]}")`

##### !end-explanation

### !end-challenge

<!-- prettier-ignore-end -->

<!-- Question 3 -->
<!-- prettier-ignore-start -->
### !challenge
* type: code-snippet
* language: python3.6
* id: NyTByaBRt
* title: Travserse Nested Data, pt. 3
### !question

Given a function named `list_accomplishments`, iterate through each person and print the name, then all of that person's accomplishments. Rinse and repeat.

### !end-question
### !placeholder

```python
def list_accomplishments(data):
    pass
```
### !end-placeholder
### !tests
```python

from main import *
from unittest.mock import patch, call

@patch('builtins.print')
def test_list_accomplishments(mock_print):
    # The actual test
    list_accomplishments([
          {
            "name": "Jane Addams",
            "born": ["September 6, 1860", "Cedarville, IL"],
            "accomplishments": [
              "Nobel Peace Prize winner", 
              "mother of social work legislation"
              ]
          }])
    calls = [call("Jane Addams"),call("Nobel Peace Prize winner"), call("mother of social work legislation")]
    mock_print.assert_has_calls(calls)
```
### !end-tests
### !explanation

An example of a working implementation:

```python

def list_accomplishments(data):
  for person in data:
    print(person["name"])
    for accomp in person['accomplishments']:
      print(accomp)

```

### !end-explanation
### !end-challenge
<!-- prettier-ignore-end -->