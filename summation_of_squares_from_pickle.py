from test2 import sum_squares_of_elements
from statistics import median
import pickle

big_median_list = []
with open('test3_result_pickle', 'rb') as test3_pickle:
    data_new = [pickle.load(test3_pickle)]
    for line in data_new:
        big_median_list.append(int(median(line.split())))
print(sum_squares_of_elements(big_median_list))

