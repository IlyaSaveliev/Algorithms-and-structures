# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# В данной задаче данные хранятся в кортеже.
# Задача - найти максимальный отрицательный элемент в массиве.

import sys

tpl = (1, 22, 18, -11, 3, 14, -8, -3, 6, 7, -6, 0, 14, 32,)

i = 0
index = -1

for i in tpl:
    if tpl[index] > i:
        index = tpl.index(i)

if tpl[index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'Максимальное отрицательное число:{tpl[index]}. \n Его индекс в массиве:{index}')

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

show(tpl)
print('***')
show(i)
print('***')
show(index)

#type(x)=<class 'tuple'>, sys.getsizeof(x)=76, x=(1, 22, 18, -11, 3, 14, -8, -3, 6, 7, -6, 0, 14, 32),
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=1,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=22,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=18,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=-11,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=3,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=14,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=-8,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=-3,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=6,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=7,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=-6,
#type(x)=<class 'int'>, sys.getsizeof(x)=12, x=0,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=14,
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=32,
#***
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=32,
#***
#type(x)=<class 'int'>, sys.getsizeof(x)=14, x=3,
