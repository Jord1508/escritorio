import pyodbc
from db.conexion import *


def tablaUsuario():
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM dbo.usuario")
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return rows

def nuevoUsuario(codigo,nombre,cargo,clave):
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()

    # Insert values into a table
    cursor.execute(f' INSERT INTO your_table (codigo, nombre, cargo, clave)  VALUES ({codigo},{nombre},{cargo},{clave})')

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()