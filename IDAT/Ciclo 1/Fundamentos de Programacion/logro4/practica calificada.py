n = int(input('Ingrese la cantidad de notas a promediar: > '))
listanotas = []
def calcular_promedio(lista):
    if len(lista)==0:
        return 0
    suma=sum(lista)
    promedio=suma/len(lista)
    return promedio
for i in range(n):
    x = int(input(f'Ingrese la nota N {i+1}: >'))
    listanotas.append(x)

promedio = calcular_promedio(listanotas)
print("El promedio obtenido es: %.2f"  %promedio)