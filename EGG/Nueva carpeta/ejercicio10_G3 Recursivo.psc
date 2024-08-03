Funcion retorno <- suma ( num )
	Definir retorno, retorno2 Como Entero
	Si num=0 Entonces
		Escribir "La suma ha terminado"
	SiNo
		retorno=num+suma(num-1)
		retorno2=retorno-num
		Escribir num "+" retorno2 "=" retorno
	FinSi
Fin Funcion

//Escribir una función recursiva que devuelva la suma de los primeros N enteros.
Algoritmo ejercicio10_G3
	Definir num, resultado Como Entero
	Escribir "Ingrese un numero: "
	Leer num
	resultado=suma(num)
	Escribir "El resultado de la suma es: " resultado
FinAlgoritmo

