"""Нужно напистаь программу
В ней используем классы - имя студента name, номер группы group и список полученных оценок progress.
В самой программе вводим список всех студентов.
В программе нужно вывести список студентов, отсортированный по имени, А так же студентов, у которых низкие оценки"""

import gc
class List:
    def __init__(self,school_num):
        self.school_num = school_num
    def sort_name(self):
        alfabet = []
        for obj in gc.get_objects():
            if isinstance(obj, School):
                alfabet.append(obj.name)
        print('Отсортированный по алфавиту список: ')
        print(alfabet)
    def check_progress(self):
        for obj in gc.get_objects():
            if isinstance(obj, School):
                obj.low_progress()

class School:
    def __init__(self, name,group,progress):
        self.name = name
        self.group = group
        self.progress = progress
    def low_progress(self):
        if sum(self.progress)/len(self.progress) <= 3:
            print(f'{self.name} имеет низкие оценки')


sc_1 = List(1095)
cl_1 = School('Вася',11,[3,3,4,3])
cl_2 = School('Кира',13,[3,5,4,3])
cl_3 = School('Маша',11,[3,3,2,3])


sc_1.sort_name()
sc_1.check_progress()
