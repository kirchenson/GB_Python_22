"""
Вводим с клавиатуры целое число - это зарплата.
Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых
"""

def f(n,r,x):
    if x//n > 0:
        r+= x//n
        x=x%n
    arr = [x,r]
    return arr

x = int(input("введите x: "))
r = {25:0,10:0,3:0,1:0}
mn = 0
for key,value in r.items():
    func = f(key,value,x)
    r[key] = func[1]
    x = func[0]
    mn+= func[1]
print(f'Минимальное количество купюр: {mn}\nСколько и каких купюр использовалось:\n{r}')
