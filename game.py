#камень, ножницы, бумага
from random import randint


def game():
    auto_choice = randint(1, 3)
    d = {1: 'камень', 2: 'ножницы', 3: 'бумага'}
    choice = int(input(f'{d}\nвыбери цифру для своего хода : '))
    print(f'твой ход - {d[choice]}\nход компьютера - {d[auto_choice]}')
    if choice == auto_choice:
        print('ничья')
    elif choice == 1 and auto_choice == 2 or choice == 2 and auto_choice == 3 or choice == 3 and auto_choice == 1:
        print('ты выиграл')
    else:
        print('ты проиграл')


while True:
    start = int(input('Для начала игры нажми любую клавишу, для конца - 0 : '))
    if start == 0:
        break
    else:
        game()
