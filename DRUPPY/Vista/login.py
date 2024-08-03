from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
from Vista.ventanaPrincipal import VentanaPrincipal
from Controlador.arregloProductos import *
from Controlador.arregloClientes import *
from Controlador.arregloDetalleVenta import *
from Controlador.arregloFactura import *
from Controlador.db_usuario import *
main_user = ''
qtCreatorFile = "UI/login.ui" # Nombre del archivo aquí!!!
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

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
        valor = validarLoginUser(usuario)
        if validarLoginUser(usuario) == True:
            if validarLoginClave(contrasena) == True:
                self.close()
                vprincipal = VentanaPrincipal(self)
                vprincipal.show()
            else:
                self.txtPassword.clear()
                mensaje = QMessageBox()
                mensaje.setWindowTitle("Punto de Venta")
                mensaje.setText("La clave ingresado es incorrecto...!!!")
                x = mensaje.exec_()
             
        else:
            self.txtUsuario.clear()
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Punto de Venta")
            mensaje.setText("El usuario ingresado es incorrecto...!!!")
            x = mensaje.exec_()