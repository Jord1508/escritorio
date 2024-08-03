
import pyodbc
def conexion():
    server = 'JORD'
    database = 'druppy'
    username = 'sa'
    password = '1239875'
    driver = '{ODBC Driver 17 for SQL Server}'  # Asegúrate de tener el controlador adecuado instalado

    conn_str = f'SERVER={server};DATABASE={database};UID={username};PWD={password};DRIVER={driver}'
    return conn_str

class Usuario:
        
    def LoadUsuarios(self):
        print('Aqui se carcagaran los usuarios')
        
    def NewUser(self):
        return self.codigo , self.nombre , self.cargo , self.clave , self.estado
    
    def InsertarUsuario(self):
        lista = self.NewUser()
        print(lista)
        
        conn = pyodbc.connect(conexion())
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO usuario (codigo,nombre,cargo,clave,estado) VALUES {lista}" )
        cursor.close()
        conn.close()
    
                
        
a = Usuario()
a.codigo = 103
a.nombre = 'TESTING'
a.cargo = 'Venta'
a.clave = '123'
a.estado = 2
#a.EliminarUsuario()
a.InsertarUsuario()
#DataBase.InsertarUsuario(datos)



'''
def ReturnCodigo(self):
    return self.codigo

def EliminarUsuario(self):
    cursor = conexion()
    cursor.execute(f"DELETE FROM usuario WHERE codigo = {self.codigo}" )
    cursor.close()'''
