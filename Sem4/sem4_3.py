path = r'Testfiles/S4T2.txt'

with open(path, 'r') as f:
    a = int(f.readline())
    b = int(f.readline())
    c = int(f.readline())

disc = b**2 - 4 * a * c
x1 = -b + (disc**(1/2) / (2 * a))
x2 = -b - (disc**(1/2) / (2 * a))
print(x1, x2)

with open(path, 'a') as f:
    f.write(f'\nКорень 1: {x1}')
    f.write(f'\nКорень 2: {x2}')