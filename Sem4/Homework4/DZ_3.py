# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

list5 = [1, 2, 8, 2, 3, 5, 5, 8]
print(list5)
list_2 = []
for i in range (len(list5)):
    if list5[i] not in list_2:
        list_2.append(list5[i])

print(list_2)
print('Программа работу закончила')

# --------------------------------------------

lst = list(map(int, input('Введите числа через пробел:\n').split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")
print('Программа работу закончила')
    