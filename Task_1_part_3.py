# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков.

import random, cProfile, timeit

def max_negativ_num(size):
    array = [random.randint(size * -10, size * 10) for _ in range(size)]

    index = -1

    for i in array:
        if array[index] > i:
            index = array.index(i)

        if array[index] >= 0:
            return f'В массиве нет отрицательных элементов'
        else:
            return f'Максимальное отрицательное число:{array[index]}. \n Его индекс в массиве:{index}'


print(timeit.timeit('max_negativ_num(10)', number=1000, globals=globals()))    # 0.017320000000000002
print(timeit.timeit('max_negativ_num(100)', number=1000, globals=globals()))   # 0.1602793
print(timeit.timeit('max_negativ_num(1000)', number=1000, globals=globals()))  # 1.7049565999999998
print(timeit.timeit('max_negativ_num(10000)', number=1000, globals=globals())) # 16.855123499999998

cProfile.run('max_negativ_num(10)')
# 59 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_task_1_part_3.py:6(max_negativ_num)
#         1    0.000    0.000    0.000    0.000 Lesson_4_task_1_part_3.py:7(<listcomp>)
#        10    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:244(randint)
#        10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        14    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('max_negativ_num(100)')
#  505 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_task_1_part_3.py:6(max_negativ_num)
#         1    0.000    0.000    0.000    0.000 Lesson_4_task_1_part_3.py:7(<listcomp>)
#       100    0.000    0.000    0.000    0.000 random.py:200(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:244(randint)
#       100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       100    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('max_negativ_num(1000)')
#   5629 function calls in 0.003 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.000    0.000    0.003    0.003 Lesson_4_task_1_part_3.py:6(max_negativ_num)
#         1    0.001    0.001    0.003    0.003 Lesson_4_task_1_part_3.py:7(<listcomp>)
#      1000    0.001    0.000    0.002    0.000 random.py:200(randrange)
#      1000    0.000    0.000    0.003    0.000 random.py:244(randint)
#      1000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1623    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
cProfile.run('max_negativ_num(10000)')
#  53048 function calls in 0.029 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.029    0.029 <string>:1(<module>)
#         1    0.000    0.000    0.029    0.029 Lesson_4_task_1_part_3.py:6(max_negativ_num)
#         1    0.006    0.006    0.029    0.029 Lesson_4_task_1_part_3.py:7(<listcomp>)
#     10000    0.009    0.000    0.019    0.000 random.py:200(randrange)
#     10000    0.005    0.000    0.023    0.000 random.py:244(randint)
#     10000    0.006    0.000    0.010    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.029    0.029 {built-in method builtins.exec}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     13043    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
