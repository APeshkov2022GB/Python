# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции вводит пользователь через пробел.

from random import randint

n = int(input(' введите число N = '))
numbers = []
for i in range(-n, n+1):
    numbers.append(randint(-n, n+1))
print(f'Список случайных чисел от -N до N\n',numbers)
print(f'Введите номера индексов из списка для умножения от 0 до {n*2} через пробел')
ind = list(map(int, input ().split())) 
umn = 1
for i in ind:
    umn = umn * numbers[i]
print(umn)
print('Программа работу закончила')