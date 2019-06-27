from my_exceptions import ValueOutOfRange

# Без использования методов строк, напишите реализацию таких методов строк:
# replace, split, find. Напишите функцию remove по индексу и по подстроке.


def split_string(sentence='this is the string'):
    split_values = []
    tmp = ''
    for c in sentence:
        if c == ' ':
            split_values.append(tmp)
            tmp = ''
        else:
            tmp += c
    if tmp:
        split_values.append(tmp)
    return split_values


def replace_string(input_string='it is the test test test', sub_string='test', matches=2, new_sub_string='result'):
    result = ''
    counter = 0
    new_list = split_string(sentence=input_string)
    for e in range(0, len(new_list)):
        if new_list[e] == sub_string and counter < matches:
            new_list[e] = new_sub_string
            counter += 1
        result = result + ' ' + new_list[e]
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
