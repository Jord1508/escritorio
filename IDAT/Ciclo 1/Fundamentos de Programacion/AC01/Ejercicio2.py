#  "Ejercicio 2"
print("""Un laboratorio de cómputo tiene un consumo por ordenador de 300 wats(potencia), sabiendo
que la entrada de voltaje es igual a 220 voltios(tensión) y se cuenta con 40 computadoras se
necesita saber cual es el consumo de corriente(intensidad) total y por ordenador""")
a =300
b =220
c  =40
d = a * c
i=float( a / b)
it=float( d / b)

print("El consumo de corriente total es %.2f" %it)
print("El consumo de corriente por ordenador es %.2f" %i)