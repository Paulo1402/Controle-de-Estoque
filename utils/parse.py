from datetime import datetime
from enum import Enum


# Enumeração para a função parse_date
class DateMinMax(Enum):
    MIN = 1
    MAX = 2


# Formata uma data de um formato de entrada para o formato de saída
def parse_date(
        date: str,
        input_format: str,
        output_format: str = '%Y-%m-%d',
        on_fail: DateMinMax | None = None
) -> str | None:
    try:
        parsed_date = datetime.strptime(date, input_format)
        parsed_date = parsed_date.strftime(output_format)
    except (ValueError, TypeError):
        if on_fail == DateMinMax.MIN:
            parsed_date = datetime.min.strftime(output_format)
        elif on_fail == DateMinMax.MAX:
            parsed_date = datetime.max.strftime(output_format)
        else:
            parsed_date = None

    return parsed_date


# Converte de float para string formatada
def from_float_to_volume(value: float | int, symbol: bool = True) -> str:
    value = f'{value:_.3f}'
    value = value.replace('.', ',').replace('_', '.').replace('-', '')

    if symbol:
        value += ' M³'

    return value


# Converte de string formatada para float
def from_volume_to_float(value: str) -> float:
    value = value.replace('.', '').replace(',', '.').replace(' M³', '')
    value = float(value) if value != '' else 0

    return value
