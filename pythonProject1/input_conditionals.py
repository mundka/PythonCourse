from time import sleep

# 1. Input
"""
Let's create a temperature conversion tool: Celsius to Fahrenheit and vice versa.
    - Find the conversion formula for Celsius and Fahrenheit in the internet
    - Define the formula programmatically
    - Format the float result with 2 decimal points
"""
celsius_1 = float(input("Temperature value in degree Celsius: "))

# Given formula
fahrenheit_1 = None  # find formula for the Celsius conversion to Fahrenheit

# Print the result, format floats to 2 decimal points
print(
    f"The {celsius_1} degree Celsius is equal to: {fahrenheit_1} Fahrenheit"
)

print("----OR----")

celsius_2 = float(input("Temperature value in degree Celsius: "))
fahrenheit_2 = None # find formula for the Fahrenheit conversion to Celsius

# Print the result, format floats to 2 decimal points
print(
    f"The {celsius_2} degree Celsius is equal to: {fahrenheit_2} Fahrenheit"
)

# 2. Complete calculator
"""
Add three new operations for the calculator from the class.
    - Add square root operation
    - Add stepping operation
    - Add percentage operation

Fix the textual description of Accepted operation symbols.

⭐️ Extra: Using .isnumeric() and conditional statement, create a validation that prevents the user to enter
the string instead of a number. You are allowed to change the code accordingly.

Resource: https://www.w3schools.com/python/ref_string_isnumeric.asp 
"""

print("========================================")
print("Welcome to the calculator!")
print("========================================")
sleep(1)

first_number = float(input("Write first number: "))
print("Accepted operation symbols: +, -, /, *")
symbol = input("Operation: ")   # + or -
second_number = float(input("Enter second number: "))
result = None

if symbol == "+":
    result = first_number + second_number
elif symbol == "-":
    result = first_number - second_number
elif symbol == "*":
    result = first_number * second_number
elif symbol == "/":
    if second_number != 0:
        result = first_number / second_number
    else:
        print("You cannot divide by 0")

if isinstance(result, int) or isinstance(result, float):
    print(f"Result: {first_number} {symbol} {second_number} = {format(result, '.2f')}")
else:
    print("wrong operation")

# 3. Dictionaries and conditionals
"""
You got two dictionaries with the car details.
Depending on the six print() statements, write corresponding
conditional statements, inserting the corresponding print statement
from below. 

Example:

    if neighbours_car.get("price") > my_car.get("price"):
        print("Neighbours car is more expensive than mine")
"""

# Don't change the dictionaries
my_car = {
    "make": "Volkswagen",
    "model": "Golf  4",
    "color": "blue",
    "engine capacity": 1.9,
    "manufacture year": 2000,
    "door count": 5,
    "price": 2300
}

neighbours_car = {
    "make": "BMW",
    "model": "320d",
    "color": "blue",
    "engine capacity": 2.0,
    "manufacture year": 2000,
    "door count": 4,
    "price": 3200
}

# Write your code here

print("Me and my neighbour car makes are not the same")
print("Me and my neighbours model is not the same")
print("Our car color is the same")
print("My car engine capacity is smaller than the neighbour's")
print("Our car manufacture date is the same")
print("My car got more doors than the neighbour's")
