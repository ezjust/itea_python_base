import math
import random

'''Home tasks, 1.5b'''
#1
string_1 = 'inserted any string With one uppercase letter'
for letter in string_1:
    if letter.isupper():
        break
    else:
        print(letter, end="")
#2
value = int(input('input int value: '))
if value == 0:
    print('factorial is: ', 1)
else:
    print('factorial is: ', math.factorial(value))
#3
value = int(input('insert any int:'))
while 0 < value < 100000:
    value = value*value
    print(value*value)
#4
def is_prime(num):
    if (math.factorial(num - 1) + 1) % num != 0:
        print('NO it is not prime number')
    else:
        print('YES it is prime number')


num = int(input('insert number: '))
is_prime(num)

#5
sum = 0
num = int(input('insert number: '))
if num < 1:
    print('value < 1 could not be calculated: ')
else:
    for i in range(1, (num + 1)):
        if num % i == 0:
            sum += i
    print('sum of all dividers: ', sum)

#6
num = int(input('insert number of lines: '))
for i in range(1, (num + 1)):
    line_pic = i * '/\\'
    print(line_pic.center(n*2, ' '))

#7
a, b = list(map(int, input('nsert two values separated by comma: ').split(',')))
if a < b:
    ran = random.randint(a, b)
    guess = int(input('please try to guess value set: '))
    for i in range(a, b):
        if ran == guess:
            print("Ihhaaa, you're right")
            break
        elif ran > guess:
            guess = int(input('your value is lower then random one, try again: '))
        else:
            guess = int(input('your value is greater then random one, try again: '))
elif a > b:
    print('You have inserted bad values: {} > {} . Retry with integers'.format(a, b,))
else:
    print('You have inserted bad values: {} = {} and {} = {} . Retry with integers'.format(a, type(a), b, type(b)))





