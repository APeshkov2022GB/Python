# 5. Реализуйте алгоритм перемешивания списка.

import random
arr = [1, 2, 3, 4, 5, 6]
print("Original List: ", arr)
n = len(arr)
for i in range(n):
    j = random.randint(0, n-1)
    element=arr.pop(j)
    arr.append(element)
print("Shuffled List: ",arr)
print('Программа работу закончила')
