from collections import Counter

words_count = []
with open('test1.txt') as file1:
    for line in file1:
        for element in line.split():
            if element is not '':
                words_count.append(element)
words = Counter(words_count)
top5 = words.most_common(5)
print(top5)
with open('testit 1_result.txt', 'w') as result_file:
    for word in top5:
        result_file.write(word[0] + '\n')
