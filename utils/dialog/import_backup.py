import csv
import itertools
import functools

from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtCore import QThread, Signal

from ui.ImportBackupDialog import Ui_Dialog
from services import DatabaseConnection, QueryError, TABLES
from utils import Message


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
            Message.warning(self, 'ATENÇÃO', 'Aguarde o backup atual ser conclúido!')
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
        self.parent().setup_data()

        # Reseta campos
        self.progress_bar.setValue(0)
        self.txt_source.clear()


# Worker para a importação
class ImportBackupWorker(QThread):
    # Signals
    progress = Signal(int)
    success = Signal()
    error = Signal(str)

    def __init__(self, database: DatabaseConnection, table: str, source: str):
        super().__init__()
        self.database = database
        self.table = table
        self.source = source

    def run(self):
        # Recupera dados do backup
        with open(self.source, 'r', encoding='utf-8') as f:
            # Cria generator original
            _reader = csv.reader(f, delimiter=';')

            # Pega o cabeçalho
            header = next(_reader)

            # Cria cópias a partir do generator original
            reader_rows, reader_total_rows = itertools.tee(_reader, 2)

            # Verifica se os campos do arquivo de backup coincidem com os campos das tabelas
            for field in header:
                if field not in TABLES[self.table]:
                    message = 'Os campos do arquivo de backup não coincidem com os campos esperados para a tabela ' \
                              f'"{self.table}".\nApenas importe arquivos gerados pelo próprio sistema de backup!'
                    self.error.emit(message)
                    return

            # Deleta dados atuais
            self.database.delete(table=self.table, clause='', force=True)

            # Pega total de linhas
            row_count = 0
            total_rows = functools.reduce(lambda count, _:  count + 1, reader_total_rows, 0)

            # Insere dados na tabela
            try:
                for row in reader_rows:
                    fields = {field: value for field, value in list(zip(header, row))}
                    row_count += 1

                    self.database.create(
                        table=self.table,
                        fields=fields
                    )

                    # Emite signal de progresso
                    self.progress.emit(int((row_count / total_rows) * 100))

                self.success.emit()
            except QueryError:
                message = f'Não foi possível importar o arquivo de backup por completo. Erro na linha: {row_count}.\n' \
                          'Verifique o arquivo e tente novamente.'

                self.error.emit(message)
