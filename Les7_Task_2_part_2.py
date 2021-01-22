# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
# Решил для практики решить эту задачу двумя способами( второй четсно списан с wiki =)).
# Практика то никогда лишней не будет =)


import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

def merge_sort(arr):
    count = len(arr)
    if count > 2:
        part_1 = merge_sort(arr[:count // 2])
        part_2 = merge_sort(arr[count // 2:])
        arr = part_1 + part_2
        last_index = len(arr) - 1

        for i in range(last_index):
            min_value = arr[i]
            min_index = i

            for j in range(i + 1, last_index + 1):
                if min_value > arr[j]:
                    min_value = arr[j]
                    min_index = j

            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]

    elif len(arr) > 1 and arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]

    return arr

print(merge_sort(array))
