from PySide6.QtCore import QAbstractTableModel, Qt
import pandas as pd
import numpy as np

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data.copy()
        self._data = self._data.fillna('')

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            # Format floats to 2 decimal places
            if isinstance(value, float):
                if int(value) == value:
                    return int(value)
                else:
                    return f"{value:.2f}"
            # Convert any other non-string values to strings
            elif value == '' or pd.isna(value) or value is None:
                return ""
            else:
                return str(value)

        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self._data.columns[section]
            elif orientation == Qt.Orientation.Vertical:
                return '   '
        return None

    def flags(self, index):
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable

