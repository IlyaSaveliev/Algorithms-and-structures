#Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
#Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#В данной задаче я намерено преобразовал словарь в массив, чтобы наглядно увидеть разницу в размерах.
# Задача - найти максимальный отрицательный элемент в массиве.

import sys

dct = {1: 1, 2: -2, 3: -10, 4: 25, 5: 16, 6: 9, 7: 44, 8: 33, 9: -5, 10: 4, }
arr = list(dct.values())
print(arr)

i = 0
index = -1

while i < len(arr):
        if arr[i] < 0 and index == -1:
            index = i
        elif 0 > arr[i] > arr[index]:
                index = i
        i += 1

print(f'Максимальное отрицательное число:{arr[index]}. \n Его индекс в массиве:{index}')

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

show(dct)
print('***')
show(arr)
print('***')
show(i)
print('***')
show(index)

#type(x)=<class 'dict'>, sys.getsizeof(x)=196, x={1: 1, 2: -2, 3: -10, 4: 25, 5: 16, 6: 9, 7: 44, 8: 33, 9: -5, 10: 4},
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=1,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=1,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=2,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=-2,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=3,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=-10,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=4,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=25,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=5,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=16,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=6,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=9,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=7,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=44,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=8,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=33,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=9,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=-5,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=10,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=4,
#***
#type(x)=<class 'list'>, sys.getsizeof(x)=68, x=[1, -2, -10, 25, 16, 9, 44, 33, -5, 4],
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=1,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=-2,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=-10,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=25,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=16,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=9,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=44,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=33,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=-5,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=4,
#***
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=10,
#***
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=1,
