from fractions import Fraction
import sympy as sp

xs = []
ys = []
for i in range(5):
    xs.append(Fraction(input('x: ')))
    ys.append(Fraction(input('y: ')))

def getArea(xs, ys):
    a = Fraction(input('xの区間(小さい方): '))
    b = Fraction(input('xの区間(大きい方): '))
    new_xs, new_ys = [], []
    for x, y in zip(xs, ys):
        if a <= x and x <= b:
            new_xs.append(x)
            new_ys.append(y)
    return 1/3 * (new_xs[2]-new_xs[0])/2 * (new_ys[0] + 4*new_ys[1] + new_ys[2])

S1 = getArea(xs, ys)
print(f'S1: {S1}')
S2 = getArea(xs, ys)
print(f'S2: {S2}')
S = S1 + S2
print(f'S: {S}')

x = sp.symbols('x')
f = sp.sympify(input('∫: '))
a = Fraction(input('積分区間(小さい方): '))
b = Fraction(input('積分区間(大きい方): '))
I = sp.integrate(f, (x, a, b))

print(f'ε: {float(abs((S-I)/I))}')