
from PyQt5 import QtWidgets, uic, QtCore
import sys , os , subprocess 

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "destino.ui"), self)
        
        self.linkkk.clicked.connect(self.execute_python_file)
    def execute_python_file(self):
        #sys.exit(app.exec_())
        #Aqui se extrae el archivo del mismo directorio donde se encuentran ambos archivos py
        ui_path = os.path.dirname(os.path.abspath(__file__))
        
        #Aqui se concatena el archivo python function.py con el extraido en ui_path
        file_path = ui_path + '/function.py'
        
        #Aqui se hace el llamado ejecutando con la funcion run  que necesita parametros
        subprocess.run(['python', file_path], capture_output=True, text=True)
        
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())
