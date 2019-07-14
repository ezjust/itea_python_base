from my_exceptions import ValueOutOfRange
import re
# Без использования методов строк, напишите реализацию таких методов строк:
# replace, split, find. Напишите функцию remove по индексу и по подстроке.


def split_string(sentence='this is the string', splitter=' '):
    split_values = []
    counter = 0
    for i in range(0, len(sentence)):
        word = sentence[counter:i]
        if sentence[i] == splitter:
            split_values.append(word)
            counter = i + 1
    if word and word != ' ':
        split_values.append(sentence[counter:])
    return split_values


def replace_string(input_string='testhello testhello testhell', sub_string='hello', new_sub_string='result'):
    if sub_string in input_string:
        result = re.sub(r'{}'.format(sub_string), '{}'.format(new_sub_string), '{}'.format(input_string))
    return str(result)


def find_sub_string(input_string='this istest test', sub_string='e', start_c=0, end_c=15):
    counter = 0
    my_list = []
    if end_c < start_c:
        start_c, end_c = end_c, start_c
    if end_c < len(input_string):
        for i in range(start_c, end_c):
            if input_string[i] == sub_string and counter <= end_c:
                my_list.append('index of {} letter: {}'.format(sub_string, i))
                counter += 1
        matches = ''
        for e in my_list:
            matches += e + '\n'
        return matches
    else:
        raise ValueOutOfRange('Wrong search range, please reset the "end" value')


def remove_by_index(input_string='this istest test', index_remove=[1, 2, 100]):
    my_list = []
    for letter in range(0, len(input_string)):
        my_list.append(input_string[letter])
        for i in index_remove:
            if i >= len(input_string):
               raise ValueOutOfRange("Wrong search range, please set list of indexes properly")
            elif i == letter:
                my_list[letter] = ''
            new_string = ''
            for e in my_list:
                new_string += e
    return new_string


def remove_by_substring(input_string='this istest test', char_remove='e'):
    my_list = []
    for l in range(0, len(input_string)):
        my_list.append(input_string[l])
        if input_string[l] == char_remove:
            my_list[l] = ''
        new_string = ''
        for e in my_list:
            new_string += e
    return new_string


