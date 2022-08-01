# Примеры решения задачи


# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random # импортируем метод
def rnd(): # генерируем случйный список
     return random.randint(0,101)

def write_file(st): # 
    with open('sem4/Homework4/DZ4_2.txt', 'w') as data:
        data.write(st)

def create_list(k): # генерируем список 
    mn = [rnd() for i in range(k+1)]
    return mn

def create_str(any):
    mn = any[::]
    pr = ''
    if len(mn) <= 1:
        pr += f'{mn[0]} = 0'
        
    else:
        for i in range (len(mn)):
            if i != len(mn) -  1 and mn[i] != 0 and i != len(mn) - 2:
                pr += f'{mn[i]}x^{len(mn)-i-1}'
                if mn[i+1] != 0:
                    pr += ' + '
            elif i == len(mn) -  2 and mn[i] != 0:
                pr += f'{mn[i]}x'
                if mn[i+1] != 0:
                    pr += ' + '
            elif i == len(mn) -  1 and mn[i] != 0:
                pr += f'{mn[i]} = 0'
            elif i == len(mn) -  1 and mn[i] == 0:
                pr += ' = 0'
    return pr
    


k = int(input("Введите натуральную степень k = "))
list = create_list(k)
# print(list)
write_file(create_str(list))