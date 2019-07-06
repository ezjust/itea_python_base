from telephone_book import tel_dictionary
from exceptions import WrongValueInput

def delete_value():
    print('There are such records in this book:')
    counter = 0
    for key, values in tel_dictionary.items():
        print('Record #{} Name: {}   Phone: {}'.format(counter, key, values))
        counter += 1
    delete_item = int(input('Choose record number to be removed:'))
    if delete_item <= len(tel_dictionary.items()):
        delete_key = list(tel_dictionary.keys())[delete_item]
        tel_dictionary.pop(delete_key, None)
    else:
        raise WrongValueInput("You've inserted wrong value, try again")
