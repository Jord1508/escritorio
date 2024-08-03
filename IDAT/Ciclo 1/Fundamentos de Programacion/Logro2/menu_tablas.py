menu = input('''========= ELIJA UNA DE LAS SIGUIENTES OPCIONES =========\n1. SUMA\n2. RESTA\n3. MULTIPLICAR\n4. DIVIDIR\n>>>''')
tab_num = int(input('Cuantas Tablas desea ver...?\n>>>'))
tab_int = int(input('Deseas iniciar en la Tabla del...?\n>>>'))
rstl_num = int(input('Cuantas resultados por Tablas desea ver..?\n>>>'))
rstl_int = int(input('Les resultados iniciaran apartir del numero..?\n>>>'))

if menu.isnumeric():
   menu = int(menu)
else:
   menu = menu
rstl = 0
for n in range( tab_int , (tab_num + tab_int) +1):
    print( '=' * 50 )
    print(f'Tabla del {n}\n')
    for sub in range( rstl_int ,(rstl_int + rstl_num)+1):
        if menu == 1 or menu == 'suma' or menu == 'sumar':
            rstl = n + sub
            print(f'Es {n} + {sub} = {rstl}')
        elif menu == 2 or menu == 'resta' or menu == 'restar':
            rstl = n - sub
            if rstl < 0:
                rstl = -(rstl)
                print(f'Es {n} - {sub} = valor absoluto │{rstl}│')
            else:
                rstl = n - sub
                print(f'Es {n} - {sub} = {rstl}')
        elif menu == 3 or menu == 'multiplicar' or menu == 'multiplica':
            rstl = n * sub
            print(f'Es {n} * {sub} = {rstl}')
        elif menu == 4 or menu == 'dividir' or menu == 'divide':
            if sub == 0:
                print(f'Es {n} / 0 = No se puede dividir entre 0')
            else:
                rstl = n / sub
                if n % sub == 0:
                    print(f'Es ent {n} / {sub} = {rstl:.0f}')
                else:
                    print(f'Es dec {n} / {sub} = {rstl:.2f}')