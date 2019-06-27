from my_exceptions import ValueOutOfRange
from my_exceptions import NoValueInList

# Без использования методов словарей(кроме items), напишите  функцию remove по ключу и remove по значению


def remove_by_index(my_list=[1, 4, 5, 17, 4, 6, 8, 12, 16], index=5):
    if index > len(my_list):
        raise ValueOutOfRange("index is bigger than length of list, set index properly")
    for i in range(0, len(my_list)):
        if i == index:
            my_list = my_list[:i] + my_list[i+1:]
    return my_list


def remove_by_value(my_list=[1, 4, 5, 17, 4, 6, 8, 16, 5, 5], value=13):
    new_list = []
    exist = 0
    for i in my_list:
        if i != value:
            new_list.append(i)
        else:
            exist += 1
    if exist == 0:
        raise NoValueInList('There is no value = "{}" in provided list'.format(value))
    return new_list

print(remove_by_value())








