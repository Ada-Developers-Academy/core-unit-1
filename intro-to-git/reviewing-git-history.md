# Reviewing Git Histories

## Learning Goals

- Practice observing commit history using the commands git status, git log, git show, and git diff
- Explain different ways of "undoing" commits using git revert and git reset

## Introduction

As we create many commits, it will be crucial to review Git histories. There are a series of commands that will give developers useful information about the Git history.

This resource will focus on:

- `$ git status`
- `$ git diff`
- `$ git diff --staged`
- `$ git log`
- `$ git show`

All of these commands have many different options available. Using these options can make the information more useful and effective to you. To explore these options, look them up and follow your curiosity!

### !callout-info

## Navigating with Less commands

There are many commands in Git that will open a screen with a program called Less. The program Less is really great at displaying text. However, Less uses unique navigation keys.

When a git command brings us to a Less screen, we can navigate like so:

- up or down arrows to scroll
- `j` or `k` keys to scroll
- use spacebar to scroll down by one page
- use `b` to scroll up by one page
- `q` to exit the screen

### !end-callout

### `git status` Summarizes Untracked, Local, and Staging

The command `$ git status` outputs a summary of the changes in the local and staging areas. It also contains a lot of other information about the current state of our project as Git sees it!

Use this command all the time:

- To verify what changes are untracked, in local, and in staging
- Before moving changes from local area to staging area
- Before moving changes from the staging area to a commit
- After making a commit to witness the changes in the staging area disappearing

### !callout-warning

## `$ git status` Gives Us Clues to Debug Git

Sometimes, developers will get into a weird "state" of Git. `$ git status` will often give clues about how to debug this state. `$ git status` will tell us if we're in the middle of a process, such as merging (explained later), or in a strange Git "location."

### !end-callout

### `git diff` Reveals All Local Changes

The command `$ git diff` outputs a summary of all changes in the _local changes area._

By default, it displays chunks of the diff. It names the file that the change is in, some of the surrounding lines, and a summary of lines of code that were added, removed, or modified.

If there are a lot of local changes, we'll need to navigate this screen with Less commands.

Use this command all the time:

- Before moving changes from local area to staging area
- Reminding yourself what your most recent work has been
- Seeing what changes you've written and deleted since the last commit

### `git diff --staged` Reveals All Staged Changes

The command `$ git diff --staged` shows a summary of all changes in the _staging area_.

It follows the same rules as `$ git diff`. If there are a lot of staged changes, we'll need to navigate this screen with Less commands.

Use this command all the time:

- Before moving changes from the staging area to a commit
- Checking to see what's in the staging area

### `git log` Reveals The Commit History

The command `$ git log` will show all of the commits made on this git branch (details on branches are a separate subject. We may assume one default branch at this moment.)

The log will clearly show the order of commits, and highlight their commit messages.

Each commit is listed with the following details:

- The commit hash, which is a unique ID for the commit
- The details on the branch that this commit is on
- The author(s) of the commit
- The date and time that the commit was made
- The commit message

If there are a lot of commits, we'll need to navigate this screen with Less commands.

Use this command frequently:

- when you start a new task and should review the most recent work
- to understand and recall the current history of commits
- check a lot of commit information quickly, such as timestamps, authors, etc.

### `git show` Summarizes a Commit

The command `$ git show` will show the details of a single commit.

By default, `$ git show` will print this information:

- The commit hash (ID)
- The author(s)
- The date and time that the commit was made
- The commit message
- The entire diff of that commit

Without any arguments, `$ git show` will show the details of the most recent commit.

Optionally, we can give this command a commit hash, and it will show the details of that commit.

```bash
$ git show <commit hash, such as 26fb46ca8...>
```

Where `<commit hash, such as 26fb46ca8...>` is replaced with a commit hash.

### !callout-info

## Commit Hashes Can Be Shortened

The commit IDs of git are special. In general, each commit ID is very unique. They're so unique, that using even first several characters of it is enough to identify a commit. For example, anywhere that requires a commit hash, we can either use `06cde018c082dc4d936af278ba3b43ae5a3b9492`, or `06cde01`, and they would both work.

This notation is helpful to recognize as commit hashes are often shortened.

### !end-callout

If the commit has a big diff, we'll need to navigate this screen with Less commands.

Use this command often:

- when you want to review a commit
- to recall the contents of the most previous commit

## All of These Should Be in the Project Root

We should use all of these git commands when located in the project root.

There aren't rules about this, but these commands are most effective, straightforward, and consistent from that location.

## About "Undoing" Commits...

Sometimes, as we work on code, we'll make a commit... and then realize that the code changes in that commit were terrible! And those code changes need to be deleted, erased, and undone!

A natural instinct may be to try to "undo this commit."

However, considering the mindset that Git encourages, the best way to "undo a commit" might be to create another commit that reverts those changes. This is a different perspective than trying to "undo" or "get rid of" changes.

It is natural for code to constantly evolve and for learning and exploration to teach us lessons. Often, we learn that to move forward, we need to reverse our work.

### !callout-info

## No really, I just made a commit and I need to undo it

Git has many ways to modify, uncommit, or revert commits. Some search terms to use to look up these commands may be, "git reset," "git commit amend," "git revert," and "git squash." As a goal, programmers should not change shared Git history, unless it is an emergency.

For convenience, this command will "uncommit" the most recent commit, and put all of the commit's changes into the staging area:

```bash
$ git reset --soft HEAD^
```

### !end-callout

## Check for Understanding
