# The greatest number
#
# Write a Python program to get the largest number from a list of random numbers with the length of 10
#
# Constraints: use only while loop and random module to generate numbers
import random
i = 1
list = [random.randint(1, 10)]
while i < 10:
    list = list + [random.randint(1, 10)]
    i += 1
print(list)
print("Max element in list", max(list))