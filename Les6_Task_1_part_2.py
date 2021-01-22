# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# В данной задаче массив генерируется рандомно, но присутствуют переменные, задающие его параметры.
# Задача - найти максимальный отрицательный элемент в массиве.

import random, sys

SIZE = 10
MIN_ITEM = -15
MAX_ITEM = 25
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(arr)

i = 0
index = -1

while i < SIZE:
        if arr[i] < 0 and index == -1:
            index = i
        elif 0 > arr[i] > arr[index]:
                index = i
        i += 1

print(f'Максимальное отрицательное число:{arr[index]}.\nЕго индекс в массиве:{index}')

print('*************************************************')

def show(x):
   print(f'{type(x)=}, {sys.getsizeof(x)=}, {x=},')
   if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show(key)
                show(value)
        elif not isinstance(x, str):
            for item in x:
                show(item)

show(arr)
print('***')
show(SIZE)
print('***')
show(MAX_ITEM)
print('***')
show(MIN_ITEM)
print('***')
show(i)
print('***')
show(index)

#type(x)=<class 'list'>, sys.getsizeof(x)=92, x=[-11, -11, -3, 15, 1, 15, 24, 23, 1, 3],
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=-11,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=-11,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=-3,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=15,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=1,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=15,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=24,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=23,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=1,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=3,
#***
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=10,
#***
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=25,
#***
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=-15,
#***
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=10,
#***
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=2,
