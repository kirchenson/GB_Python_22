"""Морской бой с одним корабликом 1х1. Пользователь против программы"""

from random import randint

# создание поля для компьютера
arr = []
for i in range(5):
    arr.append(['*' for j in range(5)])
a, b, c, d = randint(0, 4), randint(0, 4), randint(0, 4), randint(0, 4)
count = 0

# создание поля пользователя
arr_1 = []
for i in range(5):
    arr_1.append(['*' for j in range(5)])
a_1,b_1 = int(input('Введите строку для первого корабля(1-5) : ')), int(input('Введите столбец для первого корабля(1-5) : '))
count_1 = 0

print('\nНа поле 5 x 5 расположен корабль. Попадите в него раньше, чем компьютер\n')

# функция для хода и изменения поля
def turn(x,y,arr,count):
    if x == a + 1 and y == b + 1:
        print('убил')
        arr[x - 1][y - 1] = '!'
        for i in arr:
            print(i)
        count += 1
        return count
    elif arr[x - 1][y - 1] == '0':
        print('уже пробовали, мимо')
    else:
        print('мимо')
        arr[x - 1][y - 1] = '0'
        for i in arr:
            print(i)
# цикл для поочередности ходов, начиная с пользователя
while True:
    x = int(input('\nВведите строку '))
    y = int(input('Введите столбец '))
    if turn(x,y,arr,count) == 1:
        print('\nвы выиграли')
        break
    print('\nХод компьютера')
    x_1, y_1 = randint(0,4),randint(0,4)
    print(f'cтрока {x_1 + 1}, столбец {y_1 + 1}')
    if turn(x_1,y_1,arr_1,count_1) == 1:
        print('\nвы проиграли')
        break
