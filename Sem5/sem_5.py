def f(x):
    return x**2
new_f = lambda x: x**2
my_list = [1, 413, 65, 346]
for item in my_list:
    print(f(item), end=' ')
f d fgntrt

new_f = lambda x: True if (x > 10) else False
my_list = [1, 413, 65, 346]
res = list(map(new_f, my_list))
print(res)

 что с длеать; с кем сделать; условие
res = [i for i in range(5)]


listt = tuple([(i, i) for i in range(1, 21) if (i % 2 == 0)])
print(listt)


my_list = list(filter(lambda x: x > 10, [124, 1, 42, 65, 76]))
print(my_list)


my_list = list(filter(lambda x: type(x)==int, [124, 1.2, 42, 65, 76]))
print(my_list)


lambda - анонимные функции
Включения - генератор list comprehension
map - применяет функцию с выражением к элементам
filter - применяет фкункцию с логическим выражением к элементам
zip - комбинирует коллекции
enimerate - нумерует

name = ['a', 'b', 'c', 'd', 'f']

my_list = tuple(enumerate(name))

print(my_list)
