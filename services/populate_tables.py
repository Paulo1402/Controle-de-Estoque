import csv

from PySide6.QtSql import QSqlQuery

from utils import parse_date, from_volume_to_float

if __name__ == '__main__':
    from services import DatabaseConnection

    database = DatabaseConnection()
    database.connect()

    connection = database.connection

    # Deleta conteúdo das tabelas
    QSqlQuery(connection).exec('DELETE FROM ciclo')
    QSqlQuery(connection).exec('DELETE FROM nfe_info')
    QSqlQuery(connection).exec('DELETE FROM bitola')
    QSqlQuery(connection).exec('DELETE FROM nfe')
    QSqlQuery(connection).exec('DELETE FROM pezinho')
    QSqlQuery(connection).exec('DELETE FROM residuo')
    QSqlQuery(connection).exec('DELETE FROM estufa')
    QSqlQuery(connection).exec('DELETE FROM cliente')

    # Cria objeto com a conexão
    query = QSqlQuery(connection)

    # Insere dados na tabela (USADO COMO SEED DURANTE O DESENVOLVIMENTO)
    query.prepare(
        """
        INSERT INTO ciclo (
            ciclo,
            estufa,
            finalidade,
            entrada,
            saida    
        )
        VALUES (?, ?, ?, ?, ?)
        """
    )

    # Faz a modelagem dos dados de um arquivo .csv para inserir na tabela
    with open('seed/bd_ciclo.csv', 'r', encoding='latin') as f:
        csvreader = csv.reader(f, delimiter=';')
        next(csvreader)

        for ciclo, finalidade, entrada, saida in csvreader:
            query.addBindValue(ciclo)
            query.addBindValue('ESTUFA 7')
            query.addBindValue(finalidade)
            query.addBindValue(parse_date(entrada, '%d/%m/%Y', '%Y-%m-%d'))
            query.addBindValue(parse_date(saida, '%d/%m/%Y', '%Y-%m-%d'))

            query.exec()

    # Verifica se a inserção foi feita corretamente
    query.exec("SELECT count(*) FROM ciclo")
    query.first()

    print('ciclo', query.value(0))

    # Repete o mesmo procedimento na tabela abaixo
    query.prepare(
        """
        INSERT INTO nfe_info (
            nfe,
            data,
            cliente,
            volume,
            fardos,
            ciclo_pezinho
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """
    )

    with open('seed/bd_nfe_info.csv', 'r', encoding='latin') as f:
        csvreader = csv.reader(f, delimiter=';')
        next(csvreader)

        for nfe, data, cliente, volume, fardos, ciclo_pezinho in csvreader:
            query.addBindValue(nfe)
            query.addBindValue(parse_date(data, '%d/%m/%Y', '%Y-%m-%d'))
            query.addBindValue(cliente)
            query.addBindValue(from_volume_to_float(volume))
            query.addBindValue(fardos)
            query.addBindValue(ciclo_pezinho)

            query.exec()

    query.exec("SELECT count(*) FROM nfe_info")
    query.first()

    print('nfe_info', query.value(0))

    # Repete o mesmo procedimento na tabela abaixo
    query.prepare(
        """
        INSERT INTO bitola (
            bitola_id,
            ciclo,
            bitola,
            fardos,
            volume_tratado
        )
        VALUES (?, ?, ?, ?, ?)
        """
    )

    with open('seed/bd_bitola.csv', 'r', encoding='latin') as f:
        csvreader = csv.reader(f, delimiter=';')
        next(csvreader)

        for bitola_id, ciclo, bitola, fardos, volume_tratado in csvreader:
            query.addBindValue(bitola_id)
            query.addBindValue(ciclo)
            query.addBindValue(bitola)
            query.addBindValue(fardos)
            query.addBindValue(from_volume_to_float(volume_tratado))

            query.exec()

    query.exec("SELECT count(*) FROM bitola")
    query.first()

    print('bitola', query.value(0))

    # Repete o mesmo procedimento na tabela abaixo
    query.prepare(
        """
        INSERT INTO nfe (
            bitola_id,
            nfe,
            volume,
            retrabalho
        )
        VALUES (?, ?, ?, ?)
        """
    )

    with open('seed/bd_nfe.csv', 'r', encoding='latin') as f:
        csvreader = csv.reader(f, delimiter=';')
        next(csvreader)

        for bitola_id, nfe, volume, retrabalho in csvreader:
            query.addBindValue(bitola_id)
            query.addBindValue(nfe)
            query.addBindValue(from_volume_to_float(volume))
            query.addBindValue(retrabalho)

            query.exec()

    query.exec("SELECT count(*) FROM nfe")
    query.first()

    print('nfe', query.value(0))

    # Repete o mesmo procedimento na tabela abaixo
    query.prepare(
        """
        INSERT INTO pezinho (
            bitola_id,
            nfe,
            volume
        )
        VALUES (?, ?, ?)
        """
    )

    with open('seed/bd_pezinho.csv', 'r', encoding='latin') as f:
        csvreader = csv.reader(f, delimiter=';')
        next(csvreader)

        for bitola_id, nfe, volume in csvreader:
            query.addBindValue(bitola_id)
            query.addBindValue(nfe or None)
            query.addBindValue(from_volume_to_float(volume))

            query.exec()

    query.exec("SELECT count(*) FROM pezinho")
    query.first()

    print('pezinho', query.value(0))

    # Repete o mesmo procedimento na tabela abaixo
    query.prepare(
        """
        INSERT INTO residuo (
            bitola_id,
            data,
            volume
        )
        VALUES (?, ?, ?)
        """
    )

    with open('seed/bd_residuo.csv', 'r', encoding='latin') as f:
        csvreader = csv.reader(f, delimiter=';')
        next(csvreader)

        for bitola_id, data, volume in csvreader:
            query.addBindValue(bitola_id)
            query.addBindValue(parse_date(data, '%d/%m/%Y', '%Y-%m-%d'))
            query.addBindValue(from_volume_to_float(volume))

            query.exec()

    query.exec("SELECT count(*) FROM residuo")
    query.first()

    print('residuo', query.value(0))

    query.prepare(
        """
        INSERT INTO estufa (
            nome
        )
        VALUES (?)
        """
    )

    values = ['ESTUFA 1', 'ESTUFA 2', 'ESTUFA 7']

    for value in values:
        query.addBindValue(value)
        query.exec()

    print('estufa', len(values))

    query.prepare(
        """
        INSERT INTO cliente (
            nome
        )
        VALUES (?)
        """
    )

    values = ['CASTILLO', 'MULTIPINE', 'MOW', 'BRASILMAD']

    for value in values:
        query.addBindValue(value)
        query.exec()

    print('cliente', len(values))
