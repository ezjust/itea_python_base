import math
import random
import time
'''tasks in lab, Constructions'''

#1
# for i in range(1, 11):
#     print(i*i)

#2
# a=0
# while a*a<=1000:
#     a+=1
#     i=a*a
#     print(i)

#3
# a=input("put the value:" ) #to make one and more itterations running, put the value that is more than 100
# while math.sqrt(int(a))>10:
#     print(math.sqrt(int(a)))
#     a=int(a)
#     a=a-1

#4
# a="This is Hard timE fOr ouR countrY"
# for i in a:
#     if i.isupper():
#         print(i, end='')

#5
# a, b = input("print two values separated by comma: ").split(',')
# a=int(a)
# b=int(b)
# print(a+b)

#6
# a=0
# while a in range(0,20):
#     a=a+1
#     if a % 2 == 0:
#         print(a)

#7
# i=int(input("input any int: "))
# v_list = []
# while i !=0:
#     v_list.append(i)
#     i=int(input("input any int: "))
#     if i == 0:
#         v_list.append(i)
# print("list length: ", (len(v_list)))
# sum=0
# for num in v_list:
#     sum=sum+num
# print("sum of elements in the list: ", sum)
# print("average value from the list is:", sum/len(v_list))


#8
# y = "5101520"
# total = 0
# for i in y:
#     total += int(i)
# print("total for str is: ", total)
# t = 0
#
# x = 5101520
# while x > 0:
#     dig = x % 10
#     t = t + dig
#     x = x//10
# print("total sum of digits in int is:", t)


#9
# a = []
# for val in range(0, 10):
#     if val == 0:
#         continue
#     if val == 1:
#         a.append(val)
#     if 1 < val < 3:
#         a.append(val-1)
#     if val > 2:
#         a.append(a[val-2] + a[val-3])
# print("fibonacchi numbers: ", a, end="")




'''Modules tasks'''
#1
# print(random.randint(3, 30))

#2
# print(time.strftime("%H:%M:%S", (time.localtime())))

#3
# x = int(input("insert integer:"))
# print("cosinus of x is: ", math.cos(x), "\nsinus of x is: ", math.sin(x))


'''Function tasks'''
#1
# def ave_val(list):
#     average = sum(list)/len(list)
#     return print("the avarage value is: ", int(average))
# ave_val([1,3,4,6,6])

#2

# def sum_list_val(list):
#     new_dict = {}
#     for i in list:
#         dig = i % 10
#         dig2 = i//10
#         t = dig + dig2
#         new_dict.update({i : t})
#         print(t, end='; ')
#     return new_dict
#
#
# def sorted_list():
#     print("\nSorted list valus by sum of digits: ", sorted(sum_list_val([74,34,55]).keys()))
# sorted_list()

#3
# def rand_vals(start, end):
#     list = []
#     for i in range(0, 5):
#         list.append(random.randint(start, end))
#     return list
#
# print("List of random values: ", rand_vals(1,2))


#4
# def num_factorial(value):
#     if value == 0:
#         return 1
#     else:
#         return value * math.factorial(value-1)
#
# print(num_factorial(40))

'''Recursion tasks'''
#1
# def sum_dig(list):
#     list2 = []
#     for i in list:
#         sum = (i % 10) + (i // 10)
#         list2.append(sum)
#     if len(list) < 2:
#         print("List was set with 1 element, so used default one, where sum of number equal: ")
#         sum_dig([33,14,15])
#     else:
#         return print(list2)
#
# sum_dig([13])

#2
# n = int(input("insert number: "))
# for i in range(0,64):
#     if n == 2**i:
#         print("YES")
#         exit()
# print("NO")

#3
# list1 = []
# n = 3456789
# for dig in reversed(str(n)):
#     print(dig, end=" ")







