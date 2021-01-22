# 9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE_X = 7
SIZE_Y = 7
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_Y)] for _ in range(SIZE_X)]
print(*matrix, sep='\n')

max_el = 0
for j in range(SIZE_X):
    max_num = 100
    for i in range(SIZE_Y):
        if matrix[i][j] < max_num:
            max_num = matrix[i][j]
    if max_num > max_el:
        max_el = max_num

print(f'Максимальный эелемент среди минимальных: {max_el}')
