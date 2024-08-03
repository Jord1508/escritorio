from PyQt5 import QtWidgets
import pyodbc
from db.conexion import *

class Usuario:

    def __init__(self, codigoUsuario, nombreUsuario, cargoUsuario,claveUsuario):
        self.__codigoUsuario = codigoUsuario 
        self.__nombreUsuario = nombreUsuario
        self.__cargoUsuario = cargoUsuario
        self.__claveUsuario = claveUsuario
    
    def getCodigoUsuario(self):
        return self.__codigoUsuario

    def getNombreUsuario(self):
        return self.__nombreUsuario

    def getCargoUsuario(self):
        return self.__cargoUsuario

    def getClaveUsuario(self):
        return self.__claveUsuario

def tablaUsuario():
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM usuario")
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return rows

def NuevoUsuario(codigo,nombre,cargo,clave):
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    
    cursor.execute(f"INSERT INTO usuario (codigo,nombre,cargo,clave) VALUES ({codigo},'{nombre}','{cargo}',{clave})")
    conn.commit()
    
    cursor.close()
    conn.close()

def TablaCargos():
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM cargo")
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return rows
        
def EliminarUsuario(codigo):
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    
    cursor.execute(f" DELETE FROM usuario WHERE codigo = {codigo}" )
    conn.commit()
    
    cursor.close()
    conn.close()
    
def ValidarExistenciaUsuario(codigo):
    lista = tablaUsuario()
    Existencia = False
    for users in lista:
        if codigo == users:
            Existencia = True
    return Existencia
    
