from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QCompleter, QLineEdit, QApplication, QTableView
from PySide6.QtCore import Qt, QStringListModel



class Utils:
    @staticmethod
    def setupCompleter(listNames, widget):
        completer = QCompleter(listNames, widget)
        completer.setCompletionColumn(0)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)
        widget.setCompleter(completer)
        # widget.completer().setCompletionMode(QCompleter.InlineCompletion)

    @staticmethod
    def setCustomQCompleter(list, widget):
        model = QStringListModel()
        completer = CustomCompleter()
        completer.setModel(model)
        model.setStringList([i[0] for i in list])

        tableModel = QStandardItemModel()
        for row in list:
            items = [QStandardItem(i) for i in row]
            tableModel.appendRow(items)
        completer.popup().setModel(tableModel)

        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)
        completer.setCompletionColumn(0)
        widget.setCompleter(completer)

    @staticmethod
    def calculateMinutes(startTime, endTime):
        '''Calculate the time difference between two time strings in minutes.
        Start and end times are in 24-hour format.
        Returns the difference in minutes.'''
        start = startTime.time()
        end = endTime.time()

        duration = start.msecsTo(end) // 60000
        if start.hour() > end.hour():
            duration += 24 * 60
        if duration > 300:
            duration -= 60
        return duration


class CustomCompleter(QCompleter):
    def __init__(self, parent=None):
        super(CustomCompleter, self).__init__(parent)
        self.setPopup(QTableView())

    def pathFromIndex(self, index):
        return index.sibling(index.row(), 0).data()

