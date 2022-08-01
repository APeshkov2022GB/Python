import os

# 'a' - добавить и читать
# w - писать
# r - читать

#path = os.path.join('folder', 'sem_4')

#path = 'papka' + os.sep + 'sem_4_2.txt'

# path = 'file.txt'
# path = 'sem4/sem_4.txt'
# path = 'sem4/papka/sem_4_2.txt'
# with open(path, 'r') as f:
#     data = f.read()
#     print(data)

# path = r'sem4/papka/sem_4_2.txt'
# with open(path, 'r') as data:
#     for line in data:
#         print(line)

# path = r'sem4/papka/sem_4_2_1.txt'  # r -  используется \nile питон не думал что это пенос строки
# with open(path, 'w') as data:
#     data.write('asdf\n')
#     data.write('aqwer\n')
#     data.write('zxcvbgf')

path = r'sem4/papka/sem_4_2.txt'  # r -  используется \nile питон не думал что это пенос строки
with open(path, 'a') as data_file:
    data.write('asdf\n')
    data.write('aqwer\n')
    data.write('zxcvbgf')



     


