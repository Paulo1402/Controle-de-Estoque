import qdarktheme
from PySide6.QtWidgets import QLineEdit, QComboBox


# Retorna volume dos pezinhos com base no algorítmo
def get_skids_volume(n_bitola_skids: int, packs: int) -> list[float]:
    long_skids = 0.00306
    short_skids = 0.00405

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

    volumes = map(lambda x: round(x, 3), volumes)

    return volumes


# Retorna campos em branco
def get_empty_fields(fields: list[QLineEdit | QComboBox]) -> list[QLineEdit | QComboBox]:
    empty_fields = []

    for field in fields:
        value = field.currentText() if isinstance(field, QComboBox) else field.text()

        # Se estiver vazio
        if not value.strip():
            empty_fields.append(field)

            # Atualiza QSS
            field.setProperty('class', 'required')
            field.style().polish(field)

    return empty_fields


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


# Carrega tema e aplica QSS
def load_theme(theme: str):
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