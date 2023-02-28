from PySide6.QtWidgets import QDialog, QComboBox
from PySide6.QtCore import QDate, QPoint, Qt, QEvent

from ui.CalendarDialog import Ui_Dialog


# Diálogo para escolher datas atráves de uma interface
class CalendarDialog(QDialog, Ui_Dialog):
    def __init__(self, parent, txt_parent):
        super().__init__(parent)
        self.setupUi(self)

        self.txt_parent: QComboBox = txt_parent

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        point = self.txt_parent.mapToGlobal(QPoint(0, 0))
        self.setGeometry(point.x(), point.y() + self.txt_parent.height(), 250, 100)

        self.calendar.clicked.connect(self.show_date)

    # Seta data ao txt vinculado a classe e encerra o diálogo
    def show_date(self, date: QDate):
        self.txt_parent.lineEdit().setText(date.toString('dd/MM/yyyy'))
        self.close()

    def changeEvent(self, event: QEvent) -> None:
        if not self.isActiveWindow():
            self.close()
