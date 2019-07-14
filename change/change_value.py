from telephone_book import tel_dictionary
from exceptions import WrongValueInput


def change_value():
    print('There are such records in this book:')
    counter = 0
    for key, values in tel_dictionary.items():
        print('Record #{} Name: {}   Phone: {}'.format(counter, key, values))
        counter += 1
    record_num = int(input("Input number of record to change:"))
    old_key = list(tel_dictionary.keys())[record_num]
    old_value = list(tel_dictionary.values())[record_num]
    new_key = input('New name:')
    tel_dictionary[new_key] = tel_dictionary.pop(old_key)
    new_value = input('New phone:')
    if new_value != '':
        tel_dictionary[new_key] = new_value
    else:
        tel_dictionary[new_key] = old_value
        raise WrongValueInput("Phone didn't change and = {}".format(old_value))
