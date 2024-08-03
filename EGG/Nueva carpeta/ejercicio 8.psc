Algoritmo Algoritmos
	Definir text Como Caracter
	Definir Ltext Como Real
	Definir inicio Como Caracter
	Definir final Como Caracter
	
	Escribir "Ingrese una palabra o texto"
	Leer text
	
	Ltext = Longitud(text) - 1
	inicio = Mayusculas(SubCadena(text,0,0))
	final = Mayusculas(SubCadena(text,Ltext,Ltext))
	
	Si inicio = final Entonces
		Escribir " Correcto"
		
		sino Escribir "InCorrecto"
	FinSi
	
FinAlgoritmo
