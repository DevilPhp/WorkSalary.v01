from PySide6.QtCore import QSortFilterProxyModel, Qt


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
