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
        # If no filters are active, accept all rows
        if not self.columnFilters:
            return True

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
            return float(leftData) > float(rightData)
        else:
            leftData = self.sourceModel().data(left)
            rightData = self.sourceModel().data(right)
            return str(leftData).lower() > str(rightData).lower()

    def clearFilters(self):
        """Clear all active filters"""
        self.columnFilters.clear()
        self.invalidateFilter()

    def clearFilterForColumn(self, column):
        """Clear filter for a specific column"""
        if column in self.columnFilters:
            del self.columnFilters[column]
            self.invalidateFilter()



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
