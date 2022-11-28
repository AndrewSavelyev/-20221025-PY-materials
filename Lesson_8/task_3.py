# A simple calculator.
#
# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep
# things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as the second
# parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:
#
#     the call make_operation(‘+’, 7, 7, 2) should return 16
#     the call make_operation(‘-’, 5, 5, -10, -20) should return 30
#     the call make_operation(‘*’, 7, 6) should return 42

def make_operation(*ar:list):
    #sum = 0
    substruct = 0
    multiple = 0
    ar = [ i for i in ar]
    count_ar = ar[2:]
    if ar[0] == "+":
       sum = ar[1]
       for j in count_ar:
           sum = sum + count_ar[j]
           print(sum)

make_operation('+', 4, 5, 6)