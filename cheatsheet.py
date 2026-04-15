"""
========================================
PYTHON LEARNING CHEAT SHEET
========================================
A comprehensive reference guide for Python beginners and intermediate developers.
Print this or keep it handy while coding!
"""

# =============================================================================
# 1. BASIC SYNTAX & DATA TYPES
# =============================================================================

# Variables and Assignment
name = "John"           # String
age = 25                # Integer
height = 5.8            # Float
is_student = True       # Boolean
grades = [90, 85, 92]   # List
person = {"name": "John", "age": 25}  # Dictionary

# Comments
# This is a single line comment
""" This is a 
    multi-line comment
    or docstring """

# Basic Operations
x = 10 + 5      # Addition: 15
y = 10 - 3      # Subtraction: 7
z = 10 * 2      # Multiplication: 20
a = 10 / 3      # Division: 3.333...
b = 10 // 3     # Floor division: 3
c = 10 % 3      # Modulus: 1
d = 10 ** 2     # Exponent: 100

# String Operations
text = "Hello, World!"
print(text.upper())        # "HELLO, WORLD!"
print(text.lower())        # "hello, world!"
print(text[0:5])           # "Hello"
print(len(text))           # 13
print(text.replace("World", "Python"))  # "Hello, Python!"

# =============================================================================
# 2. CONTROL FLOW
# =============================================================================

# If-Elif-Else Statements
age = 18
if age < 18:
    print("Minor")
elif age == 18:
    print("Exactly 18")
else:
    print("Adult")

# For Loops
# Range loop
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Loop over list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Loop with index
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# While Loops
count = 0
while count < 5:
    print(count)
    count += 1

# Loop Control
for i in range(10):
    if i == 3:
        continue    # Skip this iteration
    if i == 7:
        break       # Exit loop
    print(i)

# =============================================================================
# 3. FUNCTIONS
# =============================================================================

# Basic Function
def greet(name):
    return f"Hello, {name}!"

# Function with default parameters
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

# Function with multiple return values
def get_coordinates():
    return 10.5, 20.3

x, y = get_coordinates()

# Function with variable arguments
def sum_all(*numbers):
    return sum(numbers)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Lambda Functions
square = lambda x: x ** 2
add = lambda x, y: x + y

# =============================================================================
# 4. DATA STRUCTURES
# =============================================================================

# Lists (Mutable, ordered)
numbers = [1, 2, 3, 4, 5]
numbers.append(6)        # Add to end
numbers.insert(0, 0)     # Insert at index
numbers.remove(3)        # Remove first occurrence
numbers.pop()            # Remove last item
numbers.sort()           # Sort in place
numbers.reverse()        # Reverse list

# List Comprehensions
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# Tuples (Immutable, ordered)
coordinates = (10, 20)
x, y = coordinates      # Unpacking
single_item = (42,)     # Note the comma!

# Dictionaries (Key-value pairs)
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
person["email"] = "alice@example.com"  # Add item
person["age"] = 31                     # Update item
del person["city"]                     # Delete item

# Dictionary methods
keys = person.keys()
values = person.values()
items = person.items()

# Sets (Unique items, unordered)
numbers = {1, 2, 3, 4, 5}
numbers.add(6)          # Add item
numbers.remove(3)       # Remove item
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2     # Union
intersection = set1 & set2  # Intersection

# =============================================================================
# 5. STRING MANIPULATION
# =============================================================================

text = "Python Programming"

# String methods
print(text.lower())         # lowercase
print(text.upper())         # uppercase
print(text.title())         # title case
print(text.strip())         # remove whitespace
print(text.split())         # split into list
print(",".join(["a", "b", "c"]))  # join list into string
print(text.replace("Python", "Java"))  # replace
print(text.startswith("Py"))  # starts with
print(text.endswith("ing"))   # ends with
print("123".isdigit())        # is digit
print("abc".isalpha())        # is alpha
print("abc123".isalnum())    # is alphanumeric

# String formatting
name = "John"
age = 25
# f-strings (Python 3.6+)
print(f"{name} is {age} years old")
# .format()
print("{} is {} years old".format(name, age))
# % formatting (old)
print("%s is %d years old" % (name, age))

# =============================================================================
# 6. FILE I/O
# =============================================================================

# Reading files
with open("file.txt", "r") as file:
    content = file.read()        # Read entire file
    lines = file.readlines()     # Read all lines
    file.seek(0)                 # Reset cursor
    line = file.readline()       # Read one line

# Writing files
with open("output.txt", "w") as file:
    file.write("Hello, World!")
    file.write("\nSecond line")

# Appending to files
with open("output.txt", "a") as file:
    file.write("\nAppended line")

# =============================================================================
# 7. ERROR HANDLING
# =============================================================================

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError as e:
    print(f"Value error: {e}")
except Exception as e:
    print(f"General error: {e}")
else:
    print("No errors occurred")
finally:
    print("This always runs")

# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

# =============================================================================
# 8. MODULES AND IMPORTS
# =============================================================================

# Import entire module
import math
print(math.sqrt(16))

# Import specific functions
from random import randint, choice
print(randint(1, 10))

# Import with alias
import numpy as np
import pandas as pd

# Import all (use sparingly)
from datetime import *

# =============================================================================
# 9. CLASSES AND OBJECTS (OOP)
# =============================================================================

class Person:
    # Class attribute
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, I'm {self.name}"
    
    def celebrate_birthday(self):
        self.age += 1
        return f"Happy {self.age}th birthday!"
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2024 - birth_year
        return cls(name, age)
    
    @staticmethod
    def is_adult(age):
        return age >= 18

# Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def study(self):
        return f"{self.name} is studying"

# =============================================================================
# 10. COMMON PATTERNS & BEST PRACTICES
# =============================================================================

# List comprehension vs loop
# Good:
squares = [x**2 for x in range(10)]
# Avoid:
squares = []
for x in range(10):
    squares.append(x**2)

# Context managers (with statement)
with open("file.txt", "r") as file:
    content = file.read()  # File automatically closed

# Enumerate for index and value
for index, item in enumerate(items):
    print(f"{index}: {item}")

# Zip multiple iterables
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}

# Generator expressions (memory efficient)
squares_gen = (x**2 for x in range(1000000))

# =============================================================================
# 11. USEFUL BUILT-IN FUNCTIONS
# =============================================================================

abs(-5)          # 5 - absolute value
all([True, True]) # True - all true?
any([False, True]) # True - any true?
bin(10)          # "0b1010" - binary
bool(0)          # False - boolean conversion
chr(65)          # "A" - character from ASCII
divmod(10, 3)    # (3, 1) - quotient and remainder
enumerate([a, b]) # enumerate object
filter(lambda x: x>0, [-1, 2, -3, 4]) # filter items
float("3.14")    # 3.14 - convert to float
int("42")        # 42 - convert to int
len([1, 2, 3])   # 3 - length
list(range(5))   # [0, 1, 2, 3, 4] - create list
map(lambda x: x*2, [1, 2, 3]) # map function
max([1, 5, 3])   # 5 - maximum
min([1, 5, 3])   # 1 - minimum
ord("A")          # 65 - ASCII value
pow(2, 3)        # 8 - power
print("Hello")    # output to console
range(5)         # range object - 0 to 4
round(3.14159, 2) # 3.14 - round
sorted([3, 1, 4]) # [1, 3, 4] - sorted list
str(42)           # "42" - convert to string
sum([1, 2, 3])    # 6 - sum of items
type(42)          # <class 'int'> - get type

# =============================================================================
# 12. DEBUGGING TIPS
# =============================================================================

# Print debugging
print(f"Variable x = {x}")

# Use assert for debugging
assert x > 0, "x should be positive"

# pdb debugging (in terminal)
# import pdb; pdb.set_trace()

# =============================================================================
# 13. VIRTUAL ENVIRONMENTS
# =============================================================================

# Create virtual environment
# python -m venv myenv

# Activate (Windows)
# myenv\Scripts\activate

# Activate (Mac/Linux)
# source myenv/bin/activate

# Install packages
# pip install package_name

# Save requirements
# pip freeze > requirements.txt

# Install from requirements
# pip install -r requirements.txt

# =============================================================================
# QUICK REFERENCE CARD
# =============================================================================

"""
VARIABLES:     x = 5, name = "John", is_true = True
STRINGS:       text = "Hello", text.upper(), text.split()
LISTS:         items = [1, 2, 3], items.append(4), items[0]
LOOPS:         for item in items:, while condition:
IF STATEMENTS: if x > 5: elif x == 5: else:
FUNCTIONS:     def func(param): return param * 2
DICTIONARIES:  data = {"key": "value"}, data["key"]
FILES:         with open("file.txt") as f: content = f.read()
CLASSES:       class MyClass: def __init__(self): pass
IMPORTS:       import module, from module import func
ERRORS:        try: except Error: pass
LIST COMPS:    [x*2 for x in range(10)]
LAMBDAS:       lambda x: x**2
"""

print("Python Cheat Sheet loaded! Keep this file handy for quick reference.")

