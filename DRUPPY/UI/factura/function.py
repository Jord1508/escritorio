
from PyQt5 import QtWidgets, uic
import sys , os , subprocess


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "ejemplo_06.ui"), self)
        
        self.btn_registrar.clicked.connect(self.bloquear)
        self.b_limpiar.clicked.connect(self.validar)
        
    def bloquear(self):
        self.l_nombre.setEnabled(False)
        #os.system('python filename.py')
        #subprocess.call((["C:\Users\user\Desktop\Jord\ui\ejecut.py"]), shell= True )
        #link = "c:\Users\user\Desktop\Jord\ui\combo"
        
        
    def validar(self):
        sep = self.l_nombre.dragEnabled()
        self.d_nombre.setText(str(sep))
        self.l_nombre.setEnabled(True)
        
    
    """def calcular(self):
        precio = float(self.e_n2.text())
        cantid = float(self.e_n3.text())
        sub_total = precio * cantid
        igv = sub_total * 0.12
        neto = sub_total - igv
        self.l_subt.setText(str("%.2f" % sub_total))
        self.l_igv.setText(str("%.2f" % igv))
        self.l_neto.setText(str("%.2f" % neto))
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
        self.l_ventas.setText(str("%.2f" % total_ventas))"""
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())

