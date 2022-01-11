import sympy as sp

x = sp.symbols('x')
y = sp.symbols('y')
f = sp.sympify(input('dy/dx: '))
f2 = sp.sympify(input('常微分方程式の解: '))
xi = float(input('x0: '))
yi = float(input('y0: '))
h = float(input('h: '))
limx = float(input('x: '))
i = int(input('繰り返し回数: '))

for k in range(i):
    yi = yi + h * f.subs([(x, xi), (y, yi)])
    xi = xi + h
    print(f'x{k+1}: {xi}')
    print(f'y{k+1}: {yi}')
    print('----------')

if f2 != None:
    print(abs(yi-f2.subs(x, xi)))