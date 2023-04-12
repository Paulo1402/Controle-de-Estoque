from PySide6.QtSql import QSqlQueryModel
from PySide6.QtCore import QModelIndex, Qt

from . import parse_date, from_float_to_volume


class TableModel(QSqlQueryModel):
    """Model para tratar dados antes de adicionar a QTableView"""

    def __init__(self, date_fields: list | None = None, volume_fields: list | None = None):
        super().__init__()

        self.date_fields = date_fields
        self.volume_fields = volume_fields

    def data(self, item: QModelIndex, role: int = ...):
        # Retorna valor original
        value = super().data(item, role)

        # Alinha todos os objetos ao centro
        if role == Qt.ItemDataRole.TextAlignmentRole:
            return Qt.AlignmentFlag.AlignCenter

        if role == Qt.ItemDataRole.DisplayRole:
            # Caso seja coluna de datas, formata o valor para data brasileira
            if self.date_fields and item.column() in self.date_fields:
                return parse_date(value, input_format='%Y-%m-%d', output_format='%d/%m/%Y')

            # Caso seja coluna de volume, formata valor para volume
            if self.volume_fields and item.column() in self.volume_fields:
                return from_float_to_volume(value, symbol=False)

            return value


class ListModel(QSqlQueryModel):
    """Model para tratar dados antes de adicionar a QTableView."""

    def data(self, item: QModelIndex, role: int = ...):
        # Alinha todos os objetos ao centro
        if role == Qt.ItemDataRole.TextAlignmentRole:
            return Qt.AlignmentFlag.AlignCenter

        if role == Qt.ItemDataRole.DisplayRole:
            return super().data(item, role)
