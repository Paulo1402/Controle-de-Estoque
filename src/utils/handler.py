from abc import ABC, abstractmethod

from PySide6.QtWidgets import QTableWidget, QPushButton, QLineEdit, QComboBox, QHeaderView, QTableWidgetItem
from PySide6.QtCore import Qt, QModelIndex

from . import Message, BitolaValidator, VolumeValidator, clear_fields, check_empty_fields, DatabaseConnection


# Classe genérica para interação com as table widgets
class TableWidgetHandler(ABC):
    def __init__(
            self,
            parent,
            table_widget: QTableWidget,
            remove_button: QPushButton,
            fields: list[QLineEdit | QComboBox],
            hidden_columns_count: int = 0
    ):
        self.parent = parent
        self.table_widget = table_widget
        self.remove_button = remove_button
        self.fields = fields
        self.hidden_columns_count = hidden_columns_count

        self._ID_register = -1

        for i in range(hidden_columns_count):
            self.table_widget.setColumnHidden(i, True)

        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table_widget.clicked.connect(self.edit)

        self.remove_button.setDisabled(True)

    @property
    def ID_register(self):
        return self._ID_register

    # Método para ser imprementado nas subclasses
    @abstractmethod
    def add(self):
        pass

    # Insere dados da table widget para os campos
    def edit(self, index: QModelIndex):
        row = index.row()
        id_bitola = self.table_widget.item(row, 0).text()

        for i in range(self.hidden_columns_count, self.table_widget.columnCount()):
            item = self.table_widget.item(row, i).text()

            try:
                self.fields[i - self.hidden_columns_count].setText(item)
            except AttributeError:
                self.fields[i - self.hidden_columns_count].setCurrentText(item)

        self._ID_register = int(id_bitola)
        self.remove_button.setDisabled(False)

    # Remove registros da table widget
    def remove(self):
        if not self.table_widget.selectedIndexes():
            return

        row = self.table_widget.selectedIndexes()[0].row()
        self.table_widget.removeRow(row)

        clear_fields(self.fields)

        self._ID_register = -1
        self.remove_button.setDisabled(True)

    # Remove todas as linhas da table widget
    def remove_rows(self):
        for _ in range(self.table_widget.rowCount()):
            self.table_widget.removeRow(0)


# Handler para interagir com a table widget da página de ciclos
class CycleTableWidgetHandler(TableWidgetHandler):
    def add(self):
        # Verifica se há campos em branco
        if not check_empty_fields(self.fields):
            Message.warning(self.parent, 'ATENÇÃO', 'Preencha os campos obrigatórios!')
            return

        # Verifica se os campos estão devidamente validados
        for field in self.fields:
            validator = field.validator()

            if isinstance(validator, (BitolaValidator, VolumeValidator)) \
                    and validator.state != validator.State.Acceptable:
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

        # Adiciona id de registro como primeiro valor da lista
        values = [str(self.ID_register)]

        # Retorna dados dos campos e pega o id da bitola do campo bitola
        for field in self.fields:
            try:
                value = field.text()
            except AttributeError:
                value = field.currentText()

            values.append(value)

        # Adiciona ou atualiza registros no table widget
        for i, value in enumerate(values):
            item = QTableWidgetItem(value)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.table_widget.setItem(row, i, item)

        # Limpa campos e prepara novo registro
        clear_fields(self.fields)

        self.table_widget.clearSelection()
        self.remove_button.setDisabled(True)

        self._ID_register = -1

    def remove(self):
        if self._ID_register != -1:
            if self.table_widget.rowCount() == 1:
                Message.warning(self.parent, 'ATENÇÃO', 'Ao menos uma bitola deve ser especificada!')
                return

            if Message.warning_question(
                    self.parent,
                    'Se remover essa bitola todos os registros dependentes dela serão deletados '
                    'também. Deseja continuar?'
            ) == Message.NO:
                return

            database: DatabaseConnection = self.parent.database
            database.delete(table='bitola', clause=f'WHERE bitola_id LIKE {self._ID_register}')

            self.parent.refresh_data()
            self.parent.setup_data()

        super().remove()


# Handler para interagir com a table widget da página de nfe
class NfeTableWidgetHandler(TableWidgetHandler):
    def __init__(
            self,
            parent,
            table_widget: QTableWidget,
            remove_button: QPushButton,
            fields: list[QLineEdit | QComboBox],
            optional_fields: list[QLineEdit | QComboBox],
            hidden_columns_count: int = 0
    ):
        super().__init__(parent, table_widget, remove_button, fields, hidden_columns_count)

        self.optional_fields = optional_fields

    def add(self):
        # Remove os campos opcionais
        fields = list(filter(lambda x: x not in self.optional_fields, self.fields))

        # Verifica se há campos em branco
        if not check_empty_fields(fields):
            Message.warning(self.parent, 'ATENÇÃO', 'Preencha os campos obrigatórios!')
            return

        # Verifica se os campos estão devidamente validados
        for field in self.fields:
            # Pula iteração caso o campo em questão seja opcional e esteja em branco
            if field in self.optional_fields and not field.text():
                continue

            validator = field.validator()

            if isinstance(validator, (BitolaValidator, VolumeValidator)) \
                    and validator.state != validator.State.Acceptable:
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

            try:
                value = field.text()
            except AttributeError:
                value = field.currentText()

            values.append(value)

        values = [str(self.ID_register), bitola_id, *values]

        # Adiciona ou atualiza registros no table widget
        for i, value in enumerate(values):
            item = QTableWidgetItem(value)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.table_widget.setItem(row, i, item)

        # Limpa campos e prepara novo registro
        clear_fields(self.fields)

        self.remove_button.setDisabled(True)
        self.table_widget.clearSelection()
        self._ID_register = -1
