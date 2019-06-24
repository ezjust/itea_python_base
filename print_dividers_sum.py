# Вывести сумму всех делителей заданного числа

summation = 0
num = int(input('insert number: '))
if num < 1:
    print('value < 1 could not be calculated: ')
else:
    for i in range(1, (num + 1)):
        if num % i == 0:
            summation += i
    print('sum of all dividers: ', summation)
