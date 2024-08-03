import sys
from PyQt5 import QtWidgets, uic

class product(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(product,self).__init__(parent)
        uic.loadUi("ui/VistaAlumno.ui",self)
        self.show()
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = product()
    app.exec_()