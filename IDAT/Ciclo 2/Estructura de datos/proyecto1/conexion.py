"""from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel

db_server = 'JORD'
db_base = 'DBViernes'
db_user = 'sa'
db_clave = '1239875'
"""
import pyodbc

# Parámetros de conexión
server = 'JORD'
database = 'DBViernes'
username = 'sa'
password = '1239875'
driver = '{ODBC Driver 17 for SQL Server}'  # Asegúrate de tener el controlador adecuado instalado

# Cadena de conexión
conn_str = f'SERVER={server};DATABASE={database};UID={username};PWD={password};DRIVER={driver}'

# Intenta establecer la conexión
try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Ejemplo: ejecutar una consulta
    cursor.execute("SELECT * FROM dbo.usuario")
    rows = cursor.fetchall()
    for row in rows:
        if row[4] == '966400712':
            print('Encontrado')

    # Cierra el cursor y la conexión
    cursor.close()
    conn.close()

except Exception as e:
    print(f"Error: {e}")

