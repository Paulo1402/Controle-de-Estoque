import locale
from abc import ABC, abstractmethod

from PySide6.QtWidgets import QLineEdit, QComboBox, QPushButton, QTableWidgetItem, QTableWidget, QHeaderView
from PySide6.QtCore import QRegularExpression, Qt
from PySide6.QtGui import QRegularExpressionValidator

from utils.parse import DateMinMax, parse_date, get_today, from_float_to_volume, from_volume_to_float
from utils.config import get_config, set_config, BASEDIR
from utils.model import TableModel, ListModel
from utils.widget import CustomLineEdit, Message
from utils.dialog import *


# todo Organizar esse arquivo

__all__ = [
    'DateMinMax',
    'parse_date',
    'get_today',
    'from_float_to_volume',
    'from_volume_to_float',
    'get_empty_fields',
    'get_config',
    'set_config',
    'BASEDIR',
    'ConfigurationDialog',
    'CalendarDialog',
    'ImportBackupDialog',
    'GenericDialog',
    'TableModel',
    'ListModel',
    'Message',
    'NfeTableWidgetHandler',
    'CycleTableWidgetHandler',
    'clear_fields',
    'BitolaValidator',
    'VolumeValidator',
    'get_skids_volume'
]

# Define localização para usar a biblioteca datetime
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')


class BitolaValidator(QRegularExpressionValidator):
    def __init__(self, regex):
        super().__init__(regex)
        self.state = self.State.Invalid

    def validate(self, input_text: str, pos: int) -> object:
        result: tuple = super().validate(input_text, pos)

        if result[0] == self.State.Acceptable:
            self.state = self.State.Acceptable

        return result

    def fixup(self, input_text: str):
        regex = QRegularExpression(r'(\d{2,3}[xX]){2}\d{3,4}([mM]{2})?')
        match = regex.match(input_text)

        if not match.hasMatch():
            return

        input_text = input_text.lower()

        if 'mm' not in input_text:
            input_text += 'mm'

        return input_text


class VolumeValidator(QRegularExpressionValidator):
    def __init__(self, regex):
        super().__init__(regex)
        self.state = self.State.Invalid

    def validate(self, input_text: str, pos: int) -> object:
        result: tuple = super().validate(input_text, pos)

        if result[0] == self.State.Acceptable:
            self.state = self.State.Acceptable

        return result

    def fixup(self, input_text: str):
        regex = QRegularExpression(r'\d+')
        match = regex.match(input_text)

        if not match.hasMatch():
            return

        input_text = from_volume_to_float(input_text)

        return from_float_to_volume(input_text, symbol=False)


class TableWidgetHandler(ABC):
    def __init__(
            self,
            parent,
            table_widget: QTableWidget,
            remove_button: QPushButton,
            fields: list[QLineEdit | QComboBox]
    ):
        self.parent = parent
        self.table_widget = table_widget
        self.remove_button = remove_button
        self.fields = fields

        self.table_widget.setColumnHidden(0, True)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table_widget.clicked.connect(self.edit)

        self.remove_button.setDisabled(True)

    @abstractmethod
    def add(self):
        pass

    # Insere dados da table widget para os campos
    def edit(self):
        for i, item in enumerate(self.table_widget.selectedItems()):
            try:
                self.fields[i].setText(item.text())
            except AttributeError:
                self.fields[i].setCurrentText(item.text())

        self.remove_button.setDisabled(False)

    # Remove registros da table widget
    def remove(self):
        if not self.table_widget.selectedIndexes():
            return

        row = self.table_widget.selectedIndexes()[0].row()
        self.table_widget.removeRow(row)

        clear_fields(self.fields)
        self.remove_button.setDisabled(True)

    def remove_rows(self):
        for _ in range(self.table_widget.rowCount()):
            self.table_widget.removeRow(0)


class CycleTableWidgetHandler(TableWidgetHandler):
    def add(self):
        # Verifica se há campos em branco
        empty_fields = get_empty_fields(self.fields)

        if len(empty_fields) > 0:
            Message.warning(self.parent, 'ATENÇÃO', 'Preencha os campos obrigatórios!')
            empty_fields[0].setFocus()
            return

        # Verifica se os campos estão devidamente validados
        for field in self.fields:
            validator = field.validator()

            if isinstance(validator, BitolaValidator) or isinstance(validator, VolumeValidator):
                if validator.state != validator.State.Acceptable:
                    field_name = 'bitola' if isinstance(validator, BitolaValidator) else 'volume'

                    Message.warning(self.parent, 'ATENÇÃO', f'Preencha o campo de {field_name} corretamente!')
                    field.setFocus()
                    return

        # Verifica se é uma nova adição ou uma edição
        if self.table_widget.selectedIndexes():
            row = self.table_widget.selectedIndexes()[0].row()
        else:
            row = self.table_widget.rowCount()
            self.table_widget.insertRow(row)

        # Adiciona ou atualiza registros no table widget
        for i, field in enumerate(self.fields, 1):
            value = field.currentText() if isinstance(field, QComboBox) else field.text()
            item = QTableWidgetItem(value)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.table_widget.setItem(row, i, item)

        # Limpa campos e prepara novo registro
        clear_fields(self.fields)
        self.table_widget.clearSelection()
        self.remove_button.setDisabled(True)


class NfeTableWidgetHandler(TableWidgetHandler):
    def __init__(
            self,
            parent,
            table_widget: QTableWidget,
            remove_button: QPushButton,
            fields: list[QLineEdit | QComboBox],
            optional_fields: list[QLineEdit | QComboBox]
    ):
        super().__init__(parent, table_widget, remove_button, fields)
        self.optional_fields = optional_fields

    def add(self):
        # Verifica se há campos em branco
        fields = [field for field in self.fields if field not in self.optional_fields]
        empty_fields = get_empty_fields(fields)

        if len(empty_fields) > 0:
            Message.warning(self.parent, 'ATENÇÃO', 'Preencha os campos obrigatórios!')
            empty_fields[0].setFocus()
            return

        # Verifica se os campos estão devidamente validados
        for field in fields:
            validator = field.validator()

            if isinstance(validator, BitolaValidator) or isinstance(validator, VolumeValidator):
                if validator.state != validator.State.Acceptable:
                    field_name = 'bitola' if isinstance(validator, BitolaValidator) else 'volume'

                    Message.warning(self.parent, 'ATENÇÃO', f'Preencha o campo de {field_name} corretamente!')
                    field.setFocus()
                    return

        # Verifica se é uma nova adição ou uma edição
        if self.table_widget.selectedIndexes():
            row = self.table_widget.selectedIndexes()[0].row()
        else:
            row = self.table_widget.rowCount()
            self.table_widget.insertRow(row)

        values = []
        bitola_id = None

        # Retorna dados dos campos e pega o id da bitola do campo bitola
        for field in self.fields:
            if hasattr(field, 'bitola_id_list'):
                index = field.currentIndex()
                bitola_id = field.bitola_id_list[index]

            value = field.currentText() if isinstance(field, QComboBox) else field.text()
            values.append(value)

        if bitola_id:
            values = [bitola_id, *values]

        # Adiciona ou atualiza registros no table widget
        for i, value in enumerate(values):
            item = QTableWidgetItem(value)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.table_widget.setItem(row, i, item)

        # Limpa campos e prepara novo registro
        clear_fields(self.fields)
        self.table_widget.clearSelection()
        self.remove_button.setDisabled(True)


def get_skids_volume(n_bitola_skids: int, packs: int):
    long_skids = 0.00306
    short_skids = 0.00405

    volumes = []

    if n_bitola_skids == 1:
        volumes.append((packs * short_skids) + (packs * long_skids))
    else:
        first = True

        for _ in range(n_bitola_skids):
            if first:
                volumes.append(packs * short_skids)
            else:
                volumes.append(packs * long_skids)

            first = False

    volumes = map(lambda x: round(x, 3), volumes)

    return volumes


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


# Limpa campos
def clear_fields(fields: list[QLineEdit | QComboBox]):
    for field in fields:
        if isinstance(field, QComboBox):
            field.setCurrentIndex(-1)
        else:
            field.clear()
