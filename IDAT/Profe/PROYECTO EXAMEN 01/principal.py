from PyQt5 import QtWidgets, uic
import sys , os
from PyQt5.QtWidgets import QApplication, QMainWindow
arreglo = []  
class Persona():   
    def __init__(self):         
        self.id = 0         
        self.nombre = ""         
        self.edad   = 0    
    
    def ingresar():      
        arreglo.append(Persona())     
        return arreglo
#####################CABEZERA

class MainWindow(QtWidgets.QMainWindow, Ui_LOGIN):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
"""class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "login.ui"), self)"""
#####################LOGIN

        self.btn_aceptar.clicked.connect(self.validar)
        self.btn_cerrar.clicked.connect(self.salir)
    
    def salir(self):
        self.close()

    def validar(self):
        usu = self.txt_n1.text()
        pas = self.txt_n2.text()

        if usu !='idat' and pas !='123':
            self.txt_n1.setText('')
            self.txt_n2.setText('')
        else:
            self.txt_n1.setText('')
            self.txt_n2.setText('')

#####################TERMINO DEL LOGIN

#####################SALTO A VENTANA MENU
            self.hide()

            vent2=Ui_vent_menu()
            vent2.show()

#####################VENTANA MENU

class Ui_vent_menu(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_vent_menu, self).__init__(parent)
        loadUi('PROYECTO EXAMEN 01/menu.ui', self)
"""class Ui_vent_menu(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_vent_menu, self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "menu.ui"), self)"""
        
        self.btn_clientes.clicked.connect(self.abrirclientes)
        self.btn_clientesEmpresa.clicked.connect(self.abrirempresas)#1
        self.btn_detalleVenta.clicked.connect(self.abrirdetallev)#2
        self.btn_documentoVenta.clicked.connect(self.abrirdocventas)#3 
        self.btn_empleados.clicked.connect(self.abrirvempleados)#4  
        self.btn_productos.clicked.connect(self.vproductos)#5                
        self.btn_cerrar.clicked.connect(self.cerrarmenu)

    def abrirclientes(self):
        self.hide()
        vent3 = Ui_vent_clientes(self.parent())  
        vent3.show()

    def abrirempresas(self):#1
        self.hide()#1
        vent3 = Ui_clientesEmpresa(self.parent())  #1
        vent3.show()#1

    def abrirdetallev(self):#2
        self.hide()#2
        vent3 = Ui_detalleVenta(self.parent())  #2
        vent3.show()#2       

    def abrirdocventas(self):#3
        self.hide()#3
        vent3 = Ui_documentoVenta(self.parent())  #3
        vent3.show()#3 

    def abrirvempleados(self):#4
        self.hide()#4
        vent3 = Ui_empleados(self.parent())  #4
        vent3.show()#4 

    def vproductos(self):#5
        self.hide()#5
        vent3 = Ui_vproductos(self.parent())  #5
        vent3.show()#5 


    def cerrarmenu(self):
        self.parent().show()
        self.close() 

#####################SALTO VENTANA "1" CLIENTES

        self.hide()

        vent2=Ui_vent_menu(self)#1
        vent2.show()    

#####################VENTANA CLIENTES
class Ui_vent_clientes(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_vent_clientes, self).__init__(parent)
        loadUi('PROYECTO EXAMEN 01/clientes.ui', self)
        
"""class Ui_vent_clientes(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_vent_clientes, self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "clientes.ui"), self)"""
        
        self.btn_registrar.clicked.connect(self.contador)
        self.btn_cerrar.clicked.connect(self.volvermenu)

    def contador(self):

        dni = self.txt_n1.text()
        nombre = self.txt_n2.text()
        apaterno = self.txt_n3.text()
        amaterno = self.txt_n4.text()
        direc = self.txt_n5.text()
        tele= self.txt_n6.text()

        contador = int(self.txt_contador.text())

        empleados = Persona.ingresar()
   
        empleados[contador].dni = dni   
        empleados[contador].nombre = nombre   
        empleados[contador].apaterno   = apaterno  
        empleados[contador].amaterno =amaterno 
        empleados[contador].direc = direc  
        empleados[contador].tele   = tele
        
        self.listar.clear()
        self.listar.append("dni         nombre       apaterno       amaterno       direc       tele")

        x = 0
        while x <= contador:
            self.listar.append(empleados[x].dni+"         "+empleados[x].nombre+"      "+empleados[x].apaterno+"      "+empleados[x].amaterno+"      "+empleados[x].direc+"      "+empleados[x].tele )
            x = x+1
            
        contador = contador + 1
        self.txt_contador.setText(str(contador))
        
        
        self.txt_n1.setText("")
        self.txt_n2.setText("")
        self.txt_n3.setText("")
        self.txt_n4.setText("")
        self.txt_n5.setText("")
        self.txt_n6.setText("")        

    def volvermenu (self):

        self.hide()
        vent2=Ui_vent_menu(self)
        vent2.show()

#####################VENTANA CLIENTE EMPRESA

class Ui_clientesEmpresa(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_clientesEmpresa, self).__init__(parent)
        loadUi('PROYECTO EXAMEN 01/empresa.ui', self)
"""class Ui_clientesEmpresa(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_clientesEmpresa, self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "empresa.ui"), self)"""
        
        self.btn_registrar.clicked.connect(self.contador)
        self.btn_cerrar.clicked.connect(self.volvermenu)

    def contador(self):

        ruc = self.rucCE.text()
        rsocial = self.razonSocialCE.text()
        direc = self.direccionCE.text()
        telefono = self.telefonoCE.text()


        contador = int(self.txt_contador.text())

        empleados = Persona.ingresar()     
   
        empleados[contador].ruc = ruc   
        empleados[contador].rsocial = rsocial   
        empleados[contador].direc   = direc  
        empleados[contador].telefono =telefono 

        self.listar.clear()
        self.listar.append("ruc         rsocial       direc       telefono")

        x = 0
        while x <= contador:
            self.listar.append(empleados[x].ruc+"         "+empleados[x].rsocial+"      "+empleados[x].direc+"      "+empleados[x].telefono )
            x = x+1
            
        contador = contador + 1
        self.txt_contador.setText(str(contador))
        
        
        self.rucCE.setText("")
        self.razonSocialCE.setText("")
        self.direccionCE.setText("")
        self.telefonoCE.setText("")
      

    def volvermenu (self):

        self.hide()
        vent2=Ui_vent_menu(self)
        vent2.show()

    def volvermenu (self):

        self.hide()
        vent2=Ui_vent_menu(self)
        vent2.show()

#####################VENTANA DETALLE DE VENTA

"""class Ui_detalleVenta(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_detalleVenta, self).__init__(parent)
        loadUi('PROYECTO EXAMEN 01/detallev.ui', self)"""
class Ui_detalleVenta(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_detalleVenta, self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "detallev.ui"), self)
        
        self.b_calcular.clicked.connect(self.registar)
        self.b_limpiar.clicked.connect(self.limpiar) 
        self.btn_cerrar.clicked.connect(self.volvermenu)

    def registar (self):
        ruc=self.txt_nDocumentoVenta.text()
        item=self.txt_nItem.text()
        cproducto=self.txt_codigoProducto.text()
        pventa=self.txt_precioVenta.text() 
        cantidad=self.txt_cantidad.text()

        self.mostrar_ruc.setText(str(ruc))
        self.mostrar_itemproducto.setText(str(item))
        self.mostrar_codigoproducto.setText(str(cproducto))
        self.label_37.setText(str(pventa))   
        self.label_36.setText(str(cantidad))  

    def limpiar(self):
        self.txt_nDocumentoVenta.clear()
        self.txt_nItem.clear()
        self.txt_codigoProducto.clear()
        self.txt_precioVenta.clear()
        self.txt_cantidad.clear()
        self.mostrar_ruc.setText("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _") 
        self.mostrar_itemproducto.setText("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _") 
        self.mostrar_codigoproducto.setText("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _") 
        self.label_37.setText("0")
        self.label_36.setText("0")

    def volvermenu (self):

        self.hide()
        vent2=Ui_vent_menu(self)
        vent2.show()

#####################VENTANA DOCUMENTO DE  VENTA

"""class Ui_documentoVenta(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_documentoVenta, self).__init__(parent)
        loadUi('PROYECTO EXAMEN 01/docventas.ui', self)"""
        
class Ui_documentoVenta(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_documentoVenta, self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "docventas.ui"), self)
        
        self.b_calcular.clicked.connect(self.registar)
        self.b_calcular.clicked.connect(self.calcular)
        self.b_limpiar.clicked.connect(self.limpiar) 
        self.btn_cerrar.clicked.connect(self.volvermenu)

    def registar (self):
        ruc=self.txt_nDocumentoVenta.text()
        producto=self.txt_producto.text()
        fecha=self.txt_fecha.text()
        pventa=self.txt_int_precioUnitario.text() 
        cantidad=self.txt_cantidad.text()        

        self.mostrar_razonSocial.setText(str(ruc))
        self.mostrar_producto.setText(str(producto))
        self.mostrar_fecha.setText(str(fecha))
        self.txt_int_precioUnitario.setText(str(pventa))   
        self.txt_cantidad.setText(str(cantidad))

    def calcular(self):
        cantidad=self.txt_cantidad.text()   
        precioUnd=self.txt_int_precioUnitario.text()

        subtotal=int(cantidad) * int(precioUnd)
        self.precio_subtotal.setText(str(subtotal))
        
        igv= float(subtotal) * 0.18
        self.igv.setText(str(igv))

        total=int(subtotal) + float(igv)
        self.total.setText(str(total))     

    def limpiar(self):
        self.txt_nDocumentoVenta.clear()
        self.txt_producto.clear()
        self.txt_fecha.clear()
        self.txt_int_precioUnitario.clear()
        self.txt_cantidad.clear()
        self.mostrar_razonSocial.setText("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _") 
        self.mostrar_producto.setText("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _") 
        self.mostrar_fecha.setText("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _") 
        self.precio_subtotal.setText("0")
        self.igv.setText("0")
        self.total.setText("0")

    def volvermenu (self):

        self.hide()
        vent2=Ui_vent_menu(self)
        vent2.show()

#####################VENTANA EMPLEADOS

"""class Ui_empleados(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_empleados, self).__init__(parent)
        loadUi('PROYECTO EXAMEN 01/vempleados.ui', self)"""
class Ui_empleados(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_empleados, self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "vempleados.ui"), self)
        
        self.b_calcular.clicked.connect(self.registar)
        self.b_limpiar.clicked.connect(self.limpiar) 
        self.btn_cerrar.clicked.connect(self.volvermenu)

    def registar (self):
       # nombres=self.txt_nombres.text()
        #apaterno=self.txt_apellidoPETERNO.text()
        #amaterno=self.txt_apellidoMATERNO.text()
        #direccion=self.txt_direccion.text()
       # telefono=self.txt_telefono.text()      

       # self.mostrar_nombres.setText(str(nombres))
       # self.mostrar_papa.setText(str(apaterno))
       # self.mostrar_mama.setText(str(amaterno))       
        #self.mostrar_direcccion.setText(str(direccion))
       # self.mostrar_telefono.setText(str(telefono))   



        nombre = self.txt_nombres.text()
        apellidoP = self.txt_apellidoPETERNO.text()
        apellidoM = self.txt_apellidoMATERNO.text()
        direccion = self.txt_direccion.text()
        telefono = self.txt_telefono.text()        


        contador = int(self.txt_contador.text())

        empleados = Persona.ingresar()     
   
        empleados[contador].nombre = nombre   
        empleados[contador].apellidoP = apellidoP 
        empleados[contador].apellidoM = apellidoM  
        empleados[contador].direccion   = direccion  
        empleados[contador].telefono =telefono 

        self.listar.clear()
        self.listar.append("nombre         apellidoP       apellidoM       direccion       telefono")

        x = 0
        while x <= contador:
            self.listar.append(empleados[x].nombre+"         "+empleados[x].apellidoP+"      "+empleados[x].apellidoM+"      "+empleados[x].direccion+"      "+empleados[x].telefono )
            x = x+1
            
        contador = contador + 1
        self.txt_contador.setText(str(contador))
        
        
        self.txt_nombres.setText("")
        self.txt_apellidoPETERNO.setText("")
        self.txt_apellidoMATERNO.setText("")
        self.txt_direccion.setText("")
        self.txt_telefono.setText("")     


    def limpiar(self):

        self.txt_nombres.clear()
        self.txt_apellidoPETERNO.clear()  
        self.txt_apellidoMATERNO.clear()
        self.txt_direccion.clear()  
        self.txt_telefono.clear()          
        self.mostrar_nombres.setText("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
        self.mostrar_papa.setText("_ _ _ _ _ _ _ _")
        self.mostrar_mama.setText("_ _ _ _ _ _ _ _")
        self.mostrar_direcccion.setText("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
        self.mostrar_telefono.setText("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")       

    def volvermenu (self):

        self.hide()
        vent2=Ui_vent_menu(self)
        vent2.show()

"""class Ui_vproductos(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_vproductos, self).__init__(parent)
        loadUi('PROYECTO EXAMEN 01/vproductos.ui', self)"""
class Ui_vproductos(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_vproductos, self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "vproductos.ui"), self)
        
        self.btn_cerrar.clicked.connect(self.volvermenu)

    def volvermenu (self):

        self.hide()
        vent2=Ui_vent_menu(self)
        vent2.show()        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()



