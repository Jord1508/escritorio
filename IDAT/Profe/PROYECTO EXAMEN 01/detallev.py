# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detallev.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_detalleVenta(object):
    def setupUi(self, detalleVenta):
        detalleVenta.setObjectName("detalleVenta")
        detalleVenta.resize(404, 506)
        font = QtGui.QFont()
        font.setPointSize(10)
        detalleVenta.setFont(font)
        self.centralwidget = QtWidgets.QWidget(detalleVenta)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(60, 10, 301, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 151, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 121, 16))
        self.label_4.setObjectName("label_4")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(10, 40, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 111, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 190, 111, 16))
        self.label_6.setObjectName("label_6")
        self.txt_nDocumentoVenta = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_nDocumentoVenta.setGeometry(QtCore.QRect(210, 70, 141, 20))
        self.txt_nDocumentoVenta.setObjectName("txt_nDocumentoVenta")
        self.txt_nItem = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_nItem.setGeometry(QtCore.QRect(210, 100, 141, 20))
        self.txt_nItem.setObjectName("txt_nItem")
        self.txt_codigoProducto = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_codigoProducto.setGeometry(QtCore.QRect(210, 130, 141, 20))
        self.txt_codigoProducto.setObjectName("txt_codigoProducto")
        self.txt_precioVenta = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_precioVenta.setGeometry(QtCore.QRect(210, 160, 141, 20))
        self.txt_precioVenta.setObjectName("txt_precioVenta")
        self.txt_cantidad = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_cantidad.setGeometry(QtCore.QRect(210, 190, 141, 20))
        self.txt_cantidad.setObjectName("txt_cantidad")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 220, 351, 20))
        self.line_3.setLineWidth(5)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(10, 260, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 290, 151, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 320, 61, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 350, 121, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 380, 121, 16))
        self.label_10.setObjectName("label_10")
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setGeometry(QtCore.QRect(110, 380, 31, 16))
        self.label_37.setObjectName("label_37")
        self.mostrar_ruc = QtWidgets.QLabel(self.centralwidget)
        self.mostrar_ruc.setGeometry(QtCore.QRect(200, 290, 161, 20))
        self.mostrar_ruc.setObjectName("mostrar_ruc")
        self.mostrar_itemproducto = QtWidgets.QLabel(self.centralwidget)
        self.mostrar_itemproducto.setGeometry(QtCore.QRect(200, 320, 161, 20))
        self.mostrar_itemproducto.setObjectName("mostrar_itemproducto")
        self.mostrar_codigoproducto = QtWidgets.QLabel(self.centralwidget)
        self.mostrar_codigoproducto.setGeometry(QtCore.QRect(200, 350, 161, 20))
        self.mostrar_codigoproducto.setObjectName("mostrar_codigoproducto")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(160, 380, 51, 16))
        self.label_11.setObjectName("label_11")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(240, 380, 31, 16))
        self.label_36.setObjectName("label_36")
        self.b_limpiar = QtWidgets.QPushButton(self.centralwidget)
        self.b_limpiar.setGeometry(QtCore.QRect(30, 410, 93, 28))
        self.b_limpiar.setObjectName("b_limpiar")
        self.b_calcular = QtWidgets.QPushButton(self.centralwidget)
        self.b_calcular.setGeometry(QtCore.QRect(150, 410, 93, 28))
        self.b_calcular.setObjectName("b_calcular")
        self.btn_cerrar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cerrar.setGeometry(QtCore.QRect(270, 410, 93, 28))
        self.btn_cerrar.setObjectName("btn_cerrar")
        detalleVenta.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(detalleVenta)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 404, 23))
        self.menubar.setObjectName("menubar")
        detalleVenta.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(detalleVenta)
        self.statusbar.setObjectName("statusbar")
        detalleVenta.setStatusBar(self.statusbar)

        self.retranslateUi(detalleVenta)
        QtCore.QMetaObject.connectSlotsByName(detalleVenta)

    def retranslateUi(self, detalleVenta):
        _translate = QtCore.QCoreApplication.translate
        detalleVenta.setWindowTitle(_translate("detalleVenta", "MainWindow"))
        self.label_1.setText(_translate("detalleVenta", "VENTANA DETALLE DE VENTA"))
        self.label_2.setText(_translate("detalleVenta", "Documento de venta RUC."))
        self.label_3.setText(_translate("detalleVenta", "Item"))
        self.label_4.setText(_translate("detalleVenta", "Codigo del producto"))
        self.label_19.setText(_translate("detalleVenta", "Ingrese datos :"))
        self.label_5.setText(_translate("detalleVenta", "Precio de venta"))
        self.label_6.setText(_translate("detalleVenta", "Cantidad"))
        self.label_20.setText(_translate("detalleVenta", "Detalles de venta :"))
        self.label_7.setText(_translate("detalleVenta", "Nombre ó Razon Social :"))
        self.label_8.setText(_translate("detalleVenta", "Producto"))
        self.label_9.setText(_translate("detalleVenta", "Codigo del Producto"))
        self.label_10.setText(_translate("detalleVenta", "Precio :    s/"))
        self.label_37.setText(_translate("detalleVenta", "0"))
        self.mostrar_ruc.setText(_translate("detalleVenta", "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"))
        self.mostrar_itemproducto.setText(_translate("detalleVenta", "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"))
        self.mostrar_codigoproducto.setText(_translate("detalleVenta", "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"))
        self.label_11.setText(_translate("detalleVenta", "Cantidad :"))
        self.label_36.setText(_translate("detalleVenta", "0"))
        self.b_limpiar.setText(_translate("detalleVenta", "LIMPIAR"))
        self.b_calcular.setText(_translate("detalleVenta", "REGISTRAR"))
        self.btn_cerrar.setText(_translate("detalleVenta", "CERRAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    detalleVenta = QtWidgets.QMainWindow()
    ui = Ui_detalleVenta()
    ui.setupUi(detalleVenta)
    detalleVenta.show()
    sys.exit(app.exec_())
