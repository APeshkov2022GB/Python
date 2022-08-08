list1 = ['123', '321', '456', '96']
count = '3'
array_find = []
[array_find.append(find_count) for find_count in list1 if count in find_count] # стало
# for find_count in list: БЫЛО
#     if count in find_count:  БЫЛО
#         array_find.append(find_count) БЫЛО
print(array_find)


# -------------------------------------------------------------------------------------------

lst2 = list(map(int, input('Введите числа через пробел:\n').split()))
print(f"Исходный список: {lst2}")
new_lst = []
[new_lst.append(i) for i in lst2 if i not in new_lst] # стало
# for i in lst: было
#     if i not in new_lst: было
#         new_lst.append(i) было
print(f"Список из неповторяющихся элементов: {new_lst}")
print('Программа работу закончила')