from PySide6.QtWidgets import QComboBox, QStackedWidget, QTableWidget

from utils import Animation, CalendarDialog, TableWidgetHandler


class CustomComboBox(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)

        self.animation = Animation()
        self.popup = None

    def showPopup(self) -> None:
        self.popup = CalendarDialog(self.parent(), self)
        self.popup.show()

        self.animation.open_popup(self.popup)


class CustomTableWidget(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._handler: TableWidgetHandler | None = None

    @property
    def handler(self):
        return self._handler

    @handler.setter
    def handler(self, value):
        self._handler = value


class CustomStackedWidget(QStackedWidget):
    def __init__(self, parent):
        super().__init__(parent)

    def setCurrentIndex(self, index: int) -> None:
        super().setCurrentIndex(index)