num = int(input('Ingrese un numero de 3 cifras: '))
u = int(num % 10)
num = int(num/10)
d = num % 10
c = int(num/10)
NInver = u*100+d*10+c

print(f'Num Invertido: {NInver}')