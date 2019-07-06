def sum_squares_of_elements(custom_list):
    summation = 0
    for element in custom_list:
        summation += element**2
    return summation


test_file2 = open('test2.py', 'w')
with open('sum_squares_of_list_elements.py', 'r') as f:
    for line in f:
        if not line.strip():
            break
        test_file2.write(line)
test_file2.close
