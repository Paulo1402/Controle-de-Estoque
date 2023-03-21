from PySide6.QtWidgets import QLineEdit, QMessageBox, QComboBox
from PySide6.QtGui import QFocusEvent, QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

import utils


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
    def warning_question(cls, parent, message: str, default_button=QMessageBox.StandardButton.No):
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
    ):
        self.setWindowTitle(title)
        self.setText(message)
        self.setIcon(icon)
        self.setDefaultButton(default_button)

        return super().exec()

    # Seta captions personalizados
    def set_caption_buttons(self, buttons: list[tuple[QMessageBox.StandardButton, str]]):
        b = 0

        for button, _ in buttons:
            b |= button

        self.setStandardButtons(b)

        for button, caption in buttons:
            self.button(button).setText(caption)


class CustomComboBox(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)

        validator = QRegularExpressionValidator(
            QRegularExpression(r"(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[12])/[12][0-9]{3}")
        )

        self.setValidator(validator)

    def showPopup(self) -> None:
        utils.CalendarDialog(self.parent(), self).show()


# LineEdit com auto formatar moeda
class CustomLineEdit(QLineEdit):
    # Formata para float ao receber o foco
    def focusInEvent(self, a0: QFocusEvent) -> None:
        value = utils.from_volume_to_float(self.text())
        value = str(value).replace('.', ',')
        self.setText(value)

        super().focusInEvent(a0)

    # Formata para moeda ao perder o foco
    def focusOutEvent(self, a0: QFocusEvent) -> None:
        value = utils.from_volume_to_float(self.text())
        value = utils.from_float_to_volume(value)
        self.setText(value)

        super().focusOutEvent(a0)
