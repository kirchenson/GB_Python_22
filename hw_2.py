"""Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11
"""
import datetime,random

n = float(input("введите число : "))
s = 0
n = str(n)
for i in n:
    try:
	s += int(i) 
    except ValueError:
	continue
		
print(s)
	


"""Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)"""

n = int(input('Введите n для набора произведений от 1 до n:  '))
d = []
s = 1
for i in range(1, n+1):
    s *= i
    d.append(s)
print(d)


"""Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
Пример:
- Для n = 5: сумма = 11,55"""

n = int(input('Введите n для суммы последовательности (1+ (1/n))^n: '))
l = []
for i in range(1,n+1):
    l.append((1 + (1/i))**i)
print(round(sum(l),2))

"""Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на 
указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
Реализуйте алгоритм перемешивания списка.(Без использования библиотеки random)"""

n = int(input('введите n для создания списка [-N, N] : '))
l = [i for i in range(-n,n+1)]
pr = 1
with open('file') as f:
    for line in f:
        pr *= l[int(line)]
        print(l[int(line)])
print(pr)

"Алгоритм перемешивания"

lst = []
for i in range(random.randint(10,20)):
    a = random.randint(1,100)
    lst.append(a)

for i in range(0,len(lst)):
    j = datetime.datetime.now().microsecond % len(lst)
    lst[i],lst[j] = lst[j],lst[i]

print(lst)

