from PyQt5 import QtWidgets, QtGui
from Controlador.funciones import *
from Controlador.usuario import *
from Vista.vUsuario import *
from Vista.vProducto import *
from Vista.vCategoria import *
f = C_Usuario()

        
class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaPrincipal,self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon("UI/imagenes/venta.png"))
        cargarUI("UI/vPrincipal.ui",self)
    
        self.container_botones_paginador()
    
    def container_botones_paginador(self):
        
        self.btn_indice(self.btn_A,0) #conexion a la pagina INICIAL
        self.btn_indice(self.btn_B,1) #conexion a la pagina USUARIOS
        self.btn_indice(self.btn_C,2) #conexion a la pagina PRODUCTOS
        self.btn_indice(self.btnCategoria,3)
        
        btn_action(self.btnXCerrar,self.btn_exit)
        
        self.btnUsuarioVentana.clicked.connect(self.abrirVentanaUsuario)
        self.btnOpenCategoria.clicked.connect(self.abrirVentanaCategoria)
        #self.btnClientesVentana.clicked.connect(self.abrirVentanaClientes)
        self.DatosUsuario()
        
        self.btnProducto.clicked.connect(self.abrirVentanaProducto)
    
    # BLOQUE BOTONES MENU PRINCIPAL
    def link_ir_a(self,num):
        self.container.setCurrentIndex(num)
        
    def btn_indice(self,boton,num):
        return boton.clicked.connect(lambda: self.link_ir_a(num))
    
    def Pagina0(self):
        self.container.setCurrentIndex(0)
    def Pagina1(self):
        self.container.setCurrentIndex(1)
    def Pagina2(self):
        self.container.setCurrentIndex(2)
    def Pagina3(self):
        self.container.setCurrentIndex(3)
    def btn_exit(self):
        self.close()
        return ' Boton de salida'
    def abrirVentanaCategoria(self):
        vCategoria = VentanaCategoria(self)
        vCategoria.show()
    def abrirVentanaUsuario(self):
        vUsuario = VentanaUsuario(self)
        vUsuario.show()
    
    def abrirVentanaProducto(self):
        vclientes = VentanaProducto(self)
        vclientes.show()
        
    def DatosUsuario(self):
        
        func_tblDatos(f.tablaUsuario(),self.tblMainUsuarios)
        self.txtTotalUsuario.setText(f'{f.TotalUser()} Usuarios')
        