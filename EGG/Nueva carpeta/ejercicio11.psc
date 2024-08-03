Algoritmo sin_titulo
	//Escriba un programa para obtener el grado de eficiencia de un operario de una fábrica de
	//tornillos, de acuerdo a las siguientes dos condiciones que se le imponen para un período
	//de prueba:
	//	Producir menos de 200 tornillos defectuosos.
	//	Producir más de 10000 tornillos sin defectos.
	//	El grado de eficiencia se determina de la siguiente manera:
	//	Si no cumple ninguna de las condiciones, grado 5.
	//	Si sólo cumple la primera condición, grado 6.
	//? Si sólo cumple la segunda condición, grado 7.//
	// Si cumple las dos condiciones, grado 8
	
	definir tor1, tor2 Como Entero
	Escribir "Ingrese cantidad de tornillos defectuosos"
	Leer tor1
	Escribir "Ingrese cantidad de tornillos sin defectos"
	Leer tor2
	
	si tor1<200 y tor2>10000 entonces
		Escribir "Usted cuenta con grado de eficiencia de 8"
	SiNo
		si tor1>=200 y tor2>10000
			Escribir "Usted cuenta con grado de eficiencia de 7"
		SiNo
			si tor1<200 y tor2<=10000
				Escribir "Usted cuenta con grado de eficiencia de 6"
			SiNo
				Escribir "Usted cuenta con grado de eficiencia de 5"
			FinSi
		FinSi
	FinSi
	
	
	
	
FinAlgoritmo
