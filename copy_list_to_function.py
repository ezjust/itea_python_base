# Как передать копию списка или словаря в функцию?


def get_list(list):
    return list


array_1 = [1, 2]
print(get_list(array_1.copy()))
