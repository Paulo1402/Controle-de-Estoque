import locale

from utils.globals import BASEDIR, TABLES, LONG_SKIDS, SHORT_SKIDS
from utils.function import (
    clear_fields,
    check_empty_fields,
    get_skids_volume,
    order_set,
    load_theme,
    is_date_range_valid,
    get_today
)
from utils.parse import DateMinMax, parse_date, from_float_to_volume, from_volume_to_float
from utils.config import get_config, set_config
from utils.model import TableModel, ListModel
from utils.utils import Animation, Message, Logger, BitolaInfo, Mode
from utils.validator import BitolaValidator, VolumeValidator, DateValidator
from utils.handler import TableWidgetHandler, CycleTableWidgetHandler, NfeTableWidgetHandler
from utils.worker import ImportBackupWorker
from utils.dialog import *

__all__ = [
    'DateMinMax',
    'ImportBackupWorker',
    'parse_date',
    'get_today',
    'from_float_to_volume',
    'from_volume_to_float',
    'check_empty_fields',
    'get_config',
    'set_config',
    'BASEDIR',
    'ConfigurationDialog',
    'CalendarDialog',
    'ImportBackupDialog',
    'GenericDialog',
    'TableModel',
    'ListModel',
    'Message',
    'TableWidgetHandler',
    'NfeTableWidgetHandler',
    'CycleTableWidgetHandler',
    'clear_fields',
    'BitolaValidator',
    'VolumeValidator',
    'DateValidator',
    'get_skids_volume',
    'order_set',
    'load_theme',
    'Animation',
    'Logger',
    'BitolaInfo',
    'Mode',
    'is_date_range_valid',
    'TABLES'
]

# Define localização para usar a biblioteca datetime
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
