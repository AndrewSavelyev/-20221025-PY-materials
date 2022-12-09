# Write a Python program to detect the number of local variables declared in a function.

def some_func():
    a = 1
    b = 2
    c = 4

print(some_func.__code__.co_nlocals)