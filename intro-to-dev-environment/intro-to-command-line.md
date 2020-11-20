# Intro to Command Line

## Learning Goals

- Create commands to navigate the file system through the command line using cd, ls, and pwd.
- Apply commands to create files and directories in command line using touch and mkdir.
- Apply the python3 command in the command line to run a Python script.

## Introduction

As a programmer, the terminal is one of our most important tools, and we will run thousands of commands in the terminal over our career. Before we get there, we should spend time familiarizing ourselves with the command line.

## Vocabulary and Synonyms

| Vocab          | Definition                                                                                                                                                     | Synonyms  | How to Use in a Sentence                                                                                                                                                                                                         |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| interface      | A medium that takes information from one source, and passes it to another source.The interface usually makes a meaningful translation between the two sources. | -         | "The command line and the terminal is one interface for how we interact with the file system and run programs on our computer," "That program has a graphical user interface, and there are buttons and images to interact with" |
| folder         | A named container of files and other folders (normally named sub-folders). Can be inside another folder.                                                       | directory | "I'm going to make another folder in this folder to organize things better," "Check to see if you put that file in the home directory"                                                                                           |
| Root directory | The nickname of the top-most folder that exists on the machine                                                                                                 | root      | "That program gets installed and its files live somewhere in root," "I don't usually spend much time in the root directory"                                                                                                      |

## Command Line vs. Terminal vs. Shell

In our curriculum, we will use "terminal" to mean an application that allows command input to interact with a computer, such as navigating, running programs, or making files. Often, developers use the phrases "terminal" and "console" interchangeably. In macOS, there is an application named Terminal, and we'll use that application to type in commands and use the command line.

The command line refers to the interface where developers type in commands into a terminal. The command line is the area in the terminal where we type in commands.

Often, a tutorial may stylize a command line prompt (or, command to input) with a `$` in the front. This `$` is to indicate the command line, and shouldn't be typed in.

```bash
$ ls
```

In this example, the user should execute the `ls` command by typing in `ls`.

A shell is a program that runs commands. It is the program that works between the command line and the computer's operating system, and runs our programs. There is a shell used in our terminal, that takes the commands we type in our terminal and executes them. In this curriculum, we will go into shells only at this level of depth.

Callout: There is some cool computing history about how the terms "console" and "terminal" have evolved! Follow your curiosity and look it up!

Callout: Our terminal can run several kinds of _text editors_, or programs that can read and modify text files. Over this curriculum, we will briefly cover some. However, programmers can have a lot of depth and excitement over text editors, and if you'd like to join, follow your curiosity and look it up!

## Navigating The File System

We will use the command line (in the terminal) and learn several commands to help us navigate a computer's file system.

**Here's a Metaphor:** Imagine our computer's entire file system is a house. This house contains main rooms that connect with each other. Each room can contain many pieces of furniture. A computer's file system is like the house, folders are like the rooms, and files are like the pieces of furniture.

We can only be in one room (folder) at a time. We can move pieces of furniture (files) between the different rooms (folders). In this house, we can also make or remove as many rooms (folders) or pieces of furniture (files) as we want!

In our terminal, **there is only one current working directory at a time;** the command line is only working in one folder (room) at a time. Navigating the file system in the command line means learning the commands to go between folders (rooms) and manipulate files (furniture).

### Commands

| Command in the Command Line | Description                                                                                                                | Notes                                                                                                                                                                                   |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pwd`                       | Print the path of the current working directory                                                                            | Use this command when you're lost in the terminal or need to confirm where you are; you can read this path to understand the pathway to get to the current working directory from root. |
| `ls`                        | List the visible files and folders that are inside of the current directory                                                | This command does not list hidden files or folders; there is a separate argument for that                                                                                               |
| `ls -A`                     | List all the files and folders inside of the current directory                                                             | The `-A` is an _argument_ to the `ls` command                                                                                                                                           |
| `cd somefolder`             | Change the working directory to the given path. This path is a relative path from the current location                     | In this example, `cd somefolder` will navigate to a sub-folder named `somefolder`                                                                                                       |
| `cd ..`                     | Change the working directory to the given path... And `..` is a nickname for "the parent folder of the current directory." | Use this command to go "up" one folder level                                                                                                                                            |
| `cd ~`                      | Change the working directory to the home directory                                                                         | Use this command to always go back home                                                                                                                                                 |

#### Feedback

The terminal tends to not give thorough feedback for when commands _work_. The terminal prefers to give feedback for when commands _don't work_. When commands don't work, the terminal will often print an error, such as:

```bash
cd: some-non-existing-folder: No such file or directory
```

### Home and Root

"Home directory" is the nickname of the user folder on a computer. This folder is important because it will contain:

- important system-wide configuration files for certain programs we will use like git or bash
- folders and sub-folders that contain our projects and code
- by default in macOS, has folders such as "Documents," "Pictures," "Application," "Desktop"

We can **always** navigate to the home directory with

```
$ cd ~
```

"Root directory" is the nickname of the top-most folder that exists on the computer. This folder can contain folders important to the whole system, including folders and files and programs needed to start, sleep, or run a computer. We can always navigate to the root directory with `$ cd /`.

Colloquially, a _project's_ root directory is the top-most _project_ folder.

## Working with Files and Folders in the File System

We can create and delete files and folders from the command line.

### Commands for Creating Files and Folders

| Command in the Command Line | Description                                                                                                                                          | Notes                                                                                                                             |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `mkdir new-folder-name`     | Creates a new folder with the given path and folder name. By default, this will create a new folder as a sub-folder in the current working directory | In this example, `mkdir new-folder-name` makes a new folder named `new-folder-name` inside the current directory.                 |
| `touch new_file.py`         | Creates a new file with the given path and file name. By default, this creates a new file inside the current working dierctory                       | In this example, `touch new_file.py` makes a new file named `new_file.py`. We should include the file extension in this filename. |

### Commands for Deleting Files and Folders

Files and folders deleted with these commands are difficult to recover; use them often and wisely!

| Command in the Command Line | Description                                                                                                                                                                 | Notes                                                                                                                             |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `rm -rf folder-name`        | Deletes the folder with the given path and folder name, and all of the files and folders inside of it. By default, this deletes the folder in the current working directory | In this example, `rm -rf folder-name` deletes the folder named `folder-name` inside the current directory.                        |
| `rm some_file.py`           | Deletes the file with the given path and file name. By default, this creates a new file inside the current working dierctory                                                | In this example, `touch new_file.py` makes a new file named `new_file.py`. We should include the file extension in this filename. | In this examle, `rm some_file.py` deletes the file named `some_file.py` inside the current directory. |

## Recommended File System Structure

As developers, over time, we will make hundreds of files and folders.

If you've never organized that many files and folders, and don't have a preference for how to organize, then we recommend that following this folder structure:

### `~/Developer`

- This is a folder where you put all of your developer-y code stuff!
- Make this folder with `$ mkdir ~/Developer` for the first time
- Navigate to this folder from any location in Terminal with `$ cd ~/Developer`, or using your relative commands to change directories

### `~/Developer/projects`

- This is a folder where you put all of your Ada projects
- Make this folder with `$ mkdir ~/Developer/projects` for the first time
- Navigate from anywhere with `$ cd ~/Developer/projects`

### `~/Developer/classroom`

- This is a folder where you put all of your notes, exercises, scratchwork, classroom activities, homework, etc
- Make this folder with `$ mkdir ~/Developer/classroom`
- Pick one of these two popular ways to organize your notes:
  - Organize notes by week. They will have sub-folders nested in here, such as `~/Developer/classroom/week-1`
  - Organize notes by topic. Recommended topic folder names are `git`, `cs-fun`, `python`, `flask`, `js`, `react`, so it is like `~/Developer/classroom/python`

Of course, feel free to not follow these recommendations if you have preferred ways of organizing files that will work for you better.

## Always Run Code with `python3`

This curriculum teaches programming in Python 3. By default, many macOS systems come with Python 2 installed. However, the differences between Python 3 and Python 2 are significant! It will become **crucial** to always execute our Python scripts from the command line and specify Python 3.

We can specify that we want to run specifically Python 3, we will always use this command:

```bash
python3 some_file.py
```

...where `some_file.py` is the (path and) name of the Python script we want to run.

If we forget to run our Python scripts with `python3`, there's a chance that the script runs as expected, and a chance that the script breaks or has bugs.

### !callout-info

## python3
"A lot of tutorials just use the `python` command to run Python scripts! Why? I'm not convinced that we need to use the `python3` command." One way to check if you need to use the `python3` command is to run two commands: `$ python --version` and `$ python3 --version`. If the output of these two commands differs (namely, `python` points to version 2), then we need to **avoid** using the `python` command.

### !end-callout

### !callout-info

## python3 
There are many methods to make shortcuts for the `python3` command, including terminal/bash aliases, and more. Follow your curiosity!

### !end-callout

## Continue Learning

It is crucial for our careers as developers to practice using the terminal, and to increase our skill in it. There are hundreds of more commands to learn.

We can make a commitment to ourselves to discover and learn more and more ways to use the command line, to help our development workflow become more and more robust.

Some commands to learn include:

- `man`
- `mv`
- `cat`
- `echo`
- `grep`

## Exiting Weird Screens on Terminal

Terminal and some commands bring us to different text editors. If you're ever taken to a terminal screen where:

- arrow keys or key presses don't seem to work as expected
- there is a `:` on the bottom line
- `ctrl+c` does not exit this screen

Try using the up and down arrows to scroll, and tapping the `q` or `esc` key to quit.  If you're ever in this situation, one of macOS's default text editors, [`vim`](https://en.wikipedia.org/wiki/Vim_(text_editor) is at play here! See more vim commands [with this vim resource](https://devhints.io/vim).

## Check for Understanding

## Check for Understanding
<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->

### !challenge

* type: multiple-choice
* id: 0d18747d-94a0-4136-85b1-49a1308ef647
* title: The command line 
<!-- * points: [1] (optional, the number of points for scoring as a checkpoint) -->
<!-- * topics: [python, pandas] (optional the topics for analyzing points) -->

##### !question

What is the command line? 

##### !end-question

##### !options

* The interface where developers type in commands into a terminal
* The top-most folder that exists on a machine
* a program that runs commands

##### !end-options

##### !answer

* The interface where developers type in commands into a terminal

##### !end-answer


### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->
