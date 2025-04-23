from PySide6.QtCore import QSortFilterProxyModel, Qt, Signal
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QHeaderView, QMenu, QCheckBox, QWidgetAction


class CaseInsensitiveProxyModel(QSortFilterProxyModel):
    def __init__(self, numericColumns=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columnFilters = {}
        self.numericColumns = numericColumns or []

    def setFilterForColumn(self, column, filterSet):
        self.columnFilters[column] = filterSet[column]
        self.invalidateFilter()

    def filterAcceptsRow(self, sourceRow, sourceParent):
        for column, filterSet in self.columnFilters.items():
            if not filterSet:
                continue
            index = self.sourceModel().index(sourceRow, column, sourceParent)
            data = self.sourceModel().data(index)
            if data + '   ' not in filterSet:
                return False
            # for filter in filterSet:
            #     if filter != data + '   ':
            #         return False
            # if not any(filterValue.lower() in data.lower() + '   ' for filterValue in filterSet):
            #     return False
        return True

    def lessThan(self, left, right):
        if left.column() in self.numericColumns:
            leftData = self.sourceModel().data(left, Qt.ItemDataRole.DisplayRole)
            rightData = self.sourceModel().data(right, Qt.ItemDataRole.DisplayRole)
            return float(leftData) < float(rightData)
        else:
            leftData = self.sourceModel().data(left)
            rightData = self.sourceModel().data(right)
            return str(leftData).lower() > str(rightData).lower()

class CheckableMenu(QMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.checkedItems = set()
        self._max_height = 300
        self.setStyleSheet('''
            *{
                border-radius: 5px;
                font-size: 12px;
            }
            QMenu {
                padding: 2px;
                border-radius: 4px;
                menu-scrollable: true;
            }
            QMenu QCheckBox {
                padding: 3px 5px 3px 5px;
            }
            QMenu QCheckBox:unchecked {
                color: #495466;
            }
            QCheckBox::indicator:unchecked{
                border: 1px solid #495466;
            }
        ''')
        self.setMaximumHeight(300)

    def addCheckableItems(self, items):
        for item in sorted(set(items)):
            if item:  # Skip empty values
                checkBox = QCheckBox(str(item) + '   ', self)
                action = QWidgetAction(self)
                action.setDefaultWidget(checkBox)
                self.checkedItems.add(str(item))
                checkBox.stateChanged.connect(lambda checked, selectedItem=item: self.onItemToggled(checked, selectedItem))
                self.addAction(action)

    def onItemToggled(self, checked, checkedItem):
        if checked:
            self.checkedItems.add(str(checkedItem))
        else:
            self.checkedItems.discard(str(checkedItem))

    def getCheckedItems(self):
        return self.checkedItems


class FilterableHeaderView(QHeaderView):
    # filterRequested = Signal(int)
    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self.setSectionsClickable(True)
        self.filterMenus = {}
        self.filterModel = None
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showFilterMenu)

    def setFilterModel(self, filterModel):
        self.filterModel = filterModel

    def showFilterMenu(self, pos):
        logicalIndex = self.logicalIndexAt(pos)
        print(pos)
        if logicalIndex < 0:
            return

        uniqueValues = set()
        sourceModel = self.filterModel.sourceModel()
        for row in range(sourceModel.rowCount()):
            index = sourceModel.index(row, logicalIndex)
            value = sourceModel.data(index, Qt.ItemDataRole.DisplayRole)
            if value:
                uniqueValues.add(str(value))

        # Create filter menu
        menu = CheckableMenu(self)
        menu.addCheckableItems(uniqueValues)

        # Show the menu - ensure correct position handling
        headerPos = self.mapToGlobal(pos)
        menu.popup(headerPos)
    # def mousePressEvent(self, event):
    #     section = self.logicalIndexAt(event.pos())
    #     if event.button() == Qt.MouseButton.RightButton:
    #         self.filterRequested.emit(section)  # Emit the filterRequested Signal
    #     else:
    #         super(FilterableHeaderView, self).mousePressEvent(event)