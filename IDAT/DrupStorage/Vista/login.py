
from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
from Vista.ventanaPrincipal import VentanaPrincipal
from Controlador.arregloProductos import *
from Controlador.arregloClientes import *
from Controlador.arregloDetalleVenta import *
from Controlador.arregloFactura import *


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
        usuario = self.txtUsuario.text().lower()
        contrasena = self.txtPassword.text()
        
        if usuario == "idat":
            if contrasena == "123":
                self.close()
                vprincipal = VentanaPrincipal(self)
                vprincipal.show()
            else:
                self.txtPassword.setFocus()
                mensaje = QMessageBox()
                mensaje.setWindowTitle("Punto de Venta")
                mensaje.setText("La contraseña ingresado es incorrecto...!!!")
                x = mensaje.exec_()   
        else:
            self.txtUsuario.setFocus()
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Punto de Venta")
            mensaje.setText("El usuario ingresado es incorrecto...!!!")
            x = mensaje.exec_()
            
