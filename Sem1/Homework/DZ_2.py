#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для
# всех значений предикат.

print('x y я Первое условие,    Второе условие')
for x in range(2):
    for y in range(2):
        for z in range(2):
            usl1 = not x and not y and not z
            usl2 = not(x or y or z)
            print(x,y,z, '    ', usl1, '        ',  usl2)
if usl1 == usl2:
    print('Условие верное' ) 
else:
    print('Условие  не верное' )