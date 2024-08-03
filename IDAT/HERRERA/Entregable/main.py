import sys
from PyQt5 import QtWidgets
from Vista.vLogin import Login

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Login()
    app.exec_()
