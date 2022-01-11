a = int(input('a: '))
c = int(input('c: '))
M = int(input('M: '))
xi = int(input('x0: '))
num = int(input('繰り返し回数: '))
xs = [xi]

for i in range(num):
    if i == 0:
        print(f'x{i}: {xi}')
    xi = (a*xi + c) % M
    xs.append(xi)
    print(f'x{i+1}: {xi}')

cycle = int(input('周期数(0スタートだから+1): '))
print(f'乱数の平均値: {1/cycle*sum(xs[:cycle])}')
a = 1/2 * min(xs) - 1
b = 1/2 * max(xs) - 1
print(f'下限α: {a}')
print(f'上限β: {b}')

n = int(input('rnのn: '))
print(f'r{n}: {(b - a) * xs[n] / (M - 1) + a}')