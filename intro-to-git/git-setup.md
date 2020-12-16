# Git Setup

## Learning Goals

## Introduction

This document will be written more like a resource. These topics are necessary to understand, but are less frequently used than concepts for commits and collaboration. Use this lesson as a reference guide, and to inspire you to read more.

## Vocabulary and Synonyms

| Vocab | Definition | Synonyms | How to Use in a Sentence |
| ----- | ---------- | -------- | ------------------------ |

## Navigating GitHub.com

GitHub.com is a great and huge platform. There are a lot of features, and it's worth getting to know how to locate and use the following site features:

- Going to your own profile page
- Going to the page that lists your own repositories
- Going to the settings page
- Looking at an individual repo, such as
  - Looking at the list of folders and files in this repo
  - Identifying the README, whose contents are shown below

### Repos Have Names and Owners

Every repo has a name.

Every repo either belongs to a user or to an organization.

For example, this repo that lives here is named ` ` and belongs to ` `.

## Initializing a New Git Project

Projects are not tracked with Git (and therefore don't use Git) until it is initialized as a Git project.

To turn any folder into a Git project, run this command in the project root:

```bash
$ git init
```

Callout: On a technical level, this is creating a hidden folder named `.git` in the project root. This hidden folder contains a lot of Git settings for this project (including the Git history!)

## Forking an Existing Git Project For Yourself

The community model for GitHub encourages forking repos.

When developers see a repo that would be a good _base_ for a project, and the developer wants to remix this project for themselves, they can **fork** a project.

Forking creates a copy of the repo (including its code _and_ its Git history up to that point). This copy of the repo will belong to your own user account.

To fork a repo, use GitHub.com:

- Navigate to the repo's page on Github.com
- Locate the button to fork this repo. This button is likely towards the top right corner.
- Confirm that there is a new repo with the same name, but owned by your account
  - You can check the page that lists your repositories, too

### When Do You Fork?

A developer forks a repo when they need these things:

1. A repo with a copy of this Git history so far (and the code with it)
1. More ownership, control, and access over the repo, such as permissions to add collaborators or push commits
1. Separation from the original repo

## Cloning a Repo Onto Your Computer

When developers see a repo on GitHub.com, and want a copy of this repo on their own computer, they can **clone** the repo.

Cloning will create a new folder onto the computer. This folder will have the name of the repo. This folder will contain all of the folders, files, and Git history that was in the repo.

The process of cloning requires a clone URL that GitHub usually provides. Once you have this clone URL, the command to clone is:

```bash
$ git clone <clone url>
```

To clone a repo, the full process is:

1. Go to the repo's page on GitHub.com
1. Locate the button that opens details on downloading the code or cloning the project. This button is likely labeled "Code" and located towards the top right corner.
1. This button opens details about cloning. Select "HTTPS" as a setting for cloning the project.
1. Locate the clone URL inside of this pop-up. Copy this URL.
1. Switch back to your terminal
1. Run the `$ git clone <clone URL>` command
1. Confirm there's a new project folder and `cd` into it

### Clone with HTTPS

In the process above, it specified choosing "HTTPS" as a setting for cloning the project. This setting determines the protocol used for Git commands and operations; "HTTPS" will be more appropriate for our projects.

Callout: No really, Clone with HTTPS
Cloning with SSH is welcome, and is a great and wonderful way to clone! However, it requires additional setup not covered in this curriculum. This curriculum officially recommends cloning with HTTPS for now, but follow your curiosity!

### When Do You Clone?

A developer clones a repo when they need these things:

1. A repo's code and Git history to be downloaded onto their computer

## Configuring Defaults

### Configuring the Default Text Editor
