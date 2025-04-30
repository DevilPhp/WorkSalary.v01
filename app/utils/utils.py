from datetime import datetime

from PySide6.QtGui import QStandardItemModel, QStandardItem, QCursor
from PySide6.QtWidgets import QCompleter, QLineEdit, QApplication, QTableView
from PySide6.QtCore import Qt, QStringListModel



class Utils:

    @staticmethod
    def setFloatToStr(value):
        if isinstance(value, float):
            if int(value) == value:
                return str(int(value))
            else:
                return f"{value:.2f}"
        else:
            return str(value)

    @staticmethod
    def calculatingIdealDialogShowPos(window, customDialog):
        xOffset = 15  # Distance from cursor to dialog
        yOffset = (-customDialog.height() / 2) + 20  # Vertically center
        cursorPos = QCursor.pos()
        idealPosX = cursorPos.x() + xOffset
        idealPosY = cursorPos.y() + yOffset
        screenGeometry = window.geometry()
        if idealPosX + customDialog.width() > screenGeometry.right():
            idealPosX = screenGeometry.right() - customDialog.width()
        if idealPosY + customDialog.height() > screenGeometry.bottom():
            idealPosY = screenGeometry.bottom() - customDialog.height()
        if idealPosY < screenGeometry.top():
            idealPosY = screenGeometry.top()
        customDialog.move(idealPosX, idealPosY)

    @staticmethod
    def setupCompleter(listNames, widget):
        completer = QCompleter(listNames, widget)
        completer.setCompletionColumn(0)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)
        widget.setCompleter(completer)
        # widget.completer().setCompletionMode(QCompleter.InlineCompletion)

    @staticmethod
    def setupCompleterWithModel(model, widget):
        completer = QCompleter()
        completer.setModel(model)
        # completer.setCompletionColumn(0)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)
        widget.setCompleter(completer)

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
    def convertQtimeToTime(timeQTime):
        stringTime = timeQTime.toString("hh:mm")
        return datetime.strptime(stringTime, "%H:%M").time()

    @staticmethod
    def convertQDateToDate(dateQDate):
        stringDate = dateQDate.toString("yyyy-MM-dd")
        return datetime.strptime(stringDate, "%Y-%m-%d").date()

    @staticmethod
    def calculateMinutes(startTime, endTime, breakTime=0):
        '''Calculate the time difference between two time strings in minutes.
        Start and end times are in 24-hour format.
        Returns the difference in minutes.'''
        start = startTime.time()
        end = endTime.time()

        duration = start.msecsTo(end) // 60000
        if start.hour() > end.hour():
            duration += 24 * 60

        if duration > 300 and breakTime == 0:
            duration -= 60
        else:
            duration -= breakTime

        return duration


class CustomCompleter(QCompleter):
    def __init__(self, parent=None):
        super(CustomCompleter, self).__init__(parent)
        self.setPopup(QTableView())

    def pathFromIndex(self, index):
        return index.sibling(index.row(), 0).data()

