from telephone_book import tel_dictionary
from exceptions import WrongValueInput


def show_value():
    if not tel_dictionary:
        print('This telephone book is empty now, try to \
        insert something firstly')
    else:
        search_value = int(input('What do you want to get? \
        \nphone - insert 1 and press Enter or name - insert 2 and press Enter:'))
        if search_value == 1:
            name = input('Search by name:')
            if name:
                print('the phone number is: {}'.format(tel_dictionary[name]))
            else:
                raise WrongValueInput('No such name {}:'.format(name))
        elif search_value == 2:
            phone = input('Search by phone:')
            if phone in tel_dictionary.values():
                for i in tel_dictionary.items():
                    if i[1] == '{}'.format(phone):
                        print('The name of such phone is:', i[0])
                        break
            else:
                raise WrongValueInput('No such phone number - {}'.format(phone))
        else:
            raise WrongValueInput("You've inserted wrong value, try again")

