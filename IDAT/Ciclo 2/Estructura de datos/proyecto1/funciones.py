menu = ("Invertir texto","Crear contraseña","Contar caracteres","Salir del programa")
def menu_principal():
    i = 0
    print()
    print("-"*25,"\n    MENU PRINCIPAL")
    print("-"*25)
    for item_m in menu:
        i += 1
        print(f"[{i}] {item_m}")
    print("-"*25)

def invertir_text(texto):
    txt = (texto)
    print(f'{txt[::-1]!r}')
def exit_opt():
    print("*"*25)

menu_principal()

import conexion as conectar


