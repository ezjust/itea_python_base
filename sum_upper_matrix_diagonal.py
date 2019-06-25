# Найти сумму верхней диагонали матрицы

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
counter = -1
summation = 0
for raw in matrix:
    counter += 1
    for value in raw[counter:]:
        summation = summation + value
