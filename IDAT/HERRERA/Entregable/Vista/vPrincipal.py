from PyQt5 import QtWidgets, uic , QtGui
from PyQt5 import QtGui
from Vista.vUsuario import *
from Vista.vProducto import *

class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaPrincipal,self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon("UI/imagenes/venta.png"))
        uic.loadUi("UI/vPrincipal.ui",self)
        
        self.btn_A.clicked.connect(self.btn_1) #conexion a la pagina INICIAL
        self.btn_B.clicked.connect(self.btn_2) #conexion a la pagina USUARIOS
        self.btn_C.clicked.connect(self.btn_3) #conexion a la pagina PRODUCTOS
        
        self.btnUsuarioVentana.clicked.connect(self.abrirVentanaUsuario)
        #self.btnClientesVentana.clicked.connect(self.abrirVentanaClientes)
        self.DatosUsuario()
        
        self.btnProducto.clicked.connect(self.abrirVentanaProducto)
    
    # BLOQUE BOTONES MENU PRINCIPAL
    
    def btn_1(self):
        self.container.setCurrentIndex(0)
    def btn_2(self):
        self.container.setCurrentIndex(1)
    def btn_3(self):
        self.container.setCurrentIndex(2)

    def abrirVentanaUsuario(self):
        vUsuario = VentanaUsuario(self)
        vUsuario.show()
    
    def abrirVentanaProducto(self):
        vclientes = VentanaProducto(self)
        vclientes.show()
        
    def DatosUsuario(self):
        #Cargar Lista de usuarios
        items = tablaUsuario()
        self.tblMainUsuarios.setRowCount(len(items))
        self.tblMainUsuarios.verticalHeader().setVisible(False)
        self.tblMainUsuarios.setVerticalScrollBarPolicy(False)
        
        i = 0
        for usuario in items:
            self.tblMainUsuarios.setItem(i, 0, QtWidgets.QTableWidgetItem(usuario[0]))
            self.tblMainUsuarios.setItem(i, 1, QtWidgets.QTableWidgetItem(usuario[1]))
            self.tblMainUsuarios.setItem(i, 2, QtWidgets.QTableWidgetItem(usuario[2]))
            self.tblMainUsuarios.setItem(i, 3, QtWidgets.QTableWidgetItem(usuario[3]))
            i += 1
        
        self.txtTotalUsuario.setText(f'{i} Usuarios')
        