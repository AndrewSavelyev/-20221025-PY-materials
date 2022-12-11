newlist = [x.upper() for x in fruits]
#You can set the outcome to whatever you like:

# Example
# Set all values in the new list to 'hello':

newlist = ['hello' for x in fruits]
#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

# Example
# Return "orange" instead of "banana":

newlist = [x if x != "banana" else "orange" for x in fruits]