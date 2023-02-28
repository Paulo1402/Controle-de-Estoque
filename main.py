import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

from ui.MainWindow import Ui_MainWindow
from utils import *


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.start_ui()

    def start_ui(self):
        # Conecta botões do menu principal
        self.bt_cycle_menu.clicked.connect(lambda: self.mp_main.setCurrentIndex(0))
        self.bt_nfe_menu.clicked.connect(lambda: self.mp_main.setCurrentIndex(1))
        self.bt_stock_menu.clicked.connect(lambda: self.mp_main.setCurrentIndex(2))
        self.bt_history_menu.clicked.connect(lambda: self.mp_main.setCurrentIndex(3))

        # Conecta botões do menu de histório
        self.bt_cycle_history.clicked.connect(lambda: self.mp_history.setCurrentIndex(0))
        self.bt_nfe_history.clicked.connect(lambda: self.mp_history.setCurrentIndex(2))


# Usado para auxiliar na depuração
def exception_hook(exctype, value, traceback):
    sys.__excepthook__(exctype, value, traceback)
    sys.exit(1)


# Inicia o aplicativo
if __name__ == "__main__":
    # Altera id do aplicativo para evitar bugs com o ícone na barra de tarefas
    try:
        # noinspection PyUnresolvedReferences
        from ctypes import windll

        myappid = 'apps.controle_de_estoque.1.0.0'
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except ImportError:
        pass

    # Desativa splash do pyinstaller quando a aplicação carregar
    try:
        # noinspection PyUnresolvedReferences
        import pyi_splash

        pyi_splash.close()
    except ModuleNotFoundError:
        pass

    # Vincula hook personalizado para receber logs durante desenvolvimento
    sys.excepthook = exception_hook

    qt = QApplication(sys.argv)
    qt.setStyle('Fusion')
    qt.setWindowIcon(QIcon(os.path.join(BASEDIR, 'assets/task-64.png')))

    app = App()
    app.show()

    sys.exit(qt.exec())
