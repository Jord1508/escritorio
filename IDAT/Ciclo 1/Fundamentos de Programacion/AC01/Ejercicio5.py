
Precio =float(input("Cual es el precio del producto: "))
Ventas =float(input("Cantidad de productos: "))
Paga_con =float(input("Paga cliente con $: "))

DolaresaSoles = Paga_con *3.68
Total = Precio * Ventas
SUBTOTAL = Total/1.18
IGV = SUBTOTAL*0.18
VueltoSoles = DolaresaSoles-(SUBTOTAL+IGV)
VueltoDolar = VueltoSoles /3.68

print(f"IGV: {IGV:.2f}")
print(f"SUBTOTAL: {SUBTOTAL:.2f}")
print(f"Total:  {Total:.2f}")
print(f"Su vuelto en dolares es:$ {VueltoDolar:.2f}")