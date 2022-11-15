# String manipulation
#
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string.
#
# Sample String: 'helloworld'
#
# Expected Result : 'held'
#
# Sample String: 'my'
#
# Expected Result : 'mymy'
#
# Sample String: 'x'
#
# Expected Result: Empty String
#
# Tips:
#
#     Use built-in function len() on an input string
#     Use positive indexing to get the first characters of a string and negative indexing to get the last characters
# string = 'helloworld'
# i = 0
# while i < len(string):
#     if i == 0:
#         print(string[i], sep="", end="")
#         i += 1
#         continue
#     elif i == 1:
#         print(string[i], sep="", end="")
#         i += 1
#         continue
#     i += 1
# i = len(string)
# while len(string) > 1:
#     if i == 2:
#         print(string[-i], sep="", end="")
#         i -= 1
#         continue
#     elif i == 1:
#         print(string[-i], sep="", end="")
#         i -= 1
#         break
#     i -= 1

# string = "my"
# array = [1, 2]
# for r in array:
#     i = 0
#     while i < len(string):
#         if i == 0:
#             print(string[i], sep="", end="")
#             i += 1
#             continue
#         elif i == 1:
#             print(string[i], sep="", end="")
#             i += 1
#             continue
#         i += 1

string = 'x'
i = 0
while i < len(string):
    if i == 1:
        print(string[i], sep="", end="")
        i += 1
        continue
    i += 1




