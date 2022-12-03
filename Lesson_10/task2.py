# Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns the
# value of squared a divided by b, construct a try-except block which raises an exception if the two values given by the
# input function were not numbers, and if value b was zero (cannot divide by zero).

a = input('Enter first number:')
b = input('Enter second number:')

def two_numbers():
    try:
        print(int(a)**2/int(b))
    except TypeError:
        print('Values must be integers')
    except ValueError:
        print('Values must be integers')
    except ZeroDivisionError:
        print('Second value must not be zero')

two_numbers()



