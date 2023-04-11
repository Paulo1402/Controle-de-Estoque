from PySide6.QtWidgets import QDialog, QFileDialog

from src.ui.ImportBackupDialog import Ui_Dialog
from services import DatabaseConnection
from utils import Message, ImportBackupWorker


# Diálogo para importar backup
class ImportBackupDialog(QDialog, Ui_Dialog):
    def __init__(self, parent, database: DatabaseConnection):
        super().__init__(parent)
        self.setupUi(self)

        self.database = database
        self.worker: ImportBackupWorker | None = None

        # Conecta signals
        self.bt_open.clicked.connect(self.open_file)
        self.bt_import.clicked.connect(self.import_backup_handler)
        self.txt_source.textChanged.connect(lambda: self.bt_import.setDisabled(self.txt_source.text() == ''))

        # Configura campos
        self.progress_bar_main.setValue(0)
        self.progress_bar_table.setValue(0)
        self.txt_table.clear()

        self.bt_import.setDisabled(True)

    # Abre diálogo para selecionar backup
    def open_file(self):
        path = QFileDialog.getExistingDirectory(self, 'Selecionar pasta de backup')

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
        source = self.txt_source.text()

        if Message.warning_question(
                self,
                f'Deseja importar os dados desse backup para dentro do banco de dados?\n'
                'Todos os dados atuais serão substituídos!'
        ) == Message.NO:
            return

        # Cria worker e conecta slots
        self.worker = ImportBackupWorker(self.database, source)
        self.worker.progress.connect(self.handle_progress)
        self.worker.success.connect(self.import_finished)
        self.worker.finished.connect(lambda: self.bt_import.setDisabled(False))
        self.worker.error.connect(self.handle_error)

        # Inicia worker
        self.worker.start()

        # Desabilita botão durante o processo
        self.bt_import.setDisabled(True)

    def import_finished(self):
        # Notifica usuário e recarrega dados no aplicativo
        Message.information(self, 'AVISO', f'Backup importado com sucesso.')

        self.database.create_temp_table()
        self.parent().setup_data()

        # Reseta campos
        self.progress_bar_main.setValue(0)
        self.progress_bar_table.setValue(0)
        self.txt_table.clear()
        self.txt_source.clear()

    def handle_progress(self, progress: int, bar: str):
        if bar == 'main':
            self.progress_bar_main.setValue(progress)
        else:
            self.progress_bar_table.setValue(progress)
            self.txt_table.setText(bar)

    def handle_error(self, message: str):
        Message.critical(self, 'CRÍTICO', message)
