from PyQt5 import QtWidgets, uic
import pyodbc
from Vista.conexion import *

def tablaPorEspecialidad(index , especialidad):
    print('Index del combo es ====== ', index)
    if index == 0:
        index = "select * from alumno"
    else:
        index = f"select * from alumno where especialidad = '{especialidad}'"
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    cursor.execute(index)
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return rows


def tablaAlumnos(codigo):
    
    conn = pyodbc.connect(conexion())
    cursor = conn.cursor()
    cursor.execute(f"select a.id_alu ,a.nombre,apellido,a.especialidad,r.curso,r.exa_par_2,r.exa_final_4,r.promedio,r.condicion from registros r inner join alumno  a on  a.id_alu = r.id_alu where a.id_alu = {codigo}")
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return rows


class VentanaAlumnos(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaAlumnos,self).__init__(parent)
        #self.setWindowIcon(QtGui.QIcon("UI/imagenes/venta.png"))
        uic.loadUi("UI/VistaAlumno.ui",self)
        self.cargar()
        self.btnBuscarEspecialidad.clicked.connect(self.buscarEspecialidad)
        self.btnBuscarAlumno.clicked.connect(self.buscarAlumno)
    
    def buscarEspecialidad(self):
        self.cargar()
        
    
    def cargar(self):
        index = self.comboEspecialidad.currentIndex()
        espec = self.comboEspecialidad.currentText()
        
        listado = tablaPorEspecialidad(index,espec)
        
        self.tbl_alumno.setRowCount(len(listado))
        i = 0
        for alumno in listado:
            self.tbl_alumno.setItem(i, 0, QtWidgets.QTableWidgetItem(alumno[1]))
            self.tbl_alumno.setItem(i, 1, QtWidgets.QTableWidgetItem(alumno[2]))
            self.tbl_alumno.setItem(i, 2, QtWidgets.QTableWidgetItem(alumno[3]))
            self.tbl_alumno.setItem(i, 3, QtWidgets.QTableWidgetItem(alumno[4]))
            i += 1
        
        #select * from alumno where especialidad = 'Sistemas'
    
    def buscarAlumno(self):
        #try:
        idAlunmo = self.txtCodigo.text()
        
        listas = tablaAlumnos(idAlunmo)
    
        self.tblNotas.setRowCount(len(listas))
        i = 0
        for lista in listas:
            nombre = " " + lista[1] + " " + lista[2]
            self.txtNombre.setText(nombre)
            self.txtEspecialidad.setText(" " + lista[3])
        
            self.tblNotas.setItem(i, 0, QtWidgets.QTableWidgetItem(lista[4]))
            self.tblNotas.setItem(i, 1, QtWidgets.QTableWidgetItem(str(lista[5])))
            self.tblNotas.setItem(i, 2, QtWidgets.QTableWidgetItem(str(lista[6])))
            self.tblNotas.setItem(i, 3, QtWidgets.QTableWidgetItem(str(lista[7])))
            self.tblNotas.setItem(i, 4, QtWidgets.QTableWidgetItem(lista[8]))
            i += 1
            #self.txtEspecialidad.setText(lista[3])
        
        #except:
        #    QtWidgets.QMessageBox.information(self, "Busqueda de Alumno", "Codigo de Alumno no encontrado", QtWidgets.QMessageBox.Ok)
