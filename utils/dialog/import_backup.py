from PySide6.QtWidgets import QDialog, QFileDialog

from ui.ImportBackupDialog import Ui_Dialog
from services import DatabaseConnection
from utils import Message, TABLES, ImportBackupWorker


# Diálogo para importar backup
class ImportBackupDialog(QDialog, Ui_Dialog):
    def __init__(self, parent, database: DatabaseConnection):
        super().__init__(parent)
        self.setupUi(self)

        self.database = database
        self.table = ''
        self.worker: ImportBackupWorker | None = None

        # Conecta signals
        self.bt_open.clicked.connect(self.open_file)
        self.bt_import.clicked.connect(self.import_backup_handler)
        self.txt_source.textChanged.connect(lambda: self.bt_import.setDisabled(self.txt_source.text() == ''))

        # Configura campos
        self.cb_table.addItems(TABLES.keys())
        self.progress_bar.setValue(0)
        self.bt_import.setDisabled(True)

    # Abre diálogo para selecionar backup
    def open_file(self):
        path = QFileDialog.getOpenFileName(self, 'Selecionar backup', filter='(*.csv)')[0]

        if not path:
            return

        self.txt_source.setText(path)

    # Importa backup de um arquivo .csv para dentro do banco de dados
    def import_backup_handler(self):
        # Se já houver um processo em andamento aborta a função
        if self.worker and self.worker.isRunning():
            Message.warning(self, 'ATENÇÃO', 'Aguarde o backup atual ser concluído!')
            return

        # Retorna dados dos campos
        self.table = self.cb_table.currentText()
        source = self.txt_source.text()

        if Message.warning_question(
                self,
                f'Deseja importar esses dados para dentro da tabela "{self.table}"?\n'
                'Todos os dados atuais nessa tabela serão substituídos!'
        ) == Message.NO:
            return

        # Cria worker e conecta slots
        self.worker = ImportBackupWorker(self.database, self.table, source)
        self.worker.progress.connect(self.progress_bar.setValue)
        self.worker.success.connect(self.import_finished)
        self.worker.finished.connect(lambda: self.bt_import.setDisabled(False))
        self.worker.error.connect(lambda err: Message.critical(self, 'CRÍTICO', err))

        # Inicia worker
        self.worker.start()

        # Desabilita botão temporariamente
        self.bt_import.setDisabled(True)

    def import_finished(self):
        # Notifica usuário e recarrega dados no aplicativo
        Message.information(self, 'AVISO', f'Backup da tabela "{self.table}" importado com sucesso.')
        self.database.create_temp_table()
        self.parent().setup_data()

        # Reseta campos
        self.progress_bar.setValue(0)
        self.txt_source.clear()
