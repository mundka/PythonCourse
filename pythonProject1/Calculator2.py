from math import sqrt
from time import sleep

#Refactor the calculator, using functions with arguments for the calculations

print("========================================")
print("Welcome to the calculator!")
print("========================================")
sleep(0.5)

first_number = input("Write first number: ")
print("Accepted operation symbols: +, -, /, *, **, %, r")
symbol = input("Operation: ")  # + or -
if symbol == "r" and first_number.isnumeric():
    first_number = float(first_number)
    result = sqrt(first_number)
    print(f"square root of {first_number} is {format(result, '.2f')}")
elif symbol == "r" and not first_number.isnumeric():
    print(f"{first_number} is not a number!")
else:
    second_number = input("Enter second number: ")
    result = None
    if first_number.isnumeric() and second_number.isnumeric():
        first_number = float(first_number)
        second_number = float(second_number)
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
        elif symbol == "**":
            result = first_number ** second_number
        elif symbol == "%":
            result = (first_number / second_number) * 100

    if (isinstance(result, int) or isinstance(result, float)) and symbol == "%":
        print(f"Result: {first_number} is {format(result, '.2f')} {symbol} of {second_number}. ")
    elif isinstance(result, int) or isinstance(result, float):
        print(f"Result: {first_number} {symbol} {second_number} = {format(result, '.2f')}")
    else:
        print("wrong operation")
