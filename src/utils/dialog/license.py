from PySide6.QtWidgets import QDialog

from src.ui.LicenseDialog import Ui_Dialog


class LicenseDialog(QDialog, Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle('LICENÇA')
