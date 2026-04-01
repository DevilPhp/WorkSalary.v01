from datetime import datetime
from functools import partial

from PySide6.QtCore import QSortFilterProxyModel, Qt, Signal, QPoint
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QHeaderView, QMenu, QCheckBox, QWidgetAction, QApplication


class CaseInsensitiveProxyModel(QSortFilterProxyModel):
    def __init__(self, numericColumns=None, dateColumns=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columnFilters = {}
        self.numericColumns = numericColumns or []
        self.dateColumns = dateColumns or []
        self.searchText = ""
        self.searchColumns = [0, 1]

    def setFilterForColumn(self, column, filterSet):
        self.columnFilters[column] = filterSet[column]
        self.invalidateFilter()

    def setSearchText(self, text):
        """
        Called from QLineEdit.textChanged.
        Saves the search text and refreshes the proxy filtering.
        """
        self.searchText = (text or "").strip().lower()
        self.invalidateFilter()

    def setSearchColumns(self, columns):
        """
        Allows choosing which columns are checked by text search.
        Example:
            [1]    -> search only in operation name
            [0, 1] -> search in both number and operation name
        """
        self.searchColumns = columns
        self.invalidateFilter()

    def _parseDate(self, dateString):
        """Parse a date string in DD.MM.YY or DD.MM.YYYY format to a datetime object"""
        if not dateString:
            return None
        try:
            # Try parsing with 2-digit year
            return datetime.strptime(dateString, '%d.%m.%y')
        except ValueError:
            try:
                # Try parsing with 4-digit year
                return datetime.strptime(dateString, '%d.%m.%Y')
            except ValueError:
                return None

    def filterAcceptsRow(self, sourceRow, sourceParent):
        sourceModel = self.sourceModel()

        if self.searchText:
            rowMatchesSearch = False

            # Check the search text in the chosen columns
            for column in self.searchColumns:
                index = sourceModel.index(sourceRow, column, sourceParent)
                data = sourceModel.data(index, Qt.ItemDataRole.DisplayRole)

                # Convert None safely to empty string
                data_text = str(data or "").lower()

                # If the typed text is found in this column,
                # keep this row as matching the search
                if self.searchText in data_text:
                    rowMatchesSearch = True
                    break

            # If the row does not match the search text in any searched column,
            # hide it
            if not rowMatchesSearch:
                return False

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
        return True

    def lessThan(self, left, right):
        left_column = left.column()

        # Handle numeric columns
        if left_column in self.numericColumns:
            leftData = self.sourceModel().data(left, Qt.ItemDataRole.DisplayRole)
            rightData = self.sourceModel().data(right, Qt.ItemDataRole.DisplayRole)
            try:
                return float(leftData) > float(rightData)
            except (ValueError, TypeError):
                # Fall back to string comparison if conversion fails
                return str(leftData).lower() > str(rightData).lower()

        # Handle date columns
        elif left_column in self.dateColumns:
            leftData = str(self.sourceModel().data(left))
            rightData = str(self.sourceModel().data(right))

            left_date = self._parseDate(leftData)
            right_date = self._parseDate(rightData)

            # If both are valid dates, compare them
            if left_date and right_date:
                return left_date > right_date
            # If only one is a valid date, put the valid one first
            elif left_date:
                return False
            elif right_date:
                return True
            # If neither is a valid date, fall back to string comparison

        # Default string comparison
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

    def clearSearchText(self):
        """
        Clears only the line edit search filter.
        """
        self.searchText = ""
        self.invalidateFilter()

    def clearAll(self):
        """
        Clears both text search and column filters.
        """
        self.searchText = ""
        self.columnFilters.clear()
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
        if event.button() == Qt.MouseButton.RightButton:
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
