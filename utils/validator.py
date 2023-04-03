from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator

from utils import from_float_to_volume, from_volume_to_float, get_today


# Valida campos de bitola
class BitolaValidator(QRegularExpressionValidator):
    def __init__(self, regex: QRegularExpression):
        super().__init__(regex)

        self.state = self.State.Invalid

    def validate(self, input_text: str, pos: int) -> tuple:
        result: tuple = super().validate(input_text.lower(), pos)
        self.state = result[0]

        return result

    # Seta auto-format
    def fixup(self, input_text: str) -> str:
        regex = QRegularExpression(r'(\d{2,3}[xX]){2}\d{3,4}([mM]{2})?')
        match = regex.match(input_text)

        if not match.hasMatch():
            return

        input_text = input_text.lower()

        if 'mm' not in input_text:
            input_text += 'mm'

        return input_text


# Valida campos de volume
class VolumeValidator(QRegularExpressionValidator):
    def __init__(self, regex: QRegularExpression):
        super().__init__(regex)

        self.state = self.State.Invalid

    def validate(self, input_text: str, pos: int) -> tuple:
        result: tuple = super().validate(input_text, pos)
        self.state = result[0]

        return result

    # Seta auto-format
    def fixup(self, input_text: str) -> str:
        regex = QRegularExpression(r'\d+')
        match = regex.match(input_text)

        if not match.hasMatch():
            return

        input_text = from_volume_to_float(input_text)

        return from_float_to_volume(input_text, symbol=False)


class DateValidator(QRegularExpressionValidator):
    def __init__(self, regex: QRegularExpression):
        super().__init__(regex)

        self.state = self.State.Invalid

    def validate(self, input_text: str, pos: int) -> tuple:
        result: tuple = super().validate(input_text, pos)
        self.state = result[0]

        return result

    # Seta auto-format
    def fixup(self, input_text: str) -> str:
        regex = QRegularExpression(r'(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[12])')
        match = regex.match(input_text)

        if not match.hasMatch():
            return

        year = get_today(output='/%Y')
        input_text += year

        return input_text
