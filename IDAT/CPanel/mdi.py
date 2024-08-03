import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QTextEdit, QAction

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        mdi = QMdiArea()
        self.setCentralWidget(mdi)

        # Crear acciones para abrir y cerrar ventanas secundarias
        abrir_action = QAction('Abrir Ventana', self)
        abrir_action.triggered.connect(self.abrirVentana)

        cerrar_action = QAction('Cerrar Ventana', self)
        cerrar_action.triggered.connect(self.cerrarVentana)

        # Crear menú de ventanas
        ventanas_menu = self.menuBar().addMenu('Ventanas')
        ventanas_menu.addAction(abrir_action)
        ventanas_menu.addAction(cerrar_action)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('MDI con PyQt5')
        self.show()

    def abrirVentana(self):
        subventana = QMdiSubWindow()
        subventana.setWidget(QTextEdit())
        self.centralWidget().addSubWindow(subventana)
        subventana.show()

    def cerrarVentana(self):
        subventana_actual = self.centralWidget().currentSubWindow()
        if subventana_actual:
            subventana_actual.close()

def main():
    app = QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
