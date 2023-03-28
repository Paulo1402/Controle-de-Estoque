import os
import csv
import json
import shutil
from datetime import datetime
from collections import namedtuple

from PySide6.QtSql import QSqlQuery
from PySide6.QtCore import QThread, Signal

from services.connection import DatabaseConnection, QueryError

import utils


__all__ = [
    'DatabaseConnection',
    'QueryError',
    'check_connection',
    'DoBackupWorker',
    'TABLES'
]

TABLES = {
    'ciclo': ['ciclo', 'estufa', 'finalidade', 'entrada', 'saida'],
    'bitola': ['bitola_id', 'ciclo', 'bitola', 'fardos', 'volume_tratado'],
    'nfe_info': ['nfe', 'data', 'cliente', 'volume', 'fardos', 'ciclo_pezinho'],
    'nfe': ['bitola_id', 'nfe', 'volume', 'retrabalho'],
    'pezinho': ['bitola_id', 'nfe', 'volume'],
    'residuo': ['bitola_id', 'data', 'volume'],
    'estufa': ['estufa_id', 'nome'],
    'cliente': ['cliente_id', 'nome']
 }


# Checa conexão com banco de dados antes de executar uma função que requer conexão
def check_connection(func):
    def inner(self, *_, **__):
        if self.database.connection_state != DatabaseConnection.State.CONNECTED:
            utils.Message.critical(self, 'CRÍTICO', 'Sem conexão com o banco de dados!')
            return

        func(self)

    return inner


class DoBackupWorker(QThread):
    progress = Signal(int)

    def __init__(self, database: DatabaseConnection):
        super().__init__()

        self.database = database

    # Cria arquivo csv com dados da tabela
    @staticmethod
    def _write_csv(filename: str, header: list, query: QSqlQuery):
        with open(filename, 'w', encoding='utf8') as f:
            writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
            writer.writerow(header)

            while query.next():
                values = [query.value(i) for i in range(len(header))]
                writer.writerow(values)

    def run(self):
        # Pega as configurações do aplicativo
        config = utils.get_config()

        db = config['database']
        backup = config['backup']

        frequency = backup['frequency']
        max_backups = backup['max_backups']

        # Caso não haja um banco de dados configurado ou 'no_backups' está setado, aborta backup
        if not db or frequency == 'no_backups':
            return

        # Pega raíz da pasta de backups
        root = os.path.join(os.path.dirname(db), 'backups')

        # Cria raíz caso não exista
        if not os.path.exists(root):
            os.makedirs(root)

        # Pega o arquivo de configuração da pasta de backup
        backup_config_path = os.path.join(root, 'config.json')

        # Tenta coletar data do último backup e transforma em um objeto datetime
        try:
            with open(backup_config_path, 'r', encoding='utf8') as f:
                config = json.loads(f.read())

                last_backup = config['last_backup']
                last_backup = datetime.strptime(last_backup, '%Y-%m-%d')
        except (FileNotFoundError, KeyError, ValueError, json.JSONDecodeError):
            last_backup = None

        # Retona data atual
        today = datetime.today().date()

        # Verifica se há necessidade de realizar o backup com base na configuração 'frequency'
        if last_backup:
            if frequency == 'diary' and last_backup == today:
                return
            elif frequency == 'weekly' and last_backup.isocalendar().week == today.isocalendar().week:
                return
            elif frequency == 'monthly' and last_backup.month == today.month:
                return

        # Transforma datetime em string novamente
        last_backup = today
        last_backup = last_backup.strftime('%Y-%m-%d')

        # Pega o nome do mês e ano atual
        month_folder = os.path.join(root, f'{today.month:02d}-{today.year}')

        # Cria pasta do mês caso não exista
        if not os.path.exists(month_folder):
            os.makedirs(month_folder)

        # Pega dia atual
        day_folder = os.path.join(month_folder, str(today.day))

        # Cria pasta do dia caso não exista
        if not os.path.exists(day_folder):
            os.makedirs(day_folder)

        # Tabelas e seus campos
        count = 0

        for table, header in TABLES.items():
            count += 1

            # Seta arquivo de saída
            filename = os.path.join(day_folder, f'{table}.csv')

            # Realiza consulta
            query = self.database.read(
                table=table,
                fields=header
            )

            # Cria backup em um arquivo .csv
            self._write_csv(filename, header, query)

            progress = int((count / len(TABLES)) * 100)
            self.progress.emit(progress)

        # Cria namedtuple para guardar dados do backup mais antigo
        Oldest = namedtuple('OldestBackup', ['creation', 'fullname', 'parent'])

        oldest = Oldest(datetime.now(), '', '')
        backups_count = 0

        # Itera sobra todos os arquivos na pasta de backups
        for month_folder in os.listdir(root):
            month_fullname = os.path.join(root, month_folder)

            # Caso não seja uma pasta, retorna
            if not os.path.isdir(month_fullname):
                continue

            # Itera sobre cada pasta de backup na pasta do mês
            for day_folder in os.listdir(month_fullname):
                day_fullname = os.path.join(month_fullname, day_folder)
                creation_time = datetime.fromtimestamp(os.path.getctime(day_fullname))
                backups_count += 1

                # Se a data de criação for menor que a data mais antiga atual, substitui
                if creation_time < oldest.creation:
                    oldest = Oldest(creation_time, day_fullname, month_fullname)

        # Caso a quantidade de backups seja maior que a configuração 'max_backups' remove o backup mais antigo
        if backups_count > int(max_backups):
            shutil.rmtree(oldest.fullname)

            # Caso a pasta do mês esteja vazia então remove-a
            if len(os.listdir(oldest.parent)) == 0:
                os.removedirs(oldest.parent)

        # Salva data do último backup
        with open(backup_config_path, 'w', encoding='latin') as f:
            f.write(json.dumps({"last_backup": last_backup}, indent=4))
