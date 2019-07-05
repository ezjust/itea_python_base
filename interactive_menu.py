# Реализовать интерактивное меню с двумя опциями выбора:
# а) добавление в справочник
# б) вывод номера телефона по имени
# в) вывод имени по номеру телефона
#
# Пример
# Add to dict
# Get telephone
# Get name


def manage_telephone_book(tel_dictionary):
    print('\n\n---Hello this is telephone book---\n1 - save new item \
    \n2 - show all exist items by name/phone \
    \n3 - change existing record \
    \n4 - delete the record')
    value = int(input('Input the value:'))
    if value == 1:
        tel_dictionary[input('Insert Name: ')] = input('Insert Phone number:')
    elif value == 2:
        if not tel_dictionary:
            print('This telephone book is empty now, try to \
            insert something firstly')
        else:
            search_value = int(input('What do you want to get? \
            \nphone - insert 1 and press Enter \
            \nname - insert 2 and press Enter:'))
            if search_value == 1:
                name = input('Search by name:')
                if name:
                    print('the phone number is: {}'.format(tel_dictionary[name]))
                else:
                    print('No such name {}:'.format(name))
            elif search_value == 2:
                phone = input('Search by phone:')
                if phone in tel_dictionary.values():
                    for i in tel_dictionary.items():
                        if i[1] == '{}'.format(phone):
                            print('The name of such phone is:', i[0])
                            break
                else:
                    print('No such phone number - {}'.format(phone))
            else:
                print("You've inserted wrong value, try again")
    elif value == 3:
        print('There are such records in this book:')
        counter = 0
        for key, value in tel_dictionary.items():
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
            print("Phone didn't change and = {}".format(old_value))
    elif value == 4:
        print('There are such records in this book:')
        counter = 0
        for key, values in tel_dictionary.items():
            print('Record #{} Name: {}   Phone: {}'.format(counter, key, values))
            counter += 1
        delete_item = int(input("Choose record number to be removed:"))
        delete_key = list(tel_dictionary.keys())[delete_item]
        tel_dictionary.pop(delete_key, None)
    else:
        print("You've inputted wrong one value, \
please try again with only 1 or 2")
    return tel_dictionary.items()


dictionary_1 = {'Anna': '0934540391', 'Alex': '0501761601'}
manage_telephone_book(dictionary_1)

