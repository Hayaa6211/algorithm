import sympy as sp

num = int(input('データ点の数: '))
xs = []
ys = []
for i in range(num):
    xs.append(int(input('x: ')))
    ys.append(int(input('y: ')))
a0 = sp.symbols('a0')
a1 = sp.symbols('a1')
x = int(input('x: '))

def sigmax(xs):
    s = 0
    for x in xs:
        s += x
    return s

def sigmay(ys):
    s = 0
    for y in ys:
        s += y
    return s

def sigmax2(xs):
    s = 0
    for x in xs:
        s += x**2
    return s

def sigmaxy(xs, ys):
    s = 0
    for x, y in zip(xs, ys):
        s += x*y
    return s

sigmax = sigmax(xs)
sigmay = sigmay(ys)
sigmax2 = sigmax2(xs)
sigmaxy = sigmaxy(xs, ys)

print(f'Σx: {sigmax}')
print(f'Σy: {sigmay}')
print(f'Σx^2: {sigmax2}')
print(f'Σxy: {sigmaxy}')

eq1 = sp.Eq(num*a0 + a1*sigmax, sigmay)
eq2 = sp.Eq(a0*sigmax + a1*sigmax2, sigmaxy)
ans = sp.solve([eq1, eq2], [a0, a1])
print(f'a0: {float(ans[a0])}')
print(f'a1: {float(ans[a1])}')
print(float(ans[a0] + ans[a1] * x))