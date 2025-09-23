#Loops

#while Loop (Number Guessing Game)

secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess the number (1 to 10): "))
    if guess == secret:
        print("Correct! You Guessed it.")
    else: 
        print("Try Again")
    
    
