import math
import random

'''Home tasks, 1.5b'''
#1
# a = "inserted any string With one uppercase letter"
# for let in a:
#     if let.isupper():
#         break
#     else:
#         print(let, end="")
#2
# value = int(input("input int value: "))
# if value == 0:
#     print("factorial is: ", 1)
# else:
#     print("factorial is: ", math.factorial(value))
#3
# val = int(input("insert any int:" ))
# while 0 < val < 100000:
#     val=val*val
#     print(val*val)
#4
# def is_prime(n):
#     if (math.factorial(n - 1) + 1) % n != 0:  # Теорема Вильсона
#         print('NO it is not prime number')
#     else:
#         print('YES it is prime number')
#
#
# n = int(input("insert number: "))
# Isprime(n)

#5
# sum = 0
# n = int(input("insert number: "))
# if n < 1:
#     print("value < 1 could not be calculated: ")
# else:
#     for i in range(1,(n+1)):
#         if n % i == 0:
#             summ += i
#     print("sum of all devidors: ", summ)

#6
# n = int(input("insert number of lines: "))
# for i in range(1,(n+1)):
#     cstr = i * "/\\"
#     print(cstr.center(n*2, " "))

#7
# a, b = list(map(int, input("Insert two values separated by comma: ").split(',')))
# if a < b:
#     print(a,b)
#     ran = random.randint(int(a),int(b))
#     guess = int(input("please try to guess value set: "))
#     for i in range(a,b):
#         if ran == guess:
#             print("Ihhaaa, you're right")
#             break
#         elif ran > guess:
#             guess = int(input("your value is lower then random one, try again: "))
#             continue
#         else:
#             guess = int(input("your value is greater then random one, try again: "))
#             continue
# elif a > b:
#     print("You have inserted bad values: {} > {} . Retry with integers".format(a, b,))
# else:
#     print("You have inserted bad values: {} = {} and {} = {} . Retry with integers".format(a, type(a), b, type(b)))





