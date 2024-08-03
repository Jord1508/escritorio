
# from PyQt5 import QtWidgets, uic
# import os , sys
# from Vista.VentanaPrincipal import class_VentanaPrincipal

# class class_Login(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(class_Login, self).__init__()
#         ui_path = os.path.abspath(os.curdir)
#         uic.loadUi(os.path.join(ui_path, "UI/Login.ui"), self)
#         self.login_btn_ingresar.clicked.connect(self.validar)
        
#     def validar(self):
#         user = self.login_input_usuario.text()
#         password = self.login_input_password.text()
#         le = QtWidgets.QLineEdit()
#         le.setEchoMode(QtWidgets.QLineEdit.Password)
        
#         if user == 'idat':
#             if password == '12345':
#                 self.W_principal= class_VentanaPrincipal()
#                 self.destroy()
#                 self.W_principal.show()
#             else:
#                 self.login_input_usuario.clear()
#                 self.login_input_password.clear()
#                 self.login_error_alert.setText('Clave mal ingresado')
#         else:
#             self.login_input_usuario.clear()
#             self.login_input_password.clear()
#             self.login_error_alert.setText('Error de usuario')
            
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     mainbox = class_Login()
#     mainbox.show()
#     sys.exit(app.exec_())

                    
class Producto:

    def __init__(self, codigo, nombre, descripcion, stockMinimo, stockActual,
                 precioCosto, precioVenta, proveedor, almacen):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__stockMinimo = stockMinimo
        self.__stockActual = stockActual
        self.__precioCosto = precioCosto
        self.__precioVenta = precioVenta
        self.__proveedor = proveedor
        self.__almacen = almacen
        
    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre

    def getDescripcion(self):
        return self.__descripcion

    def getStockMinimo(self):
        return self.__stockMinimo
    
    def getStockActual(self):
        return self.__stockActual

    def getPrecioCosto(self):
        return self.__precioCosto

    def getPrecioVenta(self):
        return self.__precioVenta

    def getProveedor(self):
        return self.__proveedor
        
    def getAlmacen(self):
        return self.__almacen

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion
        
    def setStockMinimo(self, stockMinimo):
        self.__stockMinimo = stockMinimo
        
    def setStockActual(self, stockActual):
        self.__stockActual = stockActual
        
    def setPrecioCosto(self, precioCosto):
        self.__precioCosto = precioCosto

    def setPrecioVenta(self, precioVenta):
        self.__precioVenta = precioVenta

    def setProveedor(self, proveedor):
        self.__proveedor = proveedor

    def setAlmacen(self, almacen):
        self.__almacen = almacen

