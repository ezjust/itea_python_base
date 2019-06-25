import math

# Проверить является ли введенное число простым.
# Число считается простым если оно не делится нацело на все числа до квадратного корня этого числа


def is_prime(num):
    if (math.factorial(num - 1) + 1) % num != 0:
        return 'NO it is not prime number'
    else:
        return 'YES it is prime number'


num = int(input('insert number: '))
is_prime(num)
