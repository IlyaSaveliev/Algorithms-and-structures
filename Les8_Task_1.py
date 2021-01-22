# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.

import hashlib

def subs(str):
    sub = set()
    for i in range(len(str)):
         for j in range(len(str), i, -1):
            hash_str = hashlib.sha1(str[i:j].encode('utf-8')).hexdigest()
            sub.add(hash_str)
    return len(sub) - 1


str = input('Введите строку, состоящую из маленьких латинских букв:')

print(subs(str))
