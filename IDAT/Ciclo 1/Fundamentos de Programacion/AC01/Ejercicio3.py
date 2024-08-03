
print("ingrese el peso en libras: ")
peso_lib = float(input(">:::"))
print("ingrese la altura en milimetros: ")
alt_mml = float(input(">:::"))
peso = peso_lib * 0.45
altura = alt_mml *0.001
imc = peso/altura ** 2
print(f"Su indice de masa corporal es: {imc:.2f}")