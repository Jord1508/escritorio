from sympy import symbols, Eq, solve
x, y , z = symbols('x y z')

ecuacion1 = Eq(3*x + 2*y + 1*z, 1)
ecuacion2 = Eq(2*x + 0*y + 1*z, 2)
ecuacion3 = Eq(-1*x + 1*y +2*z, 4)
ecuacion5 = Eq(5 * (x - 1) +  16 * (2*x + 3) , 3 * (2*x - 7)  - x  )
ecuacion6 = Eq( x - 2 / 3 -  x  -  3  / 4  , x - 4 / 5 )

#solucion = solve([ecuacion1, ecuacion2, ecuacion3 ], (x, y , z))

"""print(f'Solución: x = {solucion[x]}, y = {solucion[y]},z = {solucion[z]}')
x = solucion[x]
y = solucion[y]
z = solucion[z]
print(x +y +z)"""
solucion = solve([ecuacion6], (x))
print(f'Solución: x = {solucion[x]}')
