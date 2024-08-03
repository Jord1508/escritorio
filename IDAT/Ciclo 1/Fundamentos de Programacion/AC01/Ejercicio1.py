datos = input("Ingrese su pais, Fecha de nacimiento (dd-mm-aaaa),Ingrese sus apellidos: ").lower().strip()
datos = datos.replace(",","")
datos = datos.split()

pais = datos[0]
fecha = datos[1]
ape_mom = str(len(datos[3]))  #Extraccion del apellido y calculo de la longitud de esta misma
n_pais = str(len(pais)) #Se extrae la longitud del string pais
last_pais = pais[-2:] #Se extrae las 2 ultimas letras del string pais
edad = str(2023 - int(fecha[-4:])) # calculo de la edad
npremium = str(edad + edad*2 + edad*3)
#CONCATENADO DE LAS PARTES GENERANDO LA CLAVE
clave_segura = n_pais + last_pais + edad + ape_mom + npremium

# Cambio de vocales con tildes y reemplazadas por el @ y la “e” por el 3.
entrada = "áaéeíóú"
salida = "@@33iou"
sustit = str.maketrans(entrada,salida)

#IMPRESION DEL RESULTADO DE LA OPERACION
print(f"Esta es su clave segura: {clave_segura.translate(sustit)}")

