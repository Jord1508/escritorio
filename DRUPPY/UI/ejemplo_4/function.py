import sys
from ejemplo_04 import *
from PyQt5.QtGui import QIntValidator

onlyInt = QIntValidator()
onlyInt.setRange(0, 1100000000)


class eidan(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,*arg,**kwargs):
        QtWidgets.QMainWindow.__init__(self,*arg,**kwargs)
        self.setupUi(self)
        self.b_calcular.clicked.connect(self.calcular)
        self.b_limpiar.clicked.connect(self.limpiarcampos)
        self.b_registrar.clicked.connect(self.registrar)
        self.e_n3.setValidator(onlyInt)
    
    def calcular(self):
        precio = float(self.e_n2.text())
        cantid = float(self.e_n3.text())
        sub_total = precio * cantid
        igv = sub_total * 0.18
        neto = sub_total + igv
        self.l_subt.setText(str("%.2f" %sub_total))
        self.l_igv.setText(str("%.2f" % igv))
        self.l_neto.setText(str("%.2f" %neto))
    def limpiarcampos(self):
        self.e_n1.clear()
        self.e_n2.clear()
        self.e_n3.clear()
        self.l_subt.setText("0.00")
        self.l_igv.setText("0.00")
        self.l_neto.setText("0.00")
        
    def registrar(self):
        total_ventas = float(self.l_ventas.text())
        venta = float(self.l_neto.text())
        total_ventas += venta
        self.l_ventas.setText(str(total_ventas))
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    ventana = eidan()
    ventana.show()
    app.exec_()

