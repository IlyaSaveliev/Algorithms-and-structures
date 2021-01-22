# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random

m = 10
SIZE = 2 * m + 1
MIN_ITEM = 0
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


def median(arr):
    arr = sorted(arr)
    len(arr) // 2
    return arr[len(arr) // 2]

# Так бы выглядела функция, если бы мы точно не знали, что массив состоит из нечетного количества элементов.
#def median(arr):
#    arr = sorted(arr)
#    if len(arr) % 2 == 1:
#        return arr[len(arr) // 2]
#    else:
#        return 0.5 * (arr[len(arr) // 2 - 1] + arr[len(arr) // 2])


print(sorted(array))
print(median(array))
