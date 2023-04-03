from PySide6.QtWidgets import QDialog, QComboBox
from PySide6.QtCore import QPoint, QEvent, Qt
from PySide6.QtGui import QAction

from ui.CalendarDialog import Ui_Dialog


# Diálogo para escolher datas atráves de uma interface
class CalendarDialog(QDialog, Ui_Dialog):
    def __init__(self, parent, txt_parent):
        super().__init__(parent)
        self.setupUi(self)

        self.txt_parent: QComboBox = txt_parent

        # Remove cabeçalho da janela
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        # Seta a posição do popup relativo ao txt_parent
        point = self.txt_parent.mapToGlobal(QPoint(0, 0))
        self.setGeometry(point.x(), point.y() + self.txt_parent.height(), 275, 192)

        # Vincula handle ao evento click
        self.calendar.clicked.connect(self.show_date)

        # Cria action e seta shortcuts do teclado
        shortcut = QAction('shortcut', self)
        shortcut.setShortcuts(['enter', 'return', 'space'])
        shortcut.triggered.connect(self.show_date)

        # Seta action ao diálogo
        self.addAction(shortcut)

    # Seta data ao txt vinculado a classe e encerra o diálogo
    def show_date(self):
        date = self.calendar.selectedDate()

        self.txt_parent.lineEdit().setText(date.toString('dd/MM/yyyy'))
        self.close()

    # Fecha diálogo caso perca o foco
    def changeEvent(self, event: QEvent) -> None:
        if not self.isActiveWindow():
            self.close()
