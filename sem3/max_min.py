# 1. Задайте строку из набора чисел. Напишите программу, которая покажет
# большее и меньшее число. В качестве символа-разделителя используйте пробел.

def max_min(str_num):
    str_num = str_num.split(' ')
    str_num = [int(i) for i in str_num]
    return max(str_num), min(str_num)

str_num = input('введите числа через пробел: ')
ans = max_min(str_num)
print(f'Максимальное число: {ans[0]}\nМинимальное число: {ans[1]}')

