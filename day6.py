# Count the occurrences of "red" in the tuple
colors = ("red", "green", "blue" , "red" , "yellow", "blue" , "red", "green", "blue")
print(colors.count("red"))

#Index of first occurrence of "blue" in the tuple
print(colors.index("blue"))

# There are two methods use in tuple
#1. count() - to count the occurrences of an element in a tuple
#2. index() - to find the index of the first occurrence of an element in a tuple

#--------------------------------

a = {1, 2, 3, 4, 5}
print(a)
b = {4, 5, 6, 7, 8}
print(b)

# 

student = {
    "name": "Krupesh",
    "age": 20,
    "grade": "A"
}

print(student["name"])   # Krupesh
student["age"] = 21      # Update value
student["city"] = "Delhi"  # Add new key-value
print(student)
