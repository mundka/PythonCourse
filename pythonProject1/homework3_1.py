from time import sleep

# 1. Input
"""
Let's create a temperature conversion tool: Celsius to Fahrenheit and vice versa.
    - Find the conversion formula for Celsius and Fahrenheit in the internet
    - Define the formula programmatically
    - Format the float result with 2 decimal points
"""
celsius_1 = float(input("Temperature value in degree Fahrenheit: "))

# Given formula
fahrenheit_1 = (celsius_1 - 32) * 0.5556  # find formula for the Celsius conversion to Fahrenheit
# C == ((F - 32) x 0,5556)
# F == ((C x 1.8) + 32

# Print the result, format floats to 2 decimal points
print(
    f"The {format(celsius_1, '.2f')} degree Fahrenheit is equal to: {format(fahrenheit_1, '.2f')} Celsius"
)
sleep(0.5)
print("----OR----")
sleep(0.5)
celsius_2 = float(input("Temperature value in degree Celsius: "))
fahrenheit_2 = (celsius_1 * 1.8) + 32  # find formula for the Fahrenheit conversion to Celsius

# Print the result, format floats to 2 decimal points
print(
    f"The {format(celsius_2, '.2f')} degree Celsius is equal to: {format(fahrenheit_2, '.2f')} Fahrenheit"
)
