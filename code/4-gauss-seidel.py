import numpy as np

a1 = int(input('a1: '))
b1 = int(input('b1: '))
c1 = int(input('c1: '))
d1 = int(input('d1: '))

a2 = int(input('a2: '))
b2 = int(input('b2: '))
c2 = int(input('c2: '))
d2 = int(input('d2: '))

a3 = int(input('a3: '))
b3 = int(input('b3: '))
c3 = int(input('c3: '))
d3 = int(input('d3: '))

x1 = int(input('x1: '))
x2 = x1
x3 = x1

i = int(input('繰り返し回数: '))

for k in range(i):
    before = np.array([x1, x2, x3])
    x1 = (d1 - (b1*x2+c1*x3)) / a1
    x2 = (d2 - (a2*x1+c2*x3)) / b2
    x3 = (d3 - (a3*x1+b3*x2)) / c3
    print(f'K = {k+1}')
    print(f'x1: {x1}')
    print(f'x2: {x2}')
    print(f'x3: {x3}')
    after = np.array([x1, x2, x3])
    print(f'x{k+1}-x{k}: {np.linalg.norm(after-before, ord=2)}')
    print('----------')