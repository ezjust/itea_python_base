import random

# 

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