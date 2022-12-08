"""Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)"""

from random import randint

a = int(input())
b = int(input())
arr = []

for i in range(a):
    x = []
    s = 0
    for y in range(b):
        x.append(randint(1,10))
        s += x[y]
    arr.append(x)
    print(f'среднее арифметическое строки {i+1} = {s/b}')

print(arr)
