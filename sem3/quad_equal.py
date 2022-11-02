#Найдите корни квадратного уровнения

def quad(a,b,c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return 'нет корней'
    elif d > 0:
        x1 = (-b + d ** (0.5)) / (2 * a)
        x2 = (-b - d ** (0.5)) / (2 * a)
        return x1,x2
    else:
        x = (-b) / (2 * a)
        return x

print('Нахождение корней уравнения ax^2 + bx + c: ')
a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))
print(f'Решение уравнения : {quad(a,b,c)}')

