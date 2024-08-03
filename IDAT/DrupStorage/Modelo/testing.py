from sympy import symbols, expand, factor

# Definir las variables
c, x, a, m , y= symbols('c x a m y')

# Definir la expresión
exprexpand = (x**2 + 1) * (x + 1)**3

# Expandir la expresión
expr_expandida = expand(exprexpand)

#print(expr_expandida)

exprfactor = x ** 12 - y ** 12

# Factorizar la expresión
expr_factorizada = factor(exprfactor)

# Mostrar el resultado
print(expr_factorizada)
