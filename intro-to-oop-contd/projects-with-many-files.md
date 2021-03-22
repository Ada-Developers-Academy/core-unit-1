# Projects With Many Files

## Learning Goals

- Use Python syntax to "link" two files together
- Demonstrate how code jumps between files when working with multiple classes
- Apply lessons about OOP to managing several classes in one project

## Introduction

Scarlet is making a ride share app. In her project, she has two classes, `Driver` and `Passenger`. She starts her project in one file, `main.py`. It's important that each `Passenger` instance has an attribute `favorite_new_driver`, which is an instance of `Driver`. Her code could look like:

```python
class Driver:

    def __init__(self):
        print("I'm creating an instance of Driver!")

class Passenger:

    def __init__(self):
        print("I'm creating an instance of Passenger!")
        self.favorite_new_driver = Driver()

scarlet = Passenger()
```

Even though we can define multiple classes in one `.py` file as long as we have the correct syntax, we may want to re-organize our code.

It's conventional to place each class definition in its own `.py` file. But then how does one class find out about another that it needs to use?

Let's take a look at what we need to do to use this method of organization in our own applications. The organizational style presented in this lesson is only a recommendation, but should be a good starting point for a variety of projects!

## Vocabulary and Synonyms

| Vocab   | Definition                                                                              | How to Use in a Sentence                                                                |
| ------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Module  | Any `.py` file that contains functions, classes, variables, and/or other runnable code | "I used the `math.Euler()` from the `Math` module to calculate an angle"                |
| Package | A collection of modules                                                                | "The `requests` package contains modules to help us make HTTP requests." "My package has custom configuration in its `__init__.py` file." |

## New File Organization

Our projects so far contain source code, unit tests, git files, `README` files, configuration files (such as `requirements.txt`), etc. Now, with OOP, we're motivated to add to that; ideally, each class definition will have its own `.py` file. Consistent organization and management of these files can help make our code more navigable and discoverable. What kind of guidelines for folders and files can we follow?

There is no single _required_ structure for Python projects; different projects have different structures, and any structure that works for a project is valid. But a good place to start is the following common setup:

```
project_name/
├── README.md
├── requirements.txt
├── project_package_name
│   ├── __init__.py
│   ├── __main__.py
│   ├── example_class_a.py
│   └── example_class_b.py
└── tests
    ├── __init__.py
    ├── example_c_test.py
    └── example_d_test.py
```

Let's examine the various parts of this project structure.

### Project Root

As we have have been doing for our previous projects, our OOP project should be stored in its own folder, normally referred to as the **project root**. This folder holds all the files related to the current project. Ideally, the folder should have the same name as the project.

Our example project root is named `project_name`.

### Configuration and Miscellaneous Files

Files such as `README.md`, `requirements.txt`, and any virtual environment folders (like `venv`) should live in the project root, not nested in any folders.

Often, files and folders are in the project root because it makes the most logical sense, and there isn't a better folder. `README.md`, `requirements.txt`, and the `venv` folder are all examples of this. Some configuration files will need to be in the project root in order for them to work.

### Project Code Lives in a Package Folder

Under the project root, we will have a single folder to contain all of our project classes, one class per `.py` file. We refer to this folder as the **package folder**. At the start of a project, when we don't have many class files, we might put them all directly in the package folder. But as the project becomes more complex, we can add subfolders to further group together related class files.

There are also a number of special files that can be placed in the package folder.

The most common of these is called the `__init__.py` file, which is discussed briefly in the Package Details section below.

Projects with a clear starting point might include a `__main__.py` as a fairly standard place to put the application start up logic. Some projects may not need this file, and some might choose to put that logic somewhere else.

Our package folder usually has the same name as the project, but it must follow some package naming rules (detailed below).

The above example names this folder `project_package_name` so that we can distinguish it from the project root, but there would be nothing preventing us from calling it `project_name` to match the project root name. It contains two class files, `example_class_a.py` and `example_class_b.py`, and both an `__init__.py` file and a `__main__.py`.

### Tests Live in a Test Folder

Projects that have multiple test files should organize them under one `tests` folder.

When we start a project and have only a few test files, placing them all directly in the `tests` folder is reasonable. As the number of test files increases, we often organize the tests using the same subfolder structure we use to organize our class files.

The above example has a `tests` folder. It contains two test files, `example_c_test.py` and `example_d_test.py`, and an `__init__.py` file.

### !callout-success

## Pro Tips: Use Your IDE to Your Advantage

When we work on projects using this folder structure, we will save time if we learn how to switch between files quickly. Every IDE contains its own features for navigating files. A pro-tip is to take the time to learn at least the following:

- How to expand and collapse any "file navigator" panes, that will show all of the folders and files in a project
- The keyboard shortcut for switching to a file by name
- The keyboard shortcut for switching among recently used files

### !end-callout

## Python Details: Packages and Modules

As Pythonists, it will benefit us to understand how Python defines packages and modules.

In Python...

- A **package** is a folder that:
  - Contains _modules_
  - Contains a special file named `__init__.py`
    - The presence of this file informs Python that the folder containing it should be treated as a named package
    - Often, this file is completely empty!
    - Sometimes, it may contain configuration logic
  - Can contain other packages
- A **module** is a `.py` file that can contain any number of functions, classes, and variables, as well as other runnable code
  - Essentially, any Python file can be thought of as a module. In fact, we've been writing modules this whole time!

"Packages and modules" may seem like fancy words for "folders and files," but this terminology allows us to understand their **namespaces**. A module located inside of a package can be referenced using namespacing with dot notation, such as `package_name.module_name`. The package and module names are derived from the name of the folder and file (without `.py`).

### !callout-warning

## Be Sure to Create an `__init__.py` File in Each Package Folder

If we forget to create the `__init__.py` file, things may still seem to work. However, without this file, Python will interpret the folders as a slightly different kind of package. For most situations, we should create the `__init__.py` file in each package folder and subfolder, even if it is empty!

### !end-callout

For example, given this structure for a project named `ride-share-app`:

```
ride-share-app/
├── README.md
├── requirements.txt
├── ride_share_app
│   ├── __init__.py
│   ├── driver.py
│   └── passenger.py
└── tests
    ├── __init__.py
    ├── driver_test.py
    └── passenger_test.py
```

There is one package named `ride_share_app`. It contains the modules `driver` and `passenger`. We might reference the _passenger module_ with `.passenger` or `ride_share_app.passenger`, depending on our relative location.  More on why shortly!

### !callout-info

## Package and Module Naming Conventions

Notice in the example that the package name uses underscores (`_`) rather than hyphens (`-`). There aren't too many rules about package or module naming conventions, but a notable one is that they cannot contain hyphens. Python package names must be valid identifier names and tend to follow variable- or function-style naming. So while hyphens are valid in file names, we can't use them in files that will be part of a package or module name. *Take a moment to think about why identifiers cannot contain hyphens.*

<br />

[PEP-8](https://www.python.org/dev/peps/pep-0008/#package-and-module-names) recommends short, all-lowercase names. [PEP-423](https://www.python.org/dev/peps/pep-0423/) lists suggestions and guidelines for naming packages, namely for the purpose of public distribution.

### !end-callout

## Importing

Following the above folder structure alone is not enough to make classes in one module available to use in another. In order for Python to locate and load resources from other packages and modules, an additional step is needed.

We must _import_ any resources that we need from another module before we can use them in the current module, otherwise Python will report a `NameError`. Importing from another module into the current module allows the current module to access the other module's contents by name.

### Importing from Packages and Modules

There are three common ways that we will see packages and modules imported into our projects.

Regardless of the `import` style used, we should prefer to put `import` statements near the top of the file doing the importing. It _is_ valid syntax to put `import` statements elsewhere in a file, but by putting them near the top, other programmers will know where to look for the modules on which our module depends.

#### 1. Importing a Module by Name

This method is especially common for modules that are built-in to Python. We will tend _not_ to use this method when importing modules from our own packages, but we should be comfortable seeing it in other code, and using it to access built-in Python features.

As an example, consider the `random` module, which provides the `randint` function.

```python
import random
```

This statement imports the `random` module name into the current scope, allowing us to access identifiers in the module by using dot notation to look inside the module name as follows:

```python
my_random_int = random.randint(0, 5)
```

Python has many built-in modules, and Python will _always_ prefer them over any modules we write that share the same name. So we should take care to avoid using their names for our own modules, or make sure to put such modules into a package of our own!

#### 2. Importing a Package Module by Full Name

When we write our own modules, it is a best practice to gather them together into a package. As long as we pick a package name that doesn't match a built-in module, this lets us carve out a space to name our own types and functions.

To import the `driver` module from the `ride_share_app` package example above, we could use the following command.

```python
import ride_share_app.driver
```

This statement imports the `ride_share_app` package name into the current scope. It further imports the `driver` module as a member of the `ride_share_app` package, allowing us to access identifiers in the module by using dot notation. Consider:

```python
driver = ride_share_app.driver.Driver()
```

Assuming there is an identifier called `Driver` in the `driver` module and that it is a class, this would make a new instance and store a reference to it in the `driver` variable. Notice that there is no issue with having a variable in the current scope that matches a module name in a package. The `driver` variable name and the `driver` module name exist in two separate scopes.

### !callout-info

## Why We Keep Saying Identifier
Notice that we have been careful to say that Python imports identifiers into the current scope. Identifiers are names of things. Variables, functions, and classes are all named with identifiers. From just looking at an identifier, we don't know what it refers to. So we have to be careful to import the correct identifiers, and then use them as they are intended to be used. 

<br />

Hopefully good naming practices were employed to help hint at the proper usage of different identifiers. But if we import an identifier that refers to a value (a variable) but then try to call it like a function, this will result in a runtime error! So it's our job to read and understand the code or documentation of the module we want to use so that we import and make use of its identifiers correctly!

### !end-callout

#### 3. Importing Module Identifiers using Relative Names

Importing package modules by full name works everywhere, whether from outside or inside a package. But to access the identifiers defined in the module, we have to prefix them with the full package name. If our package were several layers deep, this could make for some long names! 

Let's say that the `passenger` module in our `ride_share_app` package needs to make use of the `Driver` class. We could certainly import the `driver` module as before and access the `Driver` class with the full package name. But `driver.py` and `passenger.py` are defined in the same package. In fact, they're in the same folder. Wouldn't it be nice if there were a shorter way?

There is!

```python
from .driver import Driver
```

This may look a little weird. It might even seem backwards! Feel free to read this statement from right to left if that's helpful!

What this statement does is:

1. Use the `from` keyword to name the module from which we want to import an identifier.
1. Use the `import` keyword to name the identifier we want Python to import into the current scope

The module name looks different from the examples we've seen before. It starts with a `.` which tells Python to look for the module in the folder containing the current file. When Python finds the specified module, rather than importing the name of the module into the current scope, it looks at the names listed after `import` (we can write multiple names separated by commas) and imports just those identifiers into the current scope.

If we assume as before that the `Driver` identifier is a class, this lets us write the following:
```python
driver = Driver()
```

Shorter and clearer!


```
├── ride_share_app
│   ├── __init__.py
│   ├── driver.py
│   ├── passenger.py
│   └── payment
        ├── __init__.py
        ├── cash.py
        └── credit.py
```

If our package had a folder called `payment` under `ride_share_app` (with an `__init__.py` file), and `payment` had the modules `cash.py` and `credit.py`, then from either of these modules we could access the `Driver` identifier in `driver.py` as:

```python
from ..driver import Driver
```

We added another `.` at the beginning, which tells Python to look up one folder. In principle, we can preface the name we give to `from` with as many `.`s as needed to move us up through folders in the package.

### Importing With `from` Works for All Import Methods

Using `from` to name a module, and then importing specific symbols is very useful. It's so useful that we can also use the `from` style to import from built-in modules and modules using their full package name as well!

```python
from random import randint
from ride_share_app.driver import Driver

my_random_int = randint(0, 5)
driver = Driver()
```

### Handling Duplicate Names

There is one more optional keyword that can be used with `import` statements. What if there are two modules we want to use: `module_one`, and `module_two`, and each of these modules provides an identifier `UsefulClass`? The following doesn't cause an error, but something's not right:

```python
from module_one import UsefulClass
from module_two import UsefulClass
```

After the second `import`, `UsefulClass` only refers to the version from `module_two`. Of course we could import the entire modules and use dot notation to access the appropriate `UsefulClass` as needed, but we can also import the two versions as:

```python
from module_one import UsefulClass as UsefulClassOne
from module_two import UsefulClass as UsefulClassTwo
```

Instead of importing the identifier `UsefulClass` into the current scope and then overwriting it, this second version imports each of the `UsefulClass` variables into two separate identifiers: `UsefulClassOne`, and `UsefulClassTwo`, which we can use as:

```python
one = UsefulClassOne()
one.do_something()
two = UsefulClassTwo()
two.do_something_else()
```

### So Many Ways to Import

As we have shown, there are _many_ different syntaxes and strategies we can use to import modules. If a particular import syntax works for a project, it's valid!

Different situations will need to use different ways of importing. So we should be ready to see many styles of importing. We may even encounter styles that we haven't discussed that we might need to look up. That's ok! But we should feel confident that we can recognize importing when we see it!

## Restructuring a Project

Let's return to Scarlet's project and see how she decides to reorganize her project. Remember that she started with a single file `main.py` that contained two classes, `Driver` and `Passenger`, and there was some main logic to create a `Passenger` instance.


Scarlet is making a ride share app, so she decides to call her project root `ride-share-app`. She puts her standard project files in the project root. She knows that in Python we like to have each class in its own module, and that the modules for a project are usually grouped into a package. She can't use hyphens in the package name, so she decides on `ride_share_app` as her package name. She makes the folder, adds the `__init__.py` file to tell Python this is a package folder, then makes a module file for each class: `driver.py` and `passenger.py`.

She considers renaming the `main.py` which now only contains the application startup to `ride_share_app.py` to be a little more descriptive on the command line. But Scarlet learned about another strategy for where to put her startup code that she wants to try, so for now she leaves the code in `main.py`

This gives Scarlet the following file structure:

```
ride-share-app/
├── README.md
├── requirements.txt
├── main.py
└── ride_share_app
    ├── __init__.py
    ├── driver.py
    └── passenger.py
```

`driver.py`:

```python
class Driver:

    def __init__(self):
        print("I'm creating an instance of Driver!")
```

`passenger.py`:

```python
class Passenger:

    def __init__(self):
        print("I'm creating an instance of Passenger!")
        self.favorite_new_driver = Driver()
```

`main.py`:
```python
scarlet = Passenger()
```

She runs the project with `python3 main.py`, but she gets this runtime error:

```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    scarlet = Passenger()
NameError: name 'Passenger' is not defined
```

`NameError: name 'Passenger' is not defined` indicates that the main file can't instantiate `Passenger` because it doesn't know what that is. She needs to import the `Passenger` class from the `ride_share_app.passenger` module first!

She fixes `main.py` with an `import` statement as follows:

```python
from ride_share_app.passenger import Passenger

scarlet = Passenger()
```

She runs the project again with `python3 main.py` and gets a slightly different error:

```
I'm creating an instance of Passenger!
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    scarlet = Passenger()
  File "ride_share_app/passenger.py", line 5, in __init__
    self.favorite_new_driver = Driver()
NameError: name 'Driver' is not defined
```

She sees the expected `print` output from inside the `Passenger __init__` method. But there's another `NameError`. This time it's in the `passenger.py` module where she instantiated a new `Driver`. Here again, Python doesn't know what the `Driver` identifier refers to since it hasn't been imported. But Scarlet knows exactly how to fix this! She adds an `import` statement to `passenger.py`:

```python
from .driver import Driver

class Passenger:

    def __init__(self):
        print("I'm creating an instance of Passenger!")
        self.favorite_new_driver = Driver()
```

This `import` tells Python to get the `Driver` identifier from the `driver` module located in the same folder as `passenger.py`. Running once more with `python3 main.py`, Scarlet gets the following output:


```
I'm creating an instance of Passenger!
I'm creating an instance of Driver!
```

No more `NameError` problems!

Scarlet used an appropriate `import` statement for each case where Python needed to know where to find the identifier. From `main.py` she had to use a package full name import, since `main.py` is not part of the `ride_share_app` package. But from `passenger.py` she could use a relative `import`, since `passenger.py` and `driver.py` are in the same package.

## Moving Startup Logic Into Our Package

There are many approaches to where we should put the code that starts our applications.  Python doesn't have a strong opinion about this. Leaving it in a `main.py` file is fine. Using a different file name that's more descriptive of our project is also fine.

Applications written in Python often include extra files so that the end user doesn't have to worry about exactly the command line to use. For instance, when we use `pytest` we run the command `pytest`. But this command is really only used to locate and run the real application startup for `pytest` which is actually in a really weird place!

Another way we can run `pytest` is with the following command:

```python
python3 -m pytest
```

This might look a little familiar. This is the same style of command we use to create our virtual environments:

```python
python3 -m venv venv
```

If the argument to `-m` is a module name, Python runs the module in the context of its package (so relative package imports would work). If the argument is a package name (as in the examples), Python looks for a special file called `__main__.py` in the specified package and runs that! We can think of the `-m` argument as standing for _main_ or _module_ to help us remember what it does.

_We_ can follow this pattern in our own code as well. Since this is a semi-standard Python pattern, other users who download our code should understand how it works. Again, Python will let us start our programs however we like, and as long as we communicate how to use our program to our users, anything that works is a valid approach! But let's see how Scarlet can use this pattern in her ride share app.

Remember that she left the startup logic for her app in the `main.py` file, which is _not_ a part of her package. To start with, she can move the file into her package, and rename it to `__main__.py`.

```
ride-share-app/
├── README.md
├── requirements.txt
└── ride_share_app
    ├── __init__.py
    ├── __main__.py
    ├── driver.py
    └── passenger.py
```

Now Scarlet can run her app with the following command:

```python
python3 -m ride_share_app
```

She runs the app and gets the same output as before. Great! But she remembers that she had to use a package full name `import` in `main.py` since it wasn't in the `ride_share_app` package. What if she changes that to a relative import?

She changes the `import` in `__main__.py` as follows:

```python
from .passenger import Passenger

scarlet = Passenger()
```

She runs the app once more with `python3 -m ride_share_app` and sees that everything is still working fine!

We can do the same thing in our own projects if we like how this looks. There are many ways to start Python programs, so if this is an interesting topic, we can consider looking into how some Python tools we like let their users run them. Follow your curiosity!

## Debugging Imports

Here are some common bugs that we may come across with importing:

### `ModuleNotFoundError`

```
Traceback (most recent call last):
  ... (some details omitted for clarity) ...
  File "ride_share_app/passenger.py", line 1, in <module>
    from non_existing_module import Driver
ModuleNotFoundError: No module named 'non_existing_module'
```

Where `passenger.py` looks like:

```python
from non_existing_module import Driver
```

The `ModuleNotFoundError` is raised because the program can't find `non_existing_module`. In general, this error tells us:

- There's an `import` statement that can't find the specified module
  - Double-check the `from` part. Do we need to including the package name, if this file isn't in the same package? Ar we missing a `.` (one or more) for a relative import?

### `ImportError`

```
Traceback (most recent call last):
  ... (some details omitted for clarity) ...
  File "ride_share_app/passenger.py", line 1, in <module>
    from .driver import non_existing_class_or_function
ImportError: cannot import name 'non_existing_class_or_function' from 'ride_share_app.driver'
```

Where `passenger.py` looks like:

```python
from .driver import non_existing_class_or_function
```

The `ImportError` is raised because we're trying to import an identifier that can't be found,  `non_existing_class_or_function`, from an existing module `driver`. In general, this error tells us:

- There's an `import` statement that can't find what to import within the module
  - Double-check that the module defines what we're trying to import with the exact same name
  - The name should refer to a top-level class, function, or variable defined in the module

## Summary

## Check for Understanding

<!-- The first question (Project Structure) should use a main.py, or some other file outside the package to hold the main logic. Generally, only logic related to the setup of the package or package-level exports should be in init.py

For the second question (Importing modules)

it refers to guest.py in the question and the file label, but the class shown is Host, so change the filenames to match
consider rephrasing to something like "if we try to use the host.py module in our project" rather than "running" it. We shouldn't encourage running package modules directly. -->


<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- prettier-ignore-start -->

### !challenge

* type: multiple-choice
* id: 46c0a465-88fe-4b98-b012-e12f2818525a
* title: Projects With Many Files

##### !question

Consider a project for a photo filtering app that can select from any of the cameras on a device, and apply any of several available filters. We started working on this project, and all the classes are in a single file called `photo_app.py`. A simplified version is given here:

```python
# adds cat ears to any portrait
class CatEarsFilter:
    pass

# tints a photo to use sepia tones
class SepiaFilter:
    pass

# produces a picture using the back-facing camera
class BackCamera:
    pass

# produces a picture using the front-facing camera
class FrontCamera:
    pass

class Processor:
    def __init__(self, image_source, filter):
        self.image_source = image_source
        self.filter = filter

    def filter_image(self):
        return self.filter(self.image_source)

# returns an image source instance based on user input
def select_image_source():
    pass

# returns a filter instance based on user input
def select_filter():
    pass

# writes an image to storage
def save_image(image):
    pass

camera = select_image_source()
filter = select_filter()
processor = Processor(camera, filter)
save_image(processor.filter_image())
```

Which option best captures a possible layout for this project?

##### !end-question

##### !options

* ```
photo-app/
├── README.md
├── requirements.txt
├── photo_app.py
├── photo_app_pkg
│   ├── processor.py
│   ├── filters
│   │   ├── cat_ears_filter.py
│   │   └── sepia_filter.py
│   └── image_source
│       ├── back_camera.py
│       └── front_camera.py
└── tests
    ├── processor_test.py
    ├── filters
    │   ├── cat_ears_filter_test.py
    │   └── sepia_filter_test.py
    └── image_source
        ├── back_camera_test.py
        └── front_camera_test.py
```
* ```
photo-app/
├── README.md
├── requirements.txt
├── photo_app
│   ├── __init__.py
│   ├── __main__.py
│   ├── processor.py
│   ├── filters
│   │   ├── __init__.py
│   │   ├── cat_ears_filter.py
│   │   └── sepia_filter.py
│   └── image_source
│       ├── __init__.py
│       ├── back_camera.py
│       └── front_camera.py
└── tests
    ├── __init__.py
    ├── processor_test.py
    ├── filters
    │   ├── __init__.py
    │   ├── cat_ears_filter_test.py
    │   └── sepia_filter_test.py
    └── image_source
        ├── __init__.py
        ├── back_camera_test.py
        └── front_camera_test.py
```
* ```
photo-app/
├── README.md
├── requirements.txt
└── photo_app
    ├── __init__.py
    ├── __main__.py
    ├── processor.py
    ├── filters
    │   ├── __init__.py
    │   ├── cat_ears_filter.py
    │   └── sepia_filter.py
    ├── image_source
    │   ├── __init__.py
    │   ├── back_camera.py
    │   └── front_camera.py
    └── tests
        ├── __init__.py
        ├── processor_test.py
        ├── filters
        │   ├── __init__.py
        │   ├── cat_ears_filter_test.py
        │   └── sepia_filter_test.py
        └── image_source
            ├── __init__.py
            ├── back_camera_test.py
            └── front_camera_test.py
```
* ```
photo-app/
├── README.md
├── requirements.txt
├── photo_app
│   ├── __init__.py
│   ├── __main__.py
│   ├── back_camera.py
│   ├── cat_ears_filter.py
│   ├── front_camera.py
│   ├── processor.py
│   └── sepia_filter.py
└── tests
    ├── __init__.py
    ├── back_camera_test.py
    ├── cat_ears_filter_test.py
    ├── front_camera_test.py
    ├── processor_test.py
    └── sepia_filter_test.py
```

##### !end-options

##### !answer

* ```
photo-app/
├── README.md
├── requirements.txt
├── photo_app
│   ├── __init__.py
│   ├── __main__.py
│   ├── processor.py
│   ├── filters
│   │   ├── __init__.py
│   │   ├── cat_ears_filter.py
│   │   └── sepia_filter.py
│   └── image_source
│       ├── __init__.py
│       ├── back_camera.py
│       └── front_camera.py
└── tests
    ├── __init__.py
    ├── processor_test.py
    ├── filters
    │   ├── __init__.py
    │   ├── cat_ears_filter_test.py
    │   └── sepia_filter_test.py
    └── image_source
        ├── __init__.py
        ├── back_camera_test.py
        └── front_camera_test.py
```

##### !end-answer

##### !explanation

A good default layout is to have our general project files in the project root. Then we create two top-level packages, one for our application code, and one for the tests. The structures under each should generally mirror one another.  Each package folder should have an `__init__.py` file. And when we start dealing with a number of files, some of which are more closely related to each other than the rest of the package, we should consider creating subfolders to group the related types.

##### !end-explanation

### !end-challenge
<!-- prettier-ignore-end -->
<!-- ======================= END CHALLENGE ======================= -->

<!-- prettier-ignore-start -->
### !challenge

* type: multiple-choice
* id: f032adcb-c05b-4591-96b9-58bc24d7ee79
* title: Projects With Many Files

##### !question

Hosts for AdaBnB can host guests at multiple properties on the app. Each property is an instance of a `Place` class. If we tried to call the `create_places` method of `Host`, we would receive a `NameError`. Assuming the `place` module in which the `Place` class is defined is in the same package folder as `host.py`, select the option that best describes how to solve this `NameError`.

`host.py`
``` Python
class Host:
    def __init__(self, name, host_properties):
        self.name = name
        self.host_properties = host_properties
        print(f"I'm creating an instance of a Host named {self.name}!")

    def create_places(self):
        properties = []
        for host_property in self.host_properties:
            new_place = Place(host_property)
            properties.append(new_place)
        return properties
```

##### !end-question

##### !options

* `from place import Place` at the beginning of `host.py`
* `from .place import Place` right before we set `new_place` to an instance of the `Place` class.
* `from .place import Place` at the beginning of `host.py`
* `import Place` at the beginning of `host.py`

##### !end-options

##### !answer
* `from .place import Place` at the beginning of `host.py`
##### !end-answer

##### !explanation

Since the two modules, `host.py` and `place.py` are in the same package folder, we can use either package full name importing or relative importing to import `Place`. Of the two, there are only options given for relative importing, so we must select an option with `from .place import Place` in the answer.

<br />

The two options differ in terms of placement. While the code would work if we put the `import` statement just before using the `Place` class, we should prefer to put `import` statements near the top of the file.

##### !end-explanation


### !end-challenge
<!-- prettier-ignore-end -->
