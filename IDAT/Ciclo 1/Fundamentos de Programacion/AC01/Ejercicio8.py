# "Programa para realizar conversiones de Kilogramos a Onzas"
#Solicitando Datos
peso = float(input("Ingresar los kilogramos a onza: "))
# Ecuación para entregar resultados
Toneladas= peso / 1000
Quintales= Toneladas * 20
Arroba= Quintales * 4
Libras= Arroba * 25
Onzas= Libras * 16
#Entregando resultado
print(f"-En Onzas son: {Onzas} oz")
