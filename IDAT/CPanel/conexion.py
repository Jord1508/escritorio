import mysql.connector

host = 'bubumodabebe.com'  # Puedes encontrar esta información en cPanel
user = 'bubumoda_main'
password = 'BubuEli0915*'
database = 'bubumoda_proyecto'
        
def db_conect():  
    try:
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
            cursor.execute("SELECT * FROM categoria")
            rows = cursor.fetchall()

            for row in rows:
                print(row)

            # Cierra el cursor y la conexión
            cursor.close()
            connection.close()

    except Exception as e:
        print(f"Error: {e}")

def insert_usuario(codigo, nombre):
    # Create a cursor object to interact with the database
    connection = db_conect()
    cursor = connection.cursor()

    # Example: Insert values into a table
    insert_query = "INSERT INTO categoria (idcategoria,nombre) VALUES (%s, %s)"
    values = (codigo, nombre)

    cursor.execute(insert_query, values)  # Execute the query with the provided values
    connection.commit()                   # Commit the changes to the database
    # Close the cursor and connection
    cursor.close()
    connection.close()

insert_usuario(1,'Niño')
