# Напишите программу, которая будет принимать на
#  вход дробь и показывать первую цыфру дробной части числа

a = float(input('-->'))

b = int(a * 10)
print(b % 10)


x = input('x = ')

for i in range(len(x)):
    if x[i] == ',':
        print(x[i + 1])
        break


# x = float(input('введите число-'))
# int_x = int(x)
# x -= int_x
# x = int(x*10)
# if(x == 0):
#     print('no')
# else:
#     print(x)


# str_1 = '6,78'
# print(str_1.split(','))
