Algoritmo sin_titulo
	
	//Realizar un programa que pida introducir solo frases o palabras de 6 caracteres. Si el
	//usuario ingresa una frase o palabra de 6 caracteres se deber� de imprimir un mensaje por
	//pantalla que diga "CORRECTO", en caso contrario, se deber� imprimir "INCORRECTO".
	//Nota: investigar la funci�n Longitud() de PseInt.
	
	Definir palabra Como Caracter
	
	Escribir "Ingrese una palabra de 6 caracteres"
	Leer palabra
	
	Si 6 = Longitud(palabra) Entonces
		Escribir "Correcto"
		
		Sino Escribir "INCORRECTO"
	FinSi
	
	
FinAlgoritmo
