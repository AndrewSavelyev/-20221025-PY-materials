# Task 2
#
# The valid phone number program.
#
# Make a program that checks if a string is in the right format for a phone number. The program should check that the string contains only numerical characters and is only 10 characters long. Print a suitable message depending on the outcome of the string evaluation.
print('Enter phone number:')
x = input()
check = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for i in range(len(x)):
    if x[i] in check:
        print("Phone is correct")
    else:
        print("Phone is incorrect")

