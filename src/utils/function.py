from datetime import datetime

import qdarktheme
from PySide6.QtWidgets import QLineEdit, QComboBox

from utils import get_config, ConfigSection


# Retorna volume dos pezinhos com base no algoritmo
def get_skids_volume(n_bitola_skids: int, packs: int) -> list[float]:
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


# Retorna campos em branco
def check_empty_fields(fields: list[QLineEdit | QComboBox]) -> QLineEdit | QComboBox:
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


# Checa se a data de entrada é menor que a data de saída
def is_date_range_valid(start_date: str, end_date: str, date_format='%Y-%m-%d') -> bool:
    start_date_parsed = datetime.strptime(start_date, date_format)
    end_date_parsed = datetime.strptime(end_date, date_format)

    return start_date_parsed <= end_date_parsed


# Retorna data atual como string
def get_today(output: str = '%Y-%m-%d') -> str:
    today = datetime.today().date()

    return today.strftime(output)


# Limpa campos
def clear_fields(fields: list[QLineEdit | QComboBox]):
    for field in fields:
        if isinstance(field, QComboBox):
            field.setCurrentIndex(0)
        else:
            field.clear()

        # Atualiza QSS
        field.setProperty('class', '')
        field.style().polish(field)


# Converte um set para uma lista e a ordena
def order_set(set_instance: set) -> list[str]:
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
            'primary': '#f4d1ae'
        },
        '[light]': {
            'primary': '#12263a'
        }
    }

    qdarktheme.setup_theme(
        theme=theme,
        custom_colors=custom_colors,
        additional_qss=qss
    )
