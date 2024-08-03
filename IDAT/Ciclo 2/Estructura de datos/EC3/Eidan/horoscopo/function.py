
from PyQt5 import QtWidgets, uic
import sys , os

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "horoscopo.ui"), self)
        self.ver_signo.clicked.connect(self.mostrar_signo)
   
    def mostrar_signo(self):
        combo_mes = self.mes.currentText()
        select_dia = int(self.dia.text())

        if combo_mes == 'Marzo' and select_dia > 20 or  combo_mes == 'Abril' and  select_dia < 20: #Aries: del 21 de marzo al 19 de abril.
            self.rstl.setText("Aries")
        elif combo_mes == 'Abril' and select_dia >= 20 or  combo_mes == 'Mayo' and  select_dia <= 20: #Tauro: del 20 de abril al 20 de mayo.
            self.rstl.setText("Tauro")
        elif combo_mes == 'Mayo' and select_dia >= 21 or  combo_mes == 'Junio' and  select_dia <= 20: #Géminis: del 21 de mayo al 20 de junio.
            self.rstl.setText("Géminis")
        elif combo_mes == 'Junio' and select_dia >= 21 or  combo_mes == 'Julio' and  select_dia <= 22: #Cáncer: del 21 de junio al 22 de julio.
            self.rstl.setText("Cáncer")
        elif combo_mes == 'Julio' and select_dia >= 23 or  combo_mes == 'Agosto' and  select_dia <= 22: #Leo: del 23 de julio al 22 de agosto.
            self.rstl.setText("Leo")
        elif combo_mes == 'Agosto' and select_dia >= 23 or  combo_mes == 'Septiembre' and  select_dia <= 22: #Virgo: del 23 de agosto al 22 de septiembre.
            self.rstl.setText("Virgo")
        elif combo_mes == 'Septiembre' and select_dia >= 23 or  combo_mes == 'Octubre' and  select_dia <= 22: #Libra: del 23 de septiembre al 22 de octubre.
            self.rstl.setText("Libra")
        elif combo_mes == 'Octubre' and select_dia >= 23 or  combo_mes == 'Noviembre' and  select_dia <= 21: #Escorpio: del 23 de octubre al 21 de noviembre.
            self.rstl.setText("Escorpio")
        elif combo_mes == 'Noviembre' and select_dia >= 23 or  combo_mes == 'Diciembre' and  select_dia <= 22: #Sagitario: del 22 de noviembre al 21 de diciembre.
            self.rstl.setText("Sagitario")
        elif combo_mes == 'Diciembre' and select_dia >= 23 or  combo_mes == 'Enero' and  select_dia <= 19: #Capricornio: del 22 de diciembre al 19 de enero.
            self.rstl.setText("Capricornio")
        elif combo_mes == 'Enero' and select_dia >= 23 or  combo_mes == 'Febrero' and  select_dia <= 18: #Acuario: del 20 de enero al 18 de febrero.
            self.rstl.setText("Acuario")
        elif combo_mes == 'Febrero' and select_dia >= 23 or  combo_mes == 'Marzo' and  select_dia <= 22: #Piscis: del 19 de febrero al 20 de marzo.
            self.rstl.setText("Piscis")
                    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())
