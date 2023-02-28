import locale

from utils.parse import parse_date, parse_month, from_currency_to_float, from_float_to_currency

from PySide6.QtWidgets import QLineEdit, QComboBox

from utils.parse import DateMinMax, parse_date, parse_month, from_float_to_currency, from_currency_to_float
from utils.config import get_config, set_config, BASEDIR
from utils.model import TableModel, ListModel
from utils.widget import CustomLineEdit, Message
from utils.dialog import *

__all__ = [
    'DateMinMax',
    'parse_date',
    'parse_month',
    'from_float_to_currency',
    'from_currency_to_float',
    'get_empty_fields',
    'get_config',
    'set_config',
    'BASEDIR',
    'ConfigurationDialog',
    'CalendarDialog',
    'ImportBackupDialog',
    'TableModel',
    'ListModel',
    'Message',
]

# Define localização para usar a biblioteca datetime
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')


# Retorna campos em branco
def get_empty_fields(fields: list[QLineEdit | QComboBox]):
    empty_fields = []

    for field in fields:
        if isinstance(field, QComboBox):
            if field.currentText().strip() == '':
                empty_fields.append(field)
        else:
            if field.text().strip() == '':
                empty_fields.append(field)

    return empty_fields
