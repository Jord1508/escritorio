import sys
from ejemplo_02 import *

class sis_promediar(QtWidgets.QMainWindow, XXX):
    def __init__(self,*arg,**argumentos):
        QtWidgets.QMainWindow.__init__(self,*arg,**argumentos)
        self.setupUi(self)
        self.b_promediar.clicked.connect(self.promediar)
        self.b_limpiar.clicked.connect(self.limpiar)
        self.b_calculos.clicked.connect(self.calculos)
    def limpiar(self):
        self.e_n1.clear()
        self.e_n2.clear()
        self.e_n3.clear()
        self.e_n4.clear()
        self.l_prom.setText("---")
        self.l_condi.setText("---")

    def calculos(self):
        i = int(self.l_apro.text())
        e = int(self.l_desa.text())
        prom = float(self.l_prom.text())
        if prom >= 13:
            i += 1
            self.l_apro.setText(str(i))
        else:
            e += 1
            self.l_desa.setText(str(e))

    def promediar(self):
        n1 = int(self.e_n1.text()) + int(self.e_n2.text()) + int(self.e_n3.text()) + int(self.e_n4.text())
        opera = n1 / 4
        self.l_prom.setText(str(opera))
        
        if opera >= 13:
            self.l_condi.setText("APROBADO")
        else:
            self.l_condi.setText("DESAPROBADO")

#Bien muñeca....!
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    Eidan = sis_promediar()
    Eidan.show()
    app.exec_()