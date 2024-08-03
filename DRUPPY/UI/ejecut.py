import sys
from jord import *
from PyQt5.QtGui import QIntValidator

onlyInt = QIntValidator()
onlyInt.setRange(0, 11)


class eidan(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,*arg,**kwargs):
        QtWidgets.QMainWindow.__init__(self,*arg,**kwargs)
        self.setupUi(self)
        self.btn_enviar.clicked.connect(self.nombre)
        self.name_input.setValidator(onlyInt)
    
    def nombre(self):
        oto = self.name_input.text()
        oto2 = self.lineEdit.text()
        result = int(oto) + int(oto2)
        self.name_output.setText(str(result)) 
        self.lineEdit.setText(oto)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    ventana = eidan()
    ventana.show()
    app.exec_()

