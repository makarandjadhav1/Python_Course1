# If-Else Statement
# Program to check if a person is eligible to vote or not
# Eligibility criteria: Age must be 18 or above
age = int(input("Enter Your age: "))
if age >= 18:
    print("Your are eligible to vote.")
else:
    print("Your are not eligible to vote.")

#If-elif-else Statement
# Program to check the grade of a student based on marks
name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
if marks >= 90:
    grade = 'A'
    print("Congratulations", name, "! You have secured grade", grade)
elif marks >= 80:
    grade = 'B'
    print("Congratulations", name, "! You have secured grade", grade)
elif marks >= 70:
    grade = 'C'
    print("Congratulations", name, "! You have secured grade", grade)
else:
    grade = 'D'
    print("Sorry", name, "! You have secured grade", grade)
#--------------------------------