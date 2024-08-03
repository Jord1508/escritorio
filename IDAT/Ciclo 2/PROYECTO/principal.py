from PyQt5 import QtWidgets, uic
import sys , os

from login_ui import *
from menu_ui import *
from persona_ui import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "login.ui"), self)
        
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

            vent2=Ui_vent_menu(self)
            vent2.show()

class Ui_vent_menu(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_vent_menu, self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "menu.ui"), self)
        
        self.btn_persona.clicked.connect(self.abrirpersona)
        self.btn_cerrar.clicked.connect(self.abrirPrincipal)

    def abrirpersona(self):
        self.hide()
        vent3=Ui_vent_persona(self)
        vent3.show()
     
    def abrirPrincipal(self):
        self.parent().show()
        self.close()

class Ui_vent_persona(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_vent_menu, self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "persona.ui"), self)

        self.btn_registrar.clicked.connect(self.registro)
        self.btn_cerrar.clicked.connect(self.salir)
        
    def registro(self):
        num = int(self.lbl_regis.text())
        num += 1
        
        self.lbl_regis.setText(str(num))
        registros = num
        return registros
    
        codigo = self.txt_n1.text()
        nombre = self.txt_n2.text()
        edad = self.txt_n3.text()

    def salir(self):
        self.hide()
        self.parent().show()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()