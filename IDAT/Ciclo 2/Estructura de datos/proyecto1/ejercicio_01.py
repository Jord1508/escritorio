text = input("INGRESAR MENSAJE: ")
cipher = ""
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 32
    if code > ord("Z"):
        code = ord("A")
    cipher += chr(code) 
print(cipher)
