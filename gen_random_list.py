import random

list_len = int(input('Set value:'))
random_list = []
last_same_counter = []
last_number = []
for i in range(0, list_len):
    random_list.append(random.randint(0, 1))
print(random_list)
count_same = 1
for i in range(0, len(random_list) - 1):
    print(random_list[i], random_list[i + 1])
    if random_list[i] == random_list[i + 1]:
        count_same += 1
    else:
        last_same_counter.append(count_same)
        count_same = 1
last_same_counter.append(count_same)
print(last_same_counter)
print('Maximum same characters in a row:', max(last_same_counter))
