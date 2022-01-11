from fractions import Fraction
import sympy as sp

x = sp.symbols('x')
f = sp.sympify(input('∫: '))
a = Fraction(input('積分区間(小さい方): '))
b = Fraction(input('積分区間(大きい方): '))
I = sp.integrate(f, (x, a, b))
print(float(I))
S = float(input('S: '))
print(f'ε: {float(abs((S-I)/I))}')