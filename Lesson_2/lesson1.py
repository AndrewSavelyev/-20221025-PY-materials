# The print() function prints the given object to the standard output device (screen) or to the text stream file.
message = 'Python is fun'

# print the string message
print(message)

# Output: Python is fun
# --------------------------------------------------------------
# print() Syntax
# The full syntax of print() is:

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# Example 1 ----------------------------------------------------
print("Python is fun.")

a = 5
# Two objects are passed
print("a =", a) #sep

b = a
# Three objects are passed
print('a =', 508, '= b')
# Example 2 ----------------------------------------------------
a = 5
print("a =", a, 800, end='\n\n\n', sep='00000')
print("a =", a, sep='0', end='')
#
# # Example 3 ----------------------------------------------------
sourceFile = open('python.txt', 'w')
print('Pretty cool, huh!', file=sourceFile)
sourceFile.close()




# вивід = print
# змінна = 1
# вивід(змінна)



