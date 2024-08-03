Algoritmo operaciones

		Definir opcion como Entero
		Definir repite Como Logico
		Definir linea como Caracter
		Definir numero1, numero2 Como Entero
		Definir resultado Como Real
		
		repite = Verdadero
		Hacer
			Escribir "MENU DE OPCIONES"
			Escribir "1. Sumar dos numeros"
			Escribir "2. Restar dos numeros"
			Escribir "3. Multiplicar dos numeros"
			Escribir "4. Dividir dos numeros"
			Escribir "0. SALIR"
			
			Escribir "Ingrese una opcion: "
			Leer opcion
			
			Segun opcion Hacer
				1:
					Escribir "Ingrese primer numero: "
					Leer numero1
					
					Escribir "Ingrese segundo numero: "
					Leer numero2
					
					resultado <- numero1 + numero2;
					
					Escribir "Resultado: ", resultado
					Leer linea
				2:
					Escribir "Ingrese primer numero: "
					Leer numero1
					
					Escribir "Ingrese segundo numero: "
					Leer numero2
					
					resultado <- numero1 - numero2;
					
					Escribir "Resultado: ", resultado
					Leer linea
				3:
					Escribir "Ingrese primer numero: "
					Leer numero1
					
					Escribir "Ingrese segundo numero: "
					Leer numero2
					
					resultado <- numero1 * numero2;
					
					Escribir "Resultado: ", resultado
					Leer linea
				4:
					Escribir "Ingrese primer numero: "
					Leer numero1
					
					Escribir "Ingrese segundo numero: "
					Leer numero2
					
					Si numero2 = 0 Entonces
						Escribir "No se puede dividir por cero"
					SiNo
						resultado <- numero1 / numero2
						Escribir "Resultado: ", resultado
					Fin Si
					
					Leer linea
				0:
					repite = Falso
			Fin Segun
			
		Hasta Que (repite = Falso)
		

FinAlgoritmo
