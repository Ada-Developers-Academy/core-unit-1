1

Create a function named `adds_five`. It has one parameter, `num`. The function should add `5` to `num`, and return the sum.

Example arguments | Example return value
--- | ---
`22` | `27`
`0` | `5`

    def test_adds_five(self):
        self.assertEqual(adds_five(22), 27)
        self.assertEqual(adds_five(0), 5)

2

Create a function named `doubles_and_adds_two`. It has one parameter, `num`. The function should add `num` + `num` + `2`, and return the sum.

Example arguments | Example return value
--- | ---
`50` | `102`
`0` | `2`

    def test_doubles_and_adds_two(self):
        self.assertEqual(doubles_and_adds_two(50), 102)
        self.assertEqual(doubles_and_adds_two(0), 2)

3

Create a function named `doubles`. It has one parameter, `input`. If `input` is a number, the function should double `input` and return it. If `input` is a string, the function should concatenate `input` twice together.

Example arguments | Example return value
--- | ---
`3` | `6`
`4` | `8`
`"4"` | `"44"`
`"Hello, World!"` | `"Hello, World!Hello, World!"`

    def test_doubles(self):
        self.assertEqual(doubles(3), 6)
        self.assertEqual(doubles(4), 8)
        self.assertEqual(doubles("4"), "44")
        self.assertEqual(doubles("Hello, World!"), "Hello, World!Hello, World!")

4

Create a function named `get_third_place`. It has one parameter, `finalists`. Assuming that the first item in `finalists` is first place and the second item in `finalists` is second place, return the finalist in third place.

Example arguments | Example return value
--- | ---
`["Pikachu", "Bulbasaur", "Squirtle", "Charizard"]` | `"Squirtle"`
`["Bulbasaur", "Squirtle", "Charizard"]` | `"Charizard"`

    def test_get_third_place(self):
        self.assertEqual(get_third_place(["Pikachu", "Bulbasaur", "Squirtle", "Charizard"]), "Squirtle")
        self.assertEqual(get_third_place(["Bulbasaur", "Squirtle", "Charizard"]), "Charizard")

5

Create a function named `get_third_place`. It has one parameter, `finalists`. If there are at least three finalists, return the finalist in third place. If there aren't at least three finalists, return `None`.

Example arguments | Example return value
--- | ---
`["Pikachu", "Bulbasaur", "Squirtle", "Charizard"]` | `"Squirtle"`
`["Squirtle", "Charizard"]` | `None`
`[]` | `None`

    def test_get_third_place(self):
        self.assertEqual(get_third_place(["Pikachu", "Bulbasaur", "Squirtle", "Charizard"]), "Squirtle")
        self.assertEqual(get_third_place(["Squirtle", "Charizard"]), None)


6

Create a function named `compare_votes`. It has two parameters, `cand_a` and `cand_b` (short for "candidate"). Both `cand_a` and `cand_b` will be dictionaries that look like this:

```python
{
    "name": "Mx. Candidate Name",
    "votes": 5
}
```

Compare the votes inside `cand_a` and `cand_b`. Find the candidate with more votes, and return their name.

Example `cand_a` | Example `cand_b` | Example return value
--- | --- | ---
`{"name": "Pikachu", "votes": 25}` | `{"name": "Bulbasaur", "votes": 24}` | `"Pikachu"`
`{"name": "Pikachu", "votes": 0}` | `{"name": "Bulbasaur", "votes": 1}` | `"Bulbasaur"`

    def test_compare_votes(self):
        self.assertEqual(compare_votes({"name": "Pikachu", "votes": 25}, {"name": "Bulbasaur", "votes": 24}), "Pikachu")
        self.assertEqual(compare_votes({"name": "Pikachu", "votes": 0}, {"name": "Bulbasaur", "votes": 1}), "Bulbasaur")

7

Create a function named `compare_ids`. It has two parameters, `cand_a` and `cand_b` (short for "candidate"). Both `cand_a` and `cand_b` will be dictionaries that look like this:

```python
{
    "id": 5
    "name": "Mx. Candidate Name",
}
```

Compare the IDs inside `cand_a` and `cand_b`. Find the candidate that has an ID smaller numerical value, and return the candidate dictionary itself.

Example `cand_a` | Example `cand_b` | Example return value
--- | --- | ---
`{"id": 25, "name": "Pikachu"}` | `{"id": 1, "name": "Bulbasaur"}` | `{"id": 1, "name": "Bulbasaur"}`
`{"id": 25, "name": "Pikachu"}` | `{"id": 26, "name": "Bulbasaur"}` | `{"id": 25, "name": "Pikachu"}` 

    def test_compare_votes(self):
        self.assertEqual(compare_votes({"id": 25, "name": "Pikachu"}, {"id": 1, "name": "Bulbasaur"}), {"id": 1, "name": "Bulbasaur"})
        self.assertEqual(compare_votes({"id": 25, "name": "Pikachu"}, {"id": 26, "name": "Pikachu"}), {"id": 25, "name": "Pikachu"})


8

Comparing Strings

Python supports comparing strings with `<`, `>`, etc. Python will say that strings are compared alphabetically. Strings that begin with `"A"` are less than `"Z"`. Python orders capital letters as less than lowercase letters, so `"a"` is less than `"z"`. Consider the table below.

Code | Output
--- | ---
`"Apple" < "Banana"` | `True`
`"Apple" > "Banana"` | `False`
`"Banana" < "Apple"` | `False`
`"Banana" > "Apple"` | `True`
`"Apple" < "apple"` | `True`
`"Apple" > "apple"` | `False`

What's going on? In computing, each character in text has a value from Unicode, where Unicode is a standard for converting all characters and emojis across different platforms. Follow your curiosity!


Create a function named `compare_alphabetically`. It has two parameters, `word_a` and `word_b`, which will be strings. Compare `word_a` and `word_b` and determine which one comes first alphabetically. Follow these rules:

- Assume all characters in both words use the English alphabet
- Order uppercase letters before lowercase letters

Return `word_a` if `word_a` comes first alphabetically. Return `word_b` if `word_b` comes first. Return either `word_a` or `word_b` if they are identical strings.

Example `word_a` | Example `word_b` | Example return value
--- | --- | ---
`"Pikachu"` | `"Bulbasaur"` | `"Bulbasaur"`
`"Bulbasaur"` | `"Pikachu"` | `"Bulbasaur"`
`"Pikachu"` | `"Pikachu"` | `"Pikachu"`
`"Pikachu"` | `"pikachu"` | `"Pikachu"`


    def compare_alphabetically(self):
        self.assertEqual(compare_alphabetically("Pikachu", "Bulbasaur"), "Bulbasaur")
        self.assertEqual(compare_alphabetically("Bulbasaur", "Bulbasaur"), "Bulbasaur")
        self.assertEqual(compare_alphabetically("Pikachu", "Pikachu"), "Pikachu")
        self.assertEqual(compare_alphabetically("Pikachu", "pikachu"), "Pikachu")


9

Create a function named `compare_values`. It has two parameters, `a` and `b`, which will be numbers. Compare `a` against `b`. If `a` is less than `b`, return `-1`. If `a` is equal to `b`, return `0`. If `a` is greater than `b`, return `1`.

Example `a` | Example `b` | Example return value
--- | --- | ---
`999` | `-999` | `1`
`-5` | `-5` | `0`
`80.5` | `80.6` | `-1`

    def test_compare_values(self):
        self.assertEqual(compare_values(999, -999), 1)
        self.assertEqual(compare_values(-5, -5), 0)
        self.assertEqual(compare_values(80.5, 80.6), -1)

10

FizzBuzz

Create a function named `fizz_buzz`. It has one parameter, `num`.

If `num` is a multiple of 3, it should return `"Fizz"`. If `num` is a multiple of 5, it should return `"Buzz"`. If `num` is a multiple of 3 _and_ 5, it should return `"FizzBuzz"`. If `num` is _not_ a multiple of either 3 or 5, it should return `num`.

    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz(3), "Fizz")
        self.assertEqual(fizz_buzz(327), "Fizz")
        self.assertEqual(fizz_buzz(5), "Buzz")
        self.assertEqual(fizz_buzz(560), "Buzz")
        self.assertEqual(fizz_buzz(15), "FizzBuzz")
        self.assertEqual(fizz_buzz(450), "FizzBuzz")
