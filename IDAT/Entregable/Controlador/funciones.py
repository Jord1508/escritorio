from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets ,  QtGui
from PyQt5 import uic

def cargarUI(a,b):  
    return uic.loadUi(a,b)

def GoTo(self,indice):
        self.container.setCurrentIndex(indice)
        
def btn_action(boton,funcion):
    return boton.clicked.connect(funcion)

def func_limpiarInputs(cadena):
    for item in cadena:
        item.clear()
        
def func_limpiarCombos(cadena):
    for item in cadena:
        item.setCurrentIndex(0)
        
def func_limpiarLabel(cadena):
    for item in cadena:
        item.setText("")
        
def func_validar_campo_vacios(diccionario):
    for items in diccionario:
        if items.text() == "":
            items.setFocus()
            return "Todos los campos deben estar llenos...!!!"
    else:
        return ""
def func_validar_combo_vacios(diccionario):
    for items in diccionario:
        it = items
        print(it)
        if items.currentIndex() == 0:
            items.setFocus()
            return "Todos los campos deben estar llenos...!!!"
    else:
        return ""
    
def MensajeError(titulo,contexto):
    mensaje = QMessageBox()
    mensaje.setWindowTitle(titulo)
    mensaje.setText(contexto)
    x = mensaje.exec_()
    
def func_QMessageBoxInfoOk(self,titulo,contexto):
    return QMessageBox.information(self, titulo, contexto , QMessageBox.Ok)

def func_ComboValue(comboName,dicionario):       
    etiquet = []    
    for item in dicionario:
        etiquet.append(item[1])
    return comboName.addItems(etiquet)

def f_itemtbl(item,num):
    return QtWidgets.QTableWidgetItem(str(item[num]))

def func_tblDatos(diccionario,tabla):
    tabla.verticalHeader().setVisible(False)
    tabla.setRowCount(len(diccionario))
    filas = 0
    for item in diccionario:
        columna = 0
        while columna < len(item):
            tabla.setItem(filas, columna,f_itemtbl(item,columna))
            columna += 1
        filas += 1

def func_Favicon(self,imagen):
    self.setWindowIcon(QtGui.QIcon(f"UI/imagenes/{imagen}"))