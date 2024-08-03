import random   #Importancion del modulo Randon

def generar_numero_aleatorio():
    return random.randint(0, 9)

def adivinar_numero(numero_aleatorio, numero_usuario,intentos):
    if numero_usuario == numero_aleatorio:
        return "Has ganado"
    elif numero_usuario < numero_aleatorio:
        return (f"El número aleatorio es mayor\nTe quedan {intentos} intentos")
    elif intentos == 0:
        return True
    else:
        return (f"El número aleatorio es menor\nTe quedan {intentos} intentos")
def juego_random():
    numero_aleatorio = generar_numero_aleatorio()
    intentos = 3
    print(numero_aleatorio)
    while intentos >= 0:
        try:
            intentos -= 1
            numero_usuario = int(input("Adivina el número (entre 0 y 9): "))
            resultado = adivinar_numero(numero_aleatorio, numero_usuario,intentos)

            if resultado == "Has ganado":
                print(f"*****    ¡Lo lograste Felicidades!   ******")
                print("  Vuelve pronto Campeon!!  \(^-^)/  ")
                break
            elif resultado == True:
                print(f"¡El numero Ganador era {resultado} intentos!")
                print("********      Que Triste tu vida     ********")
                print(" ******  !!!!    Has Perdido     !!!!  ******")
                print("        Suerte para la Proxima!!  (T-T)  ")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    
#Declaracion de la funcion para las opciones del menu

def menu_principal():
    menu = ("Juego","Operaciones","Password","Salir")
    i = 0
    print()
    print("-"*25,"\n    MENU PRINCIPAL")
    print("-"*25)
    for item_m in menu:
        i += 1
        print(f"[{i}] {item_m}")
    print("-"*25)

def exit_opt():
    print()
    print("*"*25)
    print("****** Gracias por usar la APP")
def validar_texto(name,apellido):
    cadena = "".join(name + apellido)
    if not cadena.isalpha():
        return False
def change(cadena):
    cipher = ""
    for char in cadena:  
        char = char.upper()
        code = ord(char) - 32
        if code > ord("Z"):
            code = ord("A")
        cipher += chr(code)
    
