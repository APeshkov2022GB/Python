# МОЁ РЕШЕНИЕ
def get_coefficient_and_polinom(poly):
    coefficients = []
    for i in poly:
        if ('x' in i) and ('^' in i):
            coefficients.append([int(i[i.find('^')+1:]), int(i[0:i.find('x')])])
        elif ('x' in i) and ('^' not in i):
            coefficients.append([1, int(i[0:i.find('x')])])
        elif ('x' not in i) and ('^' not in i) :
            coefficients.append([0, int(i)])
    return coefficients
    
def calc_mn(st):
    st = st[:-3]
    print(st)
    st = st.replace(' ', '').split('+')
    return st

path2 = r'sem4/Homework4/DZ4_2.txt'
with open(path2, 'r') as my_file:
    str1 = my_file.readline()

path1 = r'sem4/Homework4/DZ4_1.txt'
with open(path1, 'r') as my_file:
    str2 = my_file.readline()

print(str1)
print(str2)
lst1 = calc_mn(str1)
lst2 = calc_mn(str2)

print(lst1)
print(lst2)

list1 = get_coefficient_and_polinom(lst1)
list2 = get_coefficient_and_polinom(lst2)

srez_list1= list1[::-1]
srez_list2= list2[::-1]

if len(srez_list1) < len(srez_list2):
        for i in range(len(srez_list2)-len(srez_list1)):
            leen = len(list1)
            leen2 = leen+i
            srez_list1.append([leen2,0])
else:
    if len(srez_list1) > len(srez_list2):
        for i in range(len(srez_list1)-len(srez_list2)):
            leen = len(list2)
            leen2 = leen+i
            srez_list2.append([leen2,0])

sum_list =[]
for i in range(len(srez_list1)):
    for j in range(len(srez_list2)):
        if i == j:
            summ_koef = srez_list1[i][1]+srez_list2[j][1]
            # print(summ_koef)
            sum_list.append([i,summ_koef])

srez_sum_list = sum_list[::-1] 
print(srez_sum_list)
sum_str = ''
for i in range(len(srez_sum_list)):
    if srez_sum_list[i][0] > 1:
        sum_str += f'{srez_sum_list[i][1]}x^{srez_sum_list[i][0]} + '
    elif srez_sum_list[i][0] == 1:
        sum_str += f'{srez_sum_list[i][1]}x + '
    elif srez_sum_list[i][0] == 0:
        sum_str += f'{srez_sum_list[i][1]}'
itog_str = sum_str + f' = 0'    
print('Сумма коэффициентов многочлена :\n ',itog_str)

path3 = r"sem4/Homework4/DZ5_2_rez.txt"
with open(path3, 'w') as my_file:
    my_file.writelines(f'{itog_str}\n')
print(f'\nФайл записан в {path3}\n')
print(" Программа работу закончила")




           
            


