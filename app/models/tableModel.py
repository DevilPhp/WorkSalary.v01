from PySide6.QtCore import QAbstractTableModel, Qt, Signal, QItemSelection, QItemSelectionModel
import pandas as pd
import numpy as np
from PySide6.QtWidgets import QTableView, QAbstractItemView
from app.models.customSelectionModel import SingleMultiSelectionModel


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
            # print(value)
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


class CustomTableViewWithMultiSelection(QTableView):
    selectedRows = Signal(dict)
    clearCurrentSelection = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QTableView.SelectionMode.ExtendedSelection)

        self.setDragEnabled(False)
        self.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setAlternatingRowColors(True)
        # self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.verticalHeader().hide()
        self.setCornerButtonEnabled(False)

        # self.isDragging = False
        # self.previousSelection = set()

        # self.selectionModel().selectionChanged

        # self.setSelectionModel(SingleMultiSelectionModel(self.model()))
        # self.setSelectionModel(SingleMultiSelectionModel(self))
        self.setStyleSheet('''
            QHeaderView:section{
                font: 700 10.5pt "Segoe UI";
                background-color: #dfdfdf;
                padding-left: 10px;
                padding-top:10px;
                padding-right:10px;
                selection-background-color: #7f7f7f;
            }
            QVerticalView:section{
                min-height: 30;
            }
            QAbstractItemView{
                alternate-background-color: #d3d3d3;
                font: 10.5pt "Segoe UI";
                selection-background-color: rgba(198, 228, 254, 45);
                selection-color: #324b4c;
            }
            QAbstractItemView:item{
                selection-background-color: rgba(198, 228, 254, 45);
                selection-color: #324b4c;
            }
            
            QAbstractItemView::item:selected{
                background-color: rgba(198, 228, 254, 45);
            }

        ''')

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Up, Qt.Key.Key_Down):
            selectedItems = {}
            index = self.currentIndex()

            if event.key() == Qt.Key.Key_Up and index.row() > 0:
                self.selectRow(index.row() - 1)
                selectedItems['pieces'] = self.selectionModel().selectedRows(5)
                selectedItems['piecesTime'] = self.selectionModel().selectedRows(6)
                self.selectedRows.emit(selectedItems)

            elif event.key() == Qt.Key.Key_Down and index.row() < self.model().rowCount() - 1:
                self.selectRow(index.row() + 1)
                selectedItems['pieces'] = self.selectionModel().selectedRows(5)
                selectedItems['piecesTime'] = self.selectionModel().selectedRows(6)
                self.selectedRows.emit(selectedItems)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            selectedItems = {}
            index = self.indexAt(event.pos())
            if index.isValid():
                modifiers = event.modifiers()
                if not (modifiers & Qt.KeyboardModifier.ControlModifier or
                        modifiers & Qt.KeyboardModifier.ShiftModifier) or self.selectionModel().selectedRows(0):
                    selectedItems['pieces'] = self.selectionModel().selectedRows(5)
                    selectedItems['piecesTime'] = self.selectionModel().selectedRows(6)
                    self.selectedRows.emit(selectedItems)

            else:
                self.clearCurrentSelection.emit(True)
                self.clearSelection()

        super().mouseReleaseEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            index = self.indexAt(event.pos())
            if index.isValid():
                # If clicking on a new row without Ctrl or Shift, clear previous selection
                modifiers = event.modifiers()
                if not (modifiers & Qt.KeyboardModifier.ControlModifier or
                        modifiers & Qt.KeyboardModifier.ShiftModifier):
                    # self.clearCurrentSelection.emit(True)
                    self.clearSelection()
                    # self.clearFocus()

        super().mousePressEvent(event)
