# Activity: Identifying Test Cases

In this exercise you will write a method and set of tests in TDD fashion which calculates a hand's BlackJack score.

## About BlackJack

In the card BlackJack each card has a value.
-  Number cards (2-10) carry the card's numeric value.
-  Face cards on the other hand ("Jack", "Queen", "King") have a value of 10.
-  Aces (1) can have a value of either 1 or 11, whichever will get the hand closest to 21 without going over.

For example if you have a 3, a King, and an Ace, your BlackJack score is 14 (3 + 10 + 1).  If you have an Ace, and a Jack then your score is 21 (11 + 10).

A hand, an array of Card values, must be between 2 and 5 items inclusive.

When a hand's score is greater than 21, the hand is a **bust** and the player automatically loses.

In this activity, we will write a method called:  `blackjack_score` which takes an array of card values and returns the blackjack score.

## Part 1:  Identifying Edge & Nominal Cases

- Name 2 nominal edge cases. 
- Name at least 3 edge cases.
- How would we **test** these cases?

## Part 2:  Calculating a Score

You will write a method called:  `blackjack_score` which take an array of card values and returns the blackjack score.  The card values can be any of the following, number values 2-10, "King", "Queen", "Jack", and "Ace".  If the array contains an invalid card value or the total exceeds 21, raise an `ArgumentError`.  For example `blackjack_score(["Ace", 5, 3])` will return 19.  You should also raise an error if the hand contains more than 5 cards.

In this exercise you will complete the given tests in `test/blackjack_score_test.rb` and updating the `blackjack_score` method in `lib/blackjack_score.rb` to make it pass.

Step 1:  Complete the given test
Step 2:  Update `blackjack_score` to pass the test
Step 3:  Move to the next test