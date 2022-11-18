# The Guessing Game.
#
# Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. The result should be sent back to the user
# via a print statement.
import random

player = int(input("Please write number, that should appear: "))
computer = random.randint(1, 3)
print(computer)

if player == computer:
    print("Your guess is right")
else:
    print("Your guess is wrong")
