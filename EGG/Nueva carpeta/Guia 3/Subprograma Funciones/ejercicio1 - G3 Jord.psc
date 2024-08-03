Algoritmo ejercicio_9
	Definir frase Como Caracter	
	Hacer
		Escribir "Igrese una frase con un punto (.) al final"
		Leer frase
	Mientras Que Subcadena(frase,Longitud(frase)-1,Longitud(frase)-1) <> "."
	cambio(frase)
FinAlgoritmo

SubProceso cambio(value por Referencia)
	Definir v , ltr Como Caracter
	Definir n , i Como Entero
	i = 0	
	n = Longitud(value)-1
	v = ""
	Para i <-0 Hasta n Con paso 1 Hacer
		ltr = Subcadena(value,i,i)
		Segun  ltr hacer
			"a":
				ltr <- "@"
			"e":
				ltr = "#"
			"i":
				ltr = "$"
			"o":
				ltr = "%"
			"u":
				ltr= "*"
		FinSegun
		v = Concatenar(v,ltr)
	Fin Para
	Escribir v
FinSubProceso