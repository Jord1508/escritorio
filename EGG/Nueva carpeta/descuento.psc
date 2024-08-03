Algoritmo sin_titulo
	
	Definir  fecha , compra Como real
	Escribir  "ingrese el monto de su compra :"
	leer compra 
	escribir "eliga fecha de su compra"
	escribir " 1 para ENERO"
	escribir " 2 para FEBRERO"
	escribir " 3 para MARZO"
	escribir " 4 para ABRIL"
	escribir " 5 para MAYO"
	escribir " 6 para JUNIO"
	escribir " 7 para JULIO"
	escribir " 8 para AGOSTO"
	escribir " 9 para SEPTIEMBRE"
	escribir " 10 para OCTUBRE"
	escribir " 11 para NOVIEMBRE"
	escribir " 12 para DICIEMBRE"
	leer fecha
	segun fecha hacer
		1,2,3,4,5,6,7,8,12:
			escribir " el valor de su compra es : " compra
		9,10,11:
			compra =( compra*85)/100
			escribir " el valor de su compra es : " compra
		De Otro Modo:
			Escribir "vuelva a ingresar los datos, muchas gracias"
			
	FinSegun



FinAlgoritmo


Algoritmo Ejercicioextra2guia2
	///Una tienda ofrece para los meses de septiembre, octubre y noviembre un descuento del
	///10% sobre el total de la compra que realiza un cliente. Solicitar al usuario que ingrese un
	///mes y el importe de la compra. El programa debe calcular cuál es el monto total que se
	///debe cobrar al cliente e imprimirlo por pantalla.
	
	Definir mes Como entero
	definir num1, aux Como Real
	
	Escribir "ingrese el mes de su compra en numero"
	Leer mes 
	
	si mes = 0 o mes > 11 Entonces
		Escribir "Su mes ingresado es incorrecto"
	sino 
		si mes >= 8 y mes <= 11 Entonces
			Escribir "ingrese el monto de la compra"
			leer num1
			aux = num1 *0.9
			
			Escribir "Monto a pagar es " aux
		SiNo
			Escribir "Su mes no tiene descuento su monto a pagar es " num1
		FinSi
		
	FinSi
	
	
	
	
	
FinAlgoritmo