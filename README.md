# CS4All - Summer Curriculum
Created by: Jiin Jeong<br/>
Note to collaborators: Add your ID (@) for the curriculum/projects that you created or helped create.
### Week 1-5: Python Beginner
#### Week 1: Introduction to CS (@jiinjeong)
* **What is Python?**: A programming language is a set of instructions for a computer to perform specific tasks. There are many programming languages including Java, C, C++, Ruby, etc. Python is an interpreted, high-level, general-purpose programming language created in 1991 by the Dutch programmer Guido van Rossum. The current stable release is version 3.8, so we typically say we are using Python3.
* **REPL**: [REPL](repl.it) is an online-based text editor. Advantage is that it supports many programming languages and that you don't need to download anything to run the program.
* **Print**: Prints a message to the screen.
```python
    print("Hello world")
```
* **Data types**: Tells the computer how the programmer intends to use the data. There are four primitive data types in Python: string (str), integer (int), floating-point numbers (float), and booleans (bool).
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
  * Number of pets --> Integer (you can't have 2.2 dogs)
  * Zipcode --> Integer
  * Bank balance --> Float
  * Height/Weight --> Float
  * Marital status --> Bool (True/False)
  * Shipment status --> Bool (True/False)
* **Comment**: To make single-line comments, you use a hashtag (#). Multiline comments are in three double-quotes (""" """). Computer will not execute comments. They are useful as they can explain to you/other programmers what your code does.
```python
   # This is a single-line comment.
   """
     This is a multi-line
     comment that can span over
     multiple lines.
   """
```
* **Variable**: Stores a value; can be changed (contrast with constant).
```python
    var_name = value    # The value can be of any data type (str/int/float/bool)
    # 1. Use a descriptive name
    something = "USA"   # X
    country = "USA"     # O
    # 2. Instead of spaces, use underscore (_)
    first name = "Jiin" # X
    first_name = "Jiin" # O
    # 3. Can't start with a number
    1score = 100        # X
    score1 = 100        # O
    # 4. Variable names are case-sensitive (Name and name are different). Usually, we should start with a lowercase.
    Is_student = False  # O
    is_student = False  # O
```
* **Input**: Allows user input, adding interactivity to your program.
* **String Concatenation**: Strings can be added with +.
```python
    name = input("What is your name? ")
    print("Hello " + name)
```
* **Function**: Block of code that is only run when called. Functions are useful for code organization and reusability. Analogy: You can think of a function as a "file" for your code. You create a file with content that serve a purpose. To access a file, you have to open the file (=call the file).
```python
# Defining a function
def func_name():
    print("Hello)"  # Anything inside the function, indent with four spaces.
# Calling a function
func_name()
```
Actual example:
```python
# Defining a function
def greet():
    print("Hello)"  # Anything inside the function, indent with four spaces.
# Calling a function
greet()
```
* **Main function**: Acts as the starting point of execution for the code.
```python
def main():
    greet()

if __name__ == "__main__":
    main()
```
* [Potential Projects](https://github.com/jiinjeong/CS4All/blob/master/PythonBeg/week1.py) (Lab/Assignment)

#### Week 2: Math (@Ian)
* **Math**
    * Addition (+)
    ```python3
    >>> 10 + 7
    17
    ```
    * Subtraction (-)
    ```python3
    >>> 5 + 47
    52
    >>> 4 - 12
    -8
    ```
    * Multiplication (*)
    ```python3
    >>> 4 * 12
    48
    >>> 2 * -9
    -18
    ```
    * Division (/)
    ```python3
    >>> 140 / 5
    28
    ```
    * Integer division (//): Division with truncation - rounding down
    ```python3
    >>> 25 // 5
    5
    >>> 26 // 5
    5
    >>> 9 // 2
    4
    ```
    * Modulus (%): Remainder after division.
    ```python3
    >>> 27 % 5  # 27 divided by 5 is 5 remainder 2
    2
    >>> 24 % 12 # 24 divided by 12 is 2 remainder 0
    0
    ```
    * Exponent (**): Operand for raising a number to a power 
    ```python3
    >>> 2 ** 4  # 2 raised to power 4
    16
    >>> 36 ** 0.5  # can even do a square root
    6.0
    ```
    * Order of operations: Math operations in Python conform to the normal order of operations.
    ```python3
    >>> 2 + 4 - 7 * 18 / 2
    -57.0
    >>> (32 - 7) + 48 / 4
    37.0
    ```
    * round(): Can pass optional arguments to make your rounding more specific
    ```python3
    >>> round(45.234141312)
    45
    >>> round(34562.9233232)
    34563
    >>> round(475.789, 2)
    475.79
    >>> round(47589.54789, -3)
    48000
    ```
* **Type Casting / Type Conversion**
  * Type casting/conversion is changing a value's type to the desired type (as long as it is compatible)
    ```python3
	>>> 45 / 5  # gives you a float type as the answer
	9.0
	>>> int(45/5) # type casting ensures you get an integer as your answer
	9
	>>> float(7)
	7.0
	>>> str(float(7))
	'7.0'
	>>> int("567")
	567
	>>> str(541)
	"541"
	>>> int("m")  # has to be compatible, can't convert such a string to int
	Traceback (most recent call last):
  	    File "<pyshell#14>", line 1, in <module>
    		int("m")
	ValueError: invalid literal for int() with base 10: 'm'
    ```
  * How is this useful? Many ways! An example would be if you receive numbers as strings and need to do some math with the numbers, type conversion will help.

* **String Interpolation**
  * String interpolation is having placeholders in a string into which you can substitute a variable value. Also known as string formatting
  * The two most common methods are %-formatting and str.format()
  * %-formatting example
  ```python3
  >>> name = "Ian"
  >>> print("Hello %s" %name)  # s is for string
  Hello Ian
  >>> age = 47
  >>> print("%s is %i years old" %(name, age))  # i is for integer
  ```
  * str.format() example
  ``` python3
  >>> average_time = 4  
  >>> avg_distance = 325
  >>> print("His average speed was {} kilometers per hour".format(avg_distance / average_time))
  His average speed was 81.25 kilometers per hour
  >>> print("His average speed with one decimal place was {:.1f} kilometers per hour".format(avg_distance / average_time))
  His average speed with one decimal place was 81.2 kilometers per hour
  >>> hour_hand = 4
  >>> minute_hand = 9
  >>> print("The time now is {:02d}:{:02d} pm".format(hour_hand, minute_hand))
  The time now is 04:09 pm
  ```
  * Other string interpolation methods that can be explored are f-strings and template strings
	
* [Potential Projects](https://github.com/jiinjeong/CS4All/blob/master/PythonBeg/week2.py) (Lab/Assignment)

#### Week 3: Conditions and If Statement
* Conditions
* and, or, not, in
* If-elif-else
* String methods
    * string.upper(), string.lower()
* [Potential Projects](https://github.com/jiinjeong/CS4All/blob/master/PythonBeg/week3.py) (Lab/Assignment)

#### Week 4: List, Indexing, and Random Library (@evaborton)
* **What is a list?**
    * A list of objects— can be strings, integers, Booleans, floats, anything. Elements of a list can even be lists themselves.
    * A list is surrounded by square brackets, and objects are separated by a comma
    * Can be changed/modified
```python3
newList = [7, ‘a’, False, 4.2]
pyList = list(‘python’)		# pyList = [‘p’, ‘y’, ‘t’, ‘h’, ‘o’, ‘n’]
```    
* Lists are their own type, just like str or int:
```python3
print(type(newList))	# Prints: <class ‘list’>
```
* **Indexing**
* Each element in a list is assigned an index, starting at 0 (not 1!). Each element can be accessed through its index:
```python3
newList = [7, ‘a’, False, 4.2, 13]
print(newList[0])	# Prints: 7
print(newList[1])	# Prints: a
print(newList[5])	# IndexError: list index out of range
```
* Each element can also be accessed through reverse indexing, where the last element in the list has the index -1, the second-to-last has index -2, and so on:
```python3
newList = [7, ‘a’, False, 4.2, 13]
print(newList[-1])	# Prints: 13
print(newList[-3])	# Prints: False
```
* List indexing can also be used to slice certain pieces of lists. In square brackets, the first number is the starting point of the slice (inclusive) and the second number is the ending point of the slice (exclusive). If there is a third number, it is the number to skip-count by (for example, 2 means every other, 3 means every third, and -1 means every element working backwards). See examples below:
```python3
numList = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = numList[3:8]	# a = [6, 7, 8, 9, 10]
b = numList[1:9:2]	# b = [4, 6, 8, 10]
```
* If no start point is specified, the slice starts from the beginning, and if no endpoint is specified, the slice goes to the end.
```python3
numList = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = numList[5:]	# c = [8, 9, 10, 11, 12, 13]
d = numList[::-1]	# d = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3]
```
* All of these indexing rules can be used with strings, as well. Each character in the string is treated like each element of a list.
```python3
string = ‘Hello, world!’
e = string[5]		# e = ‘,’
f = string[1:11:2]	# f = ‘el,wr’
```
* The list class comes with many different methods that are useful for changing or finding out characteristics of lists. There are too many to list here, but these are a few of the most useful. The rest can be found with a google search.
	* len(list name)—returns number of elements in list
	* list name.append(single element to add to end of list)
	* list name.extend(list to add to end of list)
	* list name.sort(key to sort by—if no key is specified, sorts numerically/alphabetically)
	* Other methods can filter, add/remove specific elements at specific indices, count number of times an element appears in a list, etc. Just google Python List Methods!

* **Libraries**
	* Libraries are packages of functions useful for some specific purpose. For example, the arcade library is useful for designing video games, the turtle library can be used to draw graphics, and the random library contains functions that can do things like selecting random numbers or random items from a list.
	* Python has hundreds of libraries!
	* Some libraries need to be installed to your device with an installer called pip before you can use them, but since we're using REPL, an online text editor, we don't need to worry about that.
	* Libraries can be easily accessed by typing the word import followed by the name of the library at the top of your program.
	* Once the library is imported, all functions in the library can be used by typing the library name, a dot, and the name of the function. See examples from the random library below:

* **Random Library**
```python3
import random
```
* Once the above line of code is typed, all functions in the random library can be used in the program. Here are a few examples of those functions:
```python3
random.randrange(6, 19) # Chooses a random number between 6 (inclusive) and 19 (exclusive).
random.choice([2, 9, 'a', False]) # Chooses a random element from the list
random.shuffle([2, 9, 'a', False]) # Shuffles the list into a random order
```
These are three functions you will probably find the most useful, but there are many more that you can easily find out what they are and how to use them by googling python random library functions. Some of these other functions can select from uneven distributions, weight certain choices over others, and generate random numbers that are not integers.
	
* [Potential Projects](https://github.com/jiinjeong/CS4All/blob/master/PythonBeg/week4.py) (Lab/Assignment)
	* create a simple rock-paper-scissors game (credit to @jiinjeong)
	* create a guessing game where the computer selects a number and two people (or one person vs. the computer) try to guess it, and whoever guesses the closest wins

#### Week 5: Git and Markdown
* Basic Git
* Additional skills that students may need to finish their independent project

#### Independent Project Ideas
Make sure that they are simple enough to pursue!
* Easy Hangman (Text-based)
* Mad Libs
* Mini Calculator

### Week 6-8: HTML/CSS
#### Week 6
* **What is HTML/CSS?**
  * HTML and CSS are two different coding languages. Together, they are used to design webpages and websites.
    * HTML is used to add content, such as words and images, to your webpage.
      * HTML stands for "hypertext markup language."
    * CSS is used to add style, such as colors and fancy fonts, to your webpage.
      * CSS stands for "cascading style sheets."
  * What is the difference between a webpage and a website?
    * A webpage is a single page with a single URL. A website is usually a collection of multiple webpages.
      * For example, the website hamilton.edu contains many webpages, including a [Contact Us](https://www.hamilton.edu/about/contact) page and an [Areas of Study](https://www.hamilton.edu/academics/areas-of-study) page.
    * We will start by creating webpages with HTML. Later, we can encorporate CSS and create more complex websites.

* **Tags**
  * In HTML, tags are used to label content so that the computer know what to do with it.
    * For example, without tags, the computer would not be able to tell the title of your webpage from the heading that you want to display from the name of the image that you want to embed.
    * Most tags come in pairs: an opening tag and a closing tag. Your content goes in between the two tags. 
      * The opening tag consists of a less than sign, the tag type, and a greater than sign, as such: `<tag_type>`.
      * The closing tag consists of a less than sign, a forward-slash, the tag type, and a greater than sign, as such: `</tag_type>`.
      * For example: `<h1>Your Content</h1>`
      * Content is said to "wrapped" in the tags.
    * Some tags are self-contained; they come individually. Your content is contained within the tag itself.
      * The tag opens with a less than sign, `<`, and closes with a greater than sign, `>`.
      * For example: `<!Doctype HTML>`

* **Nesting Tags**
  * "Nesting tags" means writing tags inside of other tags.
    * The inner tag is called the nested tag, and the outer tag is called the parent tag.
    * How do you think that nested tags are written? Perhaps like this: `<parent_tag> <nested_tag> Your Content </nested_tag> </parent_tag>`.
    * In some cases, we do nest tags just like that! But if you have too many layers of nested tags (i.e. tags nested inside tags nested inside tags nested inside tags...), it can get messy.
      * In this example, it is hard to keep track of the tags and make sure that we close them all: `<html> <body> <div> <ul> <li>Content</li> <li>More Content</li> </ul> </div> </body> </html>`
    * There is a convention for visually organizing your code (that applies to most types of nested tags):
      * When you nest a tag in another, go onto a new line (by pressing enter), and indent one space.
      * To close the outer tag, go onto a new line again, and delete one indent so that the opening and closing tags of the outer tag line up vertically.
      * For example:
        ```html
        <body>
	    	<h1>Your Content</h1>
        </body>
        ```
      * Here is the example from above, now much less messy!
		```html
		<html>
			<body>
				<div>
					<ul>
						<li>Your Content</li>
						<li>More Content</li>
					</ul>
				</div>
			</body>
		</html>
		```

* **Brackets and REPL**

* **Getting Started with HTML**
  * Now that we have opened an HTML document, it is time to start coding!
  * At the top of the document, we need to state the code is in HTML, so that computer knows how to run it. This is done with a self-contained "document type" tag: `<!Doctype HTML>`.
     * Note: The capitalization is arbitrary.
  * Furthermore, we need to wrap all of our code in an HTML tag:
	```html
	<html>
		Your code will go here.
	</html>
	```
  * Within the HTML code, there are two main sections: the head and the body.
  	* The head section contains information about your webpage. It is wrapped in a head tag:
		```html
		<head>
			Your head code will go here.
		</head>
		```
    * The body section contains the content displayed on your webpage. It is wrapped in a body tag:
		```html
		<body>
			Your body code will go here.
		</body>
		```
      * Content at the top of your body section will be displayed at the top of your webpage, and content at the bottom of your webpage will be displayed at the bottom of your webpage.
 * When we put it all together, it looks like this:
	```html
	<!Doctype HTML>
	
	<html>  
		<head>
			
		</head>
		
		<body>
		
		</body>
	</html>
	```
	* To see this in an actual HTML document, please see [Lesson 1](./HTMLCSS/Lessons/HTML_1_Getting_Started.html) or [Lesson 1 with Explanations](./HTMLCSS/Lessons/HTML_1_Getting_Started_With_Explanations.html).

* **Headings**
  * There are various ways to display text on your webpage. One such way is displaying the text as a heading, or header.
  * To make a heading, wrap the text in an "h" tag, as such: `<h1>Your Content</h1>`.
  * There are six different types of headings: h1, h2, h3, h4, h5, and h6. By default, h1 is the largest and the rest are progressively smaller.
    * Therefore, the title of your webpage is usually an h1 or h2 heading, whereas section titles and subtitles are usually h3 or h4 headings.
* **Paragraphs**
  * Paragraphs are another way to display text on your webpage.
  * To make a paragraph, wrap the text in a "p" tag, as such: `<p>Your Content</p>`.
  * To start a new paragraph, start a new paragraph tag. The two paragraphs will be separated by a space.
    * Close the first paragraph tag, go onto a new line (by pressing enter), and open a new paragraph tag.
	* For example:
	```html
	<p>This is my first paragraph.</p>
	<p>This is my second paragraph.</p>
	```
	* You *cannot* start a new paragraph by simply pressing enter within a paragraph tag. This will make your code go onto a new line, but it will have no effect on your webpage.
	  * For example:
	```html
	<p>This is my first paragraph.
		This is still part of the first paragraph.</p>
	```
* **Blockquotes**
  * Blockquotes are another way to display text on your webpage.
  * To make a blockquote, wrap the text in a blockquote tag, as such: `<blockquote>Your Content</blockquote>`.
  * By default, a blockquote is just like a paragraph, but with wider margins on both sides. It is often used for long quotations.
    * For example:
     ```html
     <p>In the words of Abraham Lincoln:</p>
     <blockquote>A house divided against itself cannot stand.</blockquote>
     ```
* To see headings, paragraphs, and blockquotes in action, please see [Lesson 2](./HTMLCSS/Lessons/HTML_2_Headings_and_Paragraphs.html).

* **Breaks**
  * You may have noticed by now that we can put spaces in between lines of code (by pressing enter) without affecting the webpage.
    * This helps us to visually organize our code.
    * For example:
     ```html
     <h2>Main Heading</h2>
     <h3>Subheading</h3>

     <p>In my code, I put a space between the headings and this paragraph.</p>
     ```
  * This raises the question: If we want to put a space between elements *on our webpage*, perhaps to separate sections of the webpage, how can we do so? With a tag called a "break"!
    * The break tag is self-contained, as such: `<br>`.
    * If placed in between elements, such as headings and paragraphs, it increases the space that already exists between them on the webpage.
      * For example:
     ```html
     <h2>Main Heading</h2>
     <br>
     <h3>Subheading</h3>
     <br>
     <p>In my code, I put breaks between elements.</p>
     ```
    * If placed within a text element-- between a pair of paragraph tags, for example-- it causes the text to go onto a new line in the webpage, but it does not put any space between the two lines.
      * In contrast, opening a new tag will create a new element, which entails putting a space between the elements.
      * For example:
     ```html
     <h2>Main<br>Heading</h2>
     <h3>Sub<br>heading</h3>
     <p>In my code, I put a break right here<br>so that the paragraph continues on a new line.</p>
     ```
    * To see the difference more clearly, please see [Lesson 3](./HTMLCSS/Lessons/HTML_3_Breaks.html).

* **Horizontal Rules**
  * Breaks are a useful tool for separating sections of a webpage. But are there any other ways to do so? Yes, with a tag called a "horizontal rule"!
    * By default, a horizontal rule is simply a horizontal line.
      * It creates a visual division on our webpage.
    * The horizontal rule tag is self-contained, as such: `<hr>`.
      * The tag should be placed between elements. It cannot be placed within an element.
      * For example:
     ```html
     <h2>Main Heading</h2>
     <h3>Subheading</h3>
     <hr>
     <p>My webpage will display a horizontal line between the headings and this paragraph.</p>
     ```
 * To see a horizontal rule on a webpage, please see [Lesson 4](./HTMLCSS/Lessons/HTML_4_Horizontal_Rules.html).
* [Potential Projects](https://github.com/jiinjeong/CS4All/blob/master/HTMLCSS/week1.html)

#### Week 7
* [Potential Projects](https://github.com/jiinjeong/CS4All/blob/master/HTMLCSS/week2.html)

#### Week 8
* [Potential Projects](https://github.com/jiinjeong/CS4All/blob/master/HTMLCSS/week3.html)

### Week 1-5: Python Intermediate
#### Week 1: Loop 1: "For" loop
* **What is a `for` loop?**: `for` loops are used to iterate over sequences. Sequences that we have seen are lists and strings. Other iterable sequences include dictionaries, sets, and tuples. `for` loops execute a set of statements for each element in the sequence.
```python
  for var in sequence:
    print("Do something.")
```
* **The Range Function**: The `range(start, end, step)` function returns a sequence of numbers. `for` loops utilize the `range()` function to generate a new iterable sequence in the given range.
```python
  # 1. Prints values from 0 to 6 (not including 6)
  for i in range(6): # range(6) = (0 1 2 3 4 5)
    print(i)
  # 2. Prints values from 2 to 6 (not including 6)
  for i in range(2, 6): # range(2, 5) = (2 3 4 5)
    print(i)
  # 3. Prints values from 0 to 6, stepping by 2 (not including 6)
  for i in range(0, 6, 2): # range(0, 6, 2) = (0 2 4)
    print(i)
```
* **Looping Through a List**: With a `for` loop, you can execute a set of statements for each element of the list.
```python
  # prints each string color in the list colors
  colors = ['red', 'blue', 'green', 'yellow']
  for color in colors:
    print(color)
```
* **Looping Over a String**: Looping over a string behaves similarly to a looping on a list, you can execute a set of statements for each character in the string.
```python
  # prints each character in "Hello!"
  greeting = "Hello!"
  for character in greeting:
    print(character)
```

* **Applications for Loops**:
```python
  # 1. Calculate the sum of the number in the range(1, 6)
  sum = 0
  for i in range(1, 6):
    sum += i  # sum += i is equivalent to sum = sum + i
  # 2. Generates a list of lengths of each string in words
  words = ["computer", "science", "is", "fun"]
  word_lengths = []
  for word in words:
    length_word = length(word)
    word_lengths.append(length_word)
  # 3. Generates new phrase with '!' instead of '.'
  phrase = "Hello. My name is Ruby. What's yours?"
  happy_phrase = ""
  for character in phrase:
    if character == '.':
      happy_phrase += '!'
    else:
      happy_phrase += character
```

* [Potential Projects](https://github.com/jiinjeong/CS4All/blob/master/PythonMed/week1.py)
#### Week 2: Loop 2: While loop
* **What is a `while` loop?**: `while` loops repeatedly execute a set of statements as long as a condition is true. Recall that a condition is a statement that evaluates to boolean type.
```python
  while condition:
    print("Do something.")
```
* **Example**: Before the body of the `while` loop executes, the condition is re-evaluated. In the example below, the condition is `counter < 10`. If the condition evaluates to true, the body is executed. Otherwise, `counter = 10` and the body does not execute.
```python
  # prints values 0 to 9
  counter = 0
  while counter < 10:
    print(counter)
    counter += 1
```
* **Indefinite `while` Loops**: `while` loops are indefinetly iterable. In the example below, the `while` loop executes an indefinte number of times, until the user inputs the the terminating word and the 'while' condition evaluates to false.
```python
  # echos user input until terminator keyword 'exit' is entered
  terminator = "exit"
  word = input("What is your word? (type 'exit' to end): ")
  while word != terminator:
    print("Did you say " + word + "?")
    word = input("What is your word? (type 'exit' to end): ")
```
* **Infinite `while` Loops**: Warning! `while` loops can be infinite if the condition never evaluates to false. In the example below, `i` is never modified and therefore the loop never exits. In the next section, you will learn to how to break a loop without the condition evaluating to false.
```python
  # prints forever and ever and ever ... forever
  print("I will go on forever... ")
  i = 0
  while i == 0:
    print("and ever... ")
```

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
