# Найти сумму цифр числа 2 способами: циклом интерпретируя число как str
# и с помощью операций ‘%’, ‘/’, интерпретируя число как Integer

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
