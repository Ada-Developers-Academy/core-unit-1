# Projects with Many Files

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

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---
| Module | Any `.py` file that contains functions, classes, variables, and/or other runnable code | - | "I used the `math.Euler()` from the `Math` module to calculate an angle" 
| Package | A collection of modules  | - | "The methods and classes accessible in a package can be found in the `__init__.py` file 

## New File Organization

Our projects so far contain source code, unit tests, git files, `README` files, configuration files (such as `requirements.txt`), etc. Now, with OOP, we're motivated to add to that; ideally, each class definition will have their own `.py` file. Consistent organization and management of these files can help make our code more navigable and discoverable. What kind of guidelines for folders and files can we follow?

Python projects do not have a _required_ file structure; different projects have different structures, and they are all valid and work. One example structure we can use is the following:

```
project_name/
├── README.md
├── requirements.txt
├── project_package_name
│   ├── __init__.py
│   ├── example_class_a.py
│   └── example_class_b.py
└── tests
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

Projects that have classes will have a `.py` file for each class. All of these files should live in one single folder. This folder may also contain an `__init__.py` file. Details about this special file are below.

Usually, this folder has the same name of the project, but must follow some package name rules (detailed below).

The above example names this folder `project_package_name`. It contains two class files, `example_class_a.py` and `example_class_b.py`, and an `__init__.py` file.

### Tests Live in a Test Folder

Projects that have multiple test files should organize these files into one `tests` folder.

The above example has a `tests` folder. It contains two test files, `example_c_test.py` and `example_d_test.py`.

### !callout-success

## Pro Tips: Use Your IDE to Your Advantage

When we work on projects using this folder structure, we will save time if we learn how to switch between files quickly. Every IDE contains its own features for navigating files. A pro-tip is to take the time to learn at least the following:

- How to expand and collapse any "file navigator" panes, that will show all of the folders and files in a project
- The keyboard shortcut for switching to a file by name

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

"Packages and modules" may seem like fancy words for "folders and files," but this terminology allows us to understand their **namespaces**. A module located inside of a package can be referenced using namespacing with `.`s, such as `package_name.module_name`. The package and module names are derived from the name of the folder and file (without `.py`).

For example, given this structure for a project named `ride-share-app`...

```
ride-share-app/
├── README.md
├── requirements.txt
├── ride_share_app
│   ├── __init__.py
│   ├── driver.py
│   └── passenger.py
└── tests
    ├── driver_test.py
    └── passenger_test.py
```

... There is one package named `ride_share_app`. It contains the modules `driver` and `passenger`. We might reference the _passenger module_ with `passenger` or `ride_share_app.passenger`, depending on our relative location.

### !callout-info

## Package and Module Naming Conventions
There aren't too many rules about package or module naming conventions, but a notable one is that they cannot contain hyphens (`-`) to be valid. [PEP-8](https://www.python.org/dev/peps/pep-0008/#package-and-module-names) recommends short, all-lowercase names. [PEP-423](https://www.python.org/dev/peps/pep-0423/) lists suggestions and guidelines for naming packages, namely for the purpose of public distribution.

### !end-callout

## Importing

Following the above folder structure alone is not enough to make classes in one module available to use in another. In order for Python to locate and load resources from other packages and modules, an additional step is needed.

We must _import_ any resources that we need from another module before we can use them in the current module, otherwise Python will report a `NameError`. Importing from another module into the current module allows the current module to access the other module's contents by name.

### Importing from Packages and Modules

There are _many_ different syntaxes and strategies we can use to import modules. If a particular import syntax works for a project, it's valid! Different situations will need to use different ways of importing.

As a starting point, let's look at one syntax for creating an import statement:

```python
from package_name.module_name import ExampleClassName
```

It may be helpful to read this line of code in "reverse order," as "Import an object named `ExampleClassName` that's defined in the `module_name` module that's located in the `package_name` package."

The above statement looks for the matching _package_ and _module within that package_. The search for the matching module begins ***relative to the file***. First, the program will look for the matching package and module in the current directory of this file. If there is no match, then our program will search for a matching package/module among all the installations of Python packages.

From that matching module, it will import anything defined in the module with the name `ExampleClassName`.

Now, after importing, we can use `ExampleClassName` in this file as much as we want!

Conventionally, these import statements are always at the top of a module.

### !callout-info

## Modules Know They're in the Same Package
Sometimes, it may be unnecessary to specify a package if both modules are in the same package already. For details on the locations that Python searches for modules (and their priority order), we can read about [Python's module search path order](https://docs.python.org/3/tutorial/modules.html#the-module-search-path).

### !end-callout

### Example Between Classes

Let's consider this file structure, and these two modules:

```
ride-share-app/
├── README.md
├── requirements.txt
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

scarlet = Passenger()
```

When we run the `passenger` module with `$ python3 ride_share_app/passenger.py` (which has the `Passenger` definition and `scarlet = Passenger()`), we get this runtime error:

```
I'm creating an instance of Passenger!
Traceback (most recent call last):
  File "ride_share_app/passenger.py", line 7, in <module>
    scarlet = Passenger()
  File "ride_share_app/passenger.py", line 5, in __init__
    self.favorite_new_driver = Driver()
NameError: name 'Driver' is not defined
```

`NameError: name 'Driver' is not defined` indicates that the `passenger` module can't instantiate `Driver` because it doesn't know what that is. We need to import the `Driver` class from the `ride_share_app.driver` module, first!

Adjusting the `passenger` module by only adding the top import line...

```python
from driver import Driver

class Passenger:

    def __init__(self):
        print("I'm creating an instance of Passenger!")
        self.favorite_new_driver = Driver()

scarlet = Passenger()
```

Now produces this output, which doesn't have a `NameError`!

```
I'm creating an instance of Passenger!
I'm creating an instance of Driver!
```

Again, the search for a matching module is relative to the file that is importing. In this example, the `driver` and `passenger` modules are in the same package, so there is no need to specify a package name. That's why `from driver` will suffice!

Inside the matching `driver` module, it will load whatever is defined with the name `Driver`, in this case, a class. Inside of our `passenger` module, now we can call `Driver()` or any other `Driver` behavior `Driver`!

## Debugging Imports

Here are some common bugs that we may come across with importing:

```
Traceback (most recent call last):
  File "ride_share_app/passenger.py", line 1, in <module>
    from non_existing_module import Driver
ModuleNotFoundError: No module named 'non_existing_module'
```

Where `passenger.py` looks like:

```python
from non_existing_module import Driver
```

- A `ModuleNotFoundError` is raised because the program can't find `non_existing_module`
- There's an import statement that can't find the specified module
    - Double-check the `from` part. Do we need to including the package name, if this file isn't in the same package? Or do we need to exclude it?

```
Traceback (most recent call last):
  File "ride_share_app/passenger.py", line 1, in <module>
    from driver import non_existing_class_or_function
ImportError: cannot import name 'non_existing_class_or_function' from 'driver'
```

Where `passenger.py` looks like:

```python
from driver import non_existing_class_or_function
```

- An `ImportError` is raised because we're trying to import an object named `non_existing_class_or_function` from an existing module `driver`
- There's an import statement that can't find what to import within the module
    - Double-check that the module defines what you're trying to import with the exact same name
    - This should be a class or function defined in the module

## Summary

## Check for Understanding

