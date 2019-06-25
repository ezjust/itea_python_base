# Написать рекурсивную функцию, которая возвращает сумму цифр числа

def sum_digits(list_1):
    list2 = []
    for i in list_1:
        summation = (i % 10) + (i // 10)
        list2.append(summation)
    if len(list_1) < 2:
        print('List was set with 1 element, so used default one, where sum of number equal: ')
        sum_digits([33, 14, 15])
    else:
        return list2


sum_digits([13])
