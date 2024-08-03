//Construir un programa que simule un menú de opciones para 
//realizar las cuatro operaciones aritméticas básicas 
//(suma, resta, multiplicación y división) con dos valores
//numéricos enteros. El usuario, además, debe especificar 
//la operación con el primer carácter de la operación que 
//desea realizar: ?S' o ?s? para la suma, ?R? o ?r? para 
//la resta, ?M? o ?m? para la multiplicación y ?D? o ?d? 
// para la división.

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
