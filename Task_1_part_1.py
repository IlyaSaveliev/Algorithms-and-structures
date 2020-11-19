# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Задача - найти максимальный отрицательный элемент в массиве.

import random, sys

size = 1
while size != 10:
    size *= 10
    arr = [random.randint(size * -5, size * 5) for _ in range(size)]
    print(arr)

print('*************************************************')

def max_negativ_num(arr):
    i = 0
    index = -1

    while i < len(arr):
        if arr[i] < 0 and index == -1:
            index = i
        elif 0 > arr[i] > arr[index]:
            index = i
        i += 1

    if index != -1:
         return f'Максимальное отрицательное число:{arr[index]}. \n Его индекс в массиве:{index}'

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

show(size)
print('***')
show(arr)
print('***')
show(max_negativ_num(arr))
print('***')
show(i)
print('***')
show(index)

#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=10,
#***
#type(x)=<class 'list'>, sys.getsizeof(x)=92, x=[-29, 38, -27, 36, 50, -49, 23, -32, -8, -40],
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=-29,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=38,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=-27,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=36,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=50,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=-49,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=23,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=-32,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=-8,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=-40,
#***
#type(x)=<class 'str'>, sys.getsizeof(x)=160, x='Максимальное отрицательное число:-8. \n Его индекс в массиве:8',
#***
