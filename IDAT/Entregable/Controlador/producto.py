from DB.conexion import *

class C_producto:
    
    def DB_Tabla(self, nombreDbTabla):
        rows = AskDataBase(f"SELECT * FROM {nombreDbTabla}")
        return rows
    
    def tablaProductos(self):
        cursor = f"select nombre,categoria,stock,precio,codigo,imagen from producto"
        rows = AskDataBase(cursor)
        return rows
    def Eliminar_User(self,codigo):
        cursor = f"DELETE usuario WHERE codigo = {codigo}"
        Delete_DataBase(cursor)
        return 'Usuario eliminado correctamente'

