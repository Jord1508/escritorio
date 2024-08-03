
from PyQt5 import QtWidgets, uic, QtCore
import sys , os


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "combo.ui"), self)
        
        self.btn_combo.currentTextChanged.connect(self.validar)
        self.accion.clicked.connect(self.crear)
        print(ui_path)
   
    def validar(self):
        
        self.cantidad.setText(self.btn_combo.currentText())
    
    def crear(self):
        row = self.tableWidget.rowCount()
        vert = row
        row += 1
        self.tableWidget.setRowCount(row)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(vert, item)
        
        
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(vert, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(vert, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(vert, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(vert, 3, item)
        
        _translate = QtCore.QCoreApplication.translate
        
        n = self.nombre.text()
        c = self.cantidad.text()
        p = self.precio.text()
        item = self.tableWidget.item(vert, 0)
        item.setText(_translate("MainWindow", str(row) ))
        item = self.tableWidget.item(vert, 1)
        item.setText(_translate("MainWindow", n ))
        item = self.tableWidget.item(vert, 2)
        item.setText(_translate("MainWindow", c))
        item = self.tableWidget.item(vert, 3)
        item.setText(_translate("MainWindow",  str(p)))
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())
