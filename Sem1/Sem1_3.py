# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    
# n = int(input('--> '))
# i = -n
# while i <= n:
#     print(i)
#     i+=1

N = int(input('введите число N - '))
a = -N
while a <= N:
    print(a)
    a +=1

x = int(input('введите число-'))
for i in range(-x,x+1):
    print(i, end=', ')



