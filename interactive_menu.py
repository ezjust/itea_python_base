from telephone_book import tel_dictionary
from show.show_existane_values import show_value
from save.save_value import save_value
from change.change_value import change_value
from delete.delete_value import delete_value

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

if value == 1:
    save_value()
elif value == 2:
    show_value()
elif value == 3:
    change_value()
elif value == 4:
    delete_value()

print('There are such telephone notes in the book:')
for name, tel in tel_dictionary.items(): # Cycle to print current values into tel book
    print(f'Name: {name}, Phone: {tel}')


