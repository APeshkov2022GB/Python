# МОЁ РЕШЕНИЕ
# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from ntpath import join
import random # импортируем метод
def rnd(): # генерируем случйный список
     return random.randint(0,101)

def write_file(st): # 
    with open('sem4/Homework4/DZ4_1.txt', 'w') as data:
        data.write(st)

def create_list(k): # генерируем список 
    mn = [rnd() for i in range(k+1)]
    return mn

def create_str(any):
    mn = any[:]
    list = [" = 0",] 
    for i in range (len(mn)):
        if i == 0 and mn[i] != 0:
            list.insert(0, f'{mn[i]}')
        elif i == 1 and mn[i] != 0:
            list.insert(0, f'{mn[i]}x + ')        
        elif i > 1 and mn[i] != 0:
            list.insert(0, f'{mn[i]}x^{i} + ')    
            # print(list)              
    return "".join(map(str, list))
k = int(input("Введите натуральную степень k = "))
list = create_list(k)
# print(list)
write_file(create_str(list))