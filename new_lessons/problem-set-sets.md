# Problem Set: Sets

## Directions

Complete all questions below.

## Practice

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: checkbox
* id: 2d93bfd4-1847-4514-9810-acb3f3db7d22
* title: Sets
<!-- * points: [1] (optional, the number of points for scoring as a checkpoint) -->
<!-- * topics: [python, pandas] (optional the topics for analyzing points) -->

##### !question

Check the expressions that evaluate to `{'apple', 'orange', 'banana'}` with the elements in any order.

##### !end-question

##### !options

* ```{'apple', 'apple', 'orange', 'orange', 'banana', 'banana'}```
* ```set(['apple', 'apple', 'orange', 'orange', 'banana', 'banana'])```
* ```{'apple', 'orange'}.union({'banana'})```
* ```{'apple', 'orange', 'banana'}.union({'melon', 'peach'})```
* ```{'apple', 'orange', 'banana'} | {'banana'}```
* ```{'apple', 'orange', 'banana', 'melon', 'peach'}.intersection({'apple', 'orange', 'banana'})```
* ```{'apple', 'orange', 'banana'} & {'melon', 'peach'}```

##### !end-options

##### !answer

* ```{'apple', 'apple', 'orange', 'orange', 'banana', 'banana'}```
* ```set(['apple', 'apple', 'orange', 'orange', 'banana', 'banana'])```
* ```{'apple', 'orange'}.union({'banana'})```
* ```{'apple', 'orange', 'banana'} | {'banana'}```
* ```{'apple', 'orange', 'banana', 'melon', 'peach'}.intersection({'apple', 'orange', 'banana'})```

##### !end-answer

##### !explanation

* `.union` and `&` are two syntax methods to create a set union.
* `.intersect` and `|` are two syntax methods to create a set intersection.

##### !end-explanation
<!-- !explanation - !end-explanation (markdown, students can see after answering correctly) -->``

<!-- other optional sections -->
<!-- !hint - !end-hint (markdown, hidden, students click to view) -->
<!-- !rubric - !end-rubric (markdown, instructors can see while scoring a checkpoint) -->
<!-- !explanation - !end-explanation (markdown, students can see after answering correctly) -->``

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: checkbox
* id: dc3885d4-35f0-4657-a574-f8ca79fac278
* title: Sets
<!-- * points: [1] (optional, the number of points for scoring as a checkpoint) -->
<!-- * topics: [python, pandas] (optional the topics for analyzing points) -->

##### !question

Check the expressions that evaluate to `True`.

##### !end-question

##### !options

* `{'apple', 'orange', 'banana'} < {'apple', 'orange', 'banana', 'melon', 'peach'} `
* `{'apple', 'orange', 'banana'} > {'apple', 'orange', 'banana', 'melon', 'peach'} `
* `{'apple', 'orange', 'banana'}.disjoint({'melon', 'peach'})`
* `{'apple', 'orange', 'banana'}.disjoint({'apple', 'orange', 'banana', 'melon', 'peach'})`

##### !end-options

##### !answer

* `{'apple', 'orange', 'banana'} < {'apple', 'orange', 'banana', 'melon', 'peach'} `
* `{'apple', 'orange', 'banana'}.disjoint({'melon', 'peach'})`

##### !end-answer

* `set_a < set_b` evaluates to `True` if `set_a` is a subset of `set_b`.
* A set is disjoint with another set if they have no overlapping elements.


### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->