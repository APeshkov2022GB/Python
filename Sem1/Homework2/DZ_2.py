# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел
# от 1 до N.
n = int(input(' введите число N = '))
f = 1
for i in range(n):
    #f *= i+1
    f = f*(i+1)
print(f)
print('Программа работу закончила')