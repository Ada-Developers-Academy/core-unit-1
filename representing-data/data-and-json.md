# Data and JSON

## Learning Goals

- Define JSON as a language-independent way to represent data

## Introduction

As we work with data, we may think, "How can this data get out of our code, and into someone else's code?"

The JSON data format allows programmers to parse and generate data that is largely compatible across languages. Getting exposure to JSON will help us visualize what our Python code may use one day.

Additionally, lessons from JSON exposes us to how applications beyond Python can represent data.

## Vocabulary and Synonyms

| Vocab | Definition                                                                                                                                              | Synonyms | How to Use in a Sentence                                                                                                     |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
| JSON  | a lightweight data-interchange format that can hold objects, arrays, strings, numbers, booleans, and other formats. Intentionally language-independent. | -        | "That API sends back the user data in JSON," "When we read the JSON data, we should find where the location data is nested." |

## What is JSON?

JSON is a specific kind of format that can hold and represent data. JSON does not belong to any specific programming language; JSON is one language-independent way to represent data. JSON uses conventions that are familiar to many programming languages, and is used for machines to parse and generate.

JSON is purely text, but represents data as a combination of _ordered lists of values, or arrays,_ and _name/value pairs, or "objects."_

### !callout-info

## What Does JSON Stand For?

JSON stands for "JavaScript Object Notation." JSON was inspired by JavaScript standards, and its syntax mimics some JavaScript patterns. However, JSON is used today as a language-independent data format.

### !end-callout

### Example JSON

This is one piece of data formatted in JSON. This data comes from an API used for a map application:

```json
{
  "markers": [
    {
      "name": "Rixos The Palm Dubai",
      "location": [25.1212, 55.1535]
    },
    {
      "name": "Shangri-La Hotel",
      "location": [25.2084, 55.2719]
    },
    {
      "name": "Grand Hyatt",
      "location": [25.2285, 55.3273]
    }
  ]
}
```

Looking at this example, we can analyze...

This JSON data is an object as the outer-most data structure.

- It has one name/value pair. The name is `"markers"`, and the value is an array.

The array of markers contains three objects:

- The first object has two name/value pairs.
  1. The first pair has the name `"name"`, and the value `"Rixos the Palm Dubai"`
  2. The second pair has the name `"location"`, and an array as its value
     - The locations array has two elements: the two numbers `25.1212` and `55.1535`
- The second object also has two name/value pairs.
  - This second object has a similar structure to the _sibling_ above, but different values
- The third object follows this pattern with different values, as well

### JSON Expresses Relationships Between Data

In JSON, data structures can be nested within each other.

Often, we use this nesting to see the implied _relationship_ between the pieces of data. Programmers interpret this data; there isn't necessarily one correct answer. It gives meaning to the data, especially for humans and computers who look at this data.

When we look at how data can be nested in JSON, we can identify different data structures within it. The relationships expressed in JSON could potentially be:

- What data _contains_ other pieces of data?
- What data _is a part of_ another piece of data?
- What data is _ordered_ like a list?
- What data represents an object, or something with distinct ideas that can be name/value pairs?
- What data is _alongside_ other pieces of data, on the same layer?

With the above example, we can come to the following conclusions:

1. There are many markers, so the value of `"markers"` is an array
1. Each marker has many pieces of related data, so each marker is an object.
   - Each marker has a `"name"` and a `"location"` associated with it
1. Each location has many pieces of data associated with it, so the value of `"location"` is an array.

### Observations About JSON and Data

- JSON arrays operate very similarly to Python lists
- JSON objects operate very similarly to Python dictionaries
- We can nest JSON arrays and objects inside each other
  - Arrays can hold arrays, objects, or other kinds of data like strings, numbers, `"true"`, `"false"`, and `"null"`
- How the data is nested can imply relationships and meaning in the data

## When is JSON Relevant?

It is possible that JSON does not feel relevant at all right now. If we're working on code that only uses Python, it's likely that developers would prefer to create Python dictionaries and Python lists.

JSON is relevant when:

- We need to read data from another piece of software, such as an API, and the API gives back data in JSON
- We need to send data to another piece of software, and we aren't sure what data format is compatible, so we choose JSON as a common format
- We want to practice reading nested data structures

![JSON data moving between webpage and server](../assets/representing-data_data-and-json_json-moving.png)

### !callout-info

## JSON Alternatives

Are there other ways to format data that are language-agnostic? Yes! There are many formats besides JSON; XML is a popular alternative. Other examples include YAML and SOAP.

### !end-callout

## Check for Understanding

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge

* type: checkbox
* id: da740fd4-4668-4581-8c24-2a8936e5377f
* title: JSON

##### !question

JSON is built specifically for which language?

##### !end-question

##### !options

* JSONish
* Python
* JavaScript
* JSON is language-agnostic, or suitable for more than one language

##### !end-options

##### !answer

* JSON is language-agnostic, or suitable for more than one language

##### !end-answer

### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->
<!-- prettier-ignore-start -->
### !challenge

* type: checkbox
* id: 68a2cbe8-7a2f-4e8b-b98a-943d288e2bd7
* title: JSON

##### !question

Select all of the following that are true: JSON supports having...

##### !end-question

##### !options

* Strings
* Numbers
* Objects
* Arrays

##### !end-options

##### !answer

* Strings
* Numbers
* Objects
* Arrays

##### !end-answer

### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question Takeaway -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: yqzwd2
* title: Data and JSON
##### !question

What was your biggest takeaway from this lesson? Feel free to answer in 1-2 sentences, draw a picture and describe it, or write a poem, an analogy, or a story.

##### !end-question
##### !placeholder

My biggest takeaway from this lesson is...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->
