# import random

# # запись в файл
# def write_file(name,st):
#     with open(name, 'w') as data:
#         data.write(st)

# # создание случайного числа от 0 до 100
# def rnd():
#     return random.randint(0,101)

# # создание коэффициентов многочлена
# def create_mn(k):
#     lst = [rnd() for i in range(k+1)]
#     return lst

# # создание многочлена в виде строки
# def create_str(sp):
#     lst= sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0 or lst[i+2] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i+1] != 0 or lst[i+2] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr

# # получение степени многочлена
# def sq_mn(k):
#     if 'x^' in k:
#         i = k.find('^')
#         num = int(k[i+1:])
#     elif ('x' in k) and ('^' not in k):
#         num = 1
#     else:
#         num = -1
#     return num

# # получение коэффицента члена многочлена
# def k_mn(k):
#     if 'x' in k:
#         i = k.find('x')
#         num = int(k[:i])
#     return num

# # разбор многочлена и получение его коэффициентов
# def calc_mn(st):
#     st = st[0].replace(' ', '').split('=')
#     st = st[0].split('+')
#     lst = []
#     l = len(st)
#     k = 0
#     if sq_mn(st[-1]) == -1:
#         lst.append(int(st[-1]))
#         l -= 1
#         k = 1
#     i = 1 # степень
#     ii = l-1 # индекс
#     while ii >= 0:
#         if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
#             lst.append(k_mn(st[ii]))
#             ii -= 1
#             i += 1
#         else:
#             lst.append(0)
#             i += 1
#     return lst


# # создание двух файлов

# k1 = int(input("Введите натуральную степень для первого файла k = "))
# k2 = int(input("Введите натуральную степень для второго файла k = "))
# koef1 = create_mn(k1)
# koef2 = create_mn(k2)
# write_file("sem4/Homework4/DZ5_1.txt", create_str(koef1))
# write_file("sem4/Homework4/DZ5_2.txt", create_str(koef2))

# # нахождение суммы многочлена

# with open('sem4/Homework4/DZ5_1.txt', 'r') as data:
#     st1 = data.readlines()
# with open('sem4/Homework4/DZ5_2.txt', 'r') as data:
#     st2 = data.readlines()
# print(f"Первый многочлен {st1}")
# print(f"Второй многочлен {st2}")
# lst1 = calc_mn(st1)
# lst2 = calc_mn(st2)
# print(lst1)
# ll = len(lst1)
# if len(lst1) > len(lst2):
#     ll = len(lst2)
# lst_new = [lst1[i] + lst2[i] for i in range(ll)]
# if len(lst1) > len(lst2):
#     mm = len(lst1)
#     for i in range(ll,mm):
#         lst_new.append(lst1[i])
# else:
#     mm = len(lst2)
#     for i in range(ll,mm):
#         lst_new.append(lst2[i])
# write_file("sem4/Homework4/DZ5_2_rez.txt", create_str(lst_new))
# with open('sem4/Homework4/DZ5_2_rez.txt', 'r') as data:
#     st3 = data.readlines()
# print(f"Результирующий многочлен {st3}")

# ----------------------------------------------------------------------
# from pathlib import Path


# def file_readline_to_str(path: Path) -> str:
#     with open(path, 'r') as file:
#         return file.readline()


# def get_coefficients_of_polynomial(poly: list) -> list:
#     coefficients = []
#     print(coefficients)
#     for i in poly:
#         if ('x' in i) and ('(' in i):
#             coefficients.append(
#                 [int(i[i.find('(')+1:i.find(')')]), int(i[0:i.find('*')])])
#         elif ('x' in i) and ('(' not in i):
#             coefficients.append([1, int(i[0:i.find('*')])])
#         elif ('x' not in i) and (i != '+') and (i != '=') and (i != '0'):
#             coefficients.append([0, int(i)])
#     return coefficients


# path1 = Path('sem4/Homework4/DZ4_1.txt')
# path2 = Path('sem4/Homework4/DZ4_2.txt')
# poly1 = file_readline_to_str(path1)
# poly2 = file_readline_to_str(path2)
# print(poly1)
# print(poly2)
# split_poly1 = poly1.split()
# split_poly2 = poly2.split()
# coef_list1 = get_coefficients_of_polynomial(split_poly1)
# coef_list2 = get_coefficients_of_polynomial(split_poly2)

# sum_str = str()

# for i in coef_list1:

#     for j in coef_list2:
#         if (j[0] == i[0] > 1):
#             sum_str += f'{i[1]+j[1]}*x**({i[0]}) + '
#         elif (j[0] == i[0] == 1):
#             sum_str += f'{i[1]+j[1]}*x + '
#         elif (j[0] == i[0] == 0):
#             sum_str += f'{i[1]+j[1]} + '

# sum_str = sum_str[0:len(sum_str)-2]+'= 0'

# path = Path("sem4/Homework4/DZ5_2_rez.txt")
# with open(path, 'w') as poly:
#     poly.writelines(f'{sum_str}\n')
# print(f'\nФайл записан в {path}\n')
