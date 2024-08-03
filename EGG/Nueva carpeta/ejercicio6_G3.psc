//Realizar un procedimiento que permita intercambiar el valor de dos variables de tipo entero.
//La variable A, debe terminar con el valor de la variable B.
Algoritmo ejercicio6_G3
	Definir val1, val2 Como Entero
	Escribir "Ingrese su primer valor: "
	Leer val1
	Escribir "Ingrese su segundo valor: "
	Leer val2
	intercambio(val1,val2)
	Escribir "La variable 1 es: " val1 ",la variable 2 es: " val2
FinAlgoritmo

SubProceso intercambio(a Por Referencia, b Por Referencia)
	Definir aux Como Entero
	aux=a
	a=b
	b=aux
	Para variable_numerica<-valor_inicial Hasta valor_final Con Paso paso Hacer
		secuencia_de_acciones
	Fin Para
FinSubProceso
