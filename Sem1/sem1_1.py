# 1. Напишите программу, которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого


a = int(input(' Введите a = '))
b = int(input(' Введите b = '))
if (b == a * a) or (a == b*b):
    print(' Число a является квадратом числа b ')
else:
    print(' Число b не является кадрато')


# a = int(input('Введите число а:'))
# b = int(input('Введите число b:'))
# if b==a*a or a==b*b:
#     print(' -> да')
# else:
#     print('-> нет')

# number_a = int(input('Введите первое число: '))
# number_b = int(input('Введите второе чисоло: '))
# if number_b == number_a ** 2:
#     print(f'Число {number_b} является квадратом числа {number_a}!')
# elif number_a == number_b ** 2:
#     print(f'Число {number_a} является квадратом числа {number_b}!')
# else:
#     print(f'Число {number_b} не является квадратом числа {number_a}!')
