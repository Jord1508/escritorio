Algoritmo sin_titulo
	definir palabra, frase Como Caracter
	
	Escribir "Ingrese una palabra"
	Leer palabra
	
	frase = Mayusculas(SubCadena(palabra,0,0))
	
	si frase = "A" Entonces
		Escribir "Correcto"
	SiNo
		Escribir "Incorrecto"
	FinSi
FinAlgoritmo
