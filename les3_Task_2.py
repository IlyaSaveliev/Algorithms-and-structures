# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 12
MIN_ITEM = 0
MAX_ITEM = 15
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

index_even = []

for n in array:
    if n % 2 == 0:
        index_even.append(array.index(n))

print(f'Индексы чётных элементов первого массива: {index_even}')
