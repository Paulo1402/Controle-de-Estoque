import csv

from PySide6.QtWidgets import QDialog, QFileDialog

from ui.ImportBackupDialog import Ui_Dialog
from services import DatabaseConnection
from utils import Message

# todo Barra de progresso para feedback visual durante importação do backup


# Diálgo para importar backup
class ImportBackupDialog(QDialog, Ui_Dialog):
    def __init__(self, parent, database: DatabaseConnection):
        super().__init__(parent)
        self.setupUi(self)
        self.setFixedSize(480, 155)

        self.database = database

        self.bt_open.clicked.connect(self.open_file)
        self.bt_import.clicked.connect(self.import_backup)
        self.txt_source.textChanged.connect(lambda: self.bt_import.setDisabled(self.txt_source.text() == ''))

        self.cb_table.addItems(['bitola', 'ciclo', 'nfe', 'nfe_info', 'pezinho', 'residuo'])
        self.bt_import.setDisabled(True)

    # Abre diálogo para selecionar backup
    def open_file(self):
        path = QFileDialog.getOpenFileName(self, 'Selecionar backup', filter='(*.csv)')[0]

        if not path:
            return

        self.txt_source.setText(path)

    # Importa backup de um arquivo .csv para dentro do banco de dados
    def import_backup(self):
        table = self.cb_table.currentText()
        source = self.txt_source.text()

        if Message.warning_question(
                self,
                f'Deseja importar esses dados para dentro da tabela "{table}"?\n'
                'Todos os dados atuais nessa tabela serão substituídos!'
        ) == Message.NO:
            return

        # Deleta dados atuais
        self.database.delete(table=table, clause='', force=True)

        # Recupera dados do backup
        with open(source, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=';')
            header = next(reader)

            for row in reader:
                fields = {field: value for field, value in list(zip(header, row))}

                # Para cada linha do backup, insere dados na tabela
                self.database.create(
                    table=table,
                    fields=fields
                )

        # Notifica usuário e recarrega dados no aplicativo
        Message.information(self, 'AVISO', f'Backup da tabela "{table}" importado com sucesso.')
        self.parent().setup_data()
