from PyQt5 import QtWidgets
import pyodbc
from DB.conexion import *

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
    cursor.execute(f"select * from usuario")
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return rows
def tablaUsuarioFull():
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    cursor.execute(f"select u.codigo,u.nombre,u.cargo,u.clave,e.act_noact from usuario u inner join estado e on u.estado = e.id_status")
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return rows

def AddDeleteUsuario(cadena):
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    cursor.execute(cadena)
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return rows

def validarUsuario(codigo):
    cadena = AddDeleteUsuario(f"select codigo from usuario where codigo={codigo}")
    print("Resultado de Validacion busqueda",cadena)
    id = 0
    for item in cadena:
        print("Aqui el Item ", id , item[0])
        if item[0]  == codigo:
            id = 1
            print("Val Item", id)
    return id
        
def EliminarUsuario(codigo):
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    
    cursor.execute(f"DELETE usuario WHERE codigo = {codigo}")
    conn.commit()
    
    cursor.close()
    conn.close()
    
    
def NuevoUsuario(codigo,nombre,cargo,clave):
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    
    cursor.execute(f"INSERT INTO usuario (codigo,nombre,cargo,clave,estado) VALUES ({codigo},'{nombre}','{cargo}',{clave},1)")
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
    
