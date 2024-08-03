import sys
from calculadora import *

class operacion_calculadora(QtWidgets.QMainWindow, Ui_Eidan):
    def __init__(self,*arg,**argumentos):
        QtWidgets.QMainWindow.__init__(self,*arg,**argumentos)
        self.setupUi(self)
        self.btn_resta.clicked.connect(self.resta)
        self.btn_clean.clicked.connect(self.limpiar)

    def limpiar(self):
        self.val_a.clear()
        self.val_b.clear()
        self.resultado.setText("---")
        self.box_msm_resultado.setText("")
    def resta(self):
        n1 = int(self.val_a.text())
        n2 = int(self.val_b.text())
        opera = n1 - n2
        self.resultado.setText(str(opera))
        self.box_msm_resultado.setText("Bien muñeca....!")

#Bien muñeca....!
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    Eidan = operacion_calculadora()
    Eidan.show()
    app.exec_()