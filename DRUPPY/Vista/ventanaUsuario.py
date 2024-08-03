from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from Controlador.arregloProductos import *
from Controlador.arregloUsuario import *
from Controlador.arregloDetalleVenta import *
from Controlador.arregloFactura import *

aCli = ArregloUsuario()

class VentanaUsuario(QtWidgets.QMainWindow):

    def __init__(self,parent = None):
        super(VentanaUsuario,self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon("UI/imagenes/venta.png"))
        uic.loadUi("UI/ventanaUsuario.ui", self)
       
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnListar.clicked.connect(self.listar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnGrabar.clicked.connect(self.grabar)
        self.listar()
        self.show()


    def obtenerDni(self):
        return self.txtDni.text()
    
    def obtenerNombres(self):
        return self.txtNombres.text()
    
    def obtenerApellidos(self):
        return self.txtApellidos.text()
    
    def obtenerPassword(self):
        return self.txtPassword.text()
    
    def limpiarTabla(self):
        self.tblUsuario.clearContents()
        self.tblUsuario.setRowCount(0)

    def valida(self):
        if self.txtDni.text() == "":
            self.txtDni.setFocus()
            return "DNI del Usuario...!!!"
        elif self.txtNombres.text() == "":
            self.txtNombres.setFocus()
            return "Nombre del Usuario...!!!"
        elif self.txtApellidos.text() == "":
            self.txtApellidos.setFocus()
            return "Apellido Paterno del Usuario...!!!"
        elif self.txtPassword.text() == "":
            self.txtPassword.setFocus()
            return "Apellido Materno del Usuario...!!!"
        else:
            return ""

    def listar(self):
        self.tblUsuario.setRowCount(aCli.tamañoArregloUsuario())
        self.tblUsuario.setColumnCount(6)
        self.tblUsuario.verticalHeader().setVisible(False)
        for i in range(0, aCli.tamañoArregloUsuario()):
            self.tblUsuario.setItem(i, 0, QtWidgets.QTableWidgetItem(aCli.devolverUsuario(i).getDniUsuario()))
            self.tblUsuario.setItem(i, 1, QtWidgets.QTableWidgetItem(aCli.devolverUsuario(i).getNombresUsuario()))
            self.tblUsuario.setItem(i, 2, QtWidgets.QTableWidgetItem(aCli.devolverUsuario(i).getApellidosUsuario()))
            self.tblUsuario.setItem(i, 3, QtWidgets.QTableWidgetItem(aCli.devolverUsuario(i).getPasswordUsuario()))

    def limpiarControles(self):
        self.txtDni.clear()
        self.txtNombres.clear()
        self.txtApellidos.clear()
        self.txtPassword.clear()

    def registrar(self):
        if self.valida() == "":
            objCli = Usuario(self.obtenerDni(), self.obtenerNombres(), self.obtenerApellidoPaterno(), self.obtenerPassword())
            dni = self.obtenerDni()
            if aCli.buscarUsuario(dni) == -1:
                aCli.adicionaUsuario(objCli)
                aCli.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Usuario", "El DNI ingesado ya existe...!!!", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Usuario", "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)


    def consultar(self):
        self.limpiarTabla()
        if aCli.tamañoArregloUsuario() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Usuario", "No existen Usuario a consultar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            dni, _ = QtWidgets.QInputDialog.getText(self, "Consultar Usuario", "Ingrese el DNI a consultar")
            pos = aCli.buscarUsuario(dni)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Usuario", "El DNI ingresado no existe...!!! ", 
                                                    QtWidgets.QMessageBox.Ok)
            else:
                self.tblUsuario.setRowCount(1)
                self.tblUsuario.setItem(0, 0, QtWidgets.QTableWidgetItem(aCli.devolverUsuario(pos).getDniUsuario()))
                self.tblUsuario.setItem(0, 1, QtWidgets.QTableWidgetItem(aCli.devolverUsuario(pos).getNombresUsuario()))
                self.tblUsuario.setItem(0, 2, QtWidgets.QTableWidgetItem(aCli.devolverUsuario(pos).getApellidosUsuario()))
                self.tblUsuario.setItem(0, 3, QtWidgets.QTableWidgetItem(aCli.devolverUsuario(pos).getPasswordUsuario()))

    def eliminar(self):
        if aCli.tamañoArregloUsuario() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Usuario", "No existen Usuario a eliminar...!!!", 
                                                    QtWidgets.QMessageBox.Ok)
        else:
            fila = self.tblUsuario.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                dni = self.tblUsuario.item(indiceFila, 0).text()
                pos = aCli.buscarUsuario(dni)
                aCli.eliminarUsuario(pos)
                aCli.grabar()
                self.limpiarTabla()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Usuario", "Debe seleccionar una fila...!!!", 
                                                          QtWidgets.QMessageBox.Ok)
    def modificar(self):
        if aCli.tamañoArregloUsuario() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Usuario", "No existen Usuario a modificar...!!!",                                                    QtWidgets.QMessageBox.Ok)
        else:
            dni, _ = QtWidgets.QInputDialog.getText(self, "Modificar Usuario", "Ingrese el DNI a modificar")
            pos = aCli.buscarUsuario(dni)
            if pos != -1:
                objUsuario = aCli.devolverUsuario(pos)
                self.btnModificar.setVisible(False)
                self.btnGrabar.setVisible(True)
                self.txtDni.setText(objUsuario.getDniUsuario())
                self.txtDni.setVisible(False)
                self.lblDni.setVisible(False)
                self.txtNombres.setText(objUsuario.getNombresUsuario())
                self.txtApellidos.setText(objUsuario.getApellidosUsuario())
                self.txtPassword.setText(objUsuario.getPasswordUsuario())
        
    def grabar(self):
        try:
            pos = aCli.buscarUsuario(self.obtenerDni())
            objUsuario = aCli.devolverUsuario(pos)
            objUsuario.setNombresUsuario(self.obtenerNombres())
            objUsuario.setApellidosUsuario(self.obtenerApellidos())
            objUsuario.setPasswordUsuario(self.obtenerPassword())
            self.btnModificar.setVisible(True)
            self.btnGrabar.setVisible(False)
            aCli.grabar()
            self.limpiarTabla()
            self.limpiarControles()
            self.listar()
            self.txtDni.setVisible(True)
            self.lblDni.setVisible(True)
        except:
            QtWidgets.QMessageBox.information(self, "Modificar Usuario", "Error al modificar Usuario...!!!", 
                                              QtWidgets.QMessageBox.Ok)


