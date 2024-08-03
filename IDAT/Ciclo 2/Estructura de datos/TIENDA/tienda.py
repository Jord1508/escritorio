from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
import sys
from conexion import *

class VentanaUsuario(QtWidgets.QWidget):

    def __init__(self,parent = None):
        super(VentanaUsuario,self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon("UI/imagenes/venta.png"))
        uic.loadUi("tienda.ui", self)
       
        self.btnRegistrar.clicked.connect(self.listar)
        self.btn_buscar.clicked.connect(self.buscarproducto)
        #self.listar()
        self.show()

    def listar(self):
        aCli = tablaUsuario()
        cantidad = len(aCli)
        self.tblClientes.setRowCount(cantidad)
        self.tblClientes.setColumnCount(5)
        self.tblClientes.verticalHeader().setVisible(False)
        i = 0
        for item in aCli:
            self.tblClientes.setItem(i, 0, QtWidgets.QTableWidgetItem(item[1]))
            self.tblClientes.setItem(i, 1, QtWidgets.QTableWidgetItem(item[2]))
            self.tblClientes.setItem(i, 2, QtWidgets.QTableWidgetItem(item[3]))
            self.tblClientes.setItem(i, 3, QtWidgets.QTableWidgetItem(item[4]))
            self.tblClientes.setItem(i, 4, QtWidgets.QTableWidgetItem(item[5]))
            i += 1
            
    def buscarproducto(self):
        valor = self.input_serach.text()
        aCli = buscar_producto(str("'" + valor + "'"))
        cantidad = len(aCli)
        self.tblBuscar.setRowCount(cantidad)
        self.tblBuscar.setColumnCount(5)
        self.tblBuscar.verticalHeader().setVisible(False)
        i = 0
        for item in aCli:
            self.tblBuscar.setItem(i, 0, QtWidgets.QTableWidgetItem(item[1]))
            self.tblBuscar.setItem(i, 1, QtWidgets.QTableWidgetItem(item[2]))
            self.tblBuscar.setItem(i, 2, QtWidgets.QTableWidgetItem(item[3]))
            self.tblBuscar.setItem(i, 3, QtWidgets.QTableWidgetItem(item[4]))
            self.tblBuscar.setItem(i, 4, QtWidgets.QTableWidgetItem(item[5]))
            i += 1

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = VentanaUsuario()
    app.exec()