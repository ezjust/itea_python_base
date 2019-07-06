from test2 import sum_squares_of_elements
from statistics import median

big_median_list = []
with open('test3_result.txt', 'r') as test3_file:
    for line in test3_file:
        big_median_list.append(int(median(line.split())))
print(sum_squares_of_elements(big_median_list))
