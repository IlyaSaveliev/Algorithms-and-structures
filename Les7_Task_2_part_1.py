# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    left = merge_sort(arr[:len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2:len(arr)])

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1

    while i < len(left):
        arr[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        arr[k] = right[j]
        j = j + 1
        k = k + 1
    return arr


print(merge_sort(array))
