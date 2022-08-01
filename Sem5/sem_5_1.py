# 1. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число

def f(my_list: list):
    for i in range(1, len(my_list)):
        if my_list[i] - my_list[i - 1] != 1:
            return my_list[i - 1] + 1
    return 'Not found'


