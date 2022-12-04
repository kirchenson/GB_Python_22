""" Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатиричную систему счисления."""

hex_dict = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}

dec = int(input('Введите число : '))
hex_num = ''

while dec > 0:
    x = str(dec % 16)
    if x in hex_dict:
        x = hex_dict[x]
    else:
        hex_num += x
    dec //= 16

print(hex_num[::-1])
