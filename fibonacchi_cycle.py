# Вывести n чисел фибоначчи: 1 1 2 3 5 8 13...

array = []
for value in range(0, 10):
    if value == 1:
        array.append(value)
    if 1 < value < 3:
        array.append(value-1)
    if value > 2:
        array.append(array[value-2] + array[value-3])
print('fibonacchi numbers: ', array, end='')
