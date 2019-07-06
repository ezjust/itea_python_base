from collections import Counter

words_count = []
with open('test1.txt') as file1:
    counter = Counter()
    for line in file1:
        line = line.strip().split('\t')
        words = line[0].split()
        counter.update(words)
    top5 = [word[0] for word in counter.most_common(5)]
with open('test1_result.txt', 'w') as result_file:
    for word in top5:
        result_file.write(word + '\n')
