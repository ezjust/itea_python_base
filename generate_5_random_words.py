import random
import pickle

def five_random_words():
    return ' '.join([str(item) for item in random.sample(range(1, 10), 5)])


with open('test3_result.txt', 'a') as result3_file:
    for i in range(100):
        result3_file.write(five_random_words() + '\n')
with open('test3_result_pickle', 'ab') as result3_pickle:
    for i in range(100):
        pickle.dump(five_random_words() + '\n', result3_pickle)
