# Practice: Composition

## Directions

Complete all questions below.

## Practice

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge
* type: checkbox
* id: 8Mppv3
* title: Composition
##### !question
"Ada Bank" is a mobile app for users to keep track of their banking accounts. An `AccountSummary` class is responsible for displaying balances from a user's `SavingsAccount` and `CreditCardAccount`. Select the option(s) that accurately describe these relationships.
##### !end-question
##### !options
* `AccountSummary` is the parent class, while `Savings Account` and `Credit Card Account` are child classes
* `AccountSummary` has-a `SavingsAccount`
* `AccountSummary` has-a `CreditCardAccount`
* `SavingsAccount` and `CreditCardAccount` are component classes while `AccountSummary` is the composite class
##### !end-options

##### !answer
* `AccountSummary` has-a `SavingsAccount`
* `AccountSummary` has-a `CreditCardAccount`
* `SavingsAccount` and `CreditCardAccount` are component classes while `AccountSummary` is the composite class
##### !end-answer
### !end-challenge
<!--prettier-ignore-end -->

<!-- Question 2 -->
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
