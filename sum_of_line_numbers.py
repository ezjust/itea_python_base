data = """
0.00002640
23174.4902
0.61180654
0.00002599
8434.0130
0.21919999
0.00002000
52622.1944
1.05244388
0.00001599
13708.5678
0.21919999
0.00001500
100232.3673
1.50348550
"""
numbers = []
for line in data.split():
    numbers.append(float(line))
print(numbers)
first_sum = sum(numbers[::3])
second_sum = sum(numbers[1::3])
third_sum = sum(numbers[2::3])
