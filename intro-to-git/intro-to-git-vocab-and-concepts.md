# Intro to git: Vocab and Concepts

## Learning Goals

- Explain how git is version control system used to version code
- Define a repository in git
- Compare a git repository to a project
- Define a commit in git

## Introduction

Recall that _versions_ in software are different states of a codebase.

Consider how the version of you from 10 years ago is different from the version of you from 10 minutes ago (which is different from the you of right now). Are those three versions of you very different from each other? Between the you from 10 years ago and the present you, **what was lost? What was gained? And what was modified?**

Between the you from 10 minutes ago and the present you, what was lost, gained, or modified? The difference between those two versions of you could be huge, or they could be small, incremental, barely noticeable changes.

What a codebase looked like at one point in time could be a different version of the code right now. We can say that there is a version of a codebase that passed three tests, and a version of the same codebase that passed four tests.

How can the idea of versioning help us build software?

## Vocabulary and Synonyms

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---
Version
Version Control System
Git
Repository
Tracking (in Git)
Commit

## Version Control Systems Let Us Version Our Code

Version Control Systems are tools that allow programmers to create, view, and understand different versions of code.

There are plenty of different Version Control Systems, with their own set of vocabulary and concepts. **Git** is a version control system that has widespread use and acceptance.

Git gives us the tooling to:
- create different versions of our codebases
- give names, ids, and information between different versions
- follow a specific history of versions
- collaborate on the same codebase at the same time with many people
- configure codebases and developer workflows to help programmers

Callout:
Git vs. GitHub
Git is the name of the version control system we will use. Git is a tool, and we'll primarily use this tool in the command line or using an IDE. GitHub is a service that can host our codebases. GitHub's hosting service is made for programmers who use Git in their projects. The primary way we interact with GitHub is through github.com

### VCS Will Affect Our Developer Workflow

Our developer workflow is the process that starts from a programmer reading the requirements, running the tests, writing code, and submitting the code.

Being able to get all the benefits of a version control system will require us to adapt our developer workflow, and use the version control system constantly while coding!

## Each Repository is a Distinct "Project" Code Base

Git has the concept of a repository, or repo. A repo is a way to describe a project codebase that is being versioned Git.

Often, a repo will directly correlate to a folder on your machine that contains all of a project's files.

When we say to look at someone else's repo, it likely means that they have their own project and codebase that is being versioned with Git.

## Software is Built as a History

As we track different versions of code, when we compare those versions to each other, we see how code shrinks, grows, and changes.

In a sense, version control systems let us understand that software is built over time.

In order to use Git to compare versions, sometimes we will need to tell Git to _track_ different files in a project. This is Git's way of saying that it needs to watch for changes in certain files. Of course we will want Git to watch for changes; that's how we get all the benefits!

### Commits are a Snapshot of History

**A commit** is a representation of a version of code, especially within a history.

We will build commits as we build software; we will create commits, and over time, these commits will represent different versions of code and build a history.

Commits not only represent a version of code, but also they contain a lot of extra information.

Every commit can also contain the following information:
- A summary of lines of code that were added, deleted, or changed, compared to the last commit
- A way to refer to the last commit/its "parent" commit
- A unique ID for the commit, often called the commit hash
- A commit message, which will be a string that describes the commit's contents
- The date and time that the commit was made

Large projects will be made of hundreds or thousands of commits.

## Teams Collaborate by Merging Histories

In a work day, we want any number of programmers to be able to write code, contribute commits, and build software.

Git is a version control system that allows for team collaboration. How?

Collaboration in this sense means that everyone can contribute changes to code, and look at those changes of code.

Every codebase that a team will collaborate on will have a **repository,** or a project folder that contains the files, versioned with Git. (This repository will likely be hosted on github.com)

Every developer who wants to contribute code will need access to the code and files, the repo's commit history, and a way to reference the team's repo. In order to get these three things, every developer will **clone that repo** onto their own machine.

When a developer clones the repo onto their machine, it will create a project folder on their computer, with all of the files inside of it. Then, each developer will write code, run tests, build features, **get updates from the team**, and **make commits.**

Then, each dev who has built commits will send the commits to the team's repository.

Recall that each commit includes this information:
- A summary of lines of code that were added, deleted, or changed, compared to the last commit
- A way to refer to the last commit/its "parent" commit

Using that information, Git (the tool) will go through a series of merging steps to create a unified history of commits.

Now, with a unified history of commits, the repo's history will grow. Software development with Git is a cycle of this process.

Callout:

Comparing Different Ways to Collaborate

Different versioning tools have different strategies. An older VCS used a system of _checking out a file for a period of time._ This VCS said that other team members could not open that file until that developer checked it back in!

## Check for Understanding


