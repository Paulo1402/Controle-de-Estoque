import functools
import logging
import os
from enum import Enum
from typing import Any, NamedTuple

from PySide6.QtCore import QEasingCurve, QPropertyAnimation
from PySide6.QtWidgets import QMessageBox, QWidget

from . import BASEDIR


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
    def __init__(
            self,
            widget: QWidget,
            property_name: bytes,
            start: Any,
            end: Any,
            duration: int = 250,
            easing_curve: QEasingCurve = QEasingCurve.Type.Linear
    ):
        self._animation = QPropertyAnimation(widget, property_name)
        self._animation.setDuration(duration)
        self._animation.setStartValue(start)
        self._animation.setEndValue(end)
        self._animation.setEasingCurve(easing_curve)
        self._animation.finished.connect(self._clear)

        self._animation.start(QPropertyAnimation.DeletionPolicy.DeleteWhenStopped)

    def _clear(self):
        self._animation.deleteLater()
        self._animation = None


class Logger(logging.Logger):
    def __init__(self, name=__name__):
        super().__init__(name)

        self.setLevel(logging.WARNING)

        log_file = os.path.join(BASEDIR, 'LOG.log')
        handler = logging.FileHandler(log_file, mode='a')
        formatter = logging.Formatter('%(asctime)s | %(levelname)s - %(message)s', datefmt='%d/%m/%y %H:%M:%S')

        handler.setFormatter(formatter)
        self.addHandler(handler)


class Mode(Enum):
    INSERT = 1
    UPDATE = 2


# Enumeração para a função parse_date
class DateMinMax(Enum):
    MIN = 1
    MAX = 2


class ConfigSection(Enum):
    ALL = 1
    APP = 2
    DATABASE = 3


class BitolaInfo(NamedTuple):
    id: str
    bitola_id: str
    volume: float
    rework: str | None = None


class OldestBackup(NamedTuple):
    creation: str
    fullname: str
    parent: str
