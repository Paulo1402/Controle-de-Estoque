from datetime import datetime

from . import DateMinMax


def parse_date(
        date: str,
        input_format: str,
        output_format: str = '%Y-%m-%d',
        on_fail: DateMinMax | None = None
) -> str | None:
    """
    Formata uma data de um formato de entrada para o formato de saída.

    :param date: Data como string
    :param input_format: Formato de entrada
    :param output_format: Formato de saída
    :param on_fail: Tentar converter para outro formato caso algum erro aconteça
    :return: Data formatada ou None caso 'on_fail' não seja enviado
    """
    try:
        parsed_date = datetime.strptime(date, input_format)
        parsed_date = parsed_date.strftime(output_format)
    except (ValueError, TypeError):
        parsed_date = None

        if on_fail == DateMinMax.MIN:
            parsed_date = datetime.min.strftime(output_format)
        elif on_fail == DateMinMax.MAX:
            parsed_date = datetime.max.strftime(output_format)

    return parsed_date


def from_float_to_volume(value: float | int, symbol: bool = True) -> str:
    """
    # Converte de float para string formatada.

    :param value: Valor para formatar
    :param symbol: Adicionar símbolo
    :return: Valor formatado
    """
    value = f'{value:_.3f}'
    value = value.replace('.', ',').replace('_', '.').replace('-', '')

    if symbol:
        value += ' M³'

    return value


def from_volume_to_float(value: str) -> float:
    """
    Converte de string para float.

    :param value: Valor para formatar
    :return: Valor formatado
    """
    value = value.replace('.', '').replace(',', '.').replace(' M³', '')
    value = float(value) if value != '' else 0

    return value
