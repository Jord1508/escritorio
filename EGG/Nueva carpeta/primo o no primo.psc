Funcion resultado <- prim ( num )
	Definir resultado Como Caracter
	si num mod num = 0 y num mod 2 = 0
		Escribir "Es par"
	SiNo
		Escribir "Es primo"
	FinSi
	
Fin Funcion

Algoritmo sin_titulo
	Definir num Como Entero
	Definir Result Como Caracter
	Escribir "Ingresa un numero"
	Leer num
	
	Result = prim(num)
	Escribir Result
FinAlgoritmo
