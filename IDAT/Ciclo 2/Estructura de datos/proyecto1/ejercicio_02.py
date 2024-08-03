line = input("Introduzca línea llena de números - sepárelos con espacios: ")
strings = line.split()
sum = 0
try:
    for substr in strings:
        sum += int(substr)
    print("Sum = ", sum)
except:
    print("No es un número: ", substr)

print("El valor de la tabla ASCII = ", chr(sum))
