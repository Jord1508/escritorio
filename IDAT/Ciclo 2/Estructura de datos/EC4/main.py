import sys
from PyQt5 import QtWidgets
from Vista.registro import VentanaAlumnos

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = VentanaAlumnos()
    window.show()
    app.exec_()
