from PySide6.QtCore import QAbstractTableModel, Qt, Signal, QItemSelection, QItemSelectionModel
from PySide6.QtWidgets import QTreeView, QAbstractItemView


class CustomTreeView(QTreeView):
    selectedRows = Signal(dict)
    clearCurrentSelection = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSelectionBehavior(QTreeView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QTreeView.SelectionMode.ExtendedSelection)

        self.setDragEnabled(False)
        self.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setAlternatingRowColors(True)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        # self.doubleClicked.connect(self.doubleClickedItem)

        self.setStyleSheet('''
        
                    QHeaderView:section{
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
                    }
                    QAbstractItemView:item{
                        border-bottom: 1px solid #aeaeae;
                    }
                    
                    QAbstractItemView::item:selected{
                        background-color: rgba(198, 228, 254, 45);
                        selection-color: #324b4c;
                    }
                    QAbstractItemView::item:hover{
                        background-color: rgba(198, 228, 254, 45);
                        selection-color: #324b4c;
                    }
                    
                    QTreeView::item:has-children:open {
                        background-color: #7fd1ae;
                    }
                    QTreeView::branch:has-children:open {
                        background-color: #7e7e7e;
                    }
                ''')

    def keyPressEvent(self, event):
        parrentName = self.parent().objectName()

        if event.key() == Qt.Key.Key_Escape:
            self.clearCurrentSelection.emit(True)
            self.clearSelection()

        if event.key() in (Qt.Key.Key_Up, Qt.Key.Key_Down):
            selectedItems = {}
            index = self.currentIndex()

            if event.key() == Qt.Key.Key_Up and index.row() > 0:
                self.selectRow(index.row() - 1)
                # selectedItems = self.checkSender(parrentName)
                selectedItems['payInLeva'] = self.selectionModel().selectedRows(12)
                selectedItems['payInEuro'] = self.selectionModel().selectedRows(13)
                self.selectedRows.emit(selectedItems)

            elif event.key() == Qt.Key.Key_Down and index.row() < self.model().rowCount() - 1:
                self.selectRow(index.row() + 1)
                # selectedItems = self.checkSender(parrentName)
                selectedItems['payInLeva'] = self.selectionModel().selectedRows(12)
                selectedItems['payInEuro'] = self.selectionModel().selectedRows(13)
                self.selectedRows.emit(selectedItems)

        print(selectedItems)

    def mouseReleaseEvent(self, event):
        parrentName = self.parent().objectName()
        if event.button() == Qt.MouseButton.LeftButton:
            selectedItems = {}
            index = self.indexAt(event.pos())
            if index.isValid():
                modifiers = event.modifiers()
                if not (modifiers & Qt.KeyboardModifier.ControlModifier or
                        modifiers & Qt.KeyboardModifier.ShiftModifier) or self.selectionModel().selectedRows(0):
                    # selectedItems = self.checkSender(parrentName)
                    selectedItems['payInLeva'] = self.selectionModel().selectedRows(12)
                    selectedItems['payInEuro'] = self.selectionModel().selectedRows(13)
                    print(selectedItems)
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
