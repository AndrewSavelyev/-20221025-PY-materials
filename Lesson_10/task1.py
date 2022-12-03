# Write a function called oops that explicitly raises an IndexError exception when called. Then write another function
# that calls oops inside a try/except statement to catch the error. What happens if you change oops to raise KeyError
# instead of IndexError?

#With uncommented code in line 16- program will print three messages:
# Oops
# Oops again
# Still oops
#and with commented code in line 16- program will print only two messages:
# Oops
# Still oops
#And finally, to rise KeyError # instead of IndexError we need to modify not just function oops, but also mofify list
# to dict
#list = [1, 6, 79]
dict = {'1': 'fg', '6': '79'}
def oops():
    try:
        #list[4]
        dict['5']
    #except IndexError:
    except KeyError:
        print('Oops')

def call_oops():
    try:
        oops()
#        list[5]
    except IndexError:
        print('Oops again')
    finally:
        print('Still oops')

call_oops()


