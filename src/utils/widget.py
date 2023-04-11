from PySide6.QtWidgets import QComboBox, QStackedWidget, QTableWidget, QGraphicsOpacityEffect
from PySide6.QtCore import QEasingCurve, QRect

from utils import CalendarDialog, TableWidgetHandler, Animation


class CustomComboBox(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)

        self.animation: Animation | None = None
        self.popup: CalendarDialog | None = None

    def showPopup(self):
        self.popup = CalendarDialog(self.parent(), self)
        self.popup.show()

        geo = self.popup.geometry()

        self.animation = Animation(
            widget=self.popup,
            property_name=b'geometry',
            start=QRect(geo.x(), geo.y(), geo.width(), 1),
            end=QRect(geo.x(), geo.y(), geo.width(), geo.height()),
            duration=250,
            easing_curve=QEasingCurve.Type.InCirc
        )


class CustomStackedWidget(QStackedWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.animation: Animation | None = None

    def setCurrentIndex(self, index: int):
        if index == self.currentIndex():
            return

        super().setCurrentIndex(index)

        widget = self.currentWidget()
        opacity_effect = QGraphicsOpacityEffect(self)
        widget.setGraphicsEffect(opacity_effect)

        self.animation = Animation(
            widget=opacity_effect,
            property_name=b'opacity',
            start=0,
            end=1,
            duration=250,
            easing_curve=QEasingCurve.Type.InQuad
        )


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
