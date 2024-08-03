import sys
from ejemplo_03 import *

class sis_promediar(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,*arg,**argumentos):
        QtWidgets.QMainWindow.__init__(self,*arg,**argumentos)
        self.setupUi(self)
        self.b_aceptar.clicked.connect(self.validar)
        
    def validar(self):
        i = int(self.l_opor.text())

        usuario = self.e_n1.text()
        clave = self.e_n1.text()

        if usuario == "idat" and clave == "12345" :
            self.l_opor.setText("Ingresaste")

        else:
            i -= 1
            if i == 0:
                self.l_opor.setText("ERROR")
            else:
                self.l_opor.setText(str(i))
            self.e_n1.clear()
            self.e_n2.clear()

"""
producto, precio, cantidad  / subtotal igv neto / gaurdar el monto de la venta
empleado, pago x hora, cantidad de hora / sueldo bruto , descuento afp 12%, sueldo neto / acumulador de sueldo

"""
#Bien muñeca....!
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    Eidan = sis_promediar()
    Eidan.show()
    app.exec_()