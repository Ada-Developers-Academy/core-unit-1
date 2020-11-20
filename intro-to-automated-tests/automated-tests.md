# Automated Tests

## Learning Goals

- Define automated tests 
- Define unit tests 
- Explain how automated unit tests are used to verify code correctness

## Introduction

Have you ever worked on a function, and it runs, but you weren't sure if it was implemented correctly? Have you ever refactored code, but suddenly you lost confidence if the code still worked?

## Vocabulary and Synonyms

Vocab | Definition| Synonyms| How to Use in a Sentence
-----|-----|-----|-----
Automated Test| Scripts that test specific code for correct functionality| Test | "As the application grows, we need to ensure the automated tests also scale."
Unit Test | Scripts designed to test the performance of a single function | Test Case | "Did the new feature pass the unit tests?" |

## Automated Tests Verify Code Correctness

Automated tests, often called "tests," are suites of code used to verify the correctness of another, separate suite of code.

Programmers write tests to communicate what needs to be proved in order for a feature to be complete.

Each test could follow this generic pattern:
1. Get a sample of at least one correct example: an input and and output
2. Use the inputs in the feature to test
3. Compare the actual result from the above step to the expected value

### Example: Astrology Software

Addison is writing software about astrology. They are working on a feature that, when a user provides a date, time, and location of their birth, will compute their astrological birth chart. They need to know if they've implemented the logic correctly; does the feature accurately compute the astrological birth chart? They can test their feature by finding the following information:

1. Get a sample of at least one correct example: an input and and output
    - This means, finding and using a real date, time, and location, and its real astrological birth chart
    - Addison can use January 1, 1980, Seattle, 12:00pm, and its real chart: Capricorn sun, Cancer moon, and Aries rising
2. Use the inputs in the feature to test
    - This means Addison should use this date, time, and location, and pass it into the feature
    - Addison will use January 1, 1980, Seattle, 12:00pm and pass it into the feature
3. Compare the actual result from the above step to the expected value
    - Addison should get the result from their feature, and compare it to the real astrological birth chart. Is the actual birth chart from the feature identical to the expected birth chart? If not, why?
    - Did Addison get back Capricorn sun, Cancer moon, and Aries rising from their code? If they did, their feature is accurate! If they didn't, they have more work to do.

Programmers run tests to get test output. For each test, it will either pass, fail, or give an error. Programmers should use this feedback to make more changes to their code if necessary, or to confirm that the feature is complete.

**Example:** Addison could write a test suite of 20 tests. When they run the tests, they might get 15 passing tests, 4 failing tests, and 1 error. They should continue to work towards 0 failing tests.

### Unit Tests Are for Small Units

Because there are a lot of different kinds of code, there are a lot of different kinds of tests. One kind is unit testing. Unit tests are automated tests that focus on a unit, which is commonly a single function. They're used to check that given some specific arguments, the function returns some expected value.

**Example:** Addison has a function called `calculate_chart`, which takes in 3 parameters: `date`, `location`, and `time`. They can write unit tests for this function.

### Test Cases and Scenarios

Testing a single function could have many unit tests to test it. Why? Based on the context, a single function could potentially have different arguments that give back different return values. Different scenarios in development can imply different arguments, which would produce different logic. All scenarios and possible outcomes of a function should be tested, as much as reasonably possible.

Addison could come up with the following scenarios:

| Question to Ask | Specific Arguments | Expected Return Value
| --- | --- | ---
Do we get an accurate birth chart if we pass in a date, location, and time? | `"January 1, 1980"`, `"Seattle"`, `"12:00"` | `{"Sun": "Capricorn", ...}`
What happens if the function receives `None` for time? | `"January 1, 1980"`, `"Seattle"`, `None` | `None`
What happens if the `date` argument comes as a different format? | `"1980-01-01"`, `"Seattle"`, `"12:00"` | `{"Sun": "Capricorn", ...}`
What happens if the function receives an empty string for `location`? | `"January 1, 1980"`, `"Seattle"`, `"12:00"` | should raise an exception

### !callout-info
## Testing Scenarios
There are countless more scenarios to anticipate! How many scenarios do we need to anticipate? In general, the answer to this question depends on the code you're testing. If there are a lot of conditions in the function, with a lot of different kinds of `return` values, we may have a test for one or two examples each of those `return` values.
### !end-callout


## When We Have Trustworthy Tests, Everyone Wins

Tests can be written poorly! Just like other code, test code could have varying code styles and approaches, and even be wrong. Sometimes, tests are missing, and there are more scenarios that need to be tested.

Qualities of a trustworthy test suite include:
- large test coverage
- readable
- covers many scenarios

When a codebase has a suite of trustworthy tests, everyone wins. Benefits of a good test suite include:
- ease of collaboration
- ease of refactoring
- ease of finishing features more quickly

When a whole team collaborates using the same test suite, the whole team has visibility into how the code tests as the code changes over time.

## Adjusted Workflow

To incorporate testing into our development workflow, our workflow may adjust to this:

1. Read the feature requirements
2. Think of scenarios relevant to the feature, and what their expected values would be
3. Write a test for that scenario
4. Implement the code to make that test pass
5. Create `git` commits when appropriate (at least one)
6. Repeat!
