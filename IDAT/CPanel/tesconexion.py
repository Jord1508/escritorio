import mysql.connector

# Parámetros de conexión a la base de datos en el servidor cPanel
host = 'bubumodabebe.com'  # Puedes encontrar esta información en cPanel
user = 'bubumoda_main'
password = 'Nose211013*.'
database = 'bubumoda_proyecto'

# Intenta establecer la conexión
def tryconexion():
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    
    if connection.is_connected():
        print("Conexión exitosa")

        # Aquí puedes realizar operaciones en la base de datos

        # Por ejemplo, ejecutar una consulta
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM usuario")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        # Cierra el cursor y la conexión
        cursor.close()
        connection.close()
try:
    tryconexion()    

except Exception as e:
    print(f"Error: {e}")
