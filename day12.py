def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")
greet("Krupesh", 18)
greet("Rushikesh", 21)
greet("Swaraj", 18)

#----------------------------------
def add_numbers(*args):
    total = 0
    for num in args:
        total = num - total
    return total

print(add_numbers(2, 3, 4))