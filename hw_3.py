'''Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих 
на нечётной позиции.'''

import random, math

lst = []
sum = 0
#создание списка
for i in range(random.randint(5, 10)):
    a = random.randint(1, 25)
    lst.append(a)
print(lst)

for i in lst:
    if i % 2 != 0:
        sum += i
print(sum)

'''Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
 второй и предпоследний и т.д.'''

for i in range(math.ceil(len(lst)/2)):
    print(lst[i]*lst[-i-1], end = ' ')

'''Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
значением дробной части элементов. - [1.1, 1.2, 3.1, 5, 10.01] => 0.19 '''

lst = []

for i in range(random.randint(5, 10)):
    a = random.uniform(1, 25)
    lst.append(a)
print(f'\n{lst}')
mx = lst[0] - int(lst[0])
mn = lst[0] - int(lst[0])

for i in range(1, len(lst)):
    ost = lst[i] - int(lst[i])
    if ost < mn:
        mn = ost
    if ost > mx:
        mx = ost
print(mx - mn)

'''Нaпишите программу, которая будет преобразовывать десятичное число в двоичное.'''

a = int(input('Введите число в десятичной системе измерения: '))
binary = ''

while a > 0:
    x = a%2
    binary += str(x)
    a //= 2
    
print(f'Число в двоичной системе : {binary[::-1]}')

'''Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.'''

def F(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 0:
        return F(n-1) + F(n-2)
    else:
        return F(n + 2) - F(n + 1)
    
lst = []
n = int(input('Введите число для списка чисел Фибоначчи : '))
for i in range(-n,n+1):
    lst.append(F(i))
print(lst)
