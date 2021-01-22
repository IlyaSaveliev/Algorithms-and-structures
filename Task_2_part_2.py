# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход
# натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Второй — без использования «Решета Эратосфена».

import cProfile, timeit

def search_prime(n):
    count = 1
    number = 1
    prime = [2]

    if n == 1:
        return 2

    while count != n:
        number += 2

        for num in prime:
            if number % num == 0:
                break
        else:
            count += 1
            prime.append(number)

    return number

print(timeit.timeit('search_prime(10)', number=100, globals=globals()))   # 0.0005921999999999976
print(timeit.timeit('search_prime(50)', number=100, globals=globals()))   # 0.008538700000000003
print(timeit.timeit('search_prime(100)', number=100, globals=globals()))  # 0.030337899999999994
print(timeit.timeit('search_prime(500)', number=100, globals=globals()))  # 0.8638881999999999
print(timeit.timeit('search_prime(1000)', number=100, globals=globals())) # 3.7226290000000004


cProfile.run('search_prime(100)')
# 103 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_task_2_part_2.py:9(search_prime)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('search_prime(500)')
# 503 function calls in 0.009 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.009    0.009 <string>:1(<module>)
#         1    0.009    0.009    0.009    0.009 Lesson_4_task_2_part_2.py:9(search_prime)
#         1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
#       499    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('search_prime(1000)')
# 1003 function calls in 0.037 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.037    0.037 <string>:1(<module>)
#         1    0.037    0.037    0.037    0.037 Lesson_4_task_2_part_2.py:9(search_prime)
#         1    0.000    0.000    0.037    0.037 {built-in method builtins.exec}
#       999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('search_prime(5000)')
# 5003 function calls in 1.478 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.478    1.478 <string>:1(<module>)
#         1    1.477    1.477    1.478    1.478 Lesson_4_task_2_part_2.py:9(search_prime)
#         1    0.000    0.000    1.478    1.478 {built-in method builtins.exec}
#      4999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('search_prime(10000)')
#  10003 function calls in 7.973 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    7.973    7.973 <string>:1(<module>)
#        1    7.972    7.972    7.973    7.973 Lesson_4_task_2_part_2.py:9(search_prime)
#        1    0.000    0.000    7.973    7.973 {built-in method builtins.exec}
#     9999    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
