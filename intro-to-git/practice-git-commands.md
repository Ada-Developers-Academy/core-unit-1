# Practice: Git Commands

## Prompts

`cd` into a folder that either holds projects or exercises.

Clone this specific repo for this assignment.

`cd` into the repo folder.

Confirm that there are no changes in your local changes area or staging area with `$ git status`

Run the tests

Make the test pass

Confirm that you have one file changed in your local changes area with `$ git status`

Review the changes in the local changes area with `$ git diff`. Press q to exit the `diff` if necessary.

Add that file to the staging area with either `$ git add asdf.py` or `$ git add -p`

Confirm that you have one file changed in your staging area

Review the changes in the staging area with `$ git diff --staged`

Create a commit with this commit message, or one of your own: `""`

Review the commit with `$ git log`, then `$ git show`. Press q to exit the `log` if necessary.

Confirm that there are no changes in your local changes area or staging area


List the commands that you ran during this exercise, in order. (Yes, the answers are in the directions above, but it's meaningful to type them out in order!)
(Do not list any directions; only list commands you entered in your terminal)

### Part 2

Confirm that there are no changes in your local changes area or staging area with `$ git status`

Add a new file named `README.md` in the project root with `$ touch README.md`

Open `README.md` and add some content: a title, a sentence, or a poem

Confirm that there is one untracked file in the untracked changes area with `$ git status`

Add that file to the staging area with `$ git add README.md`

Confirm that you have this file changed in your staging area

Create a commit with this commit message, or one of your own: `"create README file, adds a poem"`

Review the commit with `$ git log`, then `$ git show`

Confirm that there are no changes in your local changes area or staging area

List the commands that you ran during this exercise, in order. (Yes, the answers are in the directions above, but it's meaningful to type them out in order!)
(Do not list any directions; only list commands you entered in your terminal)

## Part 3

Open the Git history with `$ git log`

While looking at the `log`, pick an old commit; pick any commit, besides the commit you just created.

While looking at the `log`, find the commit hash of that commit. Copy the commit hash (the first ~7 characters, or the entire hash). Press q to exit the `log` if necessary.

Look at the details of this commit with `$ git show <copied commit hash>`, replacing the copied commit hash. Press q to exit the `diff` if necessary.

List the commands that you ran during this exercise, in order. (Yes, the answers are in the directions above, but it's meaningful to type them out in order!)

## Part 4

Fork this specific repo for this assignment. Confirm that there is a new repo now, and it is under your own personal GitHub account name.

`cd` into the folder that either holds projects or exercises; use the same folder as you did for Part 1.

Attempt to clone this new repo into this folder. Confirm that you get an error saying that there is already an existing folder with this name.

Delete the old project folder with `$ rm -rf asdf`

Clone this repo. Confirm that this clone was successful.
    - Note: We will not want to clone repos while inside of another repo's folder.

`cd` into this project folder

Run tests, write code to make the tests pass, and create a commit, exactly as you did in Part 1

Push your new commit to your forked repo with `$ git push`

List the commands that you ran during this exercise, in order. (Yes, the answers are in the directions above, but it's meaningful to type them out in order!)
