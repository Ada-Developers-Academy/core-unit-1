# TDD Exercise


Replit: https://replit.com/@adadev/tdd-exercise#README.md

Old Repo: https://github.com/AdaGold/tdd-exercise, not used because students haven't learned how to collaborate in Git yet.

Solution Branch: https://github.com/AdaGold/tdd-exercise/blob/solution-python/tests/test_blackjack_score.py

The TDD Exercise is introduced as part of the problem set (Part 1) and parts 2 and 3 are meant to be a classroom activity. This classroom activity likely needs 2 hours.

Many folks are not familiar with BlackJack. Hopefully by providing the prompt as part of the problem set students will have time to review the rules.
    - If not knowing the rules of blackjack proves to be an impedement to the learning goals, we should probably replace the prompt for this exercise.


For folks who finish this exercise early, here are sample additional edge cases to test:

```python
@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_blackjack_for_score_21():
  pass

@pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_two_aces():
  # Arrange
  hand = ["Ace", "Ace"]

  # Act
  score = blackjack_score(hand)

  # Assert <-- Write assert statement here

@pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_two_aces_where_it_does_not_go_over_21():
  # Arrange
  hand = ["King", "Ace", "Ace"]

  # Act
  score = blackjack_score(hand)

  # Assert <-- Write assert statement here
```
