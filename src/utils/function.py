"""Funções gerais usadas ao longo do programa."""

from datetime import datetime

import qdarktheme
from PySide6.QtWidgets import QLineEdit, QComboBox

from . import get_config, ConfigSection, Message, DARK_COLOR, LIGHT_COLOR
from services import DatabaseConnection


def get_skids_volume(n_bitola_skids: int, packs: int) -> list[float]:
    """
    Retorna volume dos pezinhos.

    Utiliza constantes previamente configuradas para calcular artificialmente o volume dos pezinhos.

    Caso haja apenas uma bitola o cálculo é feito somando a multiplicação da constante de skids curto pela
    quantidade de fardos com a multiplicação da constante de skids longo pela quantidade de fardos.

    Ex:
        volume = (packs * short_skids) + (packs * long_skids)

    Caso haja duas ou mais bitolas a primeira bitola é calculada como skids curto e as demais como skids longo.
    Ambas são multiplicadas pela quantidade de fardos e retornadas como uma lista.

    Ex:
        volume = [packs * short_kids, packs * long_kids, ...]

    Para ambos os casos o retorno será uma lista para manter a compatibilidade.

    :param n_bitola_skids: Número de bitolas do ciclo de pezinho
    :param packs: Quantidade de fardos da Nfe
    :return: Lista de volumes
    """
    config = get_config(ConfigSection.APP)

    long_skids = config['long_skids']
    short_skids = config['short_skids']

    volumes = []

    if n_bitola_skids == 1:
        volumes.append((packs * short_skids) + (packs * long_skids))
    else:
        first = True

        for _ in range(n_bitola_skids):
            if first:
                volumes.append(packs * short_skids)
            else:
                volumes.append(packs * long_skids)

            first = False

    volumes = [round(i, 3) for i in volumes]

    return volumes


def check_empty_fields(fields: list[QLineEdit | QComboBox]) -> bool:
    """
    Verifica se há campos em branco.

    Caso o campo esteja em branco atualiza o QSS para destacá-lo e coloca em foco o
    primeiro campo.

    :param fields: Lista de campos.
    :return: True se houver campos em branco e False se não houver.
    """
    empty_fields = []

    for field in fields:
        value = field.currentText() if isinstance(field, QComboBox) else field.text()

        # Se estiver vazio
        if not value.strip():
            empty_fields.append(field)

            # Atualiza QSS
            field.setProperty('class', 'required')
            field.style().polish(field)

    if empty_fields:
        empty_fields[0].setFocus()
        return False

    return True


def is_date_range_valid(start_date: str, end_date: str, date_format='%Y-%m-%d') -> bool:
    """
    Checa se a data inicial é menor que a data final.

    :param start_date: Data inicial
    :param end_date: Data final
    :param date_format: Formato da data enviada
    :return: True | False
    """
    start_date_parsed = datetime.strptime(start_date, date_format)
    end_date_parsed = datetime.strptime(end_date, date_format)

    return start_date_parsed <= end_date_parsed


def get_today(output: str = '%Y-%m-%d') -> str:
    """
    Retorna data de hoje como string.

    :param output: Formato de saída
    :return: Data formatada
    """
    today = datetime.today().date()

    return today.strftime(output)


def clear_fields(fields: list[QLineEdit | QComboBox]):
    """
    Reseta valores e QSS dos campos para o padrão.

    :param fields: Lista de campos
    """
    for field in fields:
        if isinstance(field, QComboBox):
            field.setCurrentIndex(0)
        else:
            field.clear()

        # Atualiza QSS
        field.setProperty('class', '')
        field.style().polish(field)


def order_set(set_instance: set) -> list[str]:
    """
    Converte um set para uma lista e a ordena.

    Após ordenar faz um type casting para string em todos os valores do set original.

    :param set_instance: Objeto set
    :return: Lista ordenada com strings
    """
    converted_set = [value for value in set_instance]
    converted_set.sort()

    converted_set = [str(value) for value in converted_set]

    return converted_set


def load_theme(theme: str):
    """
    Carrega tema.

    Carrega e configura tema, além de adicionar regras QSS adicionais.

    :param theme: Tema a ser carregado
    """
    if theme == 'light':
        border_color = 'black'
    else:
        border_color = 'white'

    qss = '''
        QPushButton:hover{
            border: 1px solid %s;
        }

        QLineEdit[class="required"],
        QComboBox[class="required"]{
             border: 1px solid red;
        }

        QGroupBox{
            margin: 0;
        } 
    ''' % border_color

    custom_colors = {
        '[dark]': {
            'primary': DARK_COLOR
        },
        '[light]': {
            'primary': LIGHT_COLOR
        }
    }

    qdarktheme.setup_theme(
        theme=theme,
        custom_colors=custom_colors,
        additional_qss=qss
    )


def check_connection(func):
    """
    Checa conexão com banco de dados antes de executar uma função.

    Decorar a função desejada com essa função.

    :param func: A função que deve ser checada
    :return: Uma nova função para ser executada no lugar da função original
    """

    def inner(self, *args, **kwargs):
        if self.database.connection_state != DatabaseConnection.State.CONNECTED:
            Message.critical(self, 'CRÍTICO', 'Sem conexão com o banco de dados!')
            return

        func(self, *args, **kwargs)

    return inner
