'''num = int(input("Enter your Values"))
if num > 0:
    if num % 2 == 0:
        print('Positive Even')
    else:
        print('Positive Odd')'''

#----------------------------------
#Small Project ATM Simulator
pin = 1234
balance = 5000

user_pin = int(input("Enter PIN:"))

if user_pin == pin :
    amount = int(input("Enter amount to withdraw:"))
    if amount <= balance:
        current = balance - amount
        print("Withdrawal Successful")
        print("Your Current Balance is:", current)
    else:
        print(" Insufficient Balance")
else:
    print("Wrong PIN")