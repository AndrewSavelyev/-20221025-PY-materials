# The birthday greeting program.
#
# Write a program that takes your name as input, and then your age as input and greets you with the following:
#
# “Hello <name>, on your next birthday you’ll be <age+1> years”
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
print('Hello {0}, on your next birthday you’ll be {1} years'.format(name, age+1))