# Problem Set: Git Commands

## Directions

Complete the prompts below.

Follow these guidelines:

- Try to work through one entire part in one sitting
  - This is a lot of text. Take a short screen break inbetween each part and draw a picture, or something similar
- Take notes about what commands you use as you do them
- When something unintended happens, take notes about what happened, how you know it happened, and make a guess why
  - Fix it, and take notes about the fix
  - Reach out for help any time!

## Part 1

- [ ] `cd` into a folder that either holds projects or exercises.

- [ ] Clone [this `core-practice-git-commands` repo](https://github.com/AdaGold/core-practice-git-commands) for this assignment.

- [ ] `cd` into the repo folder.

- [ ] Confirm that there are no changes in your local changes area or staging area with `$ git status`

- [ ] Run the tests using `$ python3 -m pytest main.py`

  - This requires a global installation of `pytest`. If you don't have a global installation of `pytest`, skip this step

- [ ] Make the test pass - Re-run the tests with `$ python3 -m pytest main.py`

  - If you can't run tests, read through the code and change the code to the best of your ability - You must change at least one line of code

- [ ] Confirm that you have one file changed in your local changes area with `$ git status`

- [ ] Review the changes in the local changes area with `$ git diff`. Press `q` to exit the `diff` if necessary.

- [ ] Add that file to the staging area with either `$ git add main.py` or `$ git add -p`

- [ ] Confirm that you have one file changed in your staging area with `$ git status`

- [ ] Review the changes in the staging area with `$ git diff --staged`

- [ ] Create a commit with this commit message, or one of your own: `"refactors always_returns_true() to return True"`

- [ ] Review the commit with `$ git log`, then `$ git show`. Press q to exit the `log` if necessary.

- [ ] Confirm that there are no changes in your local changes area or staging area

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: B2iBsD
* title: Git Commands
##### !question

List the commands that you ran during this part, in order. (Yes, the answers are in the directions above, but it's meaningful to type them out in order!)
(Do not list any directions; only list commands you entered in your terminal)

##### !end-question
##### !placeholder

I took the following steps, in this order...

1. cd ...
2. ...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->

## Part 2

- [ ] Confirm that there are no changes in your local changes area or staging area with `$ git status`

- [ ] Add a new file named `README.md` in the project root with `$ touch README.md`

- [ ] Open `README.md` and add some content: a title, a sentence, or a poem

- [ ] Confirm that there is one untracked file in the untracked changes area with `$ git status`

- [ ] Add that file to the staging area with `$ git add README.md`

- [ ] Confirm that you have this file changed in your staging area

- [ ] Create a commit with this commit message, or one of your own: `"creates README file, adds a poem"`

- [ ] Review the commit with `$ git log`, then `$ git show`

- [ ] Confirm that there are no changes in your local changes area or staging area

<!-- Question 2 -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: p35m0o
* title: Git Commands
##### !question

List the commands that you ran during this part, in order. (Yes, the answers are in the directions above, but it's meaningful to type them out in order!)
(Do not list any directions; only list commands you entered in your terminal)

##### !end-question
##### !placeholder

I took the following steps, in this order...

1. cd ...
2. ...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->

## Part 3

- [ ] Open the Git history with `$ git log`

- [ ] While looking at the `log`, pick an old commit; pick any commit, besides the commit you just created.

- [ ] While looking at the `log`, find the commit hash of that commit. Copy the commit hash (the first ~7 characters, or the entire hash). Press q to exit the `log` if necessary.

- [ ] Look at the details of this commit with `$ git show <copied commit hash>`, replacing the copied commit hash. Press q to exit the `diff` if necessary. Confirm you can see...
  - The commit message
  - The date of the commit
  - The file name of one changed file
  - A diff of the changes
  - You may not see this if you picked a special kind of commit, such as a merge commit.

<!-- Question 3 -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: fT86MO
* title: Git Commands
##### !question

List the commands that you ran during this exercise, in order. (Yes, the answers are in the directions above, but it's meaningful to type them out in order!)

##### !end-question
##### !placeholder

I took the following steps, in this order...

1. cd ...
2. ...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->

## Part 4

- [ ] Fork this specific repo for this assignment. Confirm that there is a new repo now, and it is under your own personal GitHub account name.

- [ ] `cd` into the folder that either holds projects or exercises; use the same folder as you did for Part 1.

- [ ] Attempt to clone this new repo into this folder. Confirm that you get an error saying that there is already an existing folder with this name.

- [ ] Delete the old project folder with `$ rm -rf <old-project-folder>`

- [ ] Clone this repo. Confirm that this clone was successful. - Note: We will not want to clone repos while inside of another repo's folder.

- [ ] `cd` into this project folder

- [ ] Run tests, write code to make the tests pass, and create a commit, exactly as you did in Part 1

- [ ] Push your new commit to your forked repo with `$ git push`

<!-- Question 4 -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: j9MwxA
* title: Git Commands
##### !question

List the commands that you ran during this exercise, in order. (Yes, the answers are in the directions above, but it's meaningful to type them out in order!)

##### !end-question
##### !placeholder

I took the following steps, in this order...

1. cd ...
2. ...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->
