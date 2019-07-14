# Без использования методов списков, напишите реализацию таких методов
# списков: insert, remove.


def remove_animal(my_list, data):
    result = []
    for i in my_list:
        if i == data:
            continue
        result += [i]
    return result


def insert_animal(my_list, index, data):
    return my_list[:index] + [data] + my_list[index:]
