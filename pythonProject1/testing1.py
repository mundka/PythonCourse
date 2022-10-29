# Modify the variables so that all of the statements evaluate to True.

var1 = 12
var2 = "python"
var3 = [1, 2, 3, 4, 5]
var4 = ("hi", "ho", "Hello, Python!")
var5 = {
    "mood": "happy",
    "values": 7,
    "egg": "tuna",
}

var6 = float(12)

# Don't edit anything below this comment

# Numbers
print(isinstance(var1, int)) #1
print(isinstance(var6, float)) #2
print(var1 < 35) #3
print(var1 <= var6) #4

# Strings
print(isinstance(var2, str)) #5
print(var2[5] == "n" and var2[0] == "p") #6

# Lists
print(isinstance(var3, list)) #7
print(len(var3) == 5) #8

# Tuples
print(isinstance(var4, tuple)) #9
print(var4[2] == "Hello, Python!") #10

# Dictionaries
print(isinstance(var5, dict)) #11
print("happy" in var5) #12
print(7 in var5.values()) #13
print(var5.get("egg") == "salad") #14
print(len(var5) == 3) #15
var5["tuna"] = "fish" #16
