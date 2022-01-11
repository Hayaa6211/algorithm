import numpy as np

matrix = []
col = int(input('行数: '))
row = int(input('列数: '))

for y in range(col):
    cols = []
    for x in range(row):
        cols.append(int(input('要素: ')))
    matrix.append(cols)

A = np.array(matrix)
x = np.array([1 for _ in range(col)]).T
num = int(input('繰り返し回数: '))

for i in range(num):
    print(f'K = {i}')
    y = np.dot(A, x)
    print(f'y{i+1}: {y}')
    x = 1/y[1] * y
    print(f'x{i+1}: {x}')
    if i == num-1:
        print(f'最大固有値: {y[1]}')
    print('-'*10)
