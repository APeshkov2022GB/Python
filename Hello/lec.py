# типы данных и переменных
# int, float, boolean, str, list, None
# value = None
# print(type(value))
# print ('Hello World')
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12334
# print(type(value))
# s = 'hello world'


# print(s) # вывод строки

# print(a, b, s)
# print(a, ' - ', b, ' - ', s)
# print('{} - {} - {} '.format(a, b, s))
# print(f'{a} - {b} - {s}')
# print('{1} - {2} - {0} '.format(a, b, s))

# f = True
# print(f)
# f = False
# print(f)

# list = []
# print(list)
 

# list = ['1', '2','3','hello', 1, 2,4.5, True]
# col = ['hello', 1, 2, 4.5, True]
# print(list)
# print(col)

# print(' Введите a')
# a = float(input()) # или int 
# print(' Введите b')
# b = float(input()) # или int 
# print(a, ' + ' , b, ' = ', a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# Арифметические операции
# a = 12
# b = 8
# c = a % b 
# print(c)
# a = 2
# b = 800
# c = a ** b 
# print(c)

# a = 1.3
# b = 3
# c = a * b 
# print(c)

# a = 1.3123
# b = 3
# c = round(a * b, 5) 
# print(c)

# a = 3
# a = a + 5
# print(a)


# a = 3
# a += 5
# print(a)

# a = 1 < 4
# print(a)


# a = 1 < 4 and 5 > 2
# print(a)

# a = 1 == 2
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = [1,2]
# b = [1,2]
# print(a == b)

# a = 1 < 3 < 5 <10
# print(a)

# func = 1
# T = 4
# x = 2
# print(func<T>x)


# f = 1 > 2 or 4 < 6
# print(f)

# f  = [1, 2, 3, 4]
# print(f)
# print(not 2 in f)

# is_odd = f[0] % 2 == 0
# print(is_odd)

# is_odd = not f[0] % 2
# print(is_odd)

# Управляющие конструкции

# a = int(input('a = '))
# b = int(input('b = '))
# if a>b:
#     print(a)
# else:
#     print(b)


# username = input('Ведите имя ')
# if username == 'Маша':
#     print(' Ура, это же Маша!')
# elif username ==' Марина':
#     print(' Я так ждала Вас, Марина!')
# elif username == ' Ильнар':
#     print(' Ильнар - топ))')
# else:
#     print(' Привет, ', username)

# while

# original = 32
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
    
# print(inverted)


# original = 32
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print(' Пожалуй')
#     print(' хватит')
# print(inverted)


# for

# for i in 1, 2, 3, 4, 5:
#     print(i**2)

# list = [1, 2, 3, 4, 10, 5]
# for i in list:
#     print(i)


# r = range(10)
# for i in r:
#     print(i)



# for i in range(1, 5):
#     print(i)


# for i in range(1, 10, 2):
#     print(i)

for i in 'qwe -rty':
    print(i)