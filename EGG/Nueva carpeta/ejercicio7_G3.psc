//Crear un procedimiento que calcule la temperatura media de un d�a a partir de la temperatura
//m�xima y m�nima. Crear un programa principal, que, utilizando un procedimiento, vaya
//pidiendo la temperatura m�xima y m�nima de n d�as y vaya mostrando la media de cada d�a. El
//programa pedir� el n�mero de d�as que se van a introducir.

Algoritmo ejercicio7_G3
	Definir max, min, dias, i Como Entero
	Definir promedio Como Real
	
	Escribir "Ingrese la cantidad de dias: "
	Leer dias
	
	promedio=0
	Para i<-1 Hasta dias Hacer
		Escribir "Ingrese la temperatura maxima: " i
		Leer max
		Escribir "Ingrese la temperatura minima: " i
		Leer min
		media(max,min,promedio)
		
		Escribir "La media del dia " i " es: " promedio
		
	Fin Para
	
FinAlgoritmo

SubProceso media(max,min , promedio por referencia)
	promedio=(max+min)/2
	
FinSubProceso
