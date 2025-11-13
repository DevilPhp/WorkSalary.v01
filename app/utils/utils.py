from datetime import datetime, date, time, timedelta
import sys
import traceback

from PySide6.QtGui import QStandardItemModel, QStandardItem, QCursor
from PySide6.QtWidgets import QCompleter, QLineEdit, QApplication, QTableView
from PySide6.QtCore import Qt, QStringListModel, QTime, QObject, Signal, QRunnable, Slot


class Utils:

    @staticmethod
    def calculatePaymentForWorker(data, mainPaymentRation, paymentInLv,
                         paymentInEuro, nightPayInLeva, nightPayInEuro):
        totalPaymentInLev = 0
        totalPaymentInEuro = 0
        totalNightTime = 0
        totalTime = 0

        for pay in data:
            efficient = pay[0]
            ratio = pay[1]
            nightMins = pay[3]

            totalPaymentInLev += Utils.calculatePayment(efficient - nightMins, ratio,
                                                        mainPaymentRation, paymentInLv)
            totalPaymentInEuro += Utils.calculatePayment(efficient - nightMins, ratio,
                                                         mainPaymentRation, paymentInEuro)
            if nightMins > 0:
                totalNightTime += nightMins
                totalPaymentInLev += Utils.calculatePayment(nightMins, ratio,
                                                            mainPaymentRation, nightPayInLeva)
                totalPaymentInEuro += Utils.calculatePayment(nightMins, ratio,
                                                             mainPaymentRation, nightPayInEuro)
            totalTime += efficient

        return totalPaymentInLev, totalPaymentInEuro, totalNightTime, totalTime

    @staticmethod
    def calculatePaymentNoRepeat(data, mainPaymentRation, paymentInLv,
                                 paymentInEuro, nightPayInLeva, nightPayInEuro):
        totalPayLv = 0
        totalPayEuro = 0
        totalPayLv += Utils.calculatePayment((data[0] - data[3]),
                                             data[1], mainPaymentRation, paymentInLv)
        totalPayEuro += Utils.calculatePayment((data[0] - data[3]),
                                               data[1], mainPaymentRation, paymentInEuro)

        if data[3] > 0:
            totalPayLv += Utils.calculatePayment(data[3], data[1],
                                                 mainPaymentRation, nightPayInLeva)
            totalPayEuro += Utils.calculatePayment(data[3], data[1],
                                                   mainPaymentRation, nightPayInEuro)
        return totalPayLv, totalPayEuro


    @staticmethod
    def calculatePayment(efficient, ratio, paymentRatio, payment):
        return (efficient *
                ratio *
                paymentRatio *
                payment)

    @staticmethod
    def setReturnBtnForCompleter(completer):
        currentIndex = completer.popup().currentIndex()
        if currentIndex.isValid():
            selectedText = currentIndex.data()
        else:
            selectedText = completer.completionModel().index(0, 0).data()
        return selectedText

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
        completer.popup().setStyleSheet("font-size: 8pt;")
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
    def checkNightShiftMins(startTime, endTime):
        if startTime is None or endTime is None:
            return 0
        if isinstance(startTime, QTime) and isinstance(endTime, QTime):
            startTime = Utils.convertQtimeToTime(startTime)
            endTime = Utils.convertQtimeToTime(endTime)

        # Anchor everything to an arbitrary reference date
        DefaultDay = date(2000, 1, 1)

        # Build datetime objects for the shift start/end.
        shiftStart = datetime.combine(DefaultDay, startTime)
        shiftEnd = datetime.combine(DefaultDay, endTime)

        # If end <= start, assume the shift ends the next day (typical for night shifts).
        if shiftEnd <= shiftStart:
            shiftEnd += timedelta(days=1)

        # Night window basics: each night is (22:00, 06:00 next day).
        NightShiftStart = time(22, 0)
        NightShiftLen = timedelta(hours=8)  # 22:00 -> 06:00

        # Find the *first* night window that could overlap the shift.
        # If the shift starts between 00:00 and 06:00, the relevant night began the previous day at 22:00.
        if shiftStart.time() < time(6, 0):
            firstWindowStart = datetime.combine(shiftStart.date() - timedelta(days=1), NightShiftStart)
        else:
            # Otherwise, start from the same day at 22:00
            firstWindowStart = datetime.combine(shiftStart.date(), NightShiftStart)

        totalMinutes = 0
        windowStart = firstWindowStart
        windowEnd = windowStart + NightShiftLen

        # Slide the night window forward one day at a time and sum overlaps.
        while windowStart < shiftEnd:
            # Compute overlap between [shiftStart, shiftEnd) and [windowStart, windowEnd)
            overlapStart = max(shiftStart, windowStart)
            overlapEnd = min(shiftEnd, windowEnd)
            if overlapEnd > overlapStart:
                totalMinutes += int((overlapEnd - overlapStart).total_seconds() // 60)

            # Move to the next night's window
            windowStart += timedelta(days=1)
            windowEnd += timedelta(days=1)

            # Optional fast-exit: if the next window starts after shiftEnd, we can break
            if windowStart >= shiftEnd:
                break

        return totalMinutes

    @staticmethod
    def makeDispalyMins(time):
        if 0 < int(time % 60) < 10:
            minsDispay = f'0{int(time % 60)}'
        else:
            minsDispay = f'{int(time % 60)}'
        dispalyTime = f'{int(time / 60)}:{minsDispay}' \
            if time % 60 > 0 else f'{int(time / 60)}'
        return dispalyTime

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


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        `tuple` (exctype, value, traceback.format_exc())

    result
        `object` data returned from processing, anything

    '''
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done

