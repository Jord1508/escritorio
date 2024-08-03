#from Controlador.usuario import *
#from Controlador.db import *
from usuario import *
from db import *
class ArregloUsuario:

    def __init__(self):
        self.dataUsuario = []
        self.cargar() 
       
    def cargar(self):
        archivo = tablaUsuario()
        
        for linea in archivo:
            dni = linea[0]
            nombres = linea[1]
            apellidos = linea[2]
            password = linea[3]
            objCli = Usuario(dni, nombres, apellidos, password)
            self.adicionaUsuario(objCli)

    def grabar(self):
        archivo = open("Modelo/Usuario.txt", "w+", encoding = "utf-8")
        for i in range(self.tamañoArregloUsuario()):
            dni = str(self.devolverUsuario(i).getDniUsuario())
            nombre = str(self.devolverUsuario(i).getNombresUsuario())
            apellido = str(self.devolverUsuario(i).getApellidosUsuario())
            clave = str(self.devolverUsuario(i).getPasswordUsuario())
            
            archivo.write( dni + "," + nombre + "," + apellido + "," + clave + "\n")
        archivo.close()

    def adicionaUsuario(self, objCli):
        self.dataUsuario.append(objCli)

    def devolverUsuario(self, pos):
        return self.dataUsuario[pos]
    
    def tamañoArregloUsuario(self):
        return len(self.dataUsuario)

    def buscarUsuario(self, dni):
        for i in range(self.tamañoArregloUsuario()):
            if dni == self.dataUsuario[i].getDniUsuario():
                return i
        return -1

    def eliminarUsuario(self, indice):
        del(self.dataUsuario[indice])
               
