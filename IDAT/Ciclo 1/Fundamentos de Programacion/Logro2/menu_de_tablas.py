menu = input('''========= ELIJA UNA DE LAS SIGUIENTES OPCIONES =========\n1. SUMA\n2. RESTA\n3. MULTIPLICAR\n4. DIVIDIR\n>>>''').lower()
tab_num = int(input('Cuantas Tablas desea ver...?\n>>>'))
tab_int = int(input('Deseas iniciar en la Tabla del...?\n>>>'))
rstl_num = int(input('Cuantas resultados por Tablas desea ver..?\n>>>'))
rstl_int = int(input('Les resultados iniciaran apartir del numero..?\n>>>'))

rstl = 0
for main in range( tab_int , (tab_num + tab_int) ):
    print( '=' * 50 )
    print(f'Tabla del {main}\n')
    for sub in range( rstl_int ,(rstl_int + rstl_num)):
        if menu == 1 or menu == 'suma' or menu == 'sumar':
            rstl = main + sub
            print(f'Es {main} + {sub} = {rstl}')
        elif menu == 2 or menu == 'resta' or menu == 'restar':
            rstl = main - sub
            if rstl < 0:
                rstl = -(rstl)
                print(f'Es {main} - {sub} = valor absoluto │{rstl}│')
            else:
                rstl = main - sub
                print(f'Es {main} - {sub} = {rstl}')
        elif menu == 3 or menu == 'multiplicar' or menu == 'multiplica':
            rstl = main * sub
            print(f'Es {main} * {sub} = {rstl}')
        elif menu == 4 or menu == 'dividir' or menu == 'divide':
            rstl = main / sub
            print(f'Es {main} / {sub} = {rstl:.2f}')
        else:
            print('Ingreso un dato invalido')