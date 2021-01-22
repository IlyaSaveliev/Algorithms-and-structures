# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков.

import random, cProfile, timeit

def max_negativ_num(size):
    array = [random.randint(size * -10, size * 10) for _ in range(size)]


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

print(timeit.timeit('max_negativ_num(10)', number=1000, globals=globals()))      #0.021721
print(timeit.timeit('max_negativ_num(100)', number=1000, globals=globals()))     #0.20007080000000002
print(timeit.timeit('max_negativ_num(1000)', number=1000, globals=globals()))    #2.1280569
print(timeit.timeit('max_negativ_num(10000)', number=1000, globals=globals()))   #21.1541016


cProfile.run('max_negativ_num(10)')
#   71 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_task_1_part_1.py:6(max_negativ_num)
#         1    0.000    0.000    0.000    0.000 Lesson_4_task_1_part_1.py:7(<listcomp>)
#        10    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:244(randint)
#        10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        15    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('max_negativ_num(100)')
# 609 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_task_1_part_1.py:6(max_negativ_num)
#         1    0.000    0.000    0.000    0.000 Lesson_4_task_1_part_1.py:7(<listcomp>)
#       100    0.000    0.000    0.000    0.000 random.py:200(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:244(randint)
#       100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       103    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('max_negativ_num(1000)')
# 6633 function calls in 0.004 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#         1    0.000    0.000    0.004    0.004 Lesson_4_task_1_part_1.py:6(max_negativ_num)
#         1    0.001    0.001    0.003    0.003 Lesson_4_task_1_part_1.py:7(<listcomp>)
#      1000    0.001    0.000    0.002    0.000 random.py:200(randrange)
#      1000    0.001    0.000    0.003    0.000 random.py:244(randint)
#      1000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#      1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1627    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('max_negativ_num(10000)')
#         63214 function calls in 0.037 seconds
#
#      Ordered by: standard name

#      ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.037    0.037 <string>:1(<module>)
#        1    0.004    0.004    0.036    0.036 Lesson_4_task_1_part_1.py:6(max_negativ_num)
#        1    0.006    0.006    0.031    0.031 Lesson_4_task_1_part_1.py:7(<listcomp>)
#    10000    0.009    0.000    0.020    0.000 random.py:200(randrange)
#    10000    0.005    0.000    0.025    0.000 random.py:244(randint)
#    10000    0.007    0.000    0.010    0.000 random.py:250(_randbelow_with_getrandbits)
#        1    0.000    0.000    0.037    0.037 {built-in method builtins.exec}
#    10001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   13208    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
