# Напишите программу, которая принимает на вход число и проверяет, 
# кратно ли оно 5 и 10 или 15, но не 30.


a = int(input('--> '))

if (a % 5 == 0) and (a % 10 == 0) and (a % 15 == 0) and (a % 30 != 0):
    print('yes')
else:
    print('no')


x = int(input('введите число-'))
if((x % 5 == 0 and x % 10 == 0) or (x % 15 == 0 and not x % 30 ==0)):
    print('TRUE')
else:
    print('FALSE')


num = int(input('Введите число: '))
if (num % 5 == 0) and (num % 10 == 0) or (num % 15 == 0) and (num % 30 != 0):
    print('Заданная кратность выполняется')
else:
    print('Заданная кратность не выполняется')
