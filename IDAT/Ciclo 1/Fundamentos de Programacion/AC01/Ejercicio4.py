texto1 = "Octavio Roberto Braulio García Mejía"
texto = texto1.lower()
entrada = "áéíóú"
salida = "aeiou"
cambio = str.maketrans(entrada,salida)
newtext = texto.translate(cambio)
print(f"nuevo texto: {newtext}")

veces = int(newtext.count("a"))
separar = newtext.split(" ",veces - 1)
print(veces)