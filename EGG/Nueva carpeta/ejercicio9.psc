//Construir un programa que simule un men� de opciones para 
//realizar las cuatro operaciones aritm�ticas b�sicas 
//(suma, resta, multiplicaci�n y divisi�n) con dos valores
//num�ricos enteros. El usuario, adem�s, debe especificar 
//la operaci�n con el primer car�cter de la operaci�n que 
//desea realizar: ?S' o ?s? para la suma, ?R? o ?r? para 
//la resta, ?M? o ?m? para la multiplicaci�n y ?D? o ?d? 
// para la divisi�n.

Algoritmo frases
	Definir num1,num2 Como Entero
	Definir cuenta Como Caracter
	
	
	Escribir "ingrese un numero"
	leer num1
	Escribir "ingrese otro numero"
	leer num2
	
	Escribir "Si quieres sumar, ingresa: S o s"
	
	Escribir "Si quieres restar, ingresa: R o r"
	
	Escribir "Si quieres multiplicar, ingresa: M o m"
	
	Escribir "Si quieres dividir, ingresa: D o d"
	
	Leer cuenta
	
	Segun cuenta Hacer
		"S","s":
			Escribir  num1 + num2
		"R","r":
			Escribir  num1 - num2
		"M","m":
			Escribir  num1 * num2
		"D","d":
			Escribir num1/num2
		De Otro Modo:
			
			Escribir  "el valor ingresado es incorrecto"
	FinSegun
	
	
	
FinAlgoritmo
