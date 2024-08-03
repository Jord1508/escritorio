import pyodbc
def conexion():
    server = 'DESKTOP-7SSD3RG'
    database = 'POKY'
    username = 'sa'
    password = '1234'
    driver = '{ODBC Driver 17 for SQL Server}'  # Asegúrate de tener el controlador adecuado instalado

    conn_str = f'SERVER={server};DATABASE={database};UID={username};PWD={password};DRIVER={driver}'
    return conn_str

def especialidadcon():
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    cursor.execute(f"select * from alumno")
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return rows

def especialidadcon():
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    cursor.execute(f"select a.id_alumno, a.nombre, a.especialidad, b.curso, b.examen_parcial_2, b.examen_final_4, b.promedio, b.condicion from registros b inner join alumno a on b.id_alumno = a.id_alumno")
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return rows