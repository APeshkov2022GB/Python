# напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# a = list()
# for i in range(5):
#     a.append(int(input('-->')))

# maxx = a[0]
# # len(a) - длина списка
# for i in range(1, len(a)):
#     if a[i] > maxx:
#         maxx = a[i]

# print(maxx)


a = []
# range(5) -> [0, 1, 2, 3, 4]
# range(5, 8) -> [5, 6, 7]
# range(1, 11, 2) -> [1, 3, 5, 7, 9]
for i in range(5):
    x = int(input('-->'))
    a.append(x)


maxx = a[0]
# len(a) - длина списка
for i in range(1, len(a)):
    if a[i] > maxx:
        maxx = a[i]

print(maxx)

