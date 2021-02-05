# Practice: Composition

## Directions

Complete all questions below.

## Practice

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: 6770bb4d-c21e-4505-ad5e-aed92cb70a5f
* title: Composition
##### !question
Willow is creating a timesheet app that will display an employee's biweekly hours and pay. Provided this code snippet, which option describes the relationship between the `PayRate` and `Employee` class?

``` Python
class Employee:
  def __init__(self, name, pay_rate, hours):
    self.name = name
    self.pay_rate = pay_rate
    self.hours = hours
    self.payroll_summary = PayRate(self.pay_rate, self.hours)

  def display_payroll_summary(self):
    return "Total Hours: " + str(self.hours) + "\nTotal Pay: " + "${:,}".format(self.payroll_summary.annual_rate()) )

class PayRate:
  def __init__(self, pay, hours):
    self.pay = pay
    self.hours = hours

  def annual_rate(self):
    return self.pay* 12* self.hours

obj_emp = Employee("Sally", 30, 200)
print(obj_emp.display_payroll_summary())
```

##### !end-question
##### !options
* `PayRate` is the child class, `Employee` is the parent class
* `PayRate` is the composite  class, `Employee` is the component class
* `PayRate` is the component class, `Employee` is the composite class
##### !end-options
##### !answer
* `PayRate` is the component class, `Employee` is the composite class
##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: acd9c2f0-3dfb-4c76-a5b1-fcf8af7522cc
* title: Composition
##### !question
Moana just moved to Europe and is having trouble converting to the metric system. To cope, she is creating an Alexa skill to convert metric measurements to imperial measurements.

Provided is her code so far. Select the option that best describes the relationship between `Temperature` and `MetricConverter`.

```python
class Temperature:
  def __init__(self, celsius):
    self.celsius = celsius
    self.metric_converter = Metric_Converter(self.celsius)

  def display_temperature(self):
    return "It is " + str(self.metric_converter.convert_to_fahrenheit()) + " degrees Fahrenheit today."

class MetricConverter:
    def __init__(self, celsius):
      self.celsius = celsius

    def convert_to_fahrenheit(self):
      return (int(self.celsius * (9/5) + 32))

today = Temperature(37)
print(today.display_temperature())
```
##### !end-question
##### !options
* `Temperature` is the component class. `MetricConverter` is the composite.
* `Temperature` is the composite class.`MetricConverter` is the component.
##### !end-options
##### !answer
* `Temperature` is the composite class.`MetricConverter` is the component.
##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 3 -->
<!-- prettier-ignore-start -->
### !challenge
* type: multiple-choice
* id: 00c359fc-58a7-4c95-94ac-3c718ed43e0a
* title: Composition

##### !question
Composition can be initiated by a single line of code. In this code snippet, which line is responsible for starting the relationship between `Bedroom` and `Area`?

```python
1   class Room:
2
3       def __init__(self, width, length):
4           self.width = width
5           self.length = length
6           self.area = Area(self.width, self.length)
7
8       def display_room_details(self):
9           return "This room is " + str(self.area.calculate_area()) + " sq.ft."
10
11
12  class Area:
13
14      def __init__(self, width, length):
15          self.width = width
16          self.length = length
17
18      def calculate_area(self):
19          return self.width * self.length
20
21
22  bedroom = Room(20, 20)
23  print(bedroom.display_room_details())
```
##### !end-question

##### !options
* 6
* 12
* 22
##### !end-options

##### !answer
* 6
##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->
