# 1.Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
# (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

import collections

n = int(input('Введите количество компаний: '))

corp = collections.defaultdict()
prof_c = collections.deque()
unprof_c = collections.deque()
all_profit = 0
quarter = 4

for i in range(n):
    name = input(f'\nВведите название {i+1}й компании: ')
    profit = 0
    q = 1

    while q <= quarter:
        profit += float(input(f'Введите прибыль за {q}й квартал: '))
        q += 1
    corp[name] = profit
    all_profit += profit

mid_profit = all_profit / n

for i, item in corp.items():
    if item > mid_profit:
        prof_c.append(i)
    elif item < mid_profit:
        unprof_c.append(i)


print(f'Средняя прибыль для всех компаний составила: {mid_profit}')
print(f'Прибыль выше среднего у {len(prof_c)} компаний:  ')
for name in prof_c:
    print(name)
print(f'Прибыль ниже среднего у {len(unprof_c)} компаний:')
for name in unprof_c:
    print(name)
