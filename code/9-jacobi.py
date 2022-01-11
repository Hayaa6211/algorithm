import numpy as np
import math

matrix = []
col = int(input('行数: '))
row = int(input('列数: '))

for y in range(col):
    cols = []
    for x in range(row):
        cols.append(int(input('要素: ')))
    matrix.append(cols)

A = np.array(matrix)
theta = (1/2) * math.atan(2*A[0][1] / (A[0][0] - A[1][1]))
print(f'θ: {theta}')
P = np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])
print(f'A`: {P.T @ A @ P}')

V = np.array([[1, 0], [0, 1]])
print(V @ P)