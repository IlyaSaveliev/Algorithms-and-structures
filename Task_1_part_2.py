# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков. Ожидаемо - это самый быстрый вариант!(=

import random, cProfile, timeit

def max_negativ_num(array):
    i = 0
    index = -1

    while i < len(array):
        if array[i] < 0 and index == -1:
            index = i
        elif 0 > array[i] > array[index]:
            index = i
        i += 1

    if index != -1:
         return f'Максимальное отрицательное число:{array[index]}. \n Его индекс в массиве:{index}'

size = 1
while size != 10000:
    size *=10
    array = [random.randint(size * -10, size * 10) for _ in range(size)]
    print(timeit.timeit('max_negativ_num(array)', number=1000, globals=globals()))
# 0.0041928
# 0.0340503
# 0.396833
# 3.9427164000000006

cProfile.run('max_negativ_num(array)')
#          10005 function calls in 0.006 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#         1    0.004    0.004    0.006    0.006 Lesson_4_task_1_part_2.py:6(max_negativ_num)
#         1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#     10001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
