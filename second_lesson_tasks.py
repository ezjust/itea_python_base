import math
import random
import time
'''tasks in lab, Constructions'''

#1
for i in range(1, 11):
    print(i*i)

#2
a = 0
while a <= 1000:
    a += 1
    i = a*a
    if i < 1000:
        print(i)

#3
a = input('put the value:')   # make one and more iterations running, put the value that is more than 100
while math.sqrt(int(a)) > 10:
    print(math.sqrt(int(a)))
    a = int(a)
    a = a-1

#4
a = 'This is Hard timE fOr ouR countrY'
for i in a:
    if i.isupper():
        print(i, end='')

#5
a, b = input('print two values separated by comma: ').split(',')
a = int(a)
b = int(b)
print(a+b)

#6
a = 0
while a in range(0, 20):
    a = a+1
    if a % 2 == 0:
        print(a)

#7
i = int(input('input any int: '))
v_list = []
while i != 0:
    v_list.append(i)
    i = int(input('input any int: '))
    if i == 0:
        v_list.append(i)
print('list length: ', (len(v_list)))
sum = 0
for num in v_list:
    sum = sum + num
print('sum of elements in the list: ', sum)
print('average value from the list is:', sum/len(v_list))


#8
y = '5101520'
total = 0
for i in y:
    total += int(i)
print('total for str is: ', total)
t = 0
x = 5101520
while x > 0:
    digit = x % 10
    t = t + digit
    x = x//10
print('total sum of digits in int is:', t)


#9
array = []
for value in range(0, 10):
    if value == 1:
        array.append(value)
    if 1 < value < 3:
        array.append(value-1)
    if value > 2:
        array.append(array[value-2] + array[value-3])
print('fibonacchi numbers: ', array, end='')




'''Modules tasks'''
#1
print(random.randint(3, 30))

#2
print(time.strftime('%H:%M:%S', (time.localtime())))

#3
x = int(input('insert integer:'))
print('cosinus of x is: ', math.cos(x), '\nsinus of x is: ', math.sin(x))


'''Function tasks'''
#1


def get_average_value(list):
    average = sum(list)/len(list)
    return print('the average value is: ', int(average))


get_average_value([1, 3, 4, 6, 6])

#2


def sum_list_values(list):
    new_dictionary = {}
    for i in list:
        digit_1 = i % 10
        digit_2 = i//10
        t = digit_1 + digit_2
        new_dictionary.update({i:t})
        print(t, end='; ')
    return new_dictitonary


def sort_list():
    print('\nSorted list values by sum of digits: ', sorted(sum_list_values([74, 34, 55]).keys()))


sort_list()

#3


def get_random_values(start, end):

    list_1 = []
    for i in range(0, 5):
        list_1.append(random.randint(start, end))
    return list_1


print('List of random values: ', get_random_values(1,2))


#4


def get_num_factorial(value):
    if value == 0:
        return 1
    else:
        return value * math.factorial(value-1)


print(get_num_factorial(40))

'''Recursion tasks'''
#1


def sum_digits(list_1):
    list2 = []
    for i in list_1:
        sum = (i % 10) + (i // 10)
        list2.append(sum)
    if len(list_1) < 2:
        print('List was set with 1 element, so used default one, where sum of number equal: ')
        sum_dig([33, 14, 15])
    else:
        return list2


sum_digits([13])

#2
number = int(input('insert number: '))
for i in range(0, 64):
    if number == 2**i:
        print("YES")
        exit()
print("NO")

#3
list1 = []
num = 3456789
for digit in reversed(str(num)):
    print(digit, end=" ")