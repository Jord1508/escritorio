import pyodbc
def conexion():
    server = 'JORD'
    database = 'druppy'
    username = 'sa'
    password = '1239875'
    driver = '{ODBC Driver 17 for SQL Server}'  # Asegúrate de tener el controlador adecuado instalado

    conn_str = f'SERVER={server};DATABASE={database};UID={username};PWD={password};DRIVER={driver}'
    return conn_str
        
def NuevoProducto2(nombre,cantidad,precio,codigo,idCategoria,idEstado,idProveedor,idUsuario):
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    
    cursor.execute(f"insert into producto (nombre,cantidad,precio,codigo,id_categoria,id_estado,id_proveedor,id_usuario) values ('{nombre}',{cantidad},{precio},{codigo},{idCategoria},{idEstado},{idProveedor},{idUsuario})")
    conn.commit()
    print('Exito')
    cursor.close()
    conn.close()
    