# Напишите функцию, которая сортирует массив рекурсивно.


def sort_list_recursive(my_list):
    if len(my_list) <= 1:
        return my_list
    bigger = []
    smaller = []
    same = []
    zero_element = my_list[0]
    for e in range(0, len(my_list)):
        if my_list[e] > zero_element:
            bigger.append(my_list[e])
        elif my_list[e] < zero_element:
            smaller.append(my_list[e])
        else:
            same.append(my_list[e])
    sorted_smaller = sort_list_recursive(smaller)
    sorted_bigger = sort_list_recursive(bigger)
    return sorted_smaller + same + sorted_bigger


print(sort_list_recursive([15, 1, 16, 3, 14, 11, 17, 22, 9, 6]))
