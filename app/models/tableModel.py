import json

import pandas as pd
import numpy as np
from PySide6.QtCore import QAbstractTableModel, Qt, Signal, QItemSelection, QItemSelectionModel, QModelIndex, QRect, \
    QMimeData
from PySide6.QtGui import QDrag
from PySide6.QtWidgets import (QTableView, QAbstractItemView, QStyledItemDelegate,
                               QStyleOptionButton, QApplication, QStyle)
from app.models.customSelectionModel import SingleMultiSelectionModel


class TableModel(QAbstractTableModel):
    dataEdited = Signal(int, int, object)

    def __init__(self, data):
        super().__init__()
        self._data = data.copy()
        self.editableColumns = []
        self._data = self._data.fillna('')

    def setEditableColumns(self, columns):
        self.editableColumns = columns

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.EditRole:
            row = index.row()
            col = index.column()

            if col > 0:

                # Try to convert the value to the original data type of the column
                try:
                    original_dtype = self._data.iloc[:, col].dtype
                    if pd.api.types.is_numeric_dtype(original_dtype):
                        # Allow empty string to be set as NaN or handle as you see fit
                        if value == '':
                            self._data.iloc[row, col] = np.nan
                        else:
                            self._data.iloc[row, col] = original_dtype.type(value)
                    else:
                        self._data.iloc[row, col] = value
                except (ValueError, TypeError):
                    return False  # Failed to convert type

                self.dataChanged.emit(index, index, [role])
                self.dataEdited.emit(row, col, value)
                return True
            else:
                return False
        return False

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
        flags = Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled
        if index.column() in self.editableColumns:
            flags |= Qt.ItemFlag.ItemIsEditable
        return flags


class CustomTableViewWithMultiSelection(QTableView):
    selectedRows = Signal(dict)
    clearCurrentSelection = Signal(bool)

    def __init__(self, parent=None, singleSelection=False):
        super().__init__(parent)
        self.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QTableView.SelectionMode.ExtendedSelection)

        self.singleSelection = singleSelection

        if singleSelection:
            self.setSelectionMode(QTableView.SelectionMode.SingleSelection)

        self.setDragEnabled(False)
        self.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setAlternatingRowColors(True)
        # self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.verticalHeader().hide()
        self.verticalHeader().setDefaultSectionSize(20)
        self.verticalHeader().setMinimumSectionSize(20)
        self.setCornerButtonEnabled(False)


        # self.isDragging = False
        # self.previousSelection = set()

        # self.selectionModel().selectionChanged

        # self.setSelectionModel(SingleMultiSelectionModel(self.model()))
        # self.setSelectionModel(SingleMultiSelectionModel(self))
        self.setStyleSheet('''
            QHeaderView:section:horizontal  {
                font: 700 9pt "Segoe UI";
                background-color: #dfdfdf;
                padding-left: 5px;
                padding-top:5px;
                padding-right:5px;
                selection-background-color: #7f7f7f;
            }
            QAbstractItemView{
                alternate-background-color: #d3d3d3;
                font: 8pt "Segoe UI";
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

    def setEditTriggers(self, triggers):
        super().setEditTriggers(triggers)

    def checkSender(self, parrentName):
        if not self.singleSelection:
            selectedItems = {}
            if parrentName == 'timePaperTableHolder':
                selectedItems['pieces'] = self.selectionModel().selectedRows(5)
                selectedItems['piecesTime'] = self.selectionModel().selectedRows(6)
            elif parrentName == 'paymentsTableHolder':
                selectedItems['payInLeva'] = self.selectionModel().selectedRows(27)
                selectedItems['payInEuro'] = self.selectionModel().selectedRows(29)
            return selectedItems
        else:
            pass

    def keyPressEvent(self, event):
        parrentName = self.parent().objectName()

        if event.key() == Qt.Key.Key_Escape:
            self.clearCurrentSelection.emit(True)
            self.clearSelection()
            self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
            self.setCurrentIndex(QModelIndex())

        if event.key() in (Qt.Key.Key_Up, Qt.Key.Key_Down):
            selectedItems = {}
            index = self.currentIndex()

            if event.key() == Qt.Key.Key_Up and index.row() > 0:
                self.selectRow(index.row() - 1)
                selectedItems = self.checkSender(parrentName)
                self.selectedRows.emit(selectedItems)

            elif event.key() == Qt.Key.Key_Down and index.row() < self.model().rowCount() - 1:
                self.selectRow(index.row() + 1)
                selectedItems = self.checkSender(parrentName)
                self.selectedRows.emit(selectedItems)

    def mouseReleaseEvent(self, event):
        parrentName = self.parent().objectName()
        if event.button() == Qt.MouseButton.LeftButton:
            selectedItems = {}
            index = self.indexAt(event.pos())
            if index.isValid():
                modifiers = event.modifiers()
                if not (modifiers & Qt.KeyboardModifier.ControlModifier or
                        modifiers & Qt.KeyboardModifier.ShiftModifier) or self.selectionModel().selectedRows(0):
                    selectedItems = self.checkSender(parrentName)
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


class CustomTableWithDrag(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.DragDropMode.DragOnly)
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSizeAdjustPolicy(QAbstractItemView.SizeAdjustPolicy.AdjustToContents)
        self.setAlternatingRowColors(True)
        self.setSortingEnabled(True)
        self.setShowGrid(False)
        self.setStyleSheet('''
            QHeaderView:section:horizontal  {
                font: 700 9pt "Segoe UI";
                background-color: #dfdfdf;
            }
            ''')
        self.verticalHeader().setDefaultSectionSize(0)
        self.verticalHeader().hide()
        self.setCornerButtonEnabled(False)

    def startDrag(self, supportedActions):
        """
            Starts drag operation for the selected rows in the table.

            Important:
            In QTableView with proxy model, selected indexes belong to the proxy.
            So we map them back to the source model before reading real data.
        """

        indexes = self.selectedIndexes()
        if not indexes:
            return

        proxyModel = self.model()
        if proxyModel is None:
            return

        sourceModel = proxyModel.sourceModel() if hasattr(proxyModel, 'sourceModel') else proxyModel

        operations = []
        seenSourceRows = set()
        for proxyIndex in indexes:
            if not proxyIndex.isValid():
                continue

            # Map proxy index -> source index
            if hasattr(proxyModel, 'mapToSource'):
                sourceIndex = proxyModel.mapToSource(proxyIndex)
            else:
                sourceIndex = proxyIndex

            if not sourceIndex.isValid():
                continue
            sourceRow = sourceIndex.row()

            # Prevent reading the same row multiple times,
            # because QTableView selection includes indexes from both columns.
            if sourceRow in seenSourceRows:
                continue
            seenSourceRows.add(sourceRow)

            # Read data from the source model row.
            # Column 0 = number/id
            # Column 1 = operation name
            nameIndex = sourceModel.index(sourceRow, 2)
            timeIndex = sourceModel.index(sourceRow, 1)
            operationId = sourceModel.data(nameIndex, Qt.ItemDataRole.UserRole)
            operationName = sourceModel.data(nameIndex, Qt.ItemDataRole.DisplayRole)
            operTime = sourceModel.data(timeIndex, Qt.ItemDataRole.UserRole)

            if not operationName:
                continue

            operations.append({
                'id': operationId,
                'name': operationName,
                'time': operTime,
            })

        if not operations:
            return

        mimeData = QMimeData()
        # Plain text version
        # Useful if the drop target reads only text.
        mimeData.setText("\n".join(op["name"] for op in operations))

        # Custom JSON version
        # Useful if the drop target supports structured data.
        mimeData.setData(
            "application/x-operations-json",
            json.dumps(operations).encode("utf-8")
        )

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.exec(Qt.DropAction.CopyAction)


class ButtonDelegation(QStyledItemDelegate):
    clickedRow = Signal(int)
    """
    Delegate that draws a button in a table cell and detects clicks.
    """
    def paint(self, painter, option, index):
        """
        Draw the button inside the cell.
        """
        button = QStyleOptionButton()
        button.rect = option.rect
        button.text = "Цехове"
        button.state = QStyle.State_Enabled

        QApplication.style().drawControl(QStyle.CE_PushButton, button, painter)

    def editorEvent(self, event, model, option, index):
        """
        Detect mouse clicks on the button.
        """
        if event.type() == event.Type.MouseButtonRelease:
            if event.button() == Qt.LeftButton:
                row = index.row()

                # Execute your function
                self.buttonClicked(row)

        return True

    def buttonClicked(self, row):
        """
        Custom function executed when button is clicked.
        """
        self.clickedRow.emit(row)
        # print(self.currentId)
        # print(workingPlaces)
