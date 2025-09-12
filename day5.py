'''
#Upper Function
name = "Python"
print(name[1])
print("Capital Letter:", name.upper()[1])

#--------------------------------
#lower Function
name = "Python"
print(name[1])
print("Small Letter: ",name.lower())

#--------------------------------
#replace Function
name = "Python is so beautiful"
print("Original String:", name)
#print(name[1:4])
print(name.replace("beautiful", "wonder"))

#--------------------------------
#strip Function
name = "     Python is so beautiful"
print("Original String:", name)
print("After Strip:", name.strip())

#--------------------------------
#split Function
name = "Python is so beautiful"
print("Original String:", name) 
print("After Split:", name.split())
'''
#--------------------------------
fruits = ["apple", "Banana"]
print("Original List:", fruits)
fruits.append("cherry")
print("After Append:", fruits)
#--------------------------------
fruits = ["apple", "Banana"]
print("Original List:",fruits)
fruits.remove("Banana")
print("After remove method O/P",fruits)

#--------------------------------

fruits = ["apple", "Banana"]
print("Original List:",fruits)
fruits.extend(["watermelon", "mango", "guess"])
print("After extend method O/P",fruits)

#--------------------------------
fruits = ["apple", "Banana"]
print("Original List:",fruits)
fruits.sort(reverse=True)
print("After sort method O/P",fruits)