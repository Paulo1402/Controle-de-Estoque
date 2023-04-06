import itertools
import functools
import csv

from PySide6.QtCore import QThread, Signal

from services import DatabaseConnection, QueryError
from utils import TABLES


# Worker para a importação
class ImportBackupWorker(QThread):
    # Signals
    progress = Signal(int)
    error = Signal(str)
    success = Signal()

    def __init__(self, database: DatabaseConnection, table: str, source: str):
        super().__init__()
        self.database = database
        self.table = table
        self.source = source

    def run(self):
        # Recupera dados do backup
        with open(self.source, 'r', encoding='latin') as f:
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

            self.database.connect(enable_fk=False)

            # Deleta dados atuais
            self.database.delete(table=self.table, clause='', force=True)

            self.database.connect()

            # Pega total de linhas
            row_count = 0
            total_rows = functools.reduce(lambda count, _: count + 1, reader_total_rows, 0)

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
