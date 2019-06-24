import math

# Найти факториал числа

value = int(input('input int value: '))
if value == 0:
    print('factorial is: ', 1)
else:
    print('factorial is: ', math.factorial(value))

