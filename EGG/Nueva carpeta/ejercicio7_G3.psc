//Crear un procedimiento que calcule la temperatura media de un día a partir de la temperatura
//máxima y mínima. Crear un programa principal, que, utilizando un procedimiento, vaya
//pidiendo la temperatura máxima y mínima de n días y vaya mostrando la media de cada día. El
//programa pedirá el número de días que se van a introducir.

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
