"""
Validadores de campos.

O método 'validate' precisa ser reimplementado em cada validador, pensando nisso,
havia optado em criar uma classe abstrata para implementar esse método e as demais classes
herdariam dela, evitando boilerplate, porém a classe abc.ABC conflita com a metaclass de objetos QT.
Criando uma metaclass para contornar esse problema leva a uma complexidade desnecessária e abre brechas para
comportamentos inesperados, portanto decidi por apenas repetir o código em todos os validadores.
"""

from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator

from . import from_float_to_volume, from_volume_to_float, get_today


class BitolaValidator(QRegularExpressionValidator):
    """Validador para campos de bitola."""

    def __init__(self):
        super().__init__()

        self.state = self.State.Invalid

        regex = QRegularExpression(r'(\d{2,3}x){2}\d{3,4}m{2}')
        self.setRegularExpression(regex)

    def validate(self, input_text: str, pos: int) -> tuple:
        """
        Valida o campo.

        Esse método é chamado automaticamente quando algo é digitado no campo.
        O método foi sobreposto apenas para salvar o resultado da validação no escopo da classe para futura
        verificação.

        :param input_text: Texto de entrada
        :param pos: Posição do caractere
        :return: Tupla com texto, posição e resultado da validação
        """
        result: tuple = super().validate(input_text.lower(), pos)
        self.state = result[0]

        return result

    def fixup(self, input_text: str) -> str:
        """
        Seta auto-format.

        Esse método é chamado automaticamente para tentar auto validar um campo quer perdeu o foco e que ainda não
        foi validado.

        :param input_text: Texto de entrada
        :return: Texto manipulado
        """
        regex = QRegularExpression(r'(\d{2,3}[xX]){2}\d{3,4}([mM]{2})?')
        match = regex.match(input_text)

        if not match.hasMatch():
            return

        input_text = input_text.lower()

        if 'mm' not in input_text:
            input_text += 'mm'

        return input_text


class VolumeValidator(QRegularExpressionValidator):
    """Validador para campos de volume."""

    def __init__(self):
        super().__init__()

        self.state = self.State.Invalid

        regex = QRegularExpression(r'(\d+,\d{3})(?<!^0,000$)')
        self.setRegularExpression(regex)

    def validate(self, input_text: str, pos: int) -> tuple:
        """
        Valida o campo.

        Esse método é chamado automaticamente quando algo é digitado no campo.
        O método foi sobreposto apenas para salvar o resultado da validação no escopo da classe para futura
        verificação.

        :param input_text: Texto de entrada
        :param pos: Posição do caractere
        :return: Tupla com texto, posição e resultado da validação
        """
        result: tuple = super().validate(input_text, pos)
        self.state = result[0]

        return result

    def fixup(self, input_text: str) -> str:
        """
        Seta auto-format.

        Esse método é chamado automaticamente para tentar auto validar um campo quer perdeu o foco e que ainda não
        foi validado.

        :param input_text: Texto de entrada
        :return: Texto manipulado
        """
        regex = QRegularExpression(r'\d+')
        match = regex.match(input_text)

        if not match.hasMatch():
            return

        input_text = from_volume_to_float(input_text)

        return from_float_to_volume(input_text, symbol=False)


class DateValidator(QRegularExpressionValidator):
    """Validador para campos de data."""

    def __init__(self):
        super().__init__()

        self.state = self.State.Invalid

        regex = QRegularExpression(r'(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[12])/[12][0-9]{3}')
        self.setRegularExpression(regex)

    def validate(self, input_text: str, pos: int) -> tuple:
        """
        Valida o campo.

        Esse método é chamado automaticamente quando algo é digitado no campo.
        O método foi sobreposto apenas para salvar o resultado da validação no escopo da classe para futura
        verificação.

        :param input_text: Texto de entrada
        :param pos: Posição do caractere
        :return: Tupla com texto, posição e resultado da validação
        """
        result: tuple = super().validate(input_text, pos)
        self.state = result[0]

        return result

    def fixup(self, input_text: str) -> str:
        """
        Seta auto-format.

        Esse método é chamado automaticamente para tentar auto validar um campo quer perdeu o foco e que ainda não
        foi validado.

        :param input_text: Texto de entrada
        :return: Texto manipulado
        """
        regex = QRegularExpression(r'(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[12])')
        match = regex.match(input_text)

        if not match.hasMatch():
            return

        year = get_today(output='/%Y')
        input_text += year

        return input_text
