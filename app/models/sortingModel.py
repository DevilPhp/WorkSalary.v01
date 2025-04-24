from functools import partial

from PySide6.QtCore import QSortFilterProxyModel, Qt, Signal, QPoint
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QHeaderView, QMenu, QCheckBox, QWidgetAction, QApplication



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
            if data not in filterSet:
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

    def addCheckableItems(self, items):
        for item in sorted(set(items)):
            if item:  # Skip empty values
                checkBox = QCheckBox(str(item) + '   ', self)
                action = QWidgetAction(self)
                action.setDefaultWidget(checkBox)
                self.checkedItems.add(str(item))
                checkBox.stateChanged.connect(lambda checked, selectedItem=item: self.onItemToggled(checked, selectedItem))
                self.addAction(action)
        # self.adjustSizeForScrolling(len(items))

    # def adjustSizeForScrolling(self, itemCount):
    #     averageItemHeight = 25  # Approximate height of a menu item
    #     contentHeight = itemCount * averageItemHeight
    #
    #     if contentHeight > self._max_height:
    #         self.sizeHint().setHeight(self._max_height)
            # Enable scrolling with styling
            # self.setStyleSheet("""
            #             QMenu {
            #                 max-height: %dpx;
            #             }
            #             QMenu::item {
            #                 padding: 5px 25px 5px 20px;
            #             }
            #         """ % self._max_height)

    # def popup(self, pos):
    #     """Override popup to ensure proper positioning"""
    #     # Make sure we don't position the menu outside screen bounds
    #     screen_rect = QApplication.primaryScreen().availableGeometry()
    #
    #     # Calculate if menu would go off screen
    #     menu_height = min(self.sizeHint().height(), self._max_height)
    #     if pos.y() + menu_height > screen_rect.height():
    #         # Reposition above the cursor if it would go off screen
    #         pos.setY(pos.y() - menu_height)
    #
    #     # Call the original popup method with adjusted position
    #     super().popup(pos)

    def onItemToggled(self, checked, checkedItem):
        if checked:
            self.checkedItems.add(str(checkedItem))
        else:
            self.checkedItems.discard(str(checkedItem))

    def getCheckedItems(self):
        return self.checkedItems


class FilterableHeaderView(QHeaderView):
    filterRequested = Signal(int)
    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self.setSectionsClickable(True)
        self.filterModel = None
        self.filteredNames = []
        # self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        # self.customContextMenuRequested.connect(self.showFilterMenu)
    def mousePressEvent(self, event):
        logicalIndex = self.logicalIndexAt(event.pos())
        if event.button() == Qt.RightButton:
            self.filterRequested.emit(logicalIndex)
            # menu = CustomSortingMenuWidget(self)
            # sourceModel = self.filterModel.sourceModel()
            # for row in range(sourceModel.rowCount()):
            #     index = sourceModel.index(row, logicalIndex)
            #     value = sourceModel.data(index, Qt.ItemDataRole.DisplayRole)
            #     if value not in uniqueValues:
            #         uniqueValues.append(str(value))
            # # print(uniqueValues)
            # if uniqueValues:
            #     menu.addItems(uniqueValues)
            #     menu.move(event.globalPos())
            #     menu.checkedCheckbox.connect(partial(self.checkedCheckbox, logicalIndex))
            #     # print(menu)
            #     menu.show()
        else:
            super(FilterableHeaderView, self).mousePressEvent(event)

    # def checkedCheckbox(self, column, checkedItem):
    #     if checkedItem.isChecked() and checkedItem.text() not in self.filteredNames:
    #         self.filteredNames.append(checkedItem.text())
    #     elif not checkedItem.isChecked() and checkedItem.text() in self.filteredNames:
    #         self.filteredNames.remove(checkedItem.text())
    #     print(self.filteredNames)
    #     self.filterRequested.emit(self.filteredNames)

    # def setFilterModel(self, filterModel):
    #     self.filterModel = filterModel
    #
    # def showFilterMenu(self, pos):
    #     logicalIndex = self.logicalIndexAt(pos)
    #     # print(pos)
    #     if logicalIndex < 0:
    #         return
    #
    #     uniqueValues = set()
    #     sourceModel = self.filterModel.sourceModel()
    #     for row in range(sourceModel.rowCount()):
    #         index = sourceModel.index(row, logicalIndex)
    #         value = sourceModel.data(index, Qt.ItemDataRole.DisplayRole)
    #         if value:
    #             uniqueValues.add(str(value))
    #
    #     # Create filter menu
    #     menu = CheckableMenu(self)
    #     menu.addCheckableItems(uniqueValues)
    #     print(self.parent().horizontalHeader().pos())
    #
    #     # Show the menu - ensure correct position handling
    #     headerPos = self.mapToGlobal(pos)
    #     menu.popup(headerPos)
    #     menu.setMaximumHeight(300)
    #     print(menu.sizeHint().height())
    # def mousePressEvent(self, event):
    #     section = self.logicalIndexAt(event.pos())
    #     if event.button() == Qt.MouseButton.RightButton:
    #         self.filterRequested.emit(section)  # Emit the filterRequested Signal
    #     else:
    #         super(FilterableHeaderView, self).mousePressEvent(event)
