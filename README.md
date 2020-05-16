# CS4All - Summer Curriculum
Created by: Jiin Jeong
### Week 1-5: Python Beginner
#### Week 1: Introduction to CS
* **What is Python?**: A programming language is a set of instructions for a computer to perform specific tasks. There are many programming languages including Java, C, C++, Ruby, etc. Python is an interpreted, high-level, general-purpose programming language created in 1991 by the Dutch programmer Guido van Rossum. The current stable release is version 3.8, so we typically say we are using Python3.
* **REPL**: [REPL](repl.it) is an online-based text editor. Advantage is that it supports many programming languages and that you don't need to download anything to run the program.
* **Print**: Prints a message to the screen.
```python
    print("Hello world")
```
* **Data types**: There are four primitive data types in Python: string (str), integer (int), floating-point numbers (float), and booleans (bool).
  * Strings are sequences of characters. They are in single-quotes ('') or double-quotes (""). For example, "Hello", "123", and "abc."
  * Integers are numeric values without decimals, such as 0, 2, 10.
  * Floats are more complex numeric values with decimals, such as 0.001, 0.5, 0.2.
  * Booleans are True/False.
  * We can check with `type()`.
```python
    print(type("Hamilton College"))
    print(type(10))
    print(type(0.11))
    print(type(True))
```
* **When to use what?**:
  * Name --> String
  * Address --> String
  * License Plate --> String (although it contains numeric values)
  * Household size --> Integer (you can't have 2.2 humans)
  * Number of pets --> Integer
  * Bank balance --> Float
  * Marital status --> Bool (True/False)
* **Comment**: To make single-line comments, you use a hashtag (#). Multiline comments are in three double-quotes (""" """). Computer will not execute comments. They are useful as they can explain to you/other programmers what your code does. 
```python
   # This is a single-line comment.
   """ 
     This is a multi-line
     comment that can span over
     multiple lines.
   """
```
* **Variable**: Stores a value that can be changed (contrast with constant).
```python
    var_name = value    # The value can be of any data type (str/int/float/bool)
    # 1. Use a descriptive name
    something = "USA"   # X
    country = "USA"     # O
    # 2. Instead of spaces, use underscore (_)
    first name = "Jiin"  # X
    first_name = "Jiin"  # O
    # 3. Can't start with a number
    1lesson = "intro"    # X
    lesson1 = "intro"    # O
```
* **Input**: Allows user input, adding interactivity to your program.
* **String Concatenation**: Strings can be added with +.
```python
    name = input("What is your name? ")
    print("Hello " + name)
```
* Function (Defining/Calling)
* Main function
* Comment
* [Potential Projects](https://github.com/jiinjeong/CS4All/blob/master/PythonBeg/week1.py) (Lab/Assignment)

#### Week 2: Math
* Type Casting / Type Conversion
* String Interpolation
* Math
* [Potential Projects](https://github.com/jiinjeong/CS4All/blob/master/PythonBeg/week2.py) (Lab/Assignment)

#### Week 3: Conditions and If Statement
* Conditions
* and, or, not, in
* If-elif-else
* [Potential Projects](https://github.com/jiinjeong/CS4All/blob/master/PythonBeg/week3.py) (Lab/Assignment)

#### Week 4: List, Indexing, and Random Library
* String Indexing
* List Indexing
* Import
* [Potential Projects](https://github.com/jiinjeong/CS4All/blob/master/PythonBeg/week4.py) (Lab/Assignment)

#### Week 5: Git and Markdown
* Basic Git
* Additional skills that students may need to finish their independent project

### Week 6-8: HTML/CSS
#### Week 6
* What is HTML/CSS?
* Tags: <h1> </h1>
* [Potential Projects](https://github.com/jiinjeong/CS4All/blob/master/HTMLCSS/week1.html)

#### Week 7
* [Potential Projects](https://github.com/jiinjeong/CS4All/blob/master/HTMLCSS/week2.html)

#### Week 8
* [Potential Projects](https://github.com/jiinjeong/CS4All/blob/master/HTMLCSS/week3.html)

### Week 1-5: Python Intermediate
#### Week 1: Loop 1: For-loop
* [Potential Projects](https://github.com/jiinjeong/CS4All/blob/master/PythonMed/week1.py)
#### Week 2: Loop 2: While-loop
* [Potential Projects](https://github.com/jiinjeong/CS4All/blob/master/PythonMed/week2.py)
#### Week 3: Loop 3: Nested loop, break/continue/pass
* [Potential Projects](https://github.com/jiinjeong/CS4All/blob/master/PythonMed/week3.py)
#### Week 4: Classes and Objects
* [Potential Projects](https://github.com/jiinjeong/CS4All/blob/master/PythonMed/week4.py)
#### Week 5: Errors, API, Additional Python
* [Potential Projects](https://github.com/jiinjeong/CS4All/blob/master/PythonMed/week5.py)
### Extra
#### Command Line Interface (CLI)
### Student Projects
To be updated.
