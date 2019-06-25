# Найти сумму диагональных элементов матрицы

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
counter = 0
summation = 0
for raw in matrix:
    counter += 1
    summation += raw[len(raw)-counter] + raw[-1 + counter]
print('Sum of matrix diagonal =', summation)
