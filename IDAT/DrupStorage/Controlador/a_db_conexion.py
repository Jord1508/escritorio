import mysql.connector

class db_conexion:
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        
    # Intenta establecer la conexión
    def db_conect():
        
        host = 'bubumodabebe.com'  # Puedes encontrar esta información en cPanel
        user = 'bubumoda_main'
        password = 'Bubumodabebe211013*'
        database = 'bubumoda_base'
        
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return connection
    def db_usuarios():
        try:
            conectado = db_conexion.db_conect()
            
            if conectado.is_connected():
                print("Conexión exitosa\n")

                # Aquí puedes realizar operaciones en la base de datos

                # Por ejemplo, ejecutar una consulta
                cursor = conectado.cursor()
                cursor.execute("SELECT * FROM usuario")
                rows = cursor.fetchall()

                
                # Cierra el cursor y la conexión
                cursor.close()
                conectado.close()
                return rows
            
        except Exception as e:
            print(f"Error: {e}")


def insert_usuario(codigo, nombre, correo, telefono,status=0):
    # Create a cursor object to interact with the database
    connection = db_conexion.db_conect()
    cursor = connection.cursor()

    # Example: Insert values into a table
    insert_query = "INSERT INTO usuario (Pk_id, codigo, nombre, correo, telefono,status) VALUES (%s, %s, %s, %s, %s, %s)"
    values = ("", codigo, nombre, correo, telefono,status)

    cursor.execute(insert_query, values)  # Execute the query with the provided values
    connection.commit()                   # Commit the changes to the database
    # Close the cursor and connection
    cursor.close()
    connection.close()

insert_usuario('76698754','Julio Manuel, Palacios Orbegozo', 'jm.palacios@hotmail.com', '966300814')
