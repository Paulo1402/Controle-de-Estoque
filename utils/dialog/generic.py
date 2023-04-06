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

        # Seta model
        self.model = ListModel()
        self.lv_items.setModel(self.model)

        # Conecta slots
        self.lv_items.clicked.connect(self.edit)

        self.bt_new.clicked.connect(self.new)
        self.bt_save.clicked.connect(self.save)
        self.bt_delete.clicked.connect(self.delete)

        # Carrega lista
        self.load_list()

    # Chama a função de callback ao fechar a janela
    def closeEvent(self, event: QCloseEvent):
        self.callback()
        event.accept()

    # Carrega lista
    def load_list(self):
        query = self.database.read(
            table=self.table,
            fields=['nome']
        )

        self.model.setQuery(query)
        self.new()

    # Prepara novo registro
    def new(self):
        self.lv_items.clearSelection()
        self.bt_delete.setDisabled(True)

        self.txt_name.clear()
        self.txt_name.setFocus()

        self.old_name = None

    # Cria ou edita registro
    def save(self):
        name = self.txt_name.text().upper().strip()

        if not name:
            Message.warning(self, 'ATENÇÃO', 'Preencha o campo em branco!')
            self.txt_name.setText()
            return

        message = 'Deseja {} esse registro?'
        message = message.format('inserir' if not self.old_name else 'alterar')

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
                if not self.database.is_unique(table=self.table, field='nome', key=name):
                    Message.warning(self, 'ATENÇÃO', 'Já existe um registro com esse nome na tabela!')
                    return

                self.database.create(
                    table=self.table,
                    fields={'nome': name}
                )

                message = 'Registro inserido com sucesso!'

            # Avisa o usuário e recarrega a lista
            Message.information(self, 'AVISO', message)
            self.load_list()
        except QueryError:
            Message.critical(self, 'CRÍTICO', 'Algo deu errado durante a operação!')

    # Deleta registro
    def delete(self):
        if Message.warning_question(self, 'Deseja deletar esse registro?') == Message.NO:
            return

        self.database.delete(table=self.table, clause=f'WHERE nome LIKE "{self.old_name}"')

        Message.information(self, 'AVISO', 'Registro deletado com sucesso!')
        self.load_list()

    # Traz dados da lista para edição
    def edit(self, index: QModelIndex):
        row = index.row()
        name = self.model.index(row, 0).data()

        self.txt_name.setText(name)
        self.bt_delete.setDisabled(False)

        self.old_name = name
