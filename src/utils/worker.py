import itertools
import functools
import csv
import os

from PySide6.QtCore import QThread, Signal

from services import DatabaseConnection, QueryError
from utils import TABLES, Logger


# Worker para a importação
class ImportBackupWorker(QThread):
    # Signals
    progress = Signal(int, str)
    error = Signal(str)
    success = Signal()

    def __init__(self, database: DatabaseConnection, source: str):
        super().__init__()

        self.database = database
        self.source = source

    def run(self):
        expected_files = [f'{t}.csv' for t in TABLES.keys()]
        files = [f for f in os.listdir(self.source) if f in expected_files]

        # Verifica se todas as tabelas estão no diretório enviado
        if len(files) != len(expected_files):
            message = 'Não foram encontrados um ou mais arquivos dentro do diretório especificado.\n' \
                      f'Os arquivos esperados são: {", ".join(expected_files)}'
            self.error.emit(message)
            return

        file_count = 0

        # É necessário usar a variável 'expected_files' por que precisamos inserir os dados na ordem correta das
        # tabelas. Usando a lista retornada em 'files' é possível que alguma tabela esteja fora de ordem.
        for file in expected_files:
            # Pega nome da tabela
            table = file.replace('.csv', '')
            file_count += 1

            # Recupera dados do backup
            with open(os.path.join(self.source, file), 'r', encoding='latin') as f:
                # Cria generator original
                _reader = csv.reader(f, delimiter=';')

                # Pega o cabeçalho
                header = next(_reader)

                # Cria cópias a partir do generator original
                reader_rows, reader_total_rows = itertools.tee(_reader, 2)

                # Verifica se os campos do arquivo de backup coincidem com os campos das tabelas
                for field in header:
                    if field not in TABLES[table]:
                        message = f'Os campos do arquivo de backup "{file}" não coincidem com os campos esperados ' \
                                  f'para a tabela "{table}".\n' \
                                  f'Apenas importe arquivos gerados pelo próprio sistema de backup!'
                        self.error.emit(message)
                        return

                # Deleta dados atuais
                self.database.delete(table=table, clause='', force=True)

                # Pega total de linhas
                row_count = 1
                total_rows = functools.reduce(lambda count, _: count + 1, reader_total_rows, 0)

                # Insere dados na tabela
                try:
                    for row in reader_rows:
                        row_count += 1
                        parsed_row = [i if i else None for i in row]
                        fields = {field: value for field, value in list(zip(header, parsed_row))}
                        print(table, fields)

                        self.database.create(
                            table=table,
                            fields=fields
                        )

                        # Emite signal de progresso
                        progress = int((row_count / total_rows) * 100)
                        self.progress.emit(progress, table)

                except QueryError:
                    message = f'Não foi possível importar o arquivo de backup "{file}" por completo. ' \
                              f'Erro na linha: {row_count}.\n' \
                              'Apenas importe arquivos gerados pelo próprio sistema de backup!'

                    self.error.emit(message)

                    logger = Logger()
                    logger.error(f'Failed to import backup on line {row_count} from "{file}".')
                    return

            progress = int((file_count / len(expected_files)) * 100)
            self.progress.emit(progress, 'main')

        self.success.emit()
