import random

list_len = int(input('Set value:'))
random_list = []
last_same_counter = []
last_number = []
for i in range(0, list_len):
    random_list.append(random.randint(0, 1))
print(random_list)
count_same = 1
max_count_same = 1
for i in range(0, len(random_list) - 1):
    if random_list[i] == random_list[i+1]:
        count_same += 1
    else:
        max_count_same = max(max_count_same, count_same)
        count_same = 1
print('Maximum same characters in a row:', max_count_same)
