from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
from db.conexion import *
from Controlador.usuario import *


class VentanaUsuario(QtWidgets.QMainWindow):

    def __init__(self,parent = None):
        super(VentanaUsuario,self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon("UI/imagenes/venta.png"))
        uic.loadUi("UI/ventanaUsuario.ui", self)
        
        self.cargarTabla()
        #Pagina 1 PRINCIPAL
        self.btnMain.clicked.connect(self.btn_1)
        self.btnMain2.clicked.connect(self.btn_1)
        
        self.btnCancelarCargo.clicked.connect(self.btn_4)
        
        self.btnRefrescar.clicked.connect(self.cargarTabla)
        #Pagina 2 CREAR
        self.btnCrear.clicked.connect(self.btn_2)
        self.btn_insertData.clicked.connect(self.InsertarUsuario)
        #Pagina 3 BUSCAR
        self.btnBuscar.clicked.connect(self.btn_3)
        self.btnActualizar.clicked.connect(self.btn_4)
        self.btnEliminar.clicked.connect(self.btn_5)
        self.btnXa.clicked.connect(self.btn_6)
        self.btnXCerrar.clicked.connect(self.btn_exit)
        # PAGINA 4 ACTUALIZAR
        
        # PAGINA 5 ELIMINAR
        self.btnBuscarEliminar.clicked.connect(self.accionbtnBuscarEliminar)
        self.btnCancelarEliminar.clicked.connect(self.accionbtnCancelarEliminar)
        self.btnEliminarUsuario.clicked.connect(self.accionbtnEliminarUsuario)
        
        # PAGINA 6 CREAR CARGOS
        
    # #PAGINA PRINCIPAL USUARIO **************************************************************
    def btn_1(self):
        self.container.setCurrentIndex(0)  #BOTON HACIA PAGINA 
    #FUNCIONES DE CARGA
    def cargarTabla(self):
        items = tablaUsuario()
        self.tblUsuario.setRowCount(len(items))
        i = 0
        for usuario in items:
            self.tblUsuario.setItem(i, 0, QtWidgets.QTableWidgetItem(usuario[0]))
            self.tblUsuario.setItem(i, 1, QtWidgets.QTableWidgetItem(usuario[1]))
            self.tblUsuario.setItem(i, 2, QtWidgets.QTableWidgetItem(usuario[2]))
            i += 1
        print(i)
        self.txtTotal_item.setText(f'{i} Usuarios')
        
    def llenar_comboBox2(self):        
        etiquet = []
        lista = TablaCargos()
        
        for item in lista:
            etiquet.append(item[1])
            
        print(etiquet)
        self.inputCargo.addItems(etiquet)
        self.inputCargo_3.addItems(etiquet)
    # #PAGINA CREAR USUARIO **************************************************************
    def btn_2(self):
        self.container.setCurrentIndex(1) # BOTON HACIA PAGINA CREAR USUARIO
        
    def InsertarUsuario(self):
        if self.validar() == "":
            a = self.inputCodigo.text()
            b = self.inputNombre.text()
            c = self.inputCargo.currentText()
            d = self.inputClave.text()
            NuevoUsuario(a,b,c,d)
            self.inputCodigo.clear()
            self.inputNombre.clear()
            self.inputCargo.setCurrentIndex(0)
            self.inputClave.clear()
            self.container.setCurrentIndex(0)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Cliente", "Error en " + self.validar(), QtWidgets.QMessageBox.Ok)
    
    def btn_3(self):
        self.container.setCurrentIndex(2) # PAGINA BUSCAR USUARIO
        
        
    def btn_4(self):
        self.container.setCurrentIndex(3) # PAGINA ACTUALIZAR USUARIO
        
    #  ELIMINAR USUARIO **************************************************************
    def btn_5(self):
        self.container.setCurrentIndex(4) # BOTON HACIA PAGINA ELIMINAR USUARIO
        
        
    #BOTONES DE ACCION ELIMINAR
    
    def accionbtnCancelarEliminar(self):
        self.inputCodigoEliminar.clear()
        self.txtNombreEliminar.setText('**********')
        self.txtCargoEliminar.setText('**********')
        self.btn_1()
        
    def accionbtnBuscarEliminar(self):
        codigo = self.inputCodigoEliminar.text()
        Existe = ValidarExistenciaUsuario(codigo)
        
        if Existe == True:
            
            EliminarUsuario(codigo)
            self.inputCodigoEliminar.clear()
            self.txtNombreEliminar.setText('**********')
            self.txtCargoEliminar.setText('**********')
            
            mensaje = QMessageBox()
            mensaje.setWindowTitle("CREACION DE USUARIO")
            mensaje.setText("El usuario ingresado ha sido Eliminado...!!!")
            x = mensaje.exec_()
            
            self.btn_1()
            
        else:
            self.inputCodigoEliminar.clear()
            self.inputCodigoEliminar.setFocus()
            mensaje = QMessageBox()
            mensaje.setWindowTitle("CREACION DE USUARIO")
            mensaje.setText("El usuario no esta Registrado...!!!")
            x = mensaje.exec_()
        
    def accionbtnEliminarUsuario(self):
        codigo = self.inputCodigoEliminar.text()
        Existe = ValidarExistenciaUsuario(codigo)
        
        if Existe == True:
            
            EliminarUsuario(codigo)
            self.inputCodigoEliminar.clear()
            self.txtNombreEliminar.setText('**********')
            self.txtCargoEliminar.setText('**********')
            
            mensaje = QMessageBox()
            mensaje.setWindowTitle("CREACION DE USUARIO")
            mensaje.setText("El usuario ingresado ha sido Eliminado...!!!")
            x = mensaje.exec_()
            
            self.btn_1()
            
        else:
            self.inputCodigoEliminar.clear()
            self.inputCodigoEliminar.setFocus()
            mensaje = QMessageBox()
            mensaje.setWindowTitle("CREACION DE USUARIO")
            mensaje.setText("El usuario no esta Registrado...!!!")
            x = mensaje.exec_()
    
    def btn_6(self):
        self.container.setCurrentIndex(5) # PAGINA CREAR CARGO DE USUARIO
        
    def btn_exit(self): # BOTON DE CIERRE DE LA VENTANA
        self.close()
        return ' Boton de salida'
        
    def validar(self):
        if self.inputCodigo.text() == "":
            self.inputCodigo.setFocus()
            return "Codigo del cliente...!!!"
        elif self.inputNombre.text() == "":
            self.inputNombre.setFocus()
            return "Nombre del cliente...!!!"
        elif self.inputCargo.currentText() == "Seleccione":
            self.inputCargo.setFocus()
            return "Cargo Paterno del cliente...!!!"
        elif self.inputClave.text() == "":
            self.inputClave.setFocus() 
            return "Password Materno del cliente...!!!"
        else:
            return ""
    
    #ARREGLOS DE USUARIOS

# Estilos
# background-color: rgb(0, 170, 255);
    
