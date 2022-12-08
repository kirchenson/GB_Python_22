"""Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором."""
from random import randint

a = [randint(1, 50) for i in range(20)]
print(a)

for i in range((len(a))):
    mn = 0
    ind = 0
    for y in range(i, len(a)):
        if mn == 0 or a[y] < mn:
            mn = a[y]
            ind = y
    a[i], a[ind] = min(a[i:]), a[i]

print(f'отсортированный по возрастанию список:\n{a}')
