# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 15
MIN_ITEM = -5
MAX_ITEM = 25
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

index_max = 0
index_min = 0

for i in range(1, len(array)):
    if array[i] > array[index_max]:
        index_max = i
    if array[i] < array[index_min]:
        index_min = i
array[index_min], array[index_max] = array[index_max], array[index_min]

print(array)
