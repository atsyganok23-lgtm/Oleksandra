#Task 1
#The Guessing Game.
#Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.

import random
computer_number = random.randint(1, 10)
while True:
    your_number = int(input("Input your number between 1 and 10: "))
    if your_number == computer_number:
        print ("My Congratulations!")
    else:
        print("Try again!")
