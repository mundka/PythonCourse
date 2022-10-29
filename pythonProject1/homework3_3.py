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
if my_car.get("make") != neighbours_car.get("make"):
    print("Me and my neighbour car makes are not the same")
    if my_car.get("model") != neighbours_car.get("model"):
        print("Me and my neighbours model is not the same")
        if my_car.get("color") == neighbours_car.get("color"):
            print("Our car color is the same")
            if my_car.get("engine capacity") < neighbours_car.get("engine capacity"):
                print("My car engine capacity is smaller than the neighbour's")
                if my_car.get("manufacture year") == neighbours_car.get("manufacture year"):
                    print("Our car manufacture date is the same")
                    if my_car.get("door count") > neighbours_car.get("door count"):
                        print("My car got more doors than the neighbour's")