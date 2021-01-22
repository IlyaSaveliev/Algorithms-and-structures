# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход
# натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».

import cProfile, timeit


def eratosthenes_sieve(n):
    count = 1
    start = 3
    end = 4 * n

    sieve = [i for i in range(start, end) if i % 2 != 0]
    prime = [2]

    if n == 1:
        return 2

    while count < n:

        for i in range(len(sieve)):

            if sieve[i] != 0:
                count += 1

                if count == n:
                    return sieve[i]

                j = i + sieve[i]

                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[i]

        prime.extend([i for i in sieve if i != 0])

        start, end = end, end + 2 * n
        sieve = [i for i in range(start, end) if i % 2 != 0]

        for i in range(len(sieve)):

            for num in prime:

                if sieve[i] % num == 0:
                    sieve[i] = 0
                    break

print(timeit.timeit('eratosthenes_sieve(10)', number=100, globals=globals()))     # 0.0010560999999999973
print(timeit.timeit('eratosthenes_sieve(50)', number=100, globals=globals()))     # 0.013885700000000004
print(timeit.timeit('eratosthenes_sieve(100)', number=100, globals=globals()))    # 0.036910000000000005
print(timeit.timeit('eratosthenes_sieve(500)', number=100, globals=globals()))    # 1.0554066999999998
print(timeit.timeit('eratosthenes_sieve(1000)', number=100, globals=globals()))   # 3.5236889

cProfile.run('eratosthenes_sieve(100)')
#  353 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_task_2_part_1.py:10(eratosthenes_sieve)
#         1    0.000    0.000    0.000    0.000 Lesson_4_task_2_part_1.py:15(<listcomp>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_task_2_part_1.py:37(<listcomp>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_task_2_part_1.py:40(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       345    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
cProfile.run('eratosthenes_sieve(500)')
# 2040 function calls in 0.011 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.011    0.011 <string>:1(<module>)
#         1    0.010    0.010    0.011    0.011 Lesson_4_task_2_part_1.py:10(eratosthenes_sieve)
#         1    0.000    0.000    0.000    0.000 Lesson_4_task_2_part_1.py:15(<listcomp>)
#         2    0.000    0.000    0.000    0.000 Lesson_4_task_2_part_1.py:37(<listcomp>)
#         2    0.000    0.000    0.000    0.000 Lesson_4_task_2_part_1.py:40(<listcomp>)
#         1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
#      2029    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
cProfile.run('eratosthenes_sieve(1000)')
# 4289 function calls in 0.036 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.035    0.035 <string>:1(<module>)
#         1    0.034    0.034    0.035    0.035 Lesson_4_task_2_part_1.py:10(eratosthenes_sieve)
#         1    0.000    0.000    0.000    0.000 Lesson_4_task_2_part_1.py:15(<listcomp>)
#         2    0.000    0.000    0.000    0.000 Lesson_4_task_2_part_1.py:37(<listcomp>)
#         2    0.000    0.000    0.000    0.000 Lesson_4_task_2_part_1.py:40(<listcomp>)
#         1    0.000    0.000    0.036    0.036 {built-in method builtins.exec}
#      4278    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
cProfile.run('eratosthenes_sieve(5000)')
#  23584 function calls in 1.459 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.459    1.459 <string>:1(<module>)
#         1    1.449    1.449    1.458    1.458 Lesson_4_task_2_part_1.py:10(eratosthenes_sieve)
#         1    0.002    0.002    0.002    0.002 Lesson_4_task_2_part_1.py:15(<listcomp>)
#         3    0.001    0.000    0.001    0.000 Lesson_4_task_2_part_1.py:37(<listcomp>)
#         3    0.004    0.001    0.004    0.001 Lesson_4_task_2_part_1.py:40(<listcomp>)
#         1    0.000    0.000    1.459    1.459 {built-in method builtins.exec}
#     23570    0.003    0.000    0.003    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         3    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
cProfile.run('eratosthenes_sieve(10000)')
#  48786 function calls in 9.960 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    9.960    9.960 <string>:1(<module>)
#         1    9.936    9.936    9.960    9.960 Lesson_4_task_2_part_1.py:10(eratosthenes_sieve)
#         1    0.004    0.004    0.004    0.004 Lesson_4_task_2_part_1.py:15(<listcomp>)
#         4    0.002    0.000    0.002    0.000 Lesson_4_task_2_part_1.py:37(<listcomp>)
#         4    0.012    0.003    0.012    0.003 Lesson_4_task_2_part_1.py:40(<listcomp>)
#         1    0.000    0.000    9.960    9.960 {built-in method builtins.exec}
#     48769    0.007    0.000    0.007    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         4    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
