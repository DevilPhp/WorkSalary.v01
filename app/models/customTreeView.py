import json

from PySide6.QtCore import QAbstractTableModel, Qt, Signal, QItemSelection, QItemSelectionModel, QMimeData
from PySide6.QtGui import QDrag, QBrush, QColor
from PySide6.QtWidgets import QTreeView, QAbstractItemView, QListView, QStyledItemDelegate, QStyle, QStyleOptionViewItem


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
                selectedItems['payInLeva'] = self.selectionModel().selectedRows(26)
                selectedItems['payInEuro'] = self.selectionModel().selectedRows(28)
                self.selectedRows.emit(selectedItems)

            elif event.key() == Qt.Key.Key_Down and index.row() < self.model().rowCount() - 1:
                self.selectRow(index.row() + 1)
                # selectedItems = self.checkSender(parrentName)
                selectedItems['payInLeva'] = self.selectionModel().selectedRows(26)
                selectedItems['payInEuro'] = self.selectionModel().selectedRows(28)
                self.selectedRows.emit(selectedItems)

        # print(selectedItems)

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
                    selectedItems['payInLeva'] = self.selectionModel().selectedRows(26)
                    selectedItems['payInEuro'] = self.selectionModel().selectedRows(28)
                    # print(selectedItems)
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


class CustomTreeViewWithDrop(QTreeView):
    dropedOpers = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSelectionBehavior(QTreeView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QTreeView.SelectionMode.ExtendedSelection)

        self.setDragEnabled(True)
        self.setAcceptDrops(True)  # IMPORTANT
        self.setDropIndicatorShown(True)  # optional but useful
        self.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.setDefaultDropAction(Qt.DropAction.CopyAction)

        self.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)
        self.setAlternatingRowColors(True)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setSizeAdjustPolicy(QAbstractItemView.SizeAdjustPolicy.AdjustToContents)
        self.setSortingEnabled(True)

        # Set custom delegate for expanded type rows
        self.treeDelegate = TreeExpandedTypeDelegate(self, self)
        self.setItemDelegate(self.treeDelegate)

        # Refresh colors when rows are expanded/collapsed
        self.expanded.connect(self.refreshTreeRowColors)
        self.collapsed.connect(self.refreshTreeRowColors)

    def refreshTreeRowColors(self, *args):
        """
        Repaint the tree viewport so row colors update
        after expanding or collapsing items.
        """
        self.viewport().update()

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("application/x-operations-json"):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        index = self.indexAt(event.position().toPoint())

        if not index.isValid():
            event.ignore()
            return

        model = self.model()
        if hasattr(model, "mapToSource"):
            sourceIndex = model.mapToSource(index)
            sourceModel = model.sourceModel()
        else:
            sourceIndex = index
            sourceModel = model

        parentItem = sourceModel.itemFromIndex(sourceIndex)

        if parentItem is None:
            event.ignore()
            return

        nodeType = parentItem.data(Qt.ItemDataRole.UserRole + 1)

        if event.mimeData().hasFormat("application/x-operations-json") and nodeType in ("group", "struct"):
            event.acceptProposedAction()
        else:
            event.ignore()

    def startDrag(self, supportedActions):
        """
        Start drag only for operation rows already inside the tree.
        """
        indexes = self.selectionModel().selectedIndexes()
        if not indexes:
            return

        model = self.model()
        operations = []
        seenKeys = set()
        sourceParent = None

        for proxyIndex in indexes:
            if hasattr(model, "mapToSource"):
                sourceIndex = model.mapToSource(proxyIndex)
                sourceModel = model.sourceModel()
            else:
                sourceIndex = proxyIndex
                sourceModel = model

            item = sourceModel.itemFromIndex(sourceIndex)
            if item is None:
                continue

            nodeType = item.data(Qt.ItemDataRole.UserRole + 1)
            if nodeType != "operation":
                continue

            parentItem = item.parent()
            if parentItem is None:
                continue

            if sourceParent is None:
                sourceParent = parentItem
            elif parentItem != sourceParent:
                continue

            operId = item.data(Qt.ItemDataRole.UserRole)
            parentNodeType = parentItem.data(Qt.ItemDataRole.UserRole + 1)
            parentNodeId = parentItem.data(Qt.ItemDataRole.UserRole)
            key = (parentNodeType, parentNodeId, operId)

            if key in seenKeys:
                continue
            seenKeys.add(key)

            operations.append({
                "id": operId,
                "name": item.text()
            })

        if not operations:
            return

        mimeData = QMimeData()
        mimeData.setText("\n".join(op["name"] for op in operations))
        mimeData.setData(
            "application/x-operations-json",
            json.dumps(operations).encode("utf-8")
        )

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.exec(Qt.DropAction.CopyAction)

    def dropEvent(self, event):
        index = self.indexAt(event.position().toPoint())
        if not index.isValid():
            event.ignore()
            return

        model = self.model()
        # Map proxy index -> source index if proxy is used
        if hasattr(model, "mapToSource"):
            sourceIndex = model.mapToSource(index)
            sourceModel = model.sourceModel()
        else:
            sourceIndex = index
            sourceModel = model

        parentItem = sourceModel.itemFromIndex(sourceIndex)

        nodeType = parentItem.data(Qt.ItemDataRole.UserRole + 1)

        if parentItem is None:
            event.ignore()
            return

        if nodeType in ("group", "struct") and parentItem.text() != "Плетене":
            if not event.mimeData().hasFormat("application/x-operations-json"):
                event.ignore()
                return

            rawData = bytes(event.mimeData().data("application/x-operations-json")).decode("utf-8")
            operations = json.loads(rawData)

            event.acceptProposedAction()
            self.dropedOpers.emit([operations, parentItem])
        else:
            event.ignore()


class CustomListViewWithDrag(QListView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragEnabled(True)
        self.setAlternatingRowColors(True)
        self.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.setSizeAdjustPolicy(QAbstractItemView.SizeAdjustPolicy.AdjustToContents)

    def startDrag(self, event):
        indexes = self.selectedIndexes()
        if not indexes:
            return
        model = self.model()
        operations = []
        seenRows = set()

        for index in indexes:
            if index.row() in seenRows:
                continue
            seenRows.add(index.row())
            item = model.itemFromIndex(index)

            if item is None:
                continue

            operations.append({
                'id': item.data(Qt.ItemDataRole.UserRole),
                'name': item.text(),
            })

        if not operations:
            return

        # print(operations)

        mimeData = QMimeData()
        mimeData.setText("\n".join(op['name'] for op in operations))

        mimeData.setData(
            'application/x-operations-json',
            json.dumps(operations).encode('utf-8')
        )

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.exec(Qt.DropAction.CopyAction)


class TreeExpandedTypeDelegate(QStyledItemDelegate):
    def __init__(self, treeView, parent=None):
        super().__init__(parent)
        self.treeView = treeView

    def paint(self, painter, option, index):
        """
        Paint expanded 'type' rows with custom background color.
        """

        # Make a real copy of the style option
        opt = QStyleOptionViewItem(option)
        self.initStyleOption(opt, index)

        # Always inspect column 0 of the same row
        rowRootIndex = index.siblingAtColumn(0)

        nodeType = rowRootIndex.data(Qt.ItemDataRole.UserRole + 1)

        isExpandedType = (
            nodeType == "type" and
            self.treeView.isExpanded(rowRootIndex)
        )

        # Paint custom background BEFORE default painting
        if isExpandedType and not (opt.state & QStyle.StateFlag.State_Selected):
            painter.save()
            painter.fillRect(opt.rect, QColor(150, 207, 193))
            painter.restore()

        # Let default delegate paint text / icon / selection
        super().paint(painter, opt, index)
