class TelephoneBook:
    def __init__(self, name, phone):
        self.tel_dictionary = {name: phone}

    def add(self):
        self.tel_dictionary[input('Insert Name: ')] = input('Insert Phone number:')

    def show(self):
        if not self.tel_dictionary:
            print('This telephone book is empty now, try to \
                insert something firstly')
        else:
            search_value = int(input('What do you want to get? \
                \nphone - insert 1 and press Enter or name - insert 2 and press Enter:'))
            if search_value == 1:
                name = input('Search by name:')
                if name:
                    print('the phone number is: {}'.format(self.tel_dictionary[name]))
                else:
                    raise Exception('No such name {}:'.format(name))
            elif search_value == 2:
                phone = input('Search by phone:')
                if phone in self.tel_dictionary.values():
                    for i in self.tel_dictionary.items():
                        if i[1] == '{}'.format(phone):
                            print('The name of such phone is:', i[0])
                            break
                else:
                    raise Exception('No such phone number - {}'.format(phone))
            else:
                raise Exception("You've inserted wrong value, try again")

    def change(self):
        print('There are such records in this book:')
        counter = 0
        for key, values in self.tel_dictionary.items():
            print('Record #{} Name: {}   Phone: {}'.format(counter, key, values))
            counter += 1
        record_num = int(input("Input number of record to change:"))
        old_key = list(self.tel_dictionary.keys())[record_num]
        old_value = list(self.tel_dictionary.values())[record_num]
        new_key = input('New name:')
        self.tel_dictionary[new_key] = self.tel_dictionary.pop(old_key)
        new_value = input('New phone:')
        if new_value != '':
            self.tel_dictionary[new_key] = new_value
        else:
            self.tel_dictionary[new_key] = old_value
            raise Exception("Phone didn't change and = {}".format(old_value))

    def remove(self):
        print('There are such records in this book:')
        counter = 0
        for key, values in self.tel_dictionary.items():
            print('Record #{} Name: {}   Phone: {}'.format(counter, key, values))
            counter += 1
        delete_item = int(input('Choose record number to be removed:'))
        if delete_item <= len(self.tel_dictionary.items()):
            delete_key = list(self.tel_dictionary.keys())[delete_item]
            self.tel_dictionary.pop(delete_key, None)
        else:
            raise Exception("You've inserted wrong value, try again")

