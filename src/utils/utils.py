"""Classes, enums e namedtuples usadas ao longo do programa."""
import os
import functools
import logging
from enum import Enum
from typing import Any, NamedTuple

from PySide6.QtCore import QEasingCurve, QPropertyAnimation
from PySide6.QtWidgets import QMessageBox, QWidget

from . import BASEDIR


class Message(QMessageBox):
    """Template de QMessageBox com captions personalizados para botões"""
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

    @classmethod
    def warning_question(cls, parent, message: str, default_button=QMessageBox.StandardButton.No) -> int:
        """
        Cria e executa uma message box de aviso com botões de Sim e Não

        :param parent: Parent
        :param message: Mensagem para exibir
        :param default_button: Botão padrão
        :return: Resposta do usuário
        """
        buttons = [(QMessageBox.StandardButton.Yes, 'Sim'), (QMessageBox.StandardButton.No, 'Não')]

        self = cls(parent, buttons)
        answer = self.show_message(
            'ATENÇÃO',
            message,
            QMessageBox.Icon.Warning,
            default_button
        )

        return answer

    def show_message(
            self,
            title: str,
            message: str,
            icon: QMessageBox.Icon | None = None,
            default_button: QMessageBox.StandardButton | None = None
    ) -> int:
        """
        Executa MessageBox

        :param title: título do popup
        :param message: mensagem do popup
        :param icon: Ícone do popup
        :param default_button: Botão padrão
        :return: Resposta do usuário
        """
        self.setWindowTitle(title)
        self.setText(message)
        self.setIcon(icon)
        self.setDefaultButton(default_button)

        return super().exec()

    def set_caption_buttons(self, buttons: list[tuple[QMessageBox.StandardButton, str]]):
        """
        Seta captions personalizados.

        :param buttons: Lista contendo tuplas, sendo o primeiro valor o Enum do botão e o segundo o caption
        """
        b = functools.reduce(lambda b, button: b | button[0], buttons, 0)
        self.setStandardButtons(b)

        for button, caption in buttons:
            self.button(button).setText(caption)


# noinspection PyUnresolvedReferences
class Animation:
    """Abstração para criar animações."""

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
    """Logger para eventuais erros."""

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
