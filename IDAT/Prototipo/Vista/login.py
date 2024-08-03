from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
from Vista.ventanaPrincipal import VentanaPrincipal
from Controlador.arregloProductos import *
from Controlador.arregloClientes import *
from Controlador.arregloDetalleVenta import *
from Controlador.arregloFactura import *
from Controlador.usuario import *


class Login(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(Login,self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon("UI/imagenes/venta.png"))
        uic.loadUi("UI/login.ui",self)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btnIniciar.clicked.connect(self.iniciarSesion)
        self.show()

    # Aquí van las nuevas funciones
    def iniciarSesion(self):
        usuario = self.txtUsuario.text()
        contrasena = self.txtPassword.text()
        val = self.validarLogin(usuario,contrasena)
        if val[0] == True:
            if val[1] == True:
                self.close()
                vprincipal = VentanaPrincipal(self)
                vprincipal.show()
            else:
                self.txtPassword.clear()
                self.txtPassword.setFocus()
                mensaje = QMessageBox()
                mensaje.setWindowTitle("Punto de Venta")
                mensaje.setText("La contraseña ingresado es incorrecto...!!!")
                x = mensaje.exec_()   
        else:
            self.txtUsuario.clear()
            self.txtUsuario.setFocus()
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Punto de Venta")
            mensaje.setText("El usuario ingresado es incorrecto...!!!")
            x = mensaje.exec_()
    
    def validarLogin(self, usuario, clave):
        tabla = tablaUsuario()
        print(tabla)
        values = [False,False]
        for item in tabla:
            if item[0] == usuario and item [3] != clave:
                values = [True,False]
                break
            elif  item[0] == usuario and item [3] == clave:
                values = [True,True]
                break
        return values
                    
    
    
                    
                
        
            
