from PySide6.QtWidgets import QDialog

from ui.LicenseDialog import Ui_Dialog


class LicenseDialog(QDialog, Ui_Dialog):
    """Diálogo para exibir licença."""

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

        self.txt_license.setMarkdown(
            "**Programming Language**  "
            "Python  "
            "**3rd Party Libs**  "
            "PySide6  "
            "PyQtDarkTheme  "
            "AutoPyToExe  "
            "**Icons**  "
            "Icons8 - [https://icons8.com.br](https://icons8.com.br)"
        )
