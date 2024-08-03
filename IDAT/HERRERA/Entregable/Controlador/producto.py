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
    
    
def tablaProducto():
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
    cadena = AddDeleteUsuario(f"select id_producto from producto where id_producto={codigo}")
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
    
    
def NuevoProducto(nombre,cantidad,precio,codigo,idCategoria,idEstado,idProveedor,idUsuario):
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    
    cursor.execute(f"insert into producto (nombre,cantidad,precio,codigo,id_categoria,id_estado,id_proveedor,id_usuario) values ('{nombre}',{cantidad},{precio},'{codigo}',{idCategoria},{idEstado},{idProveedor},{idUsuario})")
    conn.commit()
    
    cursor.close()
    conn.close()

def TablaCategoria():
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM Categoria")
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return rows
    
def TablaEstado():
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM estado")
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return rows

def TablaAlmacen():
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM almacen")
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return rows
def tablaProveedor():
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM proveedor")
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return rows
    
def UltimoIDProducto():
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    
    cursor.execute(f"select max(id_producto) from producto")
    rows = cursor.fetchall()
    id = rows[0]
    id = id[0]
    
    cursor.close()
    conn.close()
    return id

def NuevoKardex(idProducto,idAlmacen,cantidad,ingreso):
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    
    cursor.execute(f"insert into kardex(id_producto,id_almacen,existencia,descripcion) values ({idProducto},{idAlmacen},{cantidad},'{ingreso}')")
    conn.commit()
    
    cursor.close()
    conn.close()
