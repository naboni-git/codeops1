     # The print() function shows text on screen
print("Hello World")      # Shows: Hello World
print("My name is Naboni")  # Shows: My name is Naboni
print(5 + 3)              # Shows: 8
      # Creating variables
name = "Naboni"           # Text data (called "string")
age = 19                 # Number data (called "integer")
height = 1.54             # Decimal number (called "float")
is_student = True        # Yes/No data (called "boolean")

    # Using variables
print(name)              # Shows: Naboni
print(age)               # Shows: 19
print("My name is", name)  # Shows: My name is Naboni
print(name, "is", age, "years old")  # Shows: Naboni is 19 years old
   # The input() function asks user to type something
name = input("What is your name? ")  
     # User types something, then presses Enter

print("Hello", name)  # Shows: Hello [what user typed]
#EX
# Step 1: Ask user for their age
age = int(input("Enter your age: ") ) 
# Step 3: Calculate
future_age = age + 10

# Step 3: Show result
print("You will be", future_age, "after 10 years")
# Anything in quotes is a string
name = "Rahul"
city = 'Delhi'
message = """Long text
can be written
in multiple lines"""

# You can combine strings (concatenation)
first = "John"
last = "Doe"
full = first + " " + last
print(full)  # Shows: John Doe
# Numbers without decimal
age = 25
count = 100
negative = -10

# Math with integers
a = 10
b = 3
print(a + b)   # 13 (addition)
print(a - b)   # 7  (subtraction)
print(a * b)   # 30 (multiplication)
print(a / b)   # 3.333 (division)
print(a // b)  # 3   (division, give whole number)
print(a % b)   # 1   (remainder)
print(a ** b)  # 1000 (power)
# Numbers with decimal point
price = 99.99
pi = 3.14159
height = 5.8

# Float operations
x = 10.5
y = 3.2
print(x + y)    # 13.7
print(x * y)    # 33.6
# Only two values: True or False
is_raining = True
is_sunny = False

# Comparisons always give True/False
x = 5
print(x > 3)   # True
print(x == 5)  # True (checking if equal)
print(x != 5)  # False (checking if not equal)
print(x < 2)   # False
# Creating a list
fruits = ["apple", "banana", "orange"]
numbers = [10, 20, 30, 40]
mixed = ["John", 25, True, 5.5]  # Can mix types

# Accessing items (index starts from 0)
print(fruits[0])  # Shows: apple (first item)
print(fruits[1])  # Shows: banana (second item)
print(fruits[2])  # Shows: orange (third item)

# Accessing from end (negative index)
print(fruits[-1])  # Shows: orange (last item)
print(fruits[-2])  # Shows: banana (second last)

# Changing items
fruits[1] = "mango"
print(fruits)  # Shows: ['apple', 'mango', 'orange']

# Adding items
fruits.append("grape")  # Add at end
print(fruits)  # Shows: ['apple', 'mango', 'orange', 'grape']

fruits.insert(1, "kiwi")  # Add at position 1
print(fruits)  # Shows: ['apple', 'kiwi', 'mango', 'orange', 'grape']

# Removing items
fruits.remove("mango")  # Remove by value
print(fruits)  # Shows: ['apple', 'kiwi', 'orange', 'grape']

last = fruits.pop()  # Remove and get last item
print(last)    # Shows: grape
print(fruits)  # Shows: ['apple', 'kiwi', 'orange']

# List length
print(len(fruits))  # Shows: 3

# Looping through a list
for fruit in fruits:
    print("I like", fruit)
    # Creating a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Engineering",
    "marks": 85
}

# Accessing values
print(student["name"])    # Shows: Rahul
print(student["age"])     # Shows: 20
print(student.get("course"))  # Shows: Engineering

# Changing values
student["age"] = 21
print(student["age"])  # Shows: 21

# Adding new key-value pair
student["grade"] = "A"
print(student)  # Shows: {'name': 'Rahul', 'age': 21, 'course': 'Engineering', 'marks': 85, 'grade': 'A'}

# Removing
del student["marks"]
print(student)  # Shows: {'name': 'Rahul', 'age': 21, 'course': 'Engineering', 'grade': 'A'}

# Checking if key exists
if "name" in student:
    print("Name exists")

# Looping through dictionary
for key in student:
    print(key, ":", student[key])

# Looping with items
for key, value in student.items():
    print(key, "=", value)
    # Basic if
age = 18
if age >= 18:
    print("You can vote")  # This runs because condition is True

# If-else
age = 16
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")  # This runs

# If-elif-else (multiple conditions)
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"  # This runs because 85 >= 80
elif score >= 70:
    grade = "C"
else:
    grade = "D"
print("Grade:", grade)

# Comparison operators (always returns True/False)
x = 10
print(x == 10)   # True (equal to)
print(x != 5)    # True (not equal)
print(x > 5)     # True (greater than)
print(x < 20)    # True (less than)
print(x >= 10)   # True (greater than or equal)
print(x <= 9)    # False (less than or equal)

# AND, OR, NOT
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")  # Both conditions must be True

if age >= 18 or has_license:
    print("Can drive")  # At least one condition must be True

if not has_license:
    print("No license")  # Reverses the condition
    # For loop with range
# range(5) = 0,1,2,3,4
for i in range(5):
    print(i)  # Prints: 0,1,2,3,4 (each on new line)

# range(start, end) - start to end-1
for i in range(2, 6):
    print(i)  # Prints: 2,3,4,5

# range(start, end, step)
for i in range(0, 10, 2):
    print(i)  # Prints: 0,2,4,6,8

# For loop with list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print("I like", fruit)

# For loop with string
for letter in "Hello":
    print(letter)  # H, e, l, l, o

# Nested loop
for i in range(3):
    for j in range(2):
        print(i, j)

# While loop (runs until condition becomes False)
count = 0
while count < 5:
    print(count)
    count = count + 1  # Important: update the variable
# Output: 0,1,2,3,4

# Infinite loop (be careful!)
# while True:
#     print("This never ends")

# Break (exit loop)
for i in range(10):
    if i == 5:
        break  # Stops loop when i equals 5
    print(i)  # Prints: 0,1,2,3,4

# Continue (skip current iteration)
for i in range(5):
    if i == 2:
        continue  # Skip when i equals 2
    print(i)  # Prints: 0,1,3,4
    # Defining a function
def greet():
    print("Hello!")

# Calling a function
greet()  # Prints: Hello!

# Function with parameter
def greet_person(name):
    print("Hello", name)

greet_person("Rahul")  # Prints: Hello Rahul
greet_person("Priya")  # Prints: Hello Priya

# Function with return value
def add(a, b):
    result = a + b
    return result  # Returns value back to caller

sum = add(5, 3)
print(sum)  # Prints: 8

# Function with multiple parameters
def calculate(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter  # Returns multiple values

area, perimeter = calculate(10, 5)
print("Area:", area)        # 50
print("Perimeter:", perimeter)  # 30

# Default parameter value
def greet_time(name, time="morning"):
    print("Good", time, name)

greet_time("Rahul")          # Good morning Rahul
greet_time("Priya", "night") # Good night Priya

# Simple calculator function
def calculator(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operation"

result = calculator(10, "+", 5)
print(result)  # 15
# STEP 1: Define the function
def add(a, b):  # add = function name, a and b = inputs
    return a + b  # return = give back the result

# STEP 2: Get user inputs
num1 = float(input("Enter first number: "))
# float() converts text to decimal number
# input() asks user to type something

num2 = float(input("Enter second number: "))
operation = input("Enter +, -, *, or /: ")

# STEP 3: Process based on operation
if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Invalid operation"

# STEP 4: Show result
print("Result:", result)