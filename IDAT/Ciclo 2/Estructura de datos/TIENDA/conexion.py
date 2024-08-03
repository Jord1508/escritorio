import pyodbc
def conexion():
    server = 'JORD'
    database = 'tienda'
    username = 'sa'
    password = '1239875'
    driver = '{ODBC Driver 17 for SQL Server}'  # Asegúrate de tener el controlador adecuado instalado

    conn_str = f'SERVER={server};DATABASE={database};UID={username};PWD={password};DRIVER={driver}'
    return conn_str

def tablaUsuario():
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM productos")
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return rows
def buscar_producto(codigo):
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos where nombre = {}".format(codigo))
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return rows