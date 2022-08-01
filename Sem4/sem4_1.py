# path = r'sem4/sem_4.txt'

# with open(path, 'r') as f:
#     data = f.readline()
#     print(type(data))
#     print(data)
 # ----------------------------------------------------   
def is_int(str: str) -> bool:
    try:
        int(str)
        return True
    except ValueError:
        return False


def input_list_int_numbers(str_in: str) -> list:
    list_dirty = str_in.split(' ')
    list_clean = []
    for elem in list_dirty:
        if is_int(elem):
            list_clean.append(int(elem))
    return list_clean


path = r'sem4/sem_4.txt'
f = open(path, 'r')
str_in = f.readline()
f.close()

numb_list = input_list_int_numbers(str_in)

print(numb_list)
print(max(numb_list))
print(min(numb_list))
 

#------------------------------------------------------------------------------------
# path = r'Testfiles/S4T1.txt'

# with open(path, 'r') as f:
# data = f.readlines()

# data_split = data[0].split(' ')
# print(data_split)

# minn = int(data_split[0])
# maxx = int(data_split[0])

# for i in data_split:
# if int(i) < minn:
# minn = int(i)
# if int(i) > maxx:
# maxx = int(i)

# print(f'Минимальное число: {minn}')
# print(f'Максимальное число: {maxx}')

#-------------------------------------------------------------
