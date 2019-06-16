import copy

#1 Build a square


def print_rectangle(n, m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i == 1 or i == n or
                    j == 1 or j == m):
                print("*", end="")
            else:
                print(" ", end="")

        print()

print_rectangle(3, 4)

#2 Sum all elements in matrix
sum = 0
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [8, 7, 6]]
for raw in matrix:
    for value in raw:
        sum += value
print(sum)


#3 Sum right diagonal of matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
counter = -1
sum = 0
for raw in matrix:
    counter += 1
    for value in raw[counter:]:
        sum = sum + value

#4 Find out sum of matrix digonals
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
counter = 0
sum = 0
for raw in matrix:
    counter += 1
    sum += raw[len(raw)-counter] + raw[-1 + counter]
print('Sum of matrix diagonal =', sum)

#5 Example of list copy


def get_list(list):
    return list

array_1 = [1, 2]
print(get_list(array_1.copy()))

#6 Interactive menu
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
                name = input('Serach by name:')
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

#7 Count numbers with same 3 digits in line
dictionary_1 = ({'Anna': '0934440391', 'Alex': '0501111601'})
for name, phone in dictionary_1.items():
    for i in range(0, len(phone) - 2):
        if phone[0+i] == phone[1+i] == phone[2+i]:
            print('There are same three "{}" digits in a row'.format(phone[0+i]))
            break








