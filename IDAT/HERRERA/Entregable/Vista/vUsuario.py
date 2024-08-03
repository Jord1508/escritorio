from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
import pyodbc
from DB.conexion import *
from Controlador.usuario import *


class VentanaUsuario(QtWidgets.QMainWindow):

    def __init__(self,parent = None):
        super(VentanaUsuario,self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon("UI/imagenes/venta.png"))
        uic.loadUi("UI/vUsuario.ui", self)
        self.cargarTabla()
        self.llenar_comboBox2()
        
        #BTNs Pagina Principal      >>>   A
        self.btnCrear.clicked.connect(self.btn_2) #conexion a la pagina crear
        self.btnBuscar.clicked.connect(self.btn_3) #conexion a la pagina Buscar
        self.btnActualizar.clicked.connect(self.btn_4)
        self.btnEliminar.clicked.connect(self.btn_5)
        
        self.btnRefrescarA.clicked.connect(self.cargarTabla)
            #BOTON CERRAR
        self.btnXCerrarA.clicked.connect(self.btn_exit)
        
        
        #BTNs Pagina Crear          >>>   B
        self.btn_insertData.clicked.connect(self.InsertarUsuario)
            #BOTON CERRAR
        self.btnXCerrarB.clicked.connect(self.btn_exit)
        self.btnCancelarCrearB.clicked.connect(self.cancelarCrear)
        
        #BTNs Pagina Buscar         >>>    C
        self.btnBuscarC.clicked.connect(self.BuscarCodigoC)
        self.btnUpdateC.clicked.connect(self.btn_4)
        #self.btnDeleteC
        self.btnXCerrarC.clicked.connect(self.btn_exit)
        self.btnCancelarC.clicked.connect(self.cancelarBuscar)
        self.btnDeleteC.clicked.connect(self.EliminarTuplaUsuario)
        
        #BTNs PAgina Actualizar
        self.btnCancelarD.clicked.connect(self.btn_1)
        self.btnXCerrarD.clicked.connect(self.btn_exit)
        
        #BTN PAgina Eliminar           >>> E
        self.btnEliminarE.clicked.connect(self.EliminarTuplaUsuarioE)
        self.btnXCerrarE.clicked.connect(self.btn_exit)
        self.btnCancelarE.clicked.connect(self.btn_1)
        
        
    def refrescarTabla(self):
        self.cargarTabla()
    #FUNCIONES DE BOTONES LATERALES
    def btn_1(self):
        self.container.setCurrentIndex(0)
    
    def btn_2(self):
        self.container.setCurrentIndex(1)
    
    def btn_3(self):
        self.container.setCurrentIndex(2)
    def btn_4(self):
        self.container.setCurrentIndex(3)
    def btn_5(self):
        self.container.setCurrentIndex(4)
    def btn_6(self):
        self.container.setCurrentIndex(5)
    def btn_exit(self):
        self.close()
        return ' Boton de salida'

    def cancelarCrear(self):
        self.inputCodigo.clear()
        self.inputNombre.clear()
        self.inputCargo.setCurrentIndex(0)
        self.inputClave.clear()
        self.container.setCurrentIndex(0)
        
    def cancelarBuscar(self):
        self.txtCodigoC.setText("")
        self.txtNombreC.setText("")
        self.txtCargoC.setText("")
        self.txtClaveC.setText("")
        self.txtEstadoC.setText("")
        self.inputCodigoC.clear()
        self.container.setCurrentIndex(0)
        
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
        print("Aqui Carga de Tupla",i)
        self.txtTotal_item.setText(f'{i} Usuarios')
        
    def InsertarUsuario(self):
        if self.validar() == "":
            a = self.inputCodigo.text()
            b = self.inputNombre.text()
            c = self.inputCargo.currentText()
            d = self.inputClave.text()
            num = validarUsuario(a)
            if num == 0:
                
                NuevoUsuario(a,b,c,d)
                self.inputCodigo.clear()
                self.inputNombre.clear()
                self.inputCargo.setCurrentIndex(0)
                self.inputClave.clear()
                QtWidgets.QMessageBox.information(self, "Registrar Cliente", "Usuario nuevo registrado", QtWidgets.QMessageBox.Ok)
                self.cancelarCrear()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Cliente", "Id de Usuario ya registrado", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Cliente", "Error en " + self.validar(), QtWidgets.QMessageBox.Ok)
        
        
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
    def validarC(self):
        if self.inputCodigoC.text() == "":
            self.inputCodigoC.setFocus()
            return "campo codigo en blanco...!!!"
        else:
            return ""
        
    #ARREGLOS DE USUARIOS
    def llenar_comboBox2(self):        
        etiquet = []
        lista = TablaCargos()
        
        for item in lista:
            etiquet.append(item[1])
            
        self.inputCargo.addItems(etiquet)
        self.inputCargoD.addItems(etiquet)
    #  PAGINA C  BUSCAR
    def BuscarCodigoC(self):
        
        if self.validarC() == "":
            a = self.inputCodigoC.text()
            if validarUsuario(a) == 1:
                tupla = tablaUsuarioFull()
                for items in tupla:
                    codigo, nombre,cargo,clave,estado = items
                    if codigo == a:
                        self.txtCodigoC.setText(str(" " + codigo))
                        self.txtNombreC.setText(str(" " + nombre))
                        self.txtCargoC.setText(str(" " + cargo))
                        self.txtClaveC.setText(str(" " + clave))
                        self.txtEstadoC.setText(str(" " + estado))
    
        else:
            QtWidgets.QMessageBox.information(self, "Buscqueda C", "Error en " + self.validarC(), QtWidgets.QMessageBox.Ok)
    
    def EliminarTuplaUsuario(self):
        codigo = self.inputCodigoC.text()
        EliminarUsuario(codigo)
        QtWidgets.QMessageBox.information(self, "Registro de Usuarios", "Usuario Eliminado Exitosamente...!!!", QtWidgets.QMessageBox.Ok)
        self.container.setCurrentIndex(0)
    def EliminarTuplaUsuarioE(self):
        try:
            codigo = self.inputCodigoE.text()
            EliminarUsuario(codigo)
            QtWidgets.QMessageBox.information(self, "Eliminacion de Usuarios", "Usuario Eliminado Exitosamente...!!!", QtWidgets.QMessageBox.Ok)
            self.container.setCurrentIndex(0)
        except:
            QtWidgets.QMessageBox.information(self, "Eliminacion de Usuarios", "Usuario No encontrado...!!!", QtWidgets.QMessageBox.Ok)
            
        
        
        
# Estilos
# background-color: rgb(0, 170, 255);
    
