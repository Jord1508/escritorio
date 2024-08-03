Algoritmo sin_titulo
	//	Escribir un programa que procese una secuencia de caracteres ingresada por teclado y
	//terminada en punto, y luego codifique la palabra o frase ingresada de la siguiente manera:
	//	cada vocal se reemplaza por el carácter que se indica en la tabla y el resto de los caracteres
	//	(incluyendo a las vocales acentuadas) se mantienen sin cambios.
	//	a e i o u
	//	@ # $ % *
	//	Realice un subprograma que reciba una secuencia de caracteres y retorne la codificación
	//	correspondiente. Utilice la estructura "según" para la transformación.
	//	Por ejemplo, si el usuario ingresa: Ayer, lunes, salimos a las once y 10.
	//		La salida del programa debería ser: @y#r, l*n#s, s@l$m%s @ l@s %nc# y 10.
	//		NOTA: investigue el uso de la función concatenar de PSeInt para armar la palabra/frase.
	
	Definir frase, nuevafrase Como Caracter
	
	Escribir "Ingrese una frase"
	Leer frase
	
	intercambioVocal(frase, nuevafrase)
	Escribir nuevafrase
	
FinAlgoritmo

SubProceso intercambioVocal (frase, nuevafrase Por Referencia)
	Definir x, largo Como Entero
	Definir i Como Caracter
	largo<-Longitud(frase)-1
	nuevafrase= " "
	Para x<-0 Hasta largo Con Paso 1 Hacer
		i<-Subcadena(frase,x,x)
		Segun i Hacer
			"a" o "A":
				i<- "@"
			"e" o "E":
				i<- "#"
			"i" o "I":
				i<- "$"
			"o" o "O":
				i<- "%"
			"u" o "U":
				i<- "*"
		Fin Segun
		nuevafrase<-Concatenar(nuevafrase,i)
	Fin Para
	
	
	
FinSubProceso
	