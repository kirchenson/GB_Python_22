"""Вводим с клавиатуры целое число X и У.
Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3"""


x = int(input("введите x: "))
y = int(input("введите y: "))
c = 0
for i in range (x+1,y):
  if i % 3 == 0 and i % 2 == 0:
    c += 1
print(c)
