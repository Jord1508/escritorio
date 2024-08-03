from Controlador.usuario import *
from Modelo.usuario import *


class ArregloUsuario:

    def __init__(self):
        self.dataClientes = []
        self.cargar()

    def cargar(self):
        datos = tablaUsuario()
        for item in datos:
            usuario = Usuario(item[0],item[1],item[2],item[3])
            self.adicionaCliente(usuario)
            
    def adicionaCliente(self, objCli):
        self.dataClientes.append(objCli)
        
    def devolverUsuario(self, pos):
        return self.dataUsuarios[pos]
    
    def tamañoArregloUsuario(self):
        return len(self.dataUsuarios)

    def buscarUsuario(self, dni):
        archivo = tablaUsuario()
        i = 0
        for item in archivo:
            codigo = item[0]
            i += 1
            if dni == codigo:
                return i
        return -1

    def eliminarUsuario(self, indice):
        del(self.dataUsuarios[indice])
               
