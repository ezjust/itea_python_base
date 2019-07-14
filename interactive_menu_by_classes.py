from tel_book_by_classes import TelephoneBook
# Реализовать интерактивное меню с двумя опциями выбора:
# а) добавление в справочник
# б) вывод номера телефона по имени
# в) вывод имени по номеру телефона
#
# Пример
# Add to dict
# Get telephone
# Get name

# This is start (greeting) menu such provides with value for other operation
print('\n\n---Hello this is telephone book---\n1 - save new item \
\n2 - show all exist items by name/phone \
\n3 - change existing record \
\n4 - delete the record')
value = int(input('Input the value:'))
book_manipulations = TelephoneBook('Anna', '0934540390')

if value == 1:
    book_manipulations.add()
elif value == 2:
    book_manipulations.show()
elif value == 3:
    book_manipulations.change()
elif value == 4:
    book_manipulations.remove()

print('There are such telephone notes in the book:')
for name, phone in book_manipulations.tel_dictionary.items():
    print(f'Name: {name}, Phone: {phone}')



