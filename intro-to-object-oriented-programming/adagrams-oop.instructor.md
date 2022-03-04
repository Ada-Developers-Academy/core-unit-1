# Instructor: Adagrams OOP

C16 Seattle did a livecode of making Adagrams Object Oriented as part of the Adagrams Wrap-up / OOP Intro

An here is the [adagrams github branch](https://github.com/AdaGold/adagrams-py/tree/oop) with an OOP solution.

Here is the [slide deck](https://docs.google.com/presentation/d/1bEcoqdfAOZC5wRDpjfi42uJyl3rnE77-xVs_8qO3QHg/edit#slide=id.geb5e70494d_0_291).

Here is a proposed structure for the livecode (that's in the slide deck).

Build the **Hand** class first:

* Instance Variables:
    * letter_bank - a list of letters in the hand

* Methods:
    * __init__(letters) - Constructor
    * uses_available_letters(word) - Checks to see if the word can be made using letters.
    * draw_letter(letter_pool) - Populates letter_bank

Next build the **Adagrams** class:

* Instance Variables:
    * hand - Instance of hand for this game
    * word_list - List to store words guessed for particular hand
    * letter_scores - A dictionary of letter scores

* Methods:
    * __init__() - Constructor
    * score_word(word) - Takes a word and returns the score get_highest_word_score(word_list) -  Returns the highest word score from word_list
    * add_valid_word_to_list(word) -Adds valid words to word_list


