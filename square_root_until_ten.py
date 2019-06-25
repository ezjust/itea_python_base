import math

# Извлекать квадратный корень из введенного пользователем числа до тех пор, пока значение больше 10.	

a = input('put the value:')   # make one and more iterations running, put the value that is more than 100
while math.sqrt(int(a)) > 10:
    print(math.sqrt(int(a)))
    a = int(a)
    a = a-1
