from funciones import *
while True:
    try:
        menu_principal()
        opt = int(input("Selecciona una opción: \n>>"))
        if opt == 1:
            print()
            print("\n*** Elejiste la opcion 1 ***\n")
            juego_random()
        elif opt == 3:
            print()
            while True:
                name = input("Ingrese su nombre: ")
                apellido = input("Ingrese su apellido: ")
                rstl = validar_texto(name,apellido)
                texto = name[0:3].upper()
                A = ord(apellido[-3].upper())
                B = ord(apellido[-2].upper())
                C = ord(apellido[-1].upper())
                if rstl == False:
                    print("Por revise valide que no tengo numeros en lo ingresado")
                else:
                    print("Aqui saldra su clave")
                    text = change(texto)
                    num = A + B + C
                    
                    print(text,num)
            break
        else:
            print()
            print(f"********     La opciónn {opt!r} esta fuera de rango!!     ********")
            print("-----                Vuelve a Intentarlo                     ----\n","*"*65)
    except:
        print("ERROR:\nLa opciónn {opt!r} es invalido\nVerifique el numero del menu para continuar con el programa!")
        