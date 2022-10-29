from datetime import date
from datetime import datetime

# 1. String interpolation


"""
Fill in the values with your name, surname and hobbies.

Print out the introduction string using all three types of string interpolations:
    - f-string method
    - .format() method
    - % modulo operator method

Resource: https://www.programiz.com/python-programming/string-interpolation

⭐️ Extra (optional): Using list *unpacking method, make "my_hobbies" as a list,
and upack it using the .format() method with necessary amount of {} placeholders.
"""

# Write your code here
my_name = "Kaimo"
my_surname = "Mund"
my_birth_country = "Estonia"
my_hobbies = ["Volley", "Python"]

# Modify the string according to each interpolation method
introduction = f"Hello! My name is {my_name} {my_surname}. " \
               f"I come from {my_birth_country}. My hobbies are {my_hobbies}. Nice to meet you!"
hobbies = "My hobbies are {} {}"
# Don't modify print() function
print("# exercise 1 #")
print(introduction)
print("### exercise 1 BONUS ###")
print(hobbies.format(*my_hobbies))

# ==================

# 2. List manipulations
"""
You have a list of various meals.

Print out each of the following results using list methods/functions
    - Remove deserts from the meals (first and last one)
    - Add "steak" at the end of the list
    - Replace "spaghetti" with "pasta carbonara"
    - Count the amount of the elements in the list
    - Sort the list in alphabetical order
    
Resource: https://www.w3schools.com/python/python_ref_list.asp

⭐️ Extra (optional): 
    - Merge list "drinks" with the "meals" list (exist various methods, google "python merge lists"),
    demonstrating two ways of doing that.
    
            drinks = ["coke", "coffee", "tea", "milkshake"]
            
"""

# Don't modify this code
meals = ["hot chocolate", "pizza", "spaghetti", "burger", "sushi", "sweet pudding"]
drinks = ["coke", "coffee", "tea", "milkshake"]

# Write your code here
print("# exercise 2 #")
meals.remove("hot chocolate")
meals.remove("sweet pudding")
meals.append("steak")
meals[2] = ("pasta carbonara")
meals.sort()
print(meals)
print(len(meals))
print("### exercise 2 BONUS ###")
merged_list = meals + drinks
print(merged_list)
# extending meals with drinks
meals.extend(drinks)
print(meals)

# ==================

# 3. Accessing dictionary values
"""
1. Access and print out the following key values (for each value use separate print()):
    - print values of key "electronics"
    - print values of key "adults"
    - print values of key "men's fashion"
    - print values of key "girls' fashion"
    - get "school uniforms" value printed 
    - get "pants" value printed
    
2. Change following values:
    - replace "computers" key values with None (NoneType)
    - remove key "remove me" using one of the dictionary method
    
Resource: https://www.w3schools.com/python/python_ref_dictionary.asp

⭐️ Extra (optional): 
    - print value of key "current date"
    - import the correct Python standard library on the top of the file
    - choose the right module which offers to get the current time
    - replace the "current time" key's value with particular module's method
    
Resource: https://www.programiz.com/python-programming/datetime/current-time
"""

# Don't modify this code
departments = {
    "electronics": ["camera", "GPS", "cell phones", "headphones", "eBook readers"],
    "computers": ["data storage", "monitors", "printers", "scanners", "laptops"],
    "fashion": {
        "adults": [
            {
                "men's fashion": ["shoes", "accessories", "pants", "t-shirts"],
                "women's fashion": ["shoes", "dresses", "jewelry", "handbags"]
            }
        ],
        "kids": [
            {
                "boys' fashion": ["school uniforms", "cartoon shirts"],
                "girls' fashion": ["clothing", "shoes", "watches"]
            }
        ]
    },
    "remove me": 420,
    "extra": {
        "current date": date.today(),
        "current time": "datetime"
    }
}

# Write your code here
# 1 part
print("# exercise 3/1 #")
print(departments.get("electronics"))
print(departments.get("fashion").get("adults"))
print(departments.get("fashion").get("adults")[0].get("men's fashion"))
print(departments.get("fashion").get("kids")[0].get("girls' fashion"))
print(departments.get("fashion").get("kids")[0].get("boys' fashion")[0])
print(departments.get("fashion").get("adults")[0].get("men's fashion")[2])

# 2 part
print("# exercise 3/2 #")
# - replace "computers" key values with None (NoneType)
departments["computers"] = None
# - remove key "remove me" using one of the dictionary method
departments.pop("remove me")
print(departments)

print("### exercise 3 BONUS ###")
now = datetime.now()
datetime = now.strftime("%H:%M")
print(departments.get("extra").get("current date"))
departments["extra"]["current time"] = str(datetime)
print(departments)

# 4. String manipulations
"""
Do following strings manipulations. Print each result:
    - count all substring in the string
    - find and count all "t" occurrences in the strings
    - capitalize whole string
    - reverse the case of the string

Resource: https://www.w3schools.com/python/python_ref_string.asp
"""

# Don't modify this code
news = "Find the latest breaking news and information on the top stories."

# Write your code here
print("# exercise 4 #")
print(len(news))
print(news.count("t"))
print(news.upper())
print(news.lower())
