days = ['понедельник','вторник','среда','четверг','пятница','суббота','воскресенье']
def init(file,days):
    f = open(file,'w',encoding='utf-8')
    for i in range(len(days)):
        f.write(f'{days[i]}\n')
    f.close()

def reading(file):
    f = open(file,'r',encoding='utf-8')
    s = f.read()
    print(s)

def change(file):
    n = int(input('Для изменения планов пиши 1, для добавки к существующим - 11: '))
    for i in range(len(days)):
        print(f'{i+1} - {days[i]}')
    day = int(input('введите номер дня недели для изменения: '))
    with open(file,'r',encoding='utf-8') as f:
        lines = f.readlines()
        x = input('введите данные: ')
    with open(file, 'w', encoding='utf-8') as f:
        if n == 1:
            lines[day - 1] = f'{days[day-1]}  {x}\n'
            f.writelines(lines)
        elif n == 11:
            lines[day-1] = f'{lines[day-1][:-2]}, {x}\n'
            f.writelines(lines)

while True:
    t = int(input('Создание пустого расписания - 1, просмотр планов - 2, редактирования - 3, выход - 4: '))
    if t == 4:
        break
    elif t == 1:
        init('bingo.txt', days)
    elif t == 2:
        reading('bingo.txt')
    elif t == 3:
        change('bingo.txt')
    else:
        print('такой функции нет')
