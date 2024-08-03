#!/usr/bin/python
# -*- coding: utf-8 -*-

# www.pythondiario.com
# Combinar 2 ComboBox

from PyQt5 import QtWidgets, uic
import sys , os
# Cargar nuestro archivo .ui
 
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))        
        uic.loadUi(os.path.join(ui_path, "combobox.ui"), self)
        
        self.comboBox.currentTextChanged.connect(self.llenar_comboBox2)
        #Rellana los datos por primera ves del comboBox_2
        #self.llenar_comboBox2()
        #Señal para cambiar, segun la selecccion, el comboBox_2
        #QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL("currentIndexChanged(QString)"), self.llenar_comboBox2)   
        self.btn_ver.clicked.connect(self.btn_Ver_clicked)

 # Evento del boton Ver
    def btn_Ver_clicked(self):

        x = self.comboBox_2.currentText()
        self.Resultado.setText(x)

    # Llena el comboBox_2
    def llenar_comboBox2(self):

        python = ["Diego", "Martin", "Lorena"]
        java = ["Sergio", "Maria", "Miguel"]

        self.comboBox_2.clear()
        if self.comboBox.currentText() == "Python":
            self.comboBox_2.addItems(python)
        elif self.comboBox.currentText() == "Java":
            self.comboBox_2.addItems(java)                                           

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())

