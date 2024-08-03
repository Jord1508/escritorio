

R1=int(input("Ingresar valor de R1: "))
R2=int(input("Ingresar valor de R2: "))
R3=int(input("Ingresar valor de R3: "))

Op1 = R1 + R2
Op2 = Op1*R3
Op3 = Op1+R3
Op_FInal=Op2/ Op3


print(f"El resultado de la resistencia equivalente es: {Op_FInal:.2f}")