
my_list = [1, 2, 2, 5]

print(my_list)

m = [x for x in my_list if my_list.count(x) < 2]

print(m)

#-------------------------------------------------------
in_list = [1, 2, 3, 3, 5]
print(list(filter(lambda x: in_list.count(x) == 1, in_list)))

#-------------------------------------------------------

for row in matrix:
    for item in row:
        ''.join('{:4}'.format(item))
    print('\n')

