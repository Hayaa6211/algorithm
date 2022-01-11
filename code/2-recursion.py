a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

def solutionFormula(a, b, c):
    solve1 = (-b - (b**2-4*a*c)**0.5) / (2*a)
    solve2 = (-b + (b**2-4*a*c)**0.5) / (2*a)
    print(f'xα: {max(solve1, solve2)}')

def recursion(a, b, c):
    xi = int(input('xiの初期値'))
    for i in range(11):
        print(f'{i}: {xi}')
        xi = ((-b*xi-c) / a) ** 0.5

solutionFormula(a, b, c)
recursion(a, b, c)