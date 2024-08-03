Algoritmo sin_titulo
	Definir dividendo , divisor , resto , cociente Como Entero
	Escribir "Ingrese dividendo"
	Leer dividendo
	Escribir " Ingrese el divisor"
	Leer divisor
	division(dividendo,divisor,resto , cociente)
	Escribir "Resto es: " resto ", Cociente es: " cociente
	
FinAlgoritmo
SubProceso division(dividendo,divisor,resto Por referencia, cociente Por referencia)
	cociente = 1
	resto = dividendo - divisor
	Mientras resto >= divisor Hacer
		resto = resto - divisor
		cociente = cociente + 1
	Fin Mientras

FinSubProceso
