"""Написать программу, где создадим класс Soup (для определения типа супа), принимающий 1 аргумент - 
который отвечает за основной продукт к выбираемому супу.
В этом классе создать метод show_my_soup(), выводящий на печать «Суп - {Основной продукт}» в случае наличия добавки
Это как доп к этой задаче - иначе отобразится следующая фраза: «Обычный кипяток»"""

class Soup:
    def __init__(self, topping='default'):
        self.topping = topping

    def show_my_soup(self):
        if self.topping == 'default':
            print('Обычный кипяток')
        else:
            print(f'Суп - {self.topping}')


porridge = Soup()
porridge.show_my_soup()
pumpkin = Soup('тыква')
pumpkin.show_my_soup()
