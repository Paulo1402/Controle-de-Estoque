from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QCloseEvent

from ui.SkidsConfigDialog import Ui_Dialog
from utils import Message, get_config, set_config, ConfigSection, DEFAULT_SHORT_SKIDS, DEFAULT_LONG_SKIDS
from services import DatabaseConnection


class SkidsConfigDialog(QDialog, Ui_Dialog):
    """Diálogo para configurar skids."""

    def __init__(self, parent, database: DatabaseConnection):
        super().__init__(parent)
        self.setupUi(self)

        self.database = database

        self.config = get_config(ConfigSection.APP)

        short_skids = self.config['short_skids']
        long_skids = self.config['long_skids']

        self.txt_short_skids.setText(str(short_skids))
        self.txt_long_skids.setText(str(long_skids))

        self.bt_reset.clicked.connect(self.reset)

    def closeEvent(self, event: QCloseEvent):
        """Salva configurações ao fechar caixa de diálogo."""
        short_skids = self.txt_short_skids.text()
        long_skids = self.txt_long_skids.text()

        self.config['short_skids'] = float(short_skids)
        self.config['long_skids'] = float(long_skids)

        set_config(self.config, ConfigSection.APP)

        event.accept()

    def reset(self):
        """Reseta configurações para o padrão."""
        if Message.warning_question(self, 'Deseja resetar as constantes de skids para o padrão?') == Message.NO:
            return

        self.txt_short_skids.setText(str(DEFAULT_SHORT_SKIDS))
        self.txt_long_skids.setText(str(DEFAULT_LONG_SKIDS))
