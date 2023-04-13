from PySide6.QtWidgets import QDialog

from ui.LicenseDialog import Ui_Dialog


class LicenseDialog(QDialog, Ui_Dialog):
    """Diálogo para exibir licença."""

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
