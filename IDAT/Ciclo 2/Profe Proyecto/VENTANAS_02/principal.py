
from PyQt5 import QtWidgets, uic
import sys , os


import classPersona as per

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
        usu = self.txt_usu.text()
        pas = int(self.txt_pas.text())

        if (usu =='idat' and pas == 123):
            self.txt_usu.setText('')
            self.txt_pas.setText('')
            self.hide()
            vent2=Ui_menu()
            vent2.show()
        else:
            self.txt_usu.setText('')
            self.txt_pas.setText('')


class Ui_menu(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_menu, self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "ventmenu.ui"), self)
  
        self.btn_personal.clicked.connect(self.abrirpersona)
        self.btn_alumno.clicked.connect(self.abriralumno)
        self.btn_cerrar.clicked.connect(self.salir)
    
    def abrirpersona(self):
        self.hide()
        vent3=Ui_persona(self)
        vent3.show()

    def abriralumno(self):
        self.hide()
        vent4=Ui_alumno()
        vent4.show()
        
    def salir(self):
        self.close()
        
class Ui_persona(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_persona, self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "ventpersona.ui"), self)
        
        self.btn_registrar.clicked.connect(self.registra)
        self.btn_retornar.clicked.connect(self.cerrar)
        
    def cerrar(self):
        self.hide()
        vent=Ui_menu()
        vent.show()    
    
    def registra(self):
        id = self.txt_id.text()
        nombre = self.txt_nombre.text()
        edad = self.txt_edad.text()
        contador = int(self.lbl_reg.text())

        empleados = per.Persona.ingresar()     
   
        empleados[contador].id = id    
        empleados[contador].nombre = nombre   
        empleados[contador].edad   = edad  
        
        self.listar.clear()
        self.listar.append("ID         NOMBRE       EDAD")

        x = 0
        while x <= contador:
            self.listar.append(empleados[x].id+"         "+empleados[x].nombre+"      "+empleados[x].edad )
            x = x+1
            
        contador = contador + 1
        self.lbl_reg.setText(str(contador))
        
        
        self.txt_id.setText("")
        self.txt_nombre.setText("")
        self.txt_edad.setText("")
        
class Ui_alumno(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_alumno, self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "ventalumno.ui"), self)

        self.btn_retornar.clicked.connect(self.cerrar)
        
    def cerrar(self):
        self.hide()
        vent=Ui_menu()
        vent.show()  

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()