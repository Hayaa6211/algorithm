import sympy as sp

x = sp.symbols('x')
y = sp.sympify(input('xの式: '))
E = float(input('イプシロンの値: '))

def newton(x, y, dy):
    xi = int(input('xiの初期値: '))
    for i in range(10):
        if i == 0:
            continue
        xi1 = xi - (y.subs(x, xi) / dy.subs(x, xi))
        print(f'{i}: {float(xi1)}')
        print(f'{i}-{i-1}: {float(abs(xi1-xi))}')
        if abs(xi1-xi) <= E:
            print('Finish!')
            break
        print('----------')
        xi=xi1

dy = sp.diff(y, x)
print(dy)

newton(x, y, dy)