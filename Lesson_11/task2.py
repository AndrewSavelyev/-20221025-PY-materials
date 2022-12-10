# Extend Phonebook application
#
# Functionality of Phonebook application:
#
# Add new entries
# Search by first name
# Search by last name
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program
#
# The first argument to the application should be the name of the phonebook.Application should load JSON data,
# if it is present in the folder with application, else raise an error.After the user exits, all data should be saved to
# loaded JSON.
import json

phonebook = input('Enter phonebook name: ')

def existing_phonebook():
    global phonebook
    try:
        with open(phonebook +'.txt') as file_object:
            string = file_object.read()

    except FileNotFoundError:
        phonebook = input('There is no such phonebook. Please enter correct name: ')

existing_phonebook()
dictionary= {}

def choise():
    global input_choise
    input_choise = input("""Actions with phonebook:
               \n\"a\" - for Add new entry
               \n\"f\" - for Search by first name
               \n\"l\" - for Search by last name
               \n\"F\" - for Search by full name
               \n\"n\" - for Search by phone number
               \n\"c\" - for Search by city ot state
               \n\"d\" - for Delete record for a given telephone number
               \n\"u\" - for Update record for a given telephone number
               \n\"e\" - for Exit from program
               \nPlease choose action: """)
choise()
i = 0
def action_with_phonebook(action):
    if action == "a":
        global i
        dictionary[i] = {}
        global first_name
        global last_name
        global full_name
        global phone_number
        global city_state
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        full_name = input('Enter full name: ')
        phone_number = input('Enter phone number: ')
        city_state = input('Enter city ot state: ')
        print(i)
        dictionary[i]['first_name'] = first_name
        dictionary[i]['last_name'] = last_name
        dictionary[i]['full_name'] = full_name
        dictionary[i]['phone_number'] = phone_number
        dictionary[i]['city_state'] = city_state

        print('\n' + str(dictionary[i]) + '\n')

        with open(phonebook +'.txt', 'w') as dict_file:
            dict_file.write(json.dumps(dictionary[i]))
        choise()

    elif action == "f":
        first_name = input('Enter first name for search: ')

        for i in range(len(dictionary[i])):
            print(dictionary[i])
            try:
                print(dictionary[i])
            except KeyError:
                print("There is no such name in phonebook")
        choise()
    elif action != "a" or action != "f" or action != "l" or action != "F" or action != "n" or action != "c" or action != "d" or action != "u" or action != "e":
        print("There is no such actions key")
        choise()



action_with_phonebook(input_choise)


