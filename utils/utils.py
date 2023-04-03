import functools
import logging
import os
from typing import Any

from PySide6.QtWidgets import QMessageBox, QWidget, QStackedWidget, QGraphicsOpacityEffect
from PySide6.QtCore import QEasingCurve, QPropertyAnimation, QRect

from utils import BASEDIR


# Template de QMessageBox com captions personalizados para botões
class Message(QMessageBox):
    YES = QMessageBox.StandardButton.Yes
    NO = QMessageBox.StandardButton.No

    def __init__(
            self,
            parent=None,
            buttons: list[tuple[QMessageBox.StandardButton, str]] | None = None,
    ):
        super().__init__(parent)

        if buttons:
            self.set_caption_buttons(buttons)

    # Cria e executa uma message box de aviso com botões de Sim e Não
    @classmethod
    def warning_question(cls, parent, message: str, default_button=QMessageBox.StandardButton.No) -> int:
        buttons = [(QMessageBox.StandardButton.Yes, 'Sim'), (QMessageBox.StandardButton.No, 'Não')]

        self = cls(parent, buttons)
        answer = self.show_message(
            'ATENÇÃO',
            message,
            QMessageBox.Icon.Warning,
            default_button
        )

        return answer

    # Executa MessageBox
    def show_message(
            self,
            title: str,
            message: str,
            icon: QMessageBox.Icon | None = None,
            default_button: QMessageBox.StandardButton | None = None
    ) -> int:
        self.setWindowTitle(title)
        self.setText(message)
        self.setIcon(icon)
        self.setDefaultButton(default_button)

        return super().exec()

    # Seta captions personalizados
    def set_caption_buttons(self, buttons: list[tuple[QMessageBox.StandardButton, str]]):
        b = functools.reduce(lambda b, button: b | button[0], buttons, 0)
        self.setStandardButtons(b)

        for button, caption in buttons:
            self.button(button).setText(caption)


# noinspection PyUnresolvedReferences
class Animation:
    def __init__(self):
        self._animation: QPropertyAnimation | None = None

    def _setup(
            self,
            widget: QWidget,
            property_name: bytes,
            start: Any,
            end: Any,
            duration: int = 300,
            easing_curve: QEasingCurve = QEasingCurve.Type.Linear
    ):
        self._animation = QPropertyAnimation(widget, property_name)
        self._animation.setDuration(duration)
        self._animation.setStartValue(start)
        self._animation.setEndValue(end)
        self._animation.setEasingCurve(easing_curve)
        self._animation.finished.connect(self._clear)

    def _clear(self):
        self._animation.deleteLater()
        self._animation = None

    def start(self, policy: QPropertyAnimation.DeletionPolicy = QPropertyAnimation.DeletionPolicy.DeleteWhenStopped):
        if self._animation:
            self._animation.start(policy)

    def fade_in(self, stacked_widget: QStackedWidget, index: int):
        if stacked_widget.currentIndex() == index:
            return

        new_page = stacked_widget.widget(index)
        stacked_widget.setCurrentIndex(index)

        opacity_effect = QGraphicsOpacityEffect(stacked_widget.parent())
        new_page.setGraphicsEffect(opacity_effect)

        self._setup(
            widget=opacity_effect,
            property_name=b'opacity',
            start=0,
            end=1,
            duration=250,
            easing_curve=QEasingCurve.Type.InQuad
        )

        self.start()

    def slide(self, stacked_widget: QStackedWidget, index: int):
        if stacked_widget.currentIndex() == index:
            return

        stacked_widget.setCurrentIndex(index)
        widget = stacked_widget.currentWidget()

        self._setup(
            widget=widget,
            property_name=b'geometry',
            start=QRect(0, stacked_widget.height(), widget.width(), widget.height()),
            end=QRect(0, widget.y(), widget.width(), widget.height()),
            duration=500,
            easing_curve=QEasingCurve.Type.OutBack
        )

        self.start()

    def open_popup(self, popup: QWidget):
        rect = popup.geometry()

        self._setup(
            widget=popup,
            property_name=b'geometry',
            start=QRect(rect.x(), rect.y(), rect.width(), 1),
            end=QRect(rect.x(), rect.y(), rect.width(), rect.height()),
            duration=250,
            easing_curve=QEasingCurve.Type.InCirc
        )

        self.start()


class Logger(logging.Logger):
    def __init__(self, name=__name__):
        super().__init__(name)

        self.setLevel(logging.WARNING)

        log_file = os.path.join(BASEDIR, 'LOG.log')

        handler = logging.FileHandler(log_file, mode='a')
        formatter = logging.Formatter('%(asctime)s | %(message)s', datefmt='%d/%m/%y %H:%M:%S')

        handler.setFormatter(formatter)

        self.addHandler(handler)
