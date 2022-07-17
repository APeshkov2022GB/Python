#3. Реализуйте алгоритм задания случайных чисел без использования встроенного
# генератора псевдослучайных чисел.
import datetime 

min_n = 1
max_n = 100

def get_rand():
    return datetime.datetime.now().microsecond%10


n = get_rand()
m = get_rand()
k = get_rand()
# print(int(len(str(min_n))))
print(n)
print(m)
print(k)



import datetime 

min_n = 1
max_n = 100

def get_rand():
    return datetime.datetime.now().microsecond%10

n = get_rand()

print(int(len(str(min_n))))
print(n)



#---------------------------------------------------------------------------------
import time

limit = int(input("Введите предел: "))

rnd_number = str(time.time())
rnd_number = rnd_number.split(".")
rnd_number = int(rnd_number[1])

def random_number(number: int, limit: int):
    while True:
        if number > limit:
            number //= 10
        else:
           return number

print(random_number(rnd_number, limit))
