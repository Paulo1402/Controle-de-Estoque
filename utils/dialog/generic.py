from typing import Callable

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QModelIndex
from PySide6.QtGui import QCloseEvent

from ui.GenericDialog import Ui_Dialog
from services import DatabaseConnection, QueryError
from utils import Message, ListModel


class GenericDialog(QDialog, Ui_Dialog):
    def __init__(self, parent, database: DatabaseConnection, title: str, table: str, callback: Callable):
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle(title)

        self.database = database
        self.table = table
        self.callback = callback

        self.old_name = None
        self.model = ListModel()
        self.lv_items.setModel(self.model)

        self.lv_items.clicked.connect(self.edit)

        self.bt_new.clicked.connect(self.new)
        self.bt_save.clicked.connect(self.save)
        self.bt_delete.clicked.connect(self.delete)

        self.load_list()

    def closeEvent(self, event: QCloseEvent):
        self.callback()
        event.accept()

    def load_list(self):
        query = self.database.read(
            table=self.table,
            fields=['nome']
        )

        self.model.setQuery(query)
        self.new()

    def new(self):
        self.lv_items.clearSelection()
        self.bt_delete.setDisabled(True)

        self.txt_name.clear()
        self.txt_name.setFocus()

        self.old_name = None

    def save(self):
        message = 'Deseja inserir esse registro?'
        name = self.txt_name.text().upper()

        if self.old_name:
            message = message.replace('inserir', 'alterar')

        if Message.warning_question(self, message) == Message.NO:
            return

        try:
            if self.old_name:
                self.database.update(
                    table=self.table,
                    fields={'nome': name},
                    clause=f'WHERE nome LIKE "{self.old_name}"'
                )
                message = 'Registro alterado com sucesso!'
            else:
                self.database.create(
                    table=self.table,
                    fields={'nome': name}
                )
                message = 'Registro inserido com sucesso!'

            Message.information(self, 'AVISO', message)

            self.load_list()
        except QueryError:
            Message.critical(self, 'CRÍTICO', 'Algo deu errado durante a operação!')

    def delete(self):
        if Message.warning_question(self, 'Deseja deletar esse registro?') == Message.NO:
            return

        self.database.delete(table=self.table, clause=f'WHERE nome LIKE "{self.old_name}"')
        Message.information(self, 'AVISO', 'Registro deletado com sucesso!')

        self.load_list()

    def edit(self, index: QModelIndex):
        row = index.row()
        name = self.model.index(row, 0).data()

        self.txt_name.setText(name)
        self.bt_delete.setDisabled(False)

        self.old_name = name



