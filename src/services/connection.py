"""Conexão e manipulação do banco de dados."""

import os
from enum import Enum

from PySide6.QtSql import QSqlDatabase, QSqlQuery

from utils import get_config, ConfigSection


class QueryError(Exception):
    """Exceção lançada ao falhar uma query."""

    def __init__(self, query: str):
        self.query = query


class DatabaseState(Enum):
    """Estados de conexão com o banco de dados."""
    CONNECTED = 1
    NO_DATABASE = 2
    DATABASE_NOT_FOUND = 3


class DatabaseConnection:
    """Classe responsável por manter a conexão com o banco de dados."""
    State: DatabaseState = DatabaseState

    def __init__(self):
        self._connection: QSqlDatabase | None = None

        self.connection_state: DatabaseState = DatabaseState.NO_DATABASE
        self.location = ''

    def connect(self):
        """Tenta se conectar ao banco de dados."""
        config = get_config(ConfigSection.DATABASE)
        db = config['name']

        # Verifica se o banco de dados pode ser localizado
        if not self.check_location(db):
            self._connection = None
            return

        self.location = db

        self._connection = QSqlDatabase.addDatabase('QSQLITE')
        self._connection.setDatabaseName(db)

        if self._connection.open():
            self.connection_state = DatabaseState.CONNECTED

            self.create_tables()
            self.create_temp_table()

    def disconnect(self):
        """Desconecta conexão caso esteja conectada"""
        if self._connection and self._connection.isOpen():
            self._connection.close()

    def check_location(self, path: str) -> bool:
        """Verifica se a localização do arquivo pode ser encontrada"""
        if not path:
            self.connection_state = DatabaseState.NO_DATABASE
            return False

        if not os.path.exists(path):
            self.connection_state = DatabaseState.DATABASE_NOT_FOUND
            return False

        return True

    def create_tables(self):
        """Cria tabelas caso não exista"""
        query = QSqlQuery(self._connection)

        query.exec("PRAGMA foreign_keys = ON")

        query.exec(
            """
            CREATE TABLE IF NOT EXISTS cliente (
                cliente_id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT
            )
            """
        )

        query.exec(
            """
            CREATE TABLE IF NOT EXISTS estufa (
                estufa_id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT
            )
            """
        )

        query.exec(
            """
            CREATE TABLE IF NOT EXISTS ciclo (
                ciclo INTEGER PRIMARY KEY,
                estufa TEXT,
                finalidade TEXT,
                entrada TEXT,
                saida TEXT
            )
            """
        )

        query.exec(
            """
            CREATE TABLE IF NOT EXISTS nfe_info (
                nfe INTEGER PRIMARY KEY,
                data TEXT,
                cliente TEXT,
                volume REAL,
                fardos INTEGER,
                ciclo_pezinho INTEGER,

                FOREIGN KEY (ciclo_pezinho)
                    REFERENCES ciclo (ciclo)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE
            )
            """
        )

        query.exec(
            """
            CREATE TABLE IF NOT EXISTS bitola (
                bitola_id INTEGER PRIMARY KEY AUTOINCREMENT,
                ciclo INTEGER,
                bitola TEXT,
                fardos INTEGER,
                volume_tratado REAL,

                FOREIGN KEY (ciclo)
                    REFERENCES ciclo (ciclo)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE
            )
            """
        )

        query.exec(
            """
            CREATE TABLE IF NOT EXISTS nfe (
                nfe_id INTEGER PRIMARY KEY AUTOINCREMENT,
                bitola_id INTEGER,
                nfe INTEGER,
                volume REAL,
                retrabalho TEXT,

                FOREIGN KEY (bitola_id)
                    REFERENCES bitola (bitola_id)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE,

                FOREIGN KEY (nfe)
                    REFERENCES nfe_info (nfe)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE
            )
            """
        )

        query.exec(
            """
            CREATE TABLE IF NOT EXISTS pezinho (
                pezinho_id INTEGER PRIMARY KEY AUTOINCREMENT,
                bitola_id INTEGER,
                nfe INTEGER,
                volume REAL,

                FOREIGN KEY (bitola_id)
                    REFERENCES bitola (bitola_id)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE,

                FOREIGN KEY (nfe)
                    REFERENCES nfe_info (nfe)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE
            )
            """
        )

        query.exec(
            """
            CREATE TABLE IF NOT EXISTS residuo (
                residuo_id INTEGER PRIMARY KEY AUTOINCREMENT,
                bitola_id INTEGER,
                data TEXT,
                volume REAL,

                FOREIGN KEY (bitola_id)
                    REFERENCES bitola (bitola_id)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE
            )
            """
        )

    def create(self, table: str, fields: dict):
        """
        Cria registro em uma tabela.

        :param table: Nome da tabela
        :param fields: Campos no formato key: value
        """
        query = QSqlQuery(self._connection)

        query.prepare(
            f"""
            INSERT INTO {table} ({', '.join([field for field in fields.keys()])})
            VALUES ({', '.join(['?' for _ in fields])})
            """
        )

        for value in fields.values():
            query.addBindValue(value)

        if not query.exec():
            raise QueryError(f'Failed execution on query expression: {query.lastQuery()}')

    def read(self, table: str, fields: list[str], clause: str = '', values: list = None, distinct=False) -> QSqlQuery:
        """
        Lê registros em uma tabela e retorna o objeto com os resultados.

        :param table: Nome da tabela
        :param fields: Lista com o nome dos campos
        :param clause: Cláusula para filtrar, ordenar ou agrupar
        :param values: Lista de valores para substituir placeholders
        :param distinct: Realizar a query com registros únicos ou não
        :return: Objeto contendo a query em questão
        """
        query = QSqlQuery(self._connection)

        query.prepare(
            f"""
            SELECT {'DISTINCT' if distinct else ''} {', '.join(fields)} FROM {table}
            {clause}
            """
        )

        if values:
            for value in values:
                query.addBindValue(value)

        if not query.exec():
            raise QueryError(f'Failed execution on query expression: {query.lastQuery()}')

        return query

    def update(self, table: str, fields: dict, clause: str, force=False):
        """
        Atualiza registros em uma tabela.

        :param table: Nome da tabela
        :param fields: Campos no formato key: value
        :param clause: Cláusula para filtrar
        :param force: Forçar update sem clause
        """
        if 'WHERE' not in clause and not force:
            raise QueryError(f'Update statement without WHERE clause')

        query = QSqlQuery(self._connection)

        query.prepare(
            f"""
            UPDATE {table} 
            SET {', '.join([field + '=?' for field in fields.keys()])}
            {clause}
            """
        )

        for value in fields.values():
            query.addBindValue(value)

        if not query.exec():
            raise QueryError(f'Failed execution on query expression: {query.lastQuery()}')

    def delete(self, table: str, clause: str, force=False):
        """
        Deleta registros em uma tabela.

        :param table: Nome da tabela
        :param clause: Cláusula para filtrar
        :param force: Forçar delete sem clause
        :return:
        """
        if 'WHERE' not in clause and not force:
            raise QueryError(f'Delete statement without WHERE clause')

        query = QSqlQuery(self._connection)

        query.prepare(
            f"""
            DELETE FROM {table}  
            {clause}
            """
        )

        if not query.exec():
            raise QueryError(f'Failed execution on query expression: {query.lastQuery()}')

    def is_unique(self, table: str, field: str, key: str) -> bool:
        """
        Retorna se o registro enviado é único na tabela.

        :param table: Nome da tabela
        :param field: Nome do campo
        :param key: Valor do campo
        :return: True se o valor for único, do contrário False
        """
        query = QSqlQuery(self._connection)

        query.prepare(
            f"""
            SELECT COUNT(*) FROM {table}
            WHERE {field} LIKE ?
            """
        )

        query.addBindValue(key)

        if not query.exec():
            raise QueryError(f'Failed execution on query expression: {query.lastQuery()}')

        query.first()

        return not bool(query.value(0))

    def get_stock(self, bitola_id: int) -> float:
        """
        Retorna estoque da bitola enviada.

        :param bitola_id: Id da bitola
        :return: Quantidade em estoque
        """
        query = QSqlQuery(self._connection)

        query.prepare(
            f"""
            SELECT estoque FROM estoque
            WHERE bitola_id = ?
            """
        )

        query.addBindValue(bitola_id)

        if not query.exec():
            raise QueryError(f'Failed execution on query expression: {query.lastQuery()}')

        query.first()

        return query.value(0)

    def reset_sequence(self, table: str):
        """
        Reseta o histórico da primary key da tabela enviada.

        :param table: Nome da tabela
        """
        query = QSqlQuery(self._connection)

        query.prepare(
            """
            DELETE FROM sqlite_sequence 
            WHERE name LIKE ?
            """
        )

        query.addBindValue(table)

        if not query.exec():
            raise QueryError(f'Failed execution on query expression: {query.lastQuery()}')

    def create_temp_table(self):
        """
        Cria tabelas temporárias.

        Cria view e a tabela estoque para consultas ao longo do programa.
        """
        query = QSqlQuery(self._connection)

        query.exec('DROP VIEW IF EXISTS resumo')
        query.exec('DROP TABLE IF EXISTS estoque')

        query.exec(
            """
            CREATE VIEW resumo
            AS 
            SELECT
                bitola.bitola_id,
                bitola.volume_tratado,
                IIF(
                    ciclo.finalidade = 'KD', COALESCE(SUM(nfe.volume), 0), 
                    COALESCE(SUM(pezinho.volume), 0)
                ) AS volume_vendido,
                COALESCE(residuo.volume, 0) AS residuo
    
            FROM ciclo
                LEFT JOIN bitola ON ciclo.ciclo = bitola.ciclo
                LEFT JOIN pezinho ON bitola.bitola_id = pezinho.bitola_id
                LEFT JOIN nfe ON bitola.bitola_id = nfe.bitola_id
                LEFT JOIN residuo ON bitola.bitola_id = residuo.bitola_id
    
            GROUP BY bitola.bitola_id
            """
        )

        query.exec(
            """
            CREATE TABLE estoque AS 
            SELECT 
                bitola.bitola_id, 
                bitola.ciclo, 
                bitola.bitola, 
                bitola.fardos,
                ROUND(resumo.volume_tratado, 3) AS volume_tratado,
                ROUND(resumo.volume_vendido, 3) AS volume_vendido,
                ROUND(resumo.residuo, 3) AS residuo,
                ROUND(resumo.volume_tratado - resumo.volume_vendido - resumo.residuo, 3) AS estoque
    
            FROM bitola
                LEFT JOIN resumo ON bitola.bitola_id = resumo.bitola_id;
            """
        )
