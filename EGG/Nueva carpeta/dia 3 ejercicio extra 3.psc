Algoritmo sin_titulo
//	Crear una funci�n llamada "Login", que recibe un nombre de usuario y una contrase�a y que
//	devuelve Verdadero si el nombre de usuario es "usuario1" y si la contrase�a es "asdasd".
//Adem�s, la funci�n calculara el n�mero de intentos que se ha usado para loguearse, tenemos
	//	solo 3 intentos, si nos quedamos sin intentos la funci�n devolver� Falso.
	definir usuario, pass Como Caracter
	definir vof Como Logico
	definir n como entero
	vof=falso
	n=0
	mientras vof= Falso y n<3
		escribir "ingrese usuario"
		leer usuario
		escribir " password?"
		leer pass
		vof=password(usuario, pass, n)
	FinMientras
	si vof=Verdadero Entonces
		escribir "ok"
		sino escribir "no ok"
	FinSi
FinAlgoritmo

Funcion vof1<-password(usuario Por Valor, pass Por Valor, n Por Referencia)
	definir vof1 Como Logico
	n=n+1
	si usuario= "usuario1" y pass="asdasd"
		vof1=Verdadero
		sino vof1=falso
	FinSi
	
FinFuncion
