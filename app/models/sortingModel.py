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


class CustomInsensitiveTreeProxyModel(CaseInsensitiveProxyModel):
    def __init__(self, numericColumns=None, dateColumns=None,  *args, **kwargs):
        super().__init__(numericColumns=numericColumns, dateColumns=dateColumns, *args, **kwargs)
        self.searchTokens = []

    def setSearchText(self, text):
        """
        Normalize the typed text and split it into tokens.
        Example:
            '  жилетка   плетене ' -> ['жилетка', 'плетене']
        """
        normalized = " ".join((text or "").lower().split())
        self.searchText = normalized
        self.searchTokens = normalized.split() if normalized else []
        self.invalidateFilter()

    def filterAcceptsRow(self, sourceRow, sourceParent):
        source_model = self.sourceModel()
        if source_model is None:
            return False

        current_index = source_model.index(sourceRow, 0, sourceParent)
        if not current_index.isValid():
            return False

        # 1) Current row/path matches search + filters
        if self._rowMatches(sourceRow, sourceParent):
            return True

        # 2) Keep parent rows visible if any child matches
        for child_row in range(source_model.rowCount(current_index)):
            if self.filterAcceptsRow(child_row, current_index):
                return True

        return False

    def _rowMatches(self, sourceRow, sourceParent):
        source_model = self.sourceModel()
        current_index = source_model.index(sourceRow, 0, sourceParent)

        # -----------------------------------------
        # Text search by path (parents + current row)
        # -----------------------------------------
        if self.searchTokens:
            path_text = self._buildPathText(current_index)

            # Every typed word must exist somewhere in the path
            if not all(token in path_text for token in self.searchTokens):
                return False

        # -----------------------------------------
        # Header / column filters for the current row
        # -----------------------------------------
        for column, filterSet in self.columnFilters.items():
            if not filterSet:
                continue

            index = source_model.index(sourceRow, column, sourceParent)
            data = source_model.data(index, Qt.ItemDataRole.DisplayRole)

            if data not in filterSet:
                return False

        return True

    def _buildPathText(self, index):
        """
        Build searchable text from:
        parent type -> gauge -> group -> struct -> current row

        This is fast and works well for hierarchical searches like:
            'жилетка плетене'
        """
        if not index.isValid():
            return ""

        source_model = self.sourceModel()
        parts = []

        current = index
        while current.isValid():
            row = current.row()
            parent = current.parent()

            # Collect text from the configured search columns for this row
            row_parts = []
            for column in self.searchColumns:
                col_index = source_model.index(row, column, parent)
                data = source_model.data(col_index, Qt.ItemDataRole.DisplayRole)
                if data is not None:
                    row_parts.append(str(data).strip().lower())

            row_text = " ".join(part for part in row_parts if part)
            if row_text:
                parts.append(row_text)

            current = current.parent()

        # Reverse so it becomes: top parent -> ... -> current row
        parts.reverse()
        return " ".join(parts)

    def _indexMatches(self, index):
        """
        Checks whether the row represented by this index matches.
        """
        if not index.isValid():
            return False

        return self._rowMatches(index.row(), index.parent())

    def _hasMatchingChildren(self, parentIndex):
        """
        Recursively checks whether any descendant of parentIndex matches.
        """
        source_model = self.sourceModel()
        if source_model is None or not parentIndex.isValid():
            return False

        child_count = source_model.rowCount(parentIndex)

        for child_row in range(child_count):
            # If the direct child matches, return True
            if self._rowMatches(child_row, parentIndex):
                return True

            # Otherwise check deeper descendants
            child_index = source_model.index(child_row, 0, parentIndex)
            if self._hasMatchingChildren(child_index):
                return True

        return False



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
