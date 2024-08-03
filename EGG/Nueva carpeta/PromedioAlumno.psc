Algoritmo PromedioAlumno
	Definir nota1, nota2, nota3, nota4 Como Entero
	Definir promedio Como Real
	Escribir "Escriba las 4 notas del estudiante"
	Leer nota1, nota2, nota3, nota4
	Si (nota1 < nota2 Y nota1 < nota3 Y nota1 < nota4) Entonces
		promedio = (nota2 + nota3 + nota4) / 3
		Escribir "La nota que se elimina es ", nota1, " y el promedio es ", promedio
	SiNo
		Si (nota2 < nota1  Y nota2 < nota3 Y nota2 < nota4) Entonces
			promedio = (nota1 + nota3 + nota4) / 3
			Escribir "La nota que se elimina es ", nota2, " y el promedio es ", promedio
		SiNo
			Si (nota3 < nota1 Y nota3 < nota2 Y nota3 < nota4) Entonces
				promedio = (nota1 + nota2 + nota4) / 3
				Escribir "La nota que se elimina es ", nota3, " y el promedio es ", promedio
			SiNo
				promedio = (nota1 + nota2 + nota3) / 3
				Escribir "La nota que se elimina es ", nota4, " y el promedio es ", promedio
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo
