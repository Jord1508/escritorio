import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QTableWidget, QTableWidgetItem, QTableWidget, QTableWidgetItem, QMainWindow, QTableWidget, QTableWidgetItem, QDockWidget, QFormLayout, QLineEdit, QWidget, QPushButton, QSpinBox


from PyQt5.uic import loadUi


from login_ui import *
from vent_menu_ui import *
from vent_tabla1_ui import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.btn_aceptar.clicked.connect(self.validar)
        self.btn_cerrar.clicked.connect(self.salir)
    
    def salir(self):
        self.close()

    def validar(self):
        usu = self.txt_n1.text()
        pas = self.txt_n2.text()

        if usu !='idat' and pas !='123':
            self.txt_n1.setText('')
            self.txt_n2.setText('')
        else:
            self.txt_n1.setText('')
            self.txt_n2.setText('')

            self.hide()

            vent2=Ui_menu(self)
            vent2.show()


class Ui_menu(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_menu, self).__init__(parent)
        loadUi('vent_menu.ui', self)
        
        self.boton1.clicked.connect(self.abrirtabla1)
        self.boton6.clicked.connect(self.abrirVentanaPrincipal)

    def abrirtabla1(self):
        self.hide()
        vent3=Ui_tabla1(self)
        vent3.show()
     
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()



class Ui_tabla1(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_tabla1, self).__init__(parent)
        loadUi('vent_tabla1.ui', self)


        self.registrar.clicked.connect(self.registro)
        self.btn_cerrar.clicked.connect(self.salir)

    def registro(self):
        id = self.txt_id.text()
        nombre = self.txt_nombre.text()
        apellido = self.txt_apellido.text()


        employees = [
            {'First Name': 'John', 'Last Name': 'Doe', 'Age': 25},
            {'First Name': 'Jane', 'Last Name': 'Doe', 'Age': 22},
            {'First Name': 'Alice', 'Last Name': 'Doe', 'Age': 22},
        ]

        self.table = QTableWidget(self)
        self.setCentralWidget(self.table)

        self.table.setColumnCount(3)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 50)

        self.table.setHorizontalHeaderLabels(employees[0].keys())
        self.table.setRowCount(len(employees))

        row = 0
        for e in employees:
            self.table.setItem(row, 0, QTableWidgetItem(e['First Name']))
            self.table.setItem(row, 1, QTableWidgetItem(e['Last Name']))
            self.table.setItem(row, 2, QTableWidgetItem(str(e['Age'])))
            row += 1



        dock = QDockWidget('New Employee')
        dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)

        # create form
        form = QWidget()
        layout = QFormLayout(form)
        form.setLayout(layout)


        self.first_name = QLineEdit(form)
        self.last_name = QLineEdit(form)
        self.age = QSpinBox(form, minimum=18, maximum=67)
        self.age.clear()

        layout.addRow('First Name:', self.first_name)
        layout.addRow('Last Name:', self.last_name)
        layout.addRow('Age:', self.age)







            
    def salir(self):
        self.parent().show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()