from PyQt5 import QtWidgets
from Controlador.producto import *
from Controlador.funciones import *

f = C_producto()

class VentanaProducto(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaProducto,self).__init__(parent)
        func_Favicon(self,"venta.png")
        cargarUI("UI/V_2Productos.ui", self)
        self.container_btn_indice_0()
        self.container_btn_indice_1()
    
    def container_btn_indice_0(self):
        #self.btn_indice(self.btnBuscar,1) 
        btn_action(self.btnEliminar,lambda: self.link_ir_a(1))
        btn_action(self.btnBackMenu,lambda: self.close())
        
    def container_btn_indice_1(self):
        btn_action(self.btnCancelarDelete,self.CancelarEliminar)
        
    def CancelarEliminar(self):
        self.link_ir_a(0)
    
    def link_ir_a(self,num):
        self.stackedWidget.setCurrentIndex(num)
        
    def btn_indice(self,boton,num):
        return boton.clicked.connect(lambda: self.link_ir_a(num))
    
    #FUNCIONES DE BOTONES LATERALES
        
    def cancelar_index_1(self):
        func_limpiarInputs(self.All_Input_Indice_1())
        func_limpiarCombos(self.All_Combo_Indice_1())
        self.link_ir_a(0)

    #FUNCIONES DE CARGA
    def cargarTabla(self):
        func_tblDatos(f.tablaProducto(),self.tblUsuario)
        
    def All_Input_Indice_1(self):
        inputs = [self.inputNombre,self.inputCodigo,self.inputCantidad,self.inputPrecio]
        return inputs
    
    def All_Combo_Indice_1(self):
        combos = [self.inputAlmacen,self.inputCategoria,self.inputEstado,self.inputProveedor]
        return combos
    