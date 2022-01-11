import sympy as sp

h = float(input('h: '))
f = sp.sympify(input('f: '))
a = float(input('代入する値: '))
x = sp.symbols('x')
df = sp.diff(f, x)

dfa = (f.subs(x, a+h) - f.subs(x, a)) / h
print(f'前進差分f`: {dfa}')
print(f'前進差分ε: {abs((df.subs(x, a) - dfa) / df.subs(x, a))}')

dfa = (f.subs(x, a) - f.subs(x, a-h)) / h
print(f'後退差分f`: {dfa}')
print(f'後退差分ε: {abs((df.subs(x, a) - dfa) / df.subs(x, a))}')

dfa = (f.subs(x, a+h) - f.subs(x, a-h)) / (h * 2)
print(f'中心差分f`: {dfa}')
print(f'中心差分ε: {abs((df.subs(x, a) - dfa) / df.subs(x, a))}')